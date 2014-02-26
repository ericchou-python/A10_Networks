########################################################################################################################
# File name: snmp_server_enable_traps_network.py
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
	'https://axapi.a10networks.com/axapi/v3/snmp-server/enable/traps/network',
]

def deserialize_Network_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk_port_threshold = data.get('trunk-port-threshold')
	result = Network(trunk_port_threshold=trunk_port_threshold)
	return result

def serialize_Network_json(obj):
	output = OrderedDict()
	output['trunk-port-threshold'] = obj.trunk_port_threshold
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

class Network_trunk_port_threshold_trunk_port_threshold(AxapiObject):
	__metaclass__ = StructMeta 
	trunk_port_threshold=PosRangedInteger(0, 1)
	def __init__(self, trunk_port_threshold):
		self.trunk_port_threshold = trunk_port_threshold

	def __str__(self):
		return str(self.trunk_port_threshold)

class Network(AxapiObject):
	__metaclass__ = StructMeta 
	trunk_port_threshold=PosRangedInteger(0, 1)
	def __init__(self, trunk_port_threshold):
		self.trunk_port_threshold = trunk_port_threshold

	def __str__(self):
		return str(self.trunk_port_threshold)

class SnmpserverEnableTrapsNetworkClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSnmpserverEnableTrapsNetwork(self, network_trunk_port_threshold_trunk_port_threshold):
		"""
		Retrieve the network identified by the specified identifier
		
		Args:
			network_trunk_port_threshold_trunk_port_threshold Network_trunk_port_threshold_trunk_port_threshold
		
		Returns:
			An instance of the Network class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(network_trunk_port_threshold_trunk_port_threshold) .replace("/", "%2f") + query, headers=headers)
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

	def putSnmpserverEnableTrapsNetwork(self, network_trunk_port_threshold_trunk_port_threshold, network):
		"""
		Replace the object network
		
		Args:
			network_trunk_port_threshold_trunk_port_threshold Network_trunk_port_threshold_trunk_port_threshold
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
		conn.request('PUT', self.get_path() + '/' + str(network_trunk_port_threshold_trunk_port_threshold) .replace("/", "%2f") + query, payload, headers)
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

	def deleteSnmpserverEnableTrapsNetwork(self, network_trunk_port_threshold_trunk_port_threshold):
		"""
		Remove the network identified by the specified identifier from the system
		
		Args:
			network_trunk_port_threshold_trunk_port_threshold Network_trunk_port_threshold_trunk_port_threshold
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(network_trunk_port_threshold_trunk_port_threshold) .replace("/", "%2f") + query, headers=headers)
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

class AllSnmpserverEnableTrapsNetworksClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSnmpserverEnableTrapsNetwork(self, network):
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

	def getAllSnmpserverEnableTrapsNetworks(self):
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

