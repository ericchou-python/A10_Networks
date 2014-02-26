########################################################################################################################
# File name: logging_single_priority.py
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
	'https://axapi.a10networks.com/axapi/v3/logging/single-priority',
]

def deserialize_Single_priority_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	log_severity = data.get('log-severity')
	levelname = data.get('levelname')
	result = Single_priority(log_severity=log_severity, levelname=levelname)
	return result

def serialize_Single_priority_json(obj):
	output = OrderedDict()
	output['log-severity'] = obj.log_severity
	output['levelname'] = obj.levelname
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Single_priority_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Single_priority_json(item))
	return list(container)

class Single_priority_log_severity_levelname(AxapiObject):
	__metaclass__ = StructMeta 
	log_severity=PosRangedInteger(0, 7)
	levelname = Enum(['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debugging'])
	def __init__(self, log_severity, levelname):
		self.log_severity = log_severity
		self.levelname = levelname

	def __str__(self):
		return str(self.log_severity) + '+' + str(self.levelname)

class Single_priority(AxapiObject):
	__metaclass__ = StructMeta 
	log_severity=PosRangedInteger(0, 7)
	levelname = Enum(['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debugging'])
	def __init__(self, log_severity, levelname):
		self.log_severity = log_severity
		self.levelname = levelname

	def __str__(self):
		return str(self.log_severity) + '+' + str(self.levelname)

class LoggingSinglepriorityClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLoggingSinglepriority(self, single_priority_log_severity_levelname):
		"""
		Retrieve the single_priority identified by the specified identifier
		
		Args:
			single_priority_log_severity_levelname Single_priority_log_severity_levelname
		
		Returns:
			An instance of the Single_priority class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(single_priority_log_severity_levelname) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified single_priority does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('single-priority')
		return deserialize_Single_priority_json(payload)

	def putLoggingSinglepriority(self, single_priority_log_severity_levelname, single_priority):
		"""
		Replace the object single_priority
		
		Args:
			single_priority_log_severity_levelname Single_priority_log_severity_levelname
			single_priority An instance of the Single_priority class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['single-priority']=serialize_Single_priority_json(single_priority)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(single_priority_log_severity_levelname) .replace("/", "%2f") + query, payload, headers)
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

	def deleteLoggingSinglepriority(self, single_priority_log_severity_levelname):
		"""
		Remove the single_priority identified by the specified identifier from the
		system
		
		Args:
			single_priority_log_severity_levelname Single_priority_log_severity_levelname
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(single_priority_log_severity_levelname) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified single_priority does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllLoggingSingleprioritysClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitLoggingSinglepriority(self, single_priority):
		"""
		Create the object single_priority
		
		Args:
			single_priority An instance of the Single_priority class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['single-priority']=serialize_Single_priority_json(single_priority)
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

	def getAllLoggingSingleprioritys(self):
		"""
		Retrieve all single_priority objects currently pending in the system
		
		Returns:
			A list of Single_priority objects
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
			payload= data.get('single-priorityList')
		return deserialize_list_Single_priority_json(payload)

