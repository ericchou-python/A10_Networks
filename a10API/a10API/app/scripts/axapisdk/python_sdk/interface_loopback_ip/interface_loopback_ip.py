########################################################################################################################
# File name: interface_loopback_ip.py
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
	'https://axapi.a10networks.com/axapi/v3/interface/loopback/ip',
]

def deserialize_Interface_loopback_ip_address_val_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val = data.get('address_val')
	netmask = data.get('netmask')
	result = Interface_loopback_ip_address_val_cfg(address_val=address_val, netmask=netmask)
	return result

def deserialize_list_Interface_loopback_ip_address_val_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_loopback_ip_address_val_cfg_json(item))
	return list(container)

def deserialize_Ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val_cfg = deserialize_list_Interface_loopback_ip_address_val_cfg_json(data.get('address_val-cfg'))
	result = Ip__address(address_val_cfg=address_val_cfg)
	return result

def deserialize_Ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Ip__address_json(data.get('address'))
	result = Ip(address=address)
	return result

def serialize_Interface_loopback_ip_address_val_cfg_json(obj):
	output = OrderedDict()
	if obj.address_val is not None:
		output['address_val'] = obj.address_val
	if obj.netmask is not None:
		output['netmask'] = obj.netmask
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Interface_loopback_ip_address_val_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_loopback_ip_address_val_cfg_json(item))
	return output

def serialize_Ip__address_json(obj):
	output = OrderedDict()
	if obj.address_val_cfg is not None:
		output['address_val-cfg'] = serialize_list_Interface_loopback_ip_address_val_cfg_json(obj.address_val_cfg)
	return output

def serialize_Ip_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = serialize_Ip__address_json(obj.address)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_json(item))
	return list(container)

class Ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address_val_cfg=None):
		self.address_val_cfg = address_val_cfg

	def __str__(self):
		return ""

class Ip(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address=None):
		self.address = address

	def __str__(self):
		return ""

class Interface_loopback_ip_address_val_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	address_val = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, address_val=None, netmask=None):
		self.address_val = address_val
		self.netmask = netmask

	def __str__(self):
		return ""

class InterfaceLoopbackIpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getInterfaceLoopbackIp(self):
		"""
		Retrieve the ip identified by the specified identifier
		
		Returns:
			An instance of the Ip class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ip does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ip')
		return deserialize_Ip_json(payload)

	def putInterfaceLoopbackIp(self, ip):
		"""
		Replace the object ip
		
		Args:
			ip An instance of the Ip class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ip']=serialize_Ip_json(ip)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + query, payload, headers)
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

	def deleteInterfaceLoopbackIp(self):
		"""
		Remove the ip identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ip does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllInterfaceLoopbackIpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitInterfaceLoopbackIp(self, ip):
		"""
		Create the object ip
		
		Args:
			ip An instance of the Ip class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ip']=serialize_Ip_json(ip)
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

	def getAllInterfaceLoopbackIps(self):
		"""
		Retrieve all ip objects currently pending in the system
		
		Returns:
			A list of Ip objects
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
			payload= data.get('ipList')
		return deserialize_list_Ip_json(payload)

