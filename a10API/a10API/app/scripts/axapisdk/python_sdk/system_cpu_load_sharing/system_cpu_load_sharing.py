########################################################################################################################
# File name: system_cpu_load_sharing.py
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
	'https://axapi.a10networks.com/axapi/v3/system/cpu-load-sharing',
]

def deserialize_Cpu_load_sharing__packets_per_second_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	min = data.get('min')
	result = Cpu_load_sharing__packets_per_second(min=min)
	return result

def deserialize_Cpu_load_sharing__cpu_usage_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	low = data.get('low')
	high = data.get('high')
	result = Cpu_load_sharing__cpu_usage(low=low, high=high)
	return result

def deserialize_Cpu_load_sharing_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	disable = data.get('disable')
	packets_per_second = deserialize_Cpu_load_sharing__packets_per_second_json(data.get('packets-per-second'))
	cpu_usage = deserialize_Cpu_load_sharing__cpu_usage_json(data.get('cpu-usage'))
	result = Cpu_load_sharing(disable=disable, packets_per_second=packets_per_second, cpu_usage=cpu_usage)
	return result

def serialize_Cpu_load_sharing__packets_per_second_json(obj):
	output = OrderedDict()
	if obj.min is not None:
		output['min'] = obj.min
	return output

def serialize_Cpu_load_sharing__cpu_usage_json(obj):
	output = OrderedDict()
	if obj.low is not None:
		output['low'] = obj.low
	if obj.high is not None:
		output['high'] = obj.high
	return output

def serialize_Cpu_load_sharing_json(obj):
	output = OrderedDict()
	if obj.disable is not None:
		output['disable'] = obj.disable
	if obj.packets_per_second is not None:
		output['packets-per-second'] = serialize_Cpu_load_sharing__packets_per_second_json(obj.packets_per_second)
	if obj.cpu_usage is not None:
		output['cpu-usage'] = serialize_Cpu_load_sharing__cpu_usage_json(obj.cpu_usage)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Cpu_load_sharing_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Cpu_load_sharing_json(item))
	return list(container)

class Cpu_load_sharing__packets_per_second(AxapiObject):
	__metaclass__ = StructMeta 
	min=PosRangedInteger(0, 30000000)
	def __init__(self, min=None):
		self.min = min

	def __str__(self):
		return ""

class Cpu_load_sharing__cpu_usage(AxapiObject):
	__metaclass__ = StructMeta 
	low=PosRangedInteger(0, 100)
	high=PosRangedInteger(0, 100)
	def __init__(self, low=None, high=None):
		self.low = low
		self.high = high

	def __str__(self):
		return ""

class Cpu_load_sharing(AxapiObject):
	__metaclass__ = StructMeta 
	disable=PosRangedInteger(0, 1)
	def __init__(self, disable=None, packets_per_second=None, cpu_usage=None):
		self.disable = disable
		self.packets_per_second = packets_per_second
		self.cpu_usage = cpu_usage

	def __str__(self):
		return ""

class SystemCpuloadsharingClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSystemCpuloadsharing(self):
		"""
		Retrieve the cpu_load_sharing identified by the specified identifier
		
		Returns:
			An instance of the Cpu_load_sharing class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified cpu_load_sharing does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('cpu-load-sharing')
		return deserialize_Cpu_load_sharing_json(payload)

	def putSystemCpuloadsharing(self, cpu_load_sharing):
		"""
		Replace the object cpu_load_sharing
		
		Args:
			cpu_load_sharing An instance of the Cpu_load_sharing class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['cpu-load-sharing']=serialize_Cpu_load_sharing_json(cpu_load_sharing)
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

	def deleteSystemCpuloadsharing(self):
		"""
		Remove the cpu_load_sharing identified by the specified identifier from
		the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified cpu_load_sharing does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSystemCpuloadsharingsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSystemCpuloadsharing(self, cpu_load_sharing):
		"""
		Create the object cpu_load_sharing
		
		Args:
			cpu_load_sharing An instance of the Cpu_load_sharing class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['cpu-load-sharing']=serialize_Cpu_load_sharing_json(cpu_load_sharing)
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

	def getAllSystemCpuloadsharings(self):
		"""
		Retrieve all cpu_load_sharing objects currently pending in the system
		
		Returns:
			A list of Cpu_load_sharing objects
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
			payload= data.get('cpu-load-sharingList')
		return deserialize_list_Cpu_load_sharing_json(payload)

