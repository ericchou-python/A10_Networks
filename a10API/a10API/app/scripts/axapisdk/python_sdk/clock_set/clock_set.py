########################################################################################################################
# File name: clock_set.py
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
	'https://axapi.a10networks.com/axapi/v3/clock/set',
]

def deserialize_Set__time_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	time = data.get('time')
	month = data.get('month')
	day_of_month = data.get('day-of-month')
	month_2 = data.get('month-2')
	day_of_month_2 = data.get('day-of-month-2')
	year = data.get('year')
	result = Set__time_cfg(time=time, month=month, day_of_month=day_of_month, month_2=month_2, day_of_month_2=day_of_month_2, year=year)
	return result

def deserialize_Set_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	time_cfg = deserialize_Set__time_cfg_json(data.get('time-cfg'))
	result = Set(time_cfg=time_cfg)
	return result

def serialize_Set__time_cfg_json(obj):
	output = OrderedDict()
	if obj.time is not None:
		output['time'] = obj.time
	if obj.month is not None:
		output['month'] = obj.month
	if obj.day_of_month is not None:
		output['day-of-month'] = obj.day_of_month
	if obj.month_2 is not None:
		output['month-2'] = obj.month_2
	if obj.day_of_month_2 is not None:
		output['day-of-month-2'] = obj.day_of_month_2
	if obj.year is not None:
		output['year'] = obj.year
	return output

def serialize_Set_json(obj):
	output = OrderedDict()
	if obj.time_cfg is not None:
		output['time-cfg'] = serialize_Set__time_cfg_json(obj.time_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Set_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Set_json(item))
	return list(container)

class Set__time_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	time=SizedString(1, 255)
	month = Enum(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
	day_of_month=PosRangedInteger(1, 31)
	month_2 = Enum(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
	day_of_month_2=PosRangedInteger(1, 31)
	year=PosRangedInteger(2005, 2035)
	def __init__(self, time=None, month=None, day_of_month=None, month_2=None, day_of_month_2=None, year=None):
		self.time = time
		self.month = month
		self.day_of_month = day_of_month
		self.month_2 = month_2
		self.day_of_month_2 = day_of_month_2
		self.year = year

	def __str__(self):
		return ""

class Set(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, time_cfg=None):
		self.time_cfg = time_cfg

	def __str__(self):
		return ""

class ClockSetClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getClockSet(self):
		"""
		Retrieve the set identified by the specified identifier
		
		Returns:
			An instance of the Set class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified set does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('set')
		return deserialize_Set_json(payload)

	def putClockSet(self, set):
		"""
		Replace the object set
		
		Args:
			set An instance of the Set class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['set']=serialize_Set_json(set)
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

	def deleteClockSet(self):
		"""
		Remove the set identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified set does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllClockSetsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitClockSet(self, set):
		"""
		Create the object set
		
		Args:
			set An instance of the Set class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['set']=serialize_Set_json(set)
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

	def getAllClockSets(self):
		"""
		Retrieve all set objects currently pending in the system
		
		Returns:
			A list of Set objects
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
			payload= data.get('setList')
		return deserialize_list_Set_json(payload)

