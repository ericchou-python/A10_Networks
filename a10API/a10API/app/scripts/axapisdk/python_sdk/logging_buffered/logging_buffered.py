########################################################################################################################
# File name: logging_buffered.py
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
	'https://axapi.a10networks.com/axapi/v3/logging/buffered',
]

def deserialize_Buffered_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	buffersize = data.get('buffersize')
	levelnum = data.get('levelnum')
	levelname = data.get('levelname')
	result = Buffered(buffersize=buffersize, levelnum=levelnum, levelname=levelname)
	return result

def serialize_Buffered_json(obj):
	output = OrderedDict()
	if obj.buffersize is not None:
		output['buffersize'] = obj.buffersize
	if obj.levelnum is not None:
		output['levelnum'] = obj.levelnum
	if obj.levelname is not None:
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

def deserialize_list_Buffered_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Buffered_json(item))
	return list(container)

class Buffered(AxapiObject):
	__metaclass__ = StructMeta 
	buffersize=PosRangedInteger(10000, 50000)
	levelnum=PosRangedInteger(0, 7)
	levelname = Enum(['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debugging'])
	def __init__(self, buffersize=None, levelnum=None, levelname=None):
		self.buffersize = buffersize
		self.levelnum = levelnum
		self.levelname = levelname

	def __str__(self):
		return ""

class LoggingBufferedClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLoggingBuffered(self):
		"""
		Retrieve the buffered identified by the specified identifier
		
		Returns:
			An instance of the Buffered class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified buffered does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('buffered')
		return deserialize_Buffered_json(payload)

	def putLoggingBuffered(self, buffered):
		"""
		Replace the object buffered
		
		Args:
			buffered An instance of the Buffered class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['buffered']=serialize_Buffered_json(buffered)
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

	def deleteLoggingBuffered(self):
		"""
		Remove the buffered identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified buffered does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllLoggingBufferedsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitLoggingBuffered(self, buffered):
		"""
		Create the object buffered
		
		Args:
			buffered An instance of the Buffered class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['buffered']=serialize_Buffered_json(buffered)
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

	def getAllLoggingBuffereds(self):
		"""
		Retrieve all buffered objects currently pending in the system
		
		Returns:
			A list of Buffered objects
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
			payload= data.get('bufferedList')
		return deserialize_list_Buffered_json(payload)

