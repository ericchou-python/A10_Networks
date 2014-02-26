########################################################################################################################
# File name: ntp_auth_key.py
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
	'https://axapi.a10networks.com/axapi/v3/ntp/auth-key',
]

def deserialize_Auth_key__key_cfg__type_cfg__hex_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	hex_key_string = data.get('hex-key-string')
	hex_encrypted = data.get('hex-encrypted')
	result = Auth_key__key_cfg__type_cfg__hex(hex_key_string=hex_key_string, hex_encrypted=hex_encrypted)
	return result

def deserialize_Auth_key__key_cfg__type_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type = data.get('type')
	hex = deserialize_Auth_key__key_cfg__type_cfg__hex_json(data.get('hex'))
	key_string = data.get('key-string')
	encrypted = data.get('encrypted')
	result = Auth_key__key_cfg__type_cfg(type=type, hex=hex, key_string=key_string, encrypted=encrypted)
	return result

def deserialize_Auth_key__key_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key = data.get('key')
	type_cfg = deserialize_Auth_key__key_cfg__type_cfg_json(data.get('type-cfg'))
	result = Auth_key__key_cfg(key=key, type_cfg=type_cfg)
	return result

def deserialize_Auth_key_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key_cfg = deserialize_Auth_key__key_cfg_json(data.get('key-cfg'))
	result = Auth_key(key_cfg=key_cfg)
	return result

def serialize_Auth_key__key_cfg__type_cfg__hex_json(obj):
	output = OrderedDict()
	output['hex-key-string'] = obj.hex_key_string
	output['hex-encrypted'] = obj.hex_encrypted
	return output

def serialize_Auth_key__key_cfg__type_cfg_json(obj):
	output = OrderedDict()
	output['type'] = obj.type
	output['hex'] = serialize_Auth_key__key_cfg__type_cfg__hex_json(obj.hex)
	output['key-string'] = obj.key_string
	output['encrypted'] = obj.encrypted
	return output

def serialize_Auth_key__key_cfg_json(obj):
	output = OrderedDict()
	output['key'] = obj.key
	if obj.type_cfg is not None:
		output['type-cfg'] = serialize_Auth_key__key_cfg__type_cfg_json(obj.type_cfg)
	return output

def serialize_Auth_key_json(obj):
	output = OrderedDict()
	output['key-cfg'] = serialize_Auth_key__key_cfg_json(obj.key_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Auth_key_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Auth_key_json(item))
	return list(container)

class Auth_key_key_cfg__key_cfg__type_cfg__hex(AxapiObject):
	__metaclass__ = StructMeta 
	hex_key_string=SizedString(21, 40)
	hex_encrypted=SizedString(1, 255)
	def __init__(self, hex_key_string, hex_encrypted):
		self.hex_key_string = hex_key_string
		self.hex_encrypted = hex_encrypted

	def __str__(self):
		return str(self.hex_key_string) + '+' + str(self.hex_encrypted)

class Auth_key_key_cfg__key_cfg__type_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	type = Enum([])
	key_string=SizedString(1, 20)
	encrypted=SizedString(1, 255)
	def __init__(self, type, hex, key_string, encrypted):
		self.type = type
		self.hex = hex
		self.key_string = key_string
		self.encrypted = encrypted

	def __str__(self):
		return str(self.type) + '+' + str(self.hex) + '+' + str(self.key_string) + '+' + str(self.encrypted)

class Auth_key_key_cfg__key_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	key=PosRangedInteger(1, 65535)
	def __init__(self, key, type_cfg=None):
		self.key = key
		self.type_cfg = type_cfg

	def __str__(self):
		return str(self.key)

class Auth_key_key_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, key_cfg):
		self.key_cfg = key_cfg

	def __str__(self):
		return str(self.key_cfg)

class Auth_key__key_cfg__type_cfg__hex(AxapiObject):
	__metaclass__ = StructMeta 
	hex_key_string=SizedString(21, 40)
	hex_encrypted=SizedString(1, 255)
	def __init__(self, hex_key_string, hex_encrypted):
		self.hex_key_string = hex_key_string
		self.hex_encrypted = hex_encrypted

	def __str__(self):
		return str(self.hex_key_string) + '+' + str(self.hex_encrypted)

class Auth_key__key_cfg__type_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	type = Enum([])
	key_string=SizedString(1, 20)
	encrypted=SizedString(1, 255)
	def __init__(self, type, hex, key_string, encrypted):
		self.type = type
		self.hex = hex
		self.key_string = key_string
		self.encrypted = encrypted

	def __str__(self):
		return str(self.type) + '+' + str(self.hex) + '+' + str(self.key_string) + '+' + str(self.encrypted)

class Auth_key__key_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	key=PosRangedInteger(1, 65535)
	def __init__(self, key, type_cfg=None):
		self.key = key
		self.type_cfg = type_cfg

	def __str__(self):
		return str(self.key)

class Auth_key(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, key_cfg):
		self.key_cfg = key_cfg

	def __str__(self):
		return str(self.key_cfg)

class NtpAuthkeyClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getNtpAuthkey(self, auth_key_key_cfg):
		"""
		Retrieve the auth_key identified by the specified identifier
		
		Args:
			auth_key_key_cfg Auth_key_key_cfg
		
		Returns:
			An instance of the Auth_key class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(auth_key_key_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified auth_key does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('auth-key')
		return deserialize_Auth_key_json(payload)

	def putNtpAuthkey(self, auth_key_key_cfg, auth_key):
		"""
		Replace the object auth_key
		
		Args:
			auth_key_key_cfg Auth_key_key_cfg
			auth_key An instance of the Auth_key class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['auth-key']=serialize_Auth_key_json(auth_key)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(auth_key_key_cfg) .replace("/", "%2f") + query, payload, headers)
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

	def deleteNtpAuthkey(self, auth_key_key_cfg):
		"""
		Remove the auth_key identified by the specified identifier from the system
		
		Args:
			auth_key_key_cfg Auth_key_key_cfg
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(auth_key_key_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified auth_key does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllNtpAuthkeysClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitNtpAuthkey(self, auth_key):
		"""
		Create the object auth_key
		
		Args:
			auth_key An instance of the Auth_key class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['auth-key']=serialize_Auth_key_json(auth_key)
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

	def getAllNtpAuthkeys(self):
		"""
		Retrieve all auth_key objects currently pending in the system
		
		Returns:
			A list of Auth_key objects
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
			payload= data.get('auth-keyList')
		return deserialize_list_Auth_key_json(payload)

