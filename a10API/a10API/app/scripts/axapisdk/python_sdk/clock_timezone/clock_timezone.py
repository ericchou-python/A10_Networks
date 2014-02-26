########################################################################################################################
# File name: clock_timezone.py
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
	'https://axapi.a10networks.com/axapi/v3/clock/timezone',
]

def deserialize_Timezone__timezone_index_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timezone_index = data.get('timezone-index')
	nodst = data.get('nodst')
	result = Timezone__timezone_index_cfg(timezone_index=timezone_index, nodst=nodst)
	return result

def deserialize_Timezone_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timezone_index_cfg = deserialize_Timezone__timezone_index_cfg_json(data.get('timezone-index-cfg'))
	result = Timezone(timezone_index_cfg=timezone_index_cfg)
	return result

def serialize_Timezone__timezone_index_cfg_json(obj):
	output = OrderedDict()
	if obj.timezone_index is not None:
		output['timezone-index'] = obj.timezone_index
	if obj.nodst is not None:
		output['nodst'] = obj.nodst
	return output

def serialize_Timezone_json(obj):
	output = OrderedDict()
	if obj.timezone_index_cfg is not None:
		output['timezone-index-cfg'] = serialize_Timezone__timezone_index_cfg_json(obj.timezone_index_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Timezone_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Timezone_json(item))
	return list(container)

class Timezone__timezone_index_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	timezone_index = Enum(['UTC'])
	nodst=PosRangedInteger(0, 1)
	def __init__(self, timezone_index=None, nodst=None):
		self.timezone_index = timezone_index
		self.nodst = nodst

	def __str__(self):
		return ""

class Timezone(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, timezone_index_cfg=None):
		self.timezone_index_cfg = timezone_index_cfg

	def __str__(self):
		return ""

class ClockTimezoneClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getClockTimezone(self):
		"""
		Retrieve the timezone identified by the specified identifier
		
		Returns:
			An instance of the Timezone class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified timezone does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('timezone')
		return deserialize_Timezone_json(payload)

	def putClockTimezone(self, timezone):
		"""
		Replace the object timezone
		
		Args:
			timezone An instance of the Timezone class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['timezone']=serialize_Timezone_json(timezone)
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

	def deleteClockTimezone(self):
		"""
		Remove the timezone identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified timezone does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllClockTimezonesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitClockTimezone(self, timezone):
		"""
		Create the object timezone
		
		Args:
			timezone An instance of the Timezone class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['timezone']=serialize_Timezone_json(timezone)
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

	def getAllClockTimezones(self):
		"""
		Retrieve all timezone objects currently pending in the system
		
		Returns:
			A list of Timezone objects
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
			payload= data.get('timezoneList')
		return deserialize_list_Timezone_json(payload)

