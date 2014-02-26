########################################################################################################################
# File name: clock.py
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
	'https://axapi.a10networks.com/axapi/v3/clock',
]

def deserialize_Clock__set__time_cfg_json(obj):
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
	result = Clock__set__time_cfg(time=time, month=month, day_of_month=day_of_month, month_2=month_2, day_of_month_2=day_of_month_2, year=year)
	return result

def deserialize_Clock__set_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	time_cfg = deserialize_Clock__set__time_cfg_json(data.get('time-cfg'))
	result = Clock__set(time_cfg=time_cfg)
	return result

def deserialize_Clock__timezone__timezone_index_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timezone_index = data.get('timezone-index')
	nodst = data.get('nodst')
	result = Clock__timezone__timezone_index_cfg(timezone_index=timezone_index, nodst=nodst)
	return result

def deserialize_Clock__timezone_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timezone_index_cfg = deserialize_Clock__timezone__timezone_index_cfg_json(data.get('timezone-index-cfg'))
	result = Clock__timezone(timezone_index_cfg=timezone_index_cfg)
	return result

def deserialize_Clock_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	set = deserialize_Clock__set_json(data.get('set'))
	timezone = deserialize_Clock__timezone_json(data.get('timezone'))
	result = Clock(set=set, timezone=timezone)
	return result

class Clock__set__time_cfg(AxapiObject):
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

class Clock__set(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, time_cfg=None):
		self.time_cfg = time_cfg

	def __str__(self):
		return ""

class Clock__timezone__timezone_index_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	timezone_index = Enum(['UTC'])
	nodst=PosRangedInteger(0, 1)
	def __init__(self, timezone_index=None, nodst=None):
		self.timezone_index = timezone_index
		self.nodst = nodst

	def __str__(self):
		return ""

class Clock__timezone(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, timezone_index_cfg=None):
		self.timezone_index_cfg = timezone_index_cfg

	def __str__(self):
		return ""

class Clock(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, set=None, timezone=None):
		self.set = set
		self.timezone = timezone

	def __str__(self):
		return ""

class ClockClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getClock(self):
		"""
		Retrieve the clock identified by the specified identifier
		
		Returns:
			An instance of the Clock class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified clock does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('clock')
		return deserialize_Clock_json(payload)

