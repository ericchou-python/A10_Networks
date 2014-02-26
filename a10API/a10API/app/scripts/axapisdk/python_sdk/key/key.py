########################################################################################################################
# File name: key.py
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
	'https://axapi.a10networks.com/axapi/v3/key',
]

def deserialize_Key__chain_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	chain = data.get('chain')
	name = data.get('name')
	result = Key__chain_cfg(chain=chain, name=name)
	return result

def deserialize_Key_key_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key_number = data.get('key-number')
	key_string = data.get('key-string')
	result = Key_key(key_number=key_number, key_string=key_string)
	return result

def deserialize_list_Key_key_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Key_key_json(item))
	return list(container)

def deserialize_Key_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	chain_cfg = deserialize_Key__chain_cfg_json(data.get('chain-cfg'))
	keylist = deserialize_list_Key_key_json(data.get('keyList'))
	result = Key(chain_cfg=chain_cfg, keylist=keylist)
	return result

def serialize_Key__chain_cfg_json(obj):
	output = OrderedDict()
	output['chain'] = obj.chain
	output['name'] = obj.name
	return output

def serialize_Key_key_json(obj):
	output = OrderedDict()
	output['key-number'] = obj.key_number
	if obj.key_string is not None:
		output['key-string'] = obj.key_string
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Key_key_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Key_key_json(item))
	return output

def serialize_Key_json(obj):
	output = OrderedDict()
	output['chain-cfg'] = serialize_Key__chain_cfg_json(obj.chain_cfg)
	if obj.keylist is not None:
		output['keyList'] = serialize_list_Key_key_json(obj.keylist)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Key_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Key_json(item))
	return list(container)

class Key__chain_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	chain=PosRangedInteger(0, 1)
	name=SizedString(1, 16)
	def __init__(self, chain, name):
		self.chain = chain
		self.name = name

	def __str__(self):
		return str(self.chain) + '+' + str(self.name)

class Key(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, chain_cfg, keylist=None):
		self.chain_cfg = chain_cfg
		self.keylist = keylist

	def __str__(self):
		return str(self.chain_cfg)

class Key_chain_cfg_name__chain_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	chain=PosRangedInteger(0, 1)
	name=SizedString(1, 16)
	def __init__(self, chain, name):
		self.chain = chain
		self.name = name

	def __str__(self):
		return str(self.chain) + '+' + str(self.name)

class Key_chain_cfg_name(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, chain_cfg):
		self.chain_cfg = chain_cfg

	def __str__(self):
		return str(self.chain_cfg)

class Key_key(AxapiObject):
	__metaclass__ = StructMeta 
	key_number=PosRangedInteger(1, 255)
	key_string=SizedString(1, 255)
	def __init__(self, key_number, key_string=None):
		self.key_number = key_number
		self.key_string = key_string

	def __str__(self):
		return str(self.key_number)

class KeyClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getKey(self, key_chain_cfg_name):
		"""
		Retrieve the key identified by the specified identifier
		
		Args:
			key_chain_cfg_name Key_chain_cfg_name
		
		Returns:
			An instance of the Key class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(key_chain_cfg_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified key does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('key')
		return deserialize_Key_json(payload)

	def putKey(self, key_chain_cfg_name, key):
		"""
		Replace the object key
		
		Args:
			key_chain_cfg_name Key_chain_cfg_name
			key An instance of the Key class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['key']=serialize_Key_json(key)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(key_chain_cfg_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteKey(self, key_chain_cfg_name):
		"""
		Remove the key identified by the specified identifier from the system
		
		Args:
			key_chain_cfg_name Key_chain_cfg_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(key_chain_cfg_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified key does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllKeysClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitKey(self, key):
		"""
		Create the object key
		
		Args:
			key An instance of the Key class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['key']=serialize_Key_json(key)
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

	def getAllKeys(self):
		"""
		Retrieve all key objects currently pending in the system
		
		Returns:
			A list of Key objects
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
			payload= data.get('keyList')
		return deserialize_list_Key_json(payload)

