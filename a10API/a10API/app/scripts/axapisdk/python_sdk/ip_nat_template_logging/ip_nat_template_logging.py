########################################################################################################################
# File name: ip_nat_template_logging.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/nat/template/logging',
]

def deserialize_Logging__log__port_mappings_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	both = data.get('both')
	creation = data.get('creation')
	result = Logging__log__port_mappings(both=both, creation=creation)
	return result

def deserialize_Logging__log_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sessions = data.get('sessions')
	port_mappings = deserialize_Logging__log__port_mappings_json(data.get('port-mappings'))
	result = Logging__log(sessions=sessions, port_mappings=port_mappings)
	return result

def deserialize_Logging__source_port_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	source_port_num = data.get('source-port-num')
	any = data.get('any')
	result = Logging__source_port(source_port_num=source_port_num, any=any)
	return result

def deserialize_Logging_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	facility = data.get('facility')
	include_destination = data.get('include-destination')
	include_rip_rport = data.get('include-rip-rport')
	log = deserialize_Logging__log_json(data.get('log'))
	severity = data.get('severity')
	source_port = deserialize_Logging__source_port_json(data.get('source-port'))
	result = Logging(name=name, facility=facility, include_destination=include_destination, include_rip_rport=include_rip_rport, log=log, severity=severity, source_port=source_port)
	return result

def serialize_Logging__log__port_mappings_json(obj):
	output = OrderedDict()
	output['both'] = obj.both
	output['creation'] = obj.creation
	return output

def serialize_Logging__log_json(obj):
	output = OrderedDict()
	output['sessions'] = obj.sessions
	output['port-mappings'] = serialize_Logging__log__port_mappings_json(obj.port_mappings)
	return output

def serialize_Logging__source_port_json(obj):
	output = OrderedDict()
	output['source-port-num'] = obj.source_port_num
	output['any'] = obj.any
	return output

def serialize_Logging_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.facility is not None:
		output['facility'] = obj.facility
	if obj.include_destination is not None:
		output['include-destination'] = obj.include_destination
	if obj.include_rip_rport is not None:
		output['include-rip-rport'] = obj.include_rip_rport
	if obj.log is not None:
		output['log'] = serialize_Logging__log_json(obj.log)
	if obj.severity is not None:
		output['severity'] = obj.severity
	if obj.source_port is not None:
		output['source-port'] = serialize_Logging__source_port_json(obj.source_port)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Logging_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Logging_json(item))
	return list(container)

class Logging_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class Logging__log__port_mappings(AxapiObject):
	__metaclass__ = StructMeta 
	both=PosRangedInteger(0, 1)
	creation=PosRangedInteger(0, 1)
	def __init__(self, both, creation):
		self.both = both
		self.creation = creation

	def __str__(self):
		return str(self.both) + '+' + str(self.creation)

class Logging__log(AxapiObject):
	__metaclass__ = StructMeta 
	sessions=PosRangedInteger(0, 1)
	def __init__(self, sessions, port_mappings):
		self.sessions = sessions
		self.port_mappings = port_mappings

	def __str__(self):
		return str(self.sessions) + '+' + str(self.port_mappings)

class Logging__source_port(AxapiObject):
	__metaclass__ = StructMeta 
	source_port_num=PosRangedInteger(1, 65535)
	any=PosRangedInteger(0, 1)
	def __init__(self, source_port_num, any):
		self.source_port_num = source_port_num
		self.any = any

	def __str__(self):
		return str(self.source_port_num) + '+' + str(self.any)

class Logging(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	facility = Enum(['kernel', 'user', 'mail', 'daemon', 'security-authorization', 'syslog', 'line-printer', 'news', 'uucp', 'cron', 'security-authorization-private', 'ftp', 'ntp', 'audit', 'alert', 'clock', 'local0', 'local1', 'local2', 'local3', 'local4', 'local5', 'local6', 'local7'])
	include_destination=PosRangedInteger(0, 1)
	include_rip_rport=PosRangedInteger(0, 1)
	severity = Enum(['emergency', 'alert', 'critical', 'error', 'warning', 'notice', 'informational', 'debugging'])
	def __init__(self, name, facility=None, include_destination=None, include_rip_rport=None, log=None, severity=None, source_port=None):
		self.name = name
		self.facility = facility
		self.include_destination = include_destination
		self.include_rip_rport = include_rip_rport
		self.log = log
		self.severity = severity
		self.source_port = source_port

	def __str__(self):
		return str(self.name)

class IpNatTemplateLoggingClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpNatTemplateLogging(self, logging_name):
		"""
		Retrieve the logging identified by the specified identifier
		
		Args:
			logging_name Logging_name
		
		Returns:
			An instance of the Logging class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(logging_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified logging does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('logging')
		return deserialize_Logging_json(payload)

	def putIpNatTemplateLogging(self, logging_name, logging):
		"""
		Replace the object logging
		
		Args:
			logging_name Logging_name
			logging An instance of the Logging class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['logging']=serialize_Logging_json(logging)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(logging_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpNatTemplateLogging(self, logging_name):
		"""
		Remove the logging identified by the specified identifier from the system
		
		Args:
			logging_name Logging_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(logging_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified logging does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpNatTemplateLoggingsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpNatTemplateLogging(self, logging):
		"""
		Create the object logging
		
		Args:
			logging An instance of the Logging class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['logging']=serialize_Logging_json(logging)
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

	def getAllIpNatTemplateLoggings(self):
		"""
		Retrieve all logging objects currently pending in the system
		
		Returns:
			A list of Logging objects
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
			payload= data.get('loggingList')
		return deserialize_list_Logging_json(payload)

