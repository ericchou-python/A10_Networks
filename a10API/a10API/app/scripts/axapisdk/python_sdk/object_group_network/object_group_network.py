########################################################################################################################
# File name: object_group_network.py
# Copyright(C) 2007-2013, A10 Networks Inc. All rights reserved.
# Software for all A10 products contain trade secrets and confidential
# information of A10 Networks and its subsidiaries and may not be
# disclosed, copied, reproduced or distributed to anyone outside of
# A10 Networks without prior written consent of A10 Networks, Inc.
########################################################################################################################
import sys
import json
sys.path.append("../common")
from axapi_common import *

BASE_URL = [
	'https://axapi.a10networks.com/axapi/v3/object-group/network',
]

def deserialize_Network_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	net_name = data.get('net-name')
	host = data.get('host')
	host_v4 = data.get('host-v4')
	host_v6 = data.get('host-v6')
	any = data.get('any')
	subnet = data.get('subnet')
	rev_subnet_mask = data.get('rev-subnet-mask')
	ipv6_subnet = data.get('ipv6-subnet')
	result = Network(net_name=net_name, host=host, host_v4=host_v4, host_v6=host_v6, any=any, subnet=subnet, rev_subnet_mask=rev_subnet_mask, ipv6_subnet=ipv6_subnet)
	return result

def serialize_Network_json(obj):
	output = OrderedDict()
	output['net-name'] = obj.net_name
	if obj.host is not None:
		output['host'] = obj.host
	if obj.host_v4 is not None:
		output['host-v4'] = obj.host_v4
	if obj.host_v6 is not None:
		output['host-v6'] = obj.host_v6
	if obj.any is not None:
		output['any'] = obj.any
	if obj.subnet is not None:
		output['subnet'] = obj.subnet
	if obj.rev_subnet_mask is not None:
		output['rev-subnet-mask'] = obj.rev_subnet_mask
	if obj.ipv6_subnet is not None:
		output['ipv6-subnet'] = obj.ipv6_subnet
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Network_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Network_json(item))
	return list(container)

class Network_net_name(AxapiObject):
	__metaclass__ = StructMeta 
	net_name=SizedString(1, 63)
	def __init__(self, net_name):
		self.net_name = net_name

	def __str__(self):
		return str(self.net_name)

class Network(AxapiObject):
	__metaclass__ = StructMeta 
	net_name=SizedString(1, 63)
	host=PosRangedInteger(0, 1)
	host_v4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	host_v6=SizedString(1, 255)
	any=PosRangedInteger(0, 1)
	subnet = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	rev_subnet_mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6_subnet=SizedString(1, 255)
	def __init__(self, net_name, host=None, host_v4=None, host_v6=None, any=None, subnet=None, rev_subnet_mask=None, ipv6_subnet=None):
		self.net_name = net_name
		self.host = host
		self.host_v4 = host_v4
		self.host_v6 = host_v6
		self.any = any
		self.subnet = subnet
		self.rev_subnet_mask = rev_subnet_mask
		self.ipv6_subnet = ipv6_subnet

	def __str__(self):
		return str(self.net_name)

class ObjectgroupNetworkClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getObjectgroupNetwork(self, network_net_name):
		"""
		Retrieve the network identified by the specified identifier
		
		Args:
			network_net_name Network_net_name
		
		Returns:
			An instance of the Network class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(network_net_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified network does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('network')
		return deserialize_Network_json(payload)

	def putObjectgroupNetwork(self, network_net_name, network):
		"""
		Replace the object network
		
		Args:
			network_net_name Network_net_name
			network An instance of the Network class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['network']=serialize_Network_json(network)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(network_net_name) .replace("/", "%2f") + query, payload, headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

	def deleteObjectgroupNetwork(self, network_net_name):
		"""
		Remove the network identified by the specified identifier from the system
		
		Args:
			network_net_name Network_net_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(network_net_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified network does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllObjectgroupNetworksClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitObjectgroupNetwork(self, network):
		"""
		Create the object network
		
		Args:
			network An instance of the Network class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['network']=serialize_Network_json(network)
		payload = serialize_final_json(output)
		conn.request('POST', self.get_path() + '/' + query, payload, headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

	def getAllObjectgroupNetworks(self):
		"""
		Retrieve all network objects currently pending in the system
		
		Returns:
			A list of Network objects
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('networkList')
		return deserialize_list_Network_json(payload)

