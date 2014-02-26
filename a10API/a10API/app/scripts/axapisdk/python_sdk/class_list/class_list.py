########################################################################################################################
# File name: class_list.py
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
	'https://axapi.a10networks.com/axapi/v3/class-list',
]

def deserialize_Class_list_ipv4_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4addr = data.get('ipv4addr')
	ipv4mask = data.get('ipv4mask')
	result = Class_list_ipv4_cfg(ipv4addr=ipv4addr, ipv4mask=ipv4mask)
	return result

def deserialize_list_Class_list_ipv4_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Class_list_ipv4_cfg_json(item))
	return list(container)

def deserialize_Class_list_ipv6_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	v6_age = data.get('v6-age')
	result = Class_list_ipv6_cfg(ipv6_addr=ipv6_addr, v6_age=v6_age)
	return result

def deserialize_list_Class_list_ipv6_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Class_list_ipv6_cfg_json(item))
	return list(container)

def deserialize_Class_list_str_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	str_lid_dummy = data.get('str-lid-dummy')
	str_lid = data.get('str-lid')
	str_glid_dummy = data.get('str-glid-dummy')
	str_glid = data.get('str-glid')
	value_str = data.get('value-str')
	result = Class_list_str_cfg(str_lid_dummy=str_lid_dummy, str_lid=str_lid, str_glid_dummy=str_glid_dummy, str_glid=str_glid, value_str=value_str)
	return result

def deserialize_list_Class_list_str_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Class_list_str_cfg_json(item))
	return list(container)

def deserialize_Class_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	ipv4_cfg = deserialize_list_Class_list_ipv4_cfg_json(data.get('ipv4-cfg'))
	ipv6_cfg = deserialize_list_Class_list_ipv6_cfg_json(data.get('ipv6-cfg'))
	str_cfg = deserialize_list_Class_list_str_cfg_json(data.get('str-cfg'))
	result = Class_list(name=name, ipv4_cfg=ipv4_cfg, ipv6_cfg=ipv6_cfg, str_cfg=str_cfg)
	return result

def serialize_Class_list_ipv4_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv4addr is not None:
		output['ipv4addr'] = obj.ipv4addr
	if obj.ipv4mask is not None:
		output['ipv4mask'] = obj.ipv4mask
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Class_list_ipv4_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Class_list_ipv4_cfg_json(item))
	return output

def serialize_Class_list_ipv6_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv6_addr is not None:
		output['ipv6-addr'] = obj.ipv6_addr
	if obj.v6_age is not None:
		output['v6-age'] = obj.v6_age
	return output

def serialize_list_Class_list_ipv6_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Class_list_ipv6_cfg_json(item))
	return output

def serialize_Class_list_str_cfg_json(obj):
	output = OrderedDict()
	if obj.str_lid_dummy is not None:
		output['str-lid-dummy'] = obj.str_lid_dummy
	if obj.str_lid is not None:
		output['str-lid'] = obj.str_lid
	if obj.str_glid_dummy is not None:
		output['str-glid-dummy'] = obj.str_glid_dummy
	if obj.str_glid is not None:
		output['str-glid'] = obj.str_glid
	if obj.value_str is not None:
		output['value-str'] = obj.value_str
	return output

def serialize_list_Class_list_str_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Class_list_str_cfg_json(item))
	return output

def serialize_Class_list_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.ipv4_cfg is not None:
		output['ipv4-cfg'] = serialize_list_Class_list_ipv4_cfg_json(obj.ipv4_cfg)
	if obj.ipv6_cfg is not None:
		output['ipv6-cfg'] = serialize_list_Class_list_ipv6_cfg_json(obj.ipv6_cfg)
	if obj.str_cfg is not None:
		output['str-cfg'] = serialize_list_Class_list_str_cfg_json(obj.str_cfg)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Class_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Class_list_json(item))
	return list(container)

class Class_list(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	def __init__(self, name, ipv4_cfg=None, ipv6_cfg=None, str_cfg=None):
		self.name = name
		self.ipv4_cfg = ipv4_cfg
		self.ipv6_cfg = ipv6_cfg
		self.str_cfg = str_cfg

	def __str__(self):
		return str(self.name)

class Class_list_ipv4_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv4mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ipv4addr=None, ipv4mask=None):
		self.ipv4addr = ipv4addr
		self.ipv4mask = ipv4mask

	def __str__(self):
		return ""

class Class_list_ipv6_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	v6_age=PosRangedInteger(1, 2000)
	def __init__(self, ipv6_addr=None, v6_age=None):
		self.ipv6_addr = ipv6_addr
		self.v6_age = v6_age

	def __str__(self):
		return ""

class Class_list_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class Class_list_str_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	str_lid_dummy=PosRangedInteger(0, 1)
	str_lid=PosRangedInteger(1, 31)
	str_glid_dummy=PosRangedInteger(0, 1)
	str_glid=PosRangedInteger(1, 1023)
	value_str=SizedString(1, 255)
	def __init__(self, str_lid_dummy=None, str_lid=None, str_glid_dummy=None, str_glid=None, value_str=None):
		self.str_lid_dummy = str_lid_dummy
		self.str_lid = str_lid
		self.str_glid_dummy = str_glid_dummy
		self.str_glid = str_glid
		self.value_str = value_str

	def __str__(self):
		return ""

class ClasslistClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getClasslist(self, class_list_name):
		"""
		Retrieve the class_list identified by the specified identifier
		
		Args:
			class_list_name Class_list_name
		
		Returns:
			An instance of the Class_list class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(class_list_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified class_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('class-list')
		return deserialize_Class_list_json(payload)

	def putClasslist(self, class_list_name, class_list):
		"""
		Replace the object class_list
		
		Args:
			class_list_name Class_list_name
			class_list An instance of the Class_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['class-list']=serialize_Class_list_json(class_list)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(class_list_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteClasslist(self, class_list_name):
		"""
		Remove the class_list identified by the specified identifier from the system
		
		Args:
			class_list_name Class_list_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(class_list_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified class_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllClasslistsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitClasslist(self, class_list):
		"""
		Create the object class_list
		
		Args:
			class_list An instance of the Class_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['class-list']=serialize_Class_list_json(class_list)
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

	def getAllClasslists(self):
		"""
		Retrieve all class_list objects currently pending in the system
		
		Returns:
			A list of Class_list objects
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
			payload= data.get('class-listList')
		return deserialize_list_Class_list_json(payload)

