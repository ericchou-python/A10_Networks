########################################################################################################################
# File name: address_group.py
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
	'https://axapi.a10networks.com/axapi/v3/address-group',
]

def deserialize_Address_group_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	net_id = data.get('net-id')
	netmask = data.get('netmask')
	start_ip = data.get('start-ip')
	end_ip = data.get('end-ip')
	ip_addr = data.get('ip-addr')
	ip_count = data.get('ip-count')
	result = Address_group(name=name, net_id=net_id, netmask=netmask, start_ip=start_ip, end_ip=end_ip, ip_addr=ip_addr, ip_count=ip_count)
	return result

def serialize_Address_group_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.net_id is not None:
		output['net-id'] = obj.net_id
	if obj.netmask is not None:
		output['netmask'] = obj.netmask
	if obj.start_ip is not None:
		output['start-ip'] = obj.start_ip
	if obj.end_ip is not None:
		output['end-ip'] = obj.end_ip
	if obj.ip_addr is not None:
		output['ip-addr'] = obj.ip_addr
	if obj.ip_count is not None:
		output['ip-count'] = obj.ip_count
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Address_group_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Address_group_json(item))
	return list(container)

class Address_group_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class Address_group(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	net_id = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	start_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	end_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_count=PosInteger()
	def __init__(self, name, net_id=None, netmask=None, start_ip=None, end_ip=None, ip_addr=None, ip_count=None):
		self.name = name
		self.net_id = net_id
		self.netmask = netmask
		self.start_ip = start_ip
		self.end_ip = end_ip
		self.ip_addr = ip_addr
		self.ip_count = ip_count

	def __str__(self):
		return str(self.name)

class AddressgroupClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getAddressgroup(self, address_group_name):
		"""
		Retrieve the address_group identified by the specified identifier
		
		Args:
			address_group_name Address_group_name
		
		Returns:
			An instance of the Address_group class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(address_group_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified address_group does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('address-group')
		return deserialize_Address_group_json(payload)

	def putAddressgroup(self, address_group_name, address_group):
		"""
		Replace the object address_group
		
		Args:
			address_group_name Address_group_name
			address_group An instance of the Address_group class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['address-group']=serialize_Address_group_json(address_group)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(address_group_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteAddressgroup(self, address_group_name):
		"""
		Remove the address_group identified by the specified identifier from the
		system
		
		Args:
			address_group_name Address_group_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(address_group_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified address_group does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllAddressgroupsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitAddressgroup(self, address_group):
		"""
		Create the object address_group
		
		Args:
			address_group An instance of the Address_group class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['address-group']=serialize_Address_group_json(address_group)
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

	def getAllAddressgroups(self):
		"""
		Retrieve all address_group objects currently pending in the system
		
		Returns:
			A list of Address_group objects
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
			payload= data.get('address-groupList')
		return deserialize_list_Address_group_json(payload)

