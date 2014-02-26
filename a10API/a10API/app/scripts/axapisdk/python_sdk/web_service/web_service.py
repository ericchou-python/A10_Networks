########################################################################################################################
# File name: web_service.py
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
	'https://axapi.a10networks.com/axapi/v3/web-service',
]

def deserialize_Web_service__timeout_policy_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	idle = data.get('idle')
	result = Web_service__timeout_policy(idle=idle)
	return result

def deserialize_Web_service__axapi_timeout_policy_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	axapi_idle = data.get('axapi-idle')
	result = Web_service__axapi_timeout_policy(axapi_idle=axapi_idle)
	return result

def deserialize_Web_service_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	auto_redir = data.get('auto-redir')
	certificate_reset = data.get('certificate-reset')
	port = data.get('port')
	secure_port = data.get('secure-port')
	server = data.get('server')
	secure_server = data.get('secure-server')
	axapi_session_limit = data.get('axapi-session-limit')
	timeout_policy = deserialize_Web_service__timeout_policy_json(data.get('timeout-policy'))
	axapi_timeout_policy = deserialize_Web_service__axapi_timeout_policy_json(data.get('axapi-timeout-policy'))
	result = Web_service(auto_redir=auto_redir, certificate_reset=certificate_reset, port=port, secure_port=secure_port, server=server, secure_server=secure_server, axapi_session_limit=axapi_session_limit, timeout_policy=timeout_policy, axapi_timeout_policy=axapi_timeout_policy)
	return result

def serialize_Web_service__timeout_policy_json(obj):
	output = OrderedDict()
	if obj.idle is not None:
		output['idle'] = obj.idle
	return output

def serialize_Web_service__axapi_timeout_policy_json(obj):
	output = OrderedDict()
	if obj.axapi_idle is not None:
		output['axapi-idle'] = obj.axapi_idle
	return output

def serialize_Web_service_json(obj):
	output = OrderedDict()
	if obj.auto_redir is not None:
		output['auto-redir'] = obj.auto_redir
	if obj.certificate_reset is not None:
		output['certificate-reset'] = obj.certificate_reset
	if obj.port is not None:
		output['port'] = obj.port
	if obj.secure_port is not None:
		output['secure-port'] = obj.secure_port
	if obj.server is not None:
		output['server'] = obj.server
	if obj.secure_server is not None:
		output['secure-server'] = obj.secure_server
	if obj.axapi_session_limit is not None:
		output['axapi-session-limit'] = obj.axapi_session_limit
	if obj.timeout_policy is not None:
		output['timeout-policy'] = serialize_Web_service__timeout_policy_json(obj.timeout_policy)
	if obj.axapi_timeout_policy is not None:
		output['axapi-timeout-policy'] = serialize_Web_service__axapi_timeout_policy_json(obj.axapi_timeout_policy)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Web_service_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Web_service_json(item))
	return list(container)

class Web_service__timeout_policy(AxapiObject):
	__metaclass__ = StructMeta 
	idle=PosRangedInteger(0, 60)
	def __init__(self, idle=None):
		self.idle = idle

	def __str__(self):
		return ""

class Web_service__axapi_timeout_policy(AxapiObject):
	__metaclass__ = StructMeta 
	axapi_idle=PosRangedInteger(0, 60)
	def __init__(self, axapi_idle=None):
		self.axapi_idle = axapi_idle

	def __str__(self):
		return ""

class Web_service(AxapiObject):
	__metaclass__ = StructMeta 
	auto_redir=PosRangedInteger(0, 1)
	certificate_reset=PosRangedInteger(0, 1)
	port=PosRangedInteger(1, 65535)
	secure_port=PosRangedInteger(1, 65535)
	server=PosRangedInteger(0, 1)
	secure_server=PosRangedInteger(0, 1)
	axapi_session_limit=PosRangedInteger(1, 100)
	def __init__(self, auto_redir=None, certificate_reset=None, port=None, secure_port=None, server=None, secure_server=None, axapi_session_limit=None, timeout_policy=None, axapi_timeout_policy=None):
		self.auto_redir = auto_redir
		self.certificate_reset = certificate_reset
		self.port = port
		self.secure_port = secure_port
		self.server = server
		self.secure_server = secure_server
		self.axapi_session_limit = axapi_session_limit
		self.timeout_policy = timeout_policy
		self.axapi_timeout_policy = axapi_timeout_policy

	def __str__(self):
		return ""

class WebserviceClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getWebservice(self):
		"""
		Retrieve the web_service identified by the specified identifier
		
		Returns:
			An instance of the Web_service class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified web_service does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('web-service')
		return deserialize_Web_service_json(payload)

	def putWebservice(self, web_service):
		"""
		Replace the object web_service
		
		Args:
			web_service An instance of the Web_service class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['web-service']=serialize_Web_service_json(web_service)
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

	def deleteWebservice(self):
		"""
		Remove the web_service identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified web_service does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllWebservicesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitWebservice(self, web_service):
		"""
		Create the object web_service
		
		Args:
			web_service An instance of the Web_service class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['web-service']=serialize_Web_service_json(web_service)
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

	def getAllWebservices(self):
		"""
		Retrieve all web_service objects currently pending in the system
		
		Returns:
			A list of Web_service objects
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
			payload= data.get('web-serviceList')
		return deserialize_list_Web_service_json(payload)

