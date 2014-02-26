########################################################################################################################
# File name: backup_log.py
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
	'https://axapi.a10networks.com/axapi/v3/backup/log',
]

def deserialize_Log__expedite_cfg__period_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	period = data.get('period')
	date = data.get('date')
	day = data.get('day')
	month = data.get('month')
	week = data.get('week')
	all = data.get('all')
	result = Log__expedite_cfg__period_cfg(period=period, date=date, day=day, month=month, week=week, all=all)
	return result

def deserialize_Log__expedite_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	expedite = data.get('expedite')
	period_cfg = deserialize_Log__expedite_cfg__period_cfg_json(data.get('period-cfg'))
	stats_data = data.get('stats-data')
	use_mgmt_port = data.get('use-mgmt-port')
	result = Log__expedite_cfg(expedite=expedite, period_cfg=period_cfg, stats_data=stats_data, use_mgmt_port=use_mgmt_port)
	return result

def deserialize_Log_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	expedite_cfg = deserialize_Log__expedite_cfg_json(data.get('expedite-cfg'))
	remote_file = data.get('remote-file')
	file_name = data.get('file_name')
	result = Log(expedite_cfg=expedite_cfg, remote_file=remote_file, file_name=file_name)
	return result

def serialize_Log__expedite_cfg__period_cfg_json(obj):
	output = OrderedDict()
	if obj.period is not None:
		output['period'] = obj.period
	if obj.date is not None:
		output['date'] = obj.date
	if obj.day is not None:
		output['day'] = obj.day
	if obj.month is not None:
		output['month'] = obj.month
	if obj.week is not None:
		output['week'] = obj.week
	if obj.all is not None:
		output['all'] = obj.all
	return output

def serialize_Log__expedite_cfg_json(obj):
	output = OrderedDict()
	if obj.expedite is not None:
		output['expedite'] = obj.expedite
	if obj.period_cfg is not None:
		output['period-cfg'] = serialize_Log__expedite_cfg__period_cfg_json(obj.period_cfg)
	if obj.stats_data is not None:
		output['stats-data'] = obj.stats_data
	if obj.use_mgmt_port is not None:
		output['use-mgmt-port'] = obj.use_mgmt_port
	return output

def serialize_Log_json(obj):
	output = OrderedDict()
	if obj.expedite_cfg is not None:
		output['expedite-cfg'] = serialize_Log__expedite_cfg_json(obj.expedite_cfg)
	if obj.remote_file is not None:
		output['remote-file'] = obj.remote_file
	if obj.file_name is not None:
		output['file_name'] = obj.file_name
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

class Log__expedite_cfg__period_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	period=PosRangedInteger(0, 1)
	date=PosRangedInteger(1, 31)
	day=PosRangedInteger(0, 1)
	month=PosRangedInteger(0, 1)
	week=PosRangedInteger(0, 1)
	all=PosRangedInteger(0, 1)
	def __init__(self, period=None, date=None, day=None, month=None, week=None, all=None):
		self.period = period
		self.date = date
		self.day = day
		self.month = month
		self.week = week
		self.all = all

	def __str__(self):
		return ""

class Log__expedite_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	expedite=PosRangedInteger(0, 1)
	stats_data=PosRangedInteger(0, 1)
	use_mgmt_port=PosRangedInteger(0, 1)
	def __init__(self, expedite=None, period_cfg=None, stats_data=None, use_mgmt_port=None):
		self.expedite = expedite
		self.period_cfg = period_cfg
		self.stats_data = stats_data
		self.use_mgmt_port = use_mgmt_port

	def __str__(self):
		return ""

class Log(AxapiObject):
	__metaclass__ = StructMeta 
	remote_file=SizedString(1, 255)
	file_name=SizedString(1, 255)
	def __init__(self, expedite_cfg=None, remote_file=None, file_name=None):
		self.expedite_cfg = expedite_cfg
		self.remote_file = remote_file
		self.file_name = file_name

	def __str__(self):
		return ""

class BackupLogClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getBackupLog(self):
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

	def putBackupLog(self, log):
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

	def deleteBackupLog(self):
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

class AllBackupLogsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitBackupLog(self, log):
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

	def getAllBackupLogs(self):
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

