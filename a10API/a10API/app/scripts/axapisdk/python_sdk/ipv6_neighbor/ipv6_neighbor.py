########################################################################################################################
# File name: ipv6_neighbor.py
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
	'https://axapi.a10networks.com/axapi/v3/ipv6/neighbor',
]

def deserialize_Neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	mac = data.get('mac')
	ethernet = data.get('ethernet')
	trunk = data.get('trunk')
	vlan = data.get('vlan')
	result = Neighbor(ipv6_addr=ipv6_addr, mac=mac, ethernet=ethernet, trunk=trunk, vlan=vlan)
	return result

def serialize_Neighbor_json(obj):
	output = OrderedDict()
	output['ipv6-addr'] = obj.ipv6_addr
	output['mac'] = obj.mac
	if obj.ethernet is not None:
		output['ethernet'] = obj.ethernet
	if obj.trunk is not None:
		output['trunk'] = obj.trunk
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Neighbor_json(item))
	return list(container)

class Neighbor_ipv6_addr_mac(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	mac=SizedString(1, 17)
	def __init__(self, ipv6_addr, mac):
		self.ipv6_addr = ipv6_addr
		self.mac = mac

	def __str__(self):
		return str(self.ipv6_addr) + '+' + str(self.mac)

class Neighbor(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	mac=SizedString(1, 17)
	ethernet=PosRangedInteger(1, 2048)
	trunk=PosRangedInteger(1, 16)
	vlan=PosRangedInteger(1, 4094)
	def __init__(self, ipv6_addr, mac, ethernet=None, trunk=None, vlan=None):
		self.ipv6_addr = ipv6_addr
		self.mac = mac
		self.ethernet = ethernet
		self.trunk = trunk
		self.vlan = vlan

	def __str__(self):
		return str(self.ipv6_addr) + '+' + str(self.mac)

class Ipv6NeighborClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpv6Neighbor(self, neighbor_ipv6_addr_mac):
		"""
		Retrieve the neighbor identified by the specified identifier
		
		Args:
			neighbor_ipv6_addr_mac Neighbor_ipv6_addr_mac
		
		Returns:
			An instance of the Neighbor class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(neighbor_ipv6_addr_mac) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified neighbor does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('neighbor')
		return deserialize_Neighbor_json(payload)

	def putIpv6Neighbor(self, neighbor_ipv6_addr_mac, neighbor):
		"""
		Replace the object neighbor
		
		Args:
			neighbor_ipv6_addr_mac Neighbor_ipv6_addr_mac
			neighbor An instance of the Neighbor class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['neighbor']=serialize_Neighbor_json(neighbor)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(neighbor_ipv6_addr_mac) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpv6Neighbor(self, neighbor_ipv6_addr_mac):
		"""
		Remove the neighbor identified by the specified identifier from the system
		
		Args:
			neighbor_ipv6_addr_mac Neighbor_ipv6_addr_mac
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(neighbor_ipv6_addr_mac) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified neighbor does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpv6NeighborsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpv6Neighbor(self, neighbor):
		"""
		Create the object neighbor
		
		Args:
			neighbor An instance of the Neighbor class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['neighbor']=serialize_Neighbor_json(neighbor)
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

	def getAllIpv6Neighbors(self):
		"""
		Retrieve all neighbor objects currently pending in the system
		
		Returns:
			A list of Neighbor objects
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
			payload= data.get('neighborList')
		return deserialize_list_Neighbor_json(payload)

