########################################################################################################################
# File name: backup_periodically.py
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
	'https://axapi.a10networks.com/axapi/v3/backup/periodically',
]

def deserialize_Periodically__period_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	day_2 = data.get('day-2')
	hour_2 = data.get('hour-2')
	week_2 = data.get('week-2')
	result = Periodically__period_cfg(day_2=day_2, hour_2=hour_2, week_2=week_2)
	return result

def deserialize_Periodically_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	system = data.get('system')
	log = data.get('log')
	use_mgmt_port = data.get('use-mgmt-port')
	remote_file = data.get('remote-file')
	file_name = data.get('file_name')
	period_cfg = deserialize_Periodically__period_cfg_json(data.get('period-cfg'))
	use_mgmt_port_2 = data.get('use-mgmt-port-2')
	remote_file_2 = data.get('remote-file-2')
	file_name_2 = data.get('file_name-2')
	result = Periodically(system=system, log=log, use_mgmt_port=use_mgmt_port, remote_file=remote_file, file_name=file_name, period_cfg=period_cfg, use_mgmt_port_2=use_mgmt_port_2, remote_file_2=remote_file_2, file_name_2=file_name_2)
	return result

def serialize_Periodically__period_cfg_json(obj):
	output = OrderedDict()
	if obj.day_2 is not None:
		output['day-2'] = obj.day_2
	if obj.hour_2 is not None:
		output['hour-2'] = obj.hour_2
	if obj.week_2 is not None:
		output['week-2'] = obj.week_2
	return output

def serialize_Periodically_json(obj):
	output = OrderedDict()
	if obj.system is not None:
		output['system'] = obj.system
	if obj.log is not None:
		output['log'] = obj.log
	if obj.use_mgmt_port is not None:
		output['use-mgmt-port'] = obj.use_mgmt_port
	if obj.remote_file is not None:
		output['remote-file'] = obj.remote_file
	if obj.file_name is not None:
		output['file_name'] = obj.file_name
	if obj.period_cfg is not None:
		output['period-cfg'] = serialize_Periodically__period_cfg_json(obj.period_cfg)
	if obj.use_mgmt_port_2 is not None:
		output['use-mgmt-port-2'] = obj.use_mgmt_port_2
	if obj.remote_file_2 is not None:
		output['remote-file-2'] = obj.remote_file_2
	if obj.file_name_2 is not None:
		output['file_name-2'] = obj.file_name_2
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Periodically_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Periodically_json(item))
	return list(container)

class Periodically__period_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	day_2=PosRangedInteger(1, 199)
	hour_2=PosRangedInteger(1, 65534)
	week_2=PosRangedInteger(1, 199)
	def __init__(self, day_2=None, hour_2=None, week_2=None):
		self.day_2 = day_2
		self.hour_2 = hour_2
		self.week_2 = week_2

	def __str__(self):
		return ""

class Periodically(AxapiObject):
	__metaclass__ = StructMeta 
	system=PosRangedInteger(0, 1)
	log=PosRangedInteger(0, 1)
	use_mgmt_port=PosRangedInteger(0, 1)
	remote_file=SizedString(1, 255)
	file_name=SizedString(1, 255)
	use_mgmt_port_2=PosRangedInteger(0, 1)
	remote_file_2=SizedString(1, 255)
	file_name_2=SizedString(1, 255)
	def __init__(self, system=None, log=None, use_mgmt_port=None, remote_file=None, file_name=None, period_cfg=None, use_mgmt_port_2=None, remote_file_2=None, file_name_2=None):
		self.system = system
		self.log = log
		self.use_mgmt_port = use_mgmt_port
		self.remote_file = remote_file
		self.file_name = file_name
		self.period_cfg = period_cfg
		self.use_mgmt_port_2 = use_mgmt_port_2
		self.remote_file_2 = remote_file_2
		self.file_name_2 = file_name_2

	def __str__(self):
		return ""

class BackupPeriodicallyClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getBackupPeriodically(self):
		"""
		Retrieve the periodically identified by the specified identifier
		
		Returns:
			An instance of the Periodically class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified periodically does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('periodically')
		return deserialize_Periodically_json(payload)

	def putBackupPeriodically(self, periodically):
		"""
		Replace the object periodically
		
		Args:
			periodically An instance of the Periodically class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['periodically']=serialize_Periodically_json(periodically)
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

	def deleteBackupPeriodically(self):
		"""
		Remove the periodically identified by the specified identifier from the
		system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified periodically does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllBackupPeriodicallysClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitBackupPeriodically(self, periodically):
		"""
		Create the object periodically
		
		Args:
			periodically An instance of the Periodically class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['periodically']=serialize_Periodically_json(periodically)
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

	def getAllBackupPeriodicallys(self):
		"""
		Retrieve all periodically objects currently pending in the system
		
		Returns:
			A list of Periodically objects
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
			payload= data.get('periodicallyList')
		return deserialize_list_Periodically_json(payload)

