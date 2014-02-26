########################################################################################################################
# File name: mac_address.py
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
	'https://axapi.a10networks.com/axapi/v3/mac-address',
]

def deserialize_Mac_address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	mac = data.get('mac')
	port = data.get('port')
	vlan = data.get('vlan')
	result = Mac_address(mac=mac, port=port, vlan=vlan)
	return result

def serialize_Mac_address_json(obj):
	output = OrderedDict()
	output['mac'] = obj.mac
	output['port'] = obj.port
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

def deserialize_list_Mac_address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Mac_address_json(item))
	return list(container)

class Mac_address_mac_port_vlan(AxapiObject):
	__metaclass__ = StructMeta 
	mac=SizedString(1, 17)
	port=PosRangedInteger(1, 2048)
	vlan=PosRangedInteger(1, 4094)
	def __init__(self, mac, port, vlan):
		self.mac = mac
		self.port = port
		self.vlan = vlan

	def __str__(self):
		return str(self.mac) + '+' + str(self.port) + '+' + str(self.vlan)

class Mac_address(AxapiObject):
	__metaclass__ = StructMeta 
	mac=SizedString(1, 17)
	port=PosRangedInteger(1, 2048)
	vlan=PosRangedInteger(1, 4094)
	def __init__(self, mac, port, vlan):
		self.mac = mac
		self.port = port
		self.vlan = vlan

	def __str__(self):
		return str(self.mac) + '+' + str(self.port) + '+' + str(self.vlan)

class MacaddressClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getMacaddress(self, mac_address_mac_port_vlan):
		"""
		Retrieve the mac_address identified by the specified identifier
		
		Args:
			mac_address_mac_port_vlan Mac_address_mac_port_vlan
		
		Returns:
			An instance of the Mac_address class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(mac_address_mac_port_vlan) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified mac_address does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('mac-address')
		return deserialize_Mac_address_json(payload)

	def putMacaddress(self, mac_address_mac_port_vlan, mac_address):
		"""
		Replace the object mac_address
		
		Args:
			mac_address_mac_port_vlan Mac_address_mac_port_vlan
			mac_address An instance of the Mac_address class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['mac-address']=serialize_Mac_address_json(mac_address)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(mac_address_mac_port_vlan) .replace("/", "%2f") + query, payload, headers)
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

	def deleteMacaddress(self, mac_address_mac_port_vlan):
		"""
		Remove the mac_address identified by the specified identifier from the system
		
		Args:
			mac_address_mac_port_vlan Mac_address_mac_port_vlan
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(mac_address_mac_port_vlan) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified mac_address does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllMacaddresssClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitMacaddress(self, mac_address):
		"""
		Create the object mac_address
		
		Args:
			mac_address An instance of the Mac_address class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['mac-address']=serialize_Mac_address_json(mac_address)
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

	def getAllMacaddresss(self):
		"""
		Retrieve all mac_address objects currently pending in the system
		
		Returns:
			A list of Mac_address objects
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
			payload= data.get('mac-addressList')
		return deserialize_list_Mac_address_json(payload)

