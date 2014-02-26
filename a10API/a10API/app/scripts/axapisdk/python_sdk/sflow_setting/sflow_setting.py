########################################################################################################################
# File name: sflow_setting.py
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
	'https://axapi.a10networks.com/axapi/v3/sflow/setting',
]

def deserialize_Setting_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	max_header = data.get('max-header')
	source_ip_use_mgmt = data.get('source-ip-use-mgmt')
	packet_sampling_rate = data.get('packet-sampling-rate')
	counter_polling_interval = data.get('counter-polling-interval')
	result = Setting(max_header=max_header, source_ip_use_mgmt=source_ip_use_mgmt, packet_sampling_rate=packet_sampling_rate, counter_polling_interval=counter_polling_interval)
	return result

def serialize_Setting_json(obj):
	output = OrderedDict()
	if obj.max_header is not None:
		output['max-header'] = obj.max_header
	if obj.source_ip_use_mgmt is not None:
		output['source-ip-use-mgmt'] = obj.source_ip_use_mgmt
	if obj.packet_sampling_rate is not None:
		output['packet-sampling-rate'] = obj.packet_sampling_rate
	if obj.counter_polling_interval is not None:
		output['counter-polling-interval'] = obj.counter_polling_interval
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Setting_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Setting_json(item))
	return list(container)

class Setting(AxapiObject):
	__metaclass__ = StructMeta 
	max_header=PosRangedInteger(14, 512)
	source_ip_use_mgmt=PosRangedInteger(0, 1)
	packet_sampling_rate=PosRangedInteger(10, 1000000)
	counter_polling_interval=PosRangedInteger(1, 200)
	def __init__(self, max_header=None, source_ip_use_mgmt=None, packet_sampling_rate=None, counter_polling_interval=None):
		self.max_header = max_header
		self.source_ip_use_mgmt = source_ip_use_mgmt
		self.packet_sampling_rate = packet_sampling_rate
		self.counter_polling_interval = counter_polling_interval

	def __str__(self):
		return ""

class SflowSettingClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSflowSetting(self):
		"""
		Retrieve the setting identified by the specified identifier
		
		Returns:
			An instance of the Setting class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified setting does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('setting')
		return deserialize_Setting_json(payload)

	def putSflowSetting(self, setting):
		"""
		Replace the object setting
		
		Args:
			setting An instance of the Setting class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['setting']=serialize_Setting_json(setting)
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

	def deleteSflowSetting(self):
		"""
		Remove the setting identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified setting does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSflowSettingsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSflowSetting(self, setting):
		"""
		Create the object setting
		
		Args:
			setting An instance of the Setting class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['setting']=serialize_Setting_json(setting)
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

	def getAllSflowSettings(self):
		"""
		Retrieve all setting objects currently pending in the system
		
		Returns:
			A list of Setting objects
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
			payload= data.get('settingList')
		return deserialize_list_Setting_json(payload)

