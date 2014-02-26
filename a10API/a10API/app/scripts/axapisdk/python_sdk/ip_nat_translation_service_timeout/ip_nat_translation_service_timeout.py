########################################################################################################################
# File name: ip_nat_translation_service_timeout.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/nat/translation/service-timeout',
]

def deserialize_Service_timeout_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	service_type = data.get('service-type')
	port = data.get('port')
	timeout_val = data.get('timeout-val')
	fast = data.get('fast')
	result = Service_timeout(service_type=service_type, port=port, timeout_val=timeout_val, fast=fast)
	return result

def serialize_Service_timeout_json(obj):
	output = OrderedDict()
	output['service-type'] = obj.service_type
	output['port'] = obj.port
	output['timeout-val'] = obj.timeout_val
	output['fast'] = obj.fast
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Service_timeout_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Service_timeout_json(item))
	return list(container)

class Service_timeout_service_type_port(AxapiObject):
	__metaclass__ = StructMeta 
	service_type = Enum(['tcp', 'udp'])
	port=PosRangedInteger(1, 65535)
	def __init__(self, service_type, port):
		self.service_type = service_type
		self.port = port

	def __str__(self):
		return str(self.service_type) + '+' + str(self.port)

class Service_timeout(AxapiObject):
	__metaclass__ = StructMeta 
	service_type = Enum(['tcp', 'udp'])
	port=PosRangedInteger(1, 65535)
	timeout_val=PosRangedInteger(2, 15000)
	fast=PosRangedInteger(0, 1)
	def __init__(self, service_type, port, timeout_val, fast):
		self.service_type = service_type
		self.port = port
		self.timeout_val = timeout_val
		self.fast = fast

	def __str__(self):
		return str(self.service_type) + '+' + str(self.port) + '+' + str(self.timeout_val) + '+' + str(self.fast)

class IpNatTranslationServicetimeoutClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpNatTranslationServicetimeout(self, service_timeout_service_type_port):
		"""
		Retrieve the service_timeout identified by the specified identifier
		
		Args:
			service_timeout_service_type_port Service_timeout_service_type_port
		
		Returns:
			An instance of the Service_timeout class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(service_timeout_service_type_port) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified service_timeout does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('service-timeout')
		return deserialize_Service_timeout_json(payload)

	def putIpNatTranslationServicetimeout(self, service_timeout_service_type_port, service_timeout):
		"""
		Replace the object service_timeout
		
		Args:
			service_timeout_service_type_port Service_timeout_service_type_port
			service_timeout An instance of the Service_timeout class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['service-timeout']=serialize_Service_timeout_json(service_timeout)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(service_timeout_service_type_port) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpNatTranslationServicetimeout(self, service_timeout_service_type_port):
		"""
		Remove the service_timeout identified by the specified identifier from the
		system
		
		Args:
			service_timeout_service_type_port Service_timeout_service_type_port
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(service_timeout_service_type_port) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified service_timeout does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpNatTranslationServicetimeoutsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpNatTranslationServicetimeout(self, service_timeout):
		"""
		Create the object service_timeout
		
		Args:
			service_timeout An instance of the Service_timeout class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['service-timeout']=serialize_Service_timeout_json(service_timeout)
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

	def getAllIpNatTranslationServicetimeouts(self):
		"""
		Retrieve all service_timeout objects currently pending in the system
		
		Returns:
			A list of Service_timeout objects
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
			payload= data.get('service-timeoutList')
		return deserialize_list_Service_timeout_json(payload)

