########################################################################################################################
# File name: netflow_monitor_monitor_ve.py
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
	'https://axapi.a10networks.com/axapi/v3/netflow/monitor/monitor/ve',
]

def deserialize_Ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ve_num = data.get('ve_num')
	result = Ve(ve_num=ve_num)
	return result

def serialize_Ve_json(obj):
	output = OrderedDict()
	output['ve_num'] = obj.ve_num
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ve_json(item))
	return list(container)

class Ve_ve_num_ve_num(AxapiObject):
	__metaclass__ = StructMeta 
	ve_num=PosRangedInteger(2, 4094)
	def __init__(self, ve_num):
		self.ve_num = ve_num

	def __str__(self):
		return str(self.ve_num)

class Ve(AxapiObject):
	__metaclass__ = StructMeta 
	ve_num=PosRangedInteger(2, 4094)
	def __init__(self, ve_num):
		self.ve_num = ve_num

	def __str__(self):
		return str(self.ve_num)

class NetflowMonitorMonitorVeClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getNetflowMonitorMonitorVe(self, ve_ve_num_ve_num):
		"""
		Retrieve the ve identified by the specified identifier
		
		Args:
			ve_ve_num_ve_num Ve_ve_num_ve_num
		
		Returns:
			An instance of the Ve class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(ve_ve_num_ve_num) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ve does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ve')
		return deserialize_Ve_json(payload)

	def putNetflowMonitorMonitorVe(self, ve_ve_num_ve_num, ve):
		"""
		Replace the object ve
		
		Args:
			ve_ve_num_ve_num Ve_ve_num_ve_num
			ve An instance of the Ve class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ve']=serialize_Ve_json(ve)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(ve_ve_num_ve_num) .replace("/", "%2f") + query, payload, headers)
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

	def deleteNetflowMonitorMonitorVe(self, ve_ve_num_ve_num):
		"""
		Remove the ve identified by the specified identifier from the system
		
		Args:
			ve_ve_num_ve_num Ve_ve_num_ve_num
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(ve_ve_num_ve_num) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ve does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllNetflowMonitorMonitorVesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitNetflowMonitorMonitorVe(self, ve):
		"""
		Create the object ve
		
		Args:
			ve An instance of the Ve class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ve']=serialize_Ve_json(ve)
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

	def getAllNetflowMonitorMonitorVes(self):
		"""
		Retrieve all ve objects currently pending in the system
		
		Returns:
			A list of Ve objects
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
			payload= data.get('veList')
		return deserialize_list_Ve_json(payload)

