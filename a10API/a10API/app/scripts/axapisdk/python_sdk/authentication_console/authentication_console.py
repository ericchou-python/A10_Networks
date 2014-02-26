########################################################################################################################
# File name: authentication_console.py
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
	'https://axapi.a10networks.com/axapi/v3/authentication/console',
]

def deserialize_Console__type_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type = data.get('type')
	ldap = data.get('ldap')
	local = data.get('local')
	radius = data.get('radius')
	tacplus = data.get('tacplus')
	result = Console__type_cfg(type=type, ldap=ldap, local=local, radius=radius, tacplus=tacplus)
	return result

def deserialize_Console_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type_cfg = deserialize_Console__type_cfg_json(data.get('type-cfg'))
	result = Console(type_cfg=type_cfg)
	return result

def serialize_Console__type_cfg_json(obj):
	output = OrderedDict()
	if obj.type is not None:
		output['type'] = obj.type
	if obj.ldap is not None:
		output['ldap'] = obj.ldap
	if obj.local is not None:
		output['local'] = obj.local
	if obj.radius is not None:
		output['radius'] = obj.radius
	if obj.tacplus is not None:
		output['tacplus'] = obj.tacplus
	return output

def serialize_Console_json(obj):
	output = OrderedDict()
	if obj.type_cfg is not None:
		output['type-cfg'] = serialize_Console__type_cfg_json(obj.type_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Console_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Console_json(item))
	return list(container)

class Console__type_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	type=PosRangedInteger(0, 1)
	ldap=PosRangedInteger(0, 1)
	local=PosRangedInteger(0, 1)
	radius=PosRangedInteger(0, 1)
	tacplus=PosRangedInteger(0, 1)
	def __init__(self, type=None, ldap=None, local=None, radius=None, tacplus=None):
		self.type = type
		self.ldap = ldap
		self.local = local
		self.radius = radius
		self.tacplus = tacplus

	def __str__(self):
		return ""

class Console(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, type_cfg=None):
		self.type_cfg = type_cfg

	def __str__(self):
		return ""

class AuthenticationConsoleClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getAuthenticationConsole(self):
		"""
		Retrieve the console identified by the specified identifier
		
		Returns:
			An instance of the Console class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified console does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('console')
		return deserialize_Console_json(payload)

	def putAuthenticationConsole(self, console):
		"""
		Replace the object console
		
		Args:
			console An instance of the Console class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['console']=serialize_Console_json(console)
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

	def deleteAuthenticationConsole(self):
		"""
		Remove the console identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified console does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllAuthenticationConsolesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitAuthenticationConsole(self, console):
		"""
		Create the object console
		
		Args:
			console An instance of the Console class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['console']=serialize_Console_json(console)
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

	def getAllAuthenticationConsoles(self):
		"""
		Retrieve all console objects currently pending in the system
		
		Returns:
			A list of Console objects
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
			payload= data.get('consoleList')
		return deserialize_list_Console_json(payload)

