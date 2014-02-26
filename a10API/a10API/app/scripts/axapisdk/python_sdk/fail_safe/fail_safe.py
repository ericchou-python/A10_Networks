########################################################################################################################
# File name: fail_safe.py
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
	'https://axapi.a10networks.com/axapi/v3/fail-safe',
]

def deserialize_Fail_safe_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	fpga_buff_recovery_threshold = data.get('fpga-buff-recovery-threshold')
	hw_error_monitor_disable = data.get('hw-error-monitor-disable')
	hw_error_monitor_enable = data.get('hw-error-monitor-enable')
	hw_error_recovery_timeout = data.get('hw-error-recovery-timeout')
	session_mem_recovery_threshold = data.get('session-mem-recovery-threshold')
	sw_error_monitor_enable = data.get('sw-error-monitor-enable')
	sw_error_recovery_timeout = data.get('sw-error-recovery-timeout')
	total_memory_size_check = data.get('total-memory-size-check')
	log = data.get('log')
	kill = data.get('kill')
	result = Fail_safe(fpga_buff_recovery_threshold=fpga_buff_recovery_threshold, hw_error_monitor_disable=hw_error_monitor_disable, hw_error_monitor_enable=hw_error_monitor_enable, hw_error_recovery_timeout=hw_error_recovery_timeout, session_mem_recovery_threshold=session_mem_recovery_threshold, sw_error_monitor_enable=sw_error_monitor_enable, sw_error_recovery_timeout=sw_error_recovery_timeout, total_memory_size_check=total_memory_size_check, log=log, kill=kill)
	return result

def serialize_Fail_safe_json(obj):
	output = OrderedDict()
	if obj.fpga_buff_recovery_threshold is not None:
		output['fpga-buff-recovery-threshold'] = obj.fpga_buff_recovery_threshold
	if obj.hw_error_monitor_disable is not None:
		output['hw-error-monitor-disable'] = obj.hw_error_monitor_disable
	if obj.hw_error_monitor_enable is not None:
		output['hw-error-monitor-enable'] = obj.hw_error_monitor_enable
	if obj.hw_error_recovery_timeout is not None:
		output['hw-error-recovery-timeout'] = obj.hw_error_recovery_timeout
	if obj.session_mem_recovery_threshold is not None:
		output['session-mem-recovery-threshold'] = obj.session_mem_recovery_threshold
	if obj.sw_error_monitor_enable is not None:
		output['sw-error-monitor-enable'] = obj.sw_error_monitor_enable
	if obj.sw_error_recovery_timeout is not None:
		output['sw-error-recovery-timeout'] = obj.sw_error_recovery_timeout
	if obj.total_memory_size_check is not None:
		output['total-memory-size-check'] = obj.total_memory_size_check
	if obj.log is not None:
		output['log'] = obj.log
	if obj.kill is not None:
		output['kill'] = obj.kill
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Fail_safe_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Fail_safe_json(item))
	return list(container)

class Fail_safe(AxapiObject):
	__metaclass__ = StructMeta 
	fpga_buff_recovery_threshold=PosRangedInteger(1, 10)
	hw_error_monitor_disable=PosRangedInteger(0, 1)
	hw_error_monitor_enable=PosRangedInteger(0, 1)
	hw_error_recovery_timeout=PosRangedInteger(1, 1440)
	session_mem_recovery_threshold=PosRangedInteger(1, 100)
	sw_error_monitor_enable=PosRangedInteger(0, 1)
	sw_error_recovery_timeout=PosRangedInteger(1, 1440)
	total_memory_size_check=PosRangedInteger(1, 256)
	log=PosRangedInteger(0, 1)
	kill=PosRangedInteger(0, 1)
	def __init__(self, fpga_buff_recovery_threshold=None, hw_error_monitor_disable=None, hw_error_monitor_enable=None, hw_error_recovery_timeout=None, session_mem_recovery_threshold=None, sw_error_monitor_enable=None, sw_error_recovery_timeout=None, total_memory_size_check=None, log=None, kill=None):
		self.fpga_buff_recovery_threshold = fpga_buff_recovery_threshold
		self.hw_error_monitor_disable = hw_error_monitor_disable
		self.hw_error_monitor_enable = hw_error_monitor_enable
		self.hw_error_recovery_timeout = hw_error_recovery_timeout
		self.session_mem_recovery_threshold = session_mem_recovery_threshold
		self.sw_error_monitor_enable = sw_error_monitor_enable
		self.sw_error_recovery_timeout = sw_error_recovery_timeout
		self.total_memory_size_check = total_memory_size_check
		self.log = log
		self.kill = kill

	def __str__(self):
		return ""

class FailsafeClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getFailsafe(self):
		"""
		Retrieve the fail_safe identified by the specified identifier
		
		Returns:
			An instance of the Fail_safe class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified fail_safe does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('fail-safe')
		return deserialize_Fail_safe_json(payload)

	def putFailsafe(self, fail_safe):
		"""
		Replace the object fail_safe
		
		Args:
			fail_safe An instance of the Fail_safe class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['fail-safe']=serialize_Fail_safe_json(fail_safe)
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

	def deleteFailsafe(self):
		"""
		Remove the fail_safe identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified fail_safe does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllFailsafesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitFailsafe(self, fail_safe):
		"""
		Create the object fail_safe
		
		Args:
			fail_safe An instance of the Fail_safe class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['fail-safe']=serialize_Fail_safe_json(fail_safe)
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

	def getAllFailsafes(self):
		"""
		Retrieve all fail_safe objects currently pending in the system
		
		Returns:
			A list of Fail_safe objects
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
			payload= data.get('fail-safeList')
		return deserialize_list_Fail_safe_json(payload)

