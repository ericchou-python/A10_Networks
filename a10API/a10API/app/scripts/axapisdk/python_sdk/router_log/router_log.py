########################################################################################################################
# File name: router_log.py
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
	'https://axapi.a10networks.com/axapi/v3/router/log',
]

def deserialize_Log__file_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	per_protocol = data.get('per-protocol')
	rotate = data.get('rotate')
	size = data.get('size')
	result = Log__file(name=name, per_protocol=per_protocol, rotate=rotate, size=size)
	return result

def deserialize_Log_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	file = deserialize_Log__file_json(data.get('file'))
	log_buffer = data.get('log-buffer')
	record_priority = data.get('record-priority')
	stdout = data.get('stdout')
	trap = data.get('trap')
	result = Log(file=file, log_buffer=log_buffer, record_priority=record_priority, stdout=stdout, trap=trap)
	return result

def serialize_Log__file_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	if obj.per_protocol is not None:
		output['per-protocol'] = obj.per_protocol
	if obj.rotate is not None:
		output['rotate'] = obj.rotate
	if obj.size is not None:
		output['size'] = obj.size
	return output

def serialize_Log_json(obj):
	output = OrderedDict()
	if obj.file is not None:
		output['file'] = serialize_Log__file_json(obj.file)
	if obj.log_buffer is not None:
		output['log-buffer'] = obj.log_buffer
	if obj.record_priority is not None:
		output['record-priority'] = obj.record_priority
	if obj.stdout is not None:
		output['stdout'] = obj.stdout
	if obj.trap is not None:
		output['trap'] = obj.trap
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Log_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Log_json(item))
	return list(container)

class Log__file(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	per_protocol=PosRangedInteger(0, 1)
	rotate=PosRangedInteger(0, 100)
	size=PosRangedInteger(0, 1000000)
	def __init__(self, name=None, per_protocol=None, rotate=None, size=None):
		self.name = name
		self.per_protocol = per_protocol
		self.rotate = rotate
		self.size = size

	def __str__(self):
		return ""

class Log(AxapiObject):
	__metaclass__ = StructMeta 
	log_buffer=PosRangedInteger(0, 1)
	record_priority=PosRangedInteger(0, 1)
	stdout=PosRangedInteger(0, 1)
	trap = Enum(['alerts', 'critical', 'debugging', 'emergencies', 'errors', 'informational', 'notifications', 'warnings'])
	def __init__(self, file=None, log_buffer=None, record_priority=None, stdout=None, trap=None):
		self.file = file
		self.log_buffer = log_buffer
		self.record_priority = record_priority
		self.stdout = stdout
		self.trap = trap

	def __str__(self):
		return ""

class RouterLogClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRouterLog(self):
		"""
		Retrieve the log identified by the specified identifier
		
		Returns:
			An instance of the Log class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified log does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('log')
		return deserialize_Log_json(payload)

	def putRouterLog(self, log):
		"""
		Replace the object log
		
		Args:
			log An instance of the Log class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['log']=serialize_Log_json(log)
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

	def deleteRouterLog(self):
		"""
		Remove the log identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified log does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllRouterLogsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitRouterLog(self, log):
		"""
		Create the object log
		
		Args:
			log An instance of the Log class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['log']=serialize_Log_json(log)
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

	def getAllRouterLogs(self):
		"""
		Retrieve all log objects currently pending in the system
		
		Returns:
			A list of Log objects
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
			payload= data.get('logList')
		return deserialize_list_Log_json(payload)

