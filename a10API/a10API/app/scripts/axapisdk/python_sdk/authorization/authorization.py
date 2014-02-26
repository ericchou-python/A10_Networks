########################################################################################################################
# File name: authorization.py
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
	'https://axapi.a10networks.com/axapi/v3/authorization',
]

def deserialize_Authorization__method_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tacplus = data.get('tacplus')
	none = data.get('none')
	result = Authorization__method(tacplus=tacplus, none=none)
	return result

def deserialize_Authorization_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	commands = data.get('commands')
	method = deserialize_Authorization__method_json(data.get('method'))
	debug = data.get('debug')
	result = Authorization(commands=commands, method=method, debug=debug)
	return result

def serialize_Authorization__method_json(obj):
	output = OrderedDict()
	if obj.tacplus is not None:
		output['tacplus'] = obj.tacplus
	if obj.none is not None:
		output['none'] = obj.none
	return output

def serialize_Authorization_json(obj):
	output = OrderedDict()
	if obj.commands is not None:
		output['commands'] = obj.commands
	if obj.method is not None:
		output['method'] = serialize_Authorization__method_json(obj.method)
	if obj.debug is not None:
		output['debug'] = obj.debug
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Authorization_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Authorization_json(item))
	return list(container)

class Authorization__method(AxapiObject):
	__metaclass__ = StructMeta 
	tacplus=PosRangedInteger(0, 1)
	none=PosRangedInteger(0, 1)
	def __init__(self, tacplus=None, none=None):
		self.tacplus = tacplus
		self.none = none

	def __str__(self):
		return ""

class Authorization(AxapiObject):
	__metaclass__ = StructMeta 
	commands=PosRangedInteger(0, 15)
	debug=PosRangedInteger(0, 15)
	def __init__(self, commands=None, method=None, debug=None):
		self.commands = commands
		self.method = method
		self.debug = debug

	def __str__(self):
		return ""

class AuthorizationClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getAuthorization(self):
		"""
		Retrieve the authorization identified by the specified identifier
		
		Returns:
			An instance of the Authorization class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified authorization does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('authorization')
		return deserialize_Authorization_json(payload)

	def putAuthorization(self, authorization):
		"""
		Replace the object authorization
		
		Args:
			authorization An instance of the Authorization class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['authorization']=serialize_Authorization_json(authorization)
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

	def deleteAuthorization(self):
		"""
		Remove the authorization identified by the specified identifier from the
		system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified authorization does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllAuthorizationsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitAuthorization(self, authorization):
		"""
		Create the object authorization
		
		Args:
			authorization An instance of the Authorization class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['authorization']=serialize_Authorization_json(authorization)
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

	def getAllAuthorizations(self):
		"""
		Retrieve all authorization objects currently pending in the system
		
		Returns:
			A list of Authorization objects
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
			payload= data.get('authorizationList')
		return deserialize_list_Authorization_json(payload)

