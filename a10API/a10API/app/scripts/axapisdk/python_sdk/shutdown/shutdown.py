########################################################################################################################
# File name: shutdown.py
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
	'https://axapi.a10networks.com/axapi/v3/shutdown',
]

def deserialize_Shutdown_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	at = data.get('at')
	py_kw_rsvd_in = data.get('in')
	cancel = data.get('cancel')
	reason = data.get('reason')
	time = data.get('time')
	month = data.get('month')
	day_of_month = data.get('day-of-month')
	result = Shutdown(at=at, py_kw_rsvd_in=py_kw_rsvd_in, cancel=cancel, reason=reason, time=time, month=month, day_of_month=day_of_month)
	return result

def serialize_Shutdown_json(obj):
	output = OrderedDict()
	if obj.at is not None:
		output['at'] = obj.at
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.cancel is not None:
		output['cancel'] = obj.cancel
	if obj.reason is not None:
		output['reason'] = obj.reason
	if obj.time is not None:
		output['time'] = obj.time
	if obj.month is not None:
		output['month'] = obj.month
	if obj.day_of_month is not None:
		output['day-of-month'] = obj.day_of_month
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Shutdown_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Shutdown_json(item))
	return list(container)

class Shutdown(AxapiObject):
	__metaclass__ = StructMeta 
	at=PosRangedInteger(0, 1)
	py_kw_rsvd_in=SizedString(1, 255)
	cancel=PosRangedInteger(0, 1)
	reason=SizedString(1, 127)
	time=SizedString(1, 255)
	month = Enum(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
	day_of_month=PosRangedInteger(1, 31)
	def __init__(self, at=None, py_kw_rsvd_in=None, cancel=None, reason=None, time=None, month=None, day_of_month=None):
		self.at = at
		self.py_kw_rsvd_in = py_kw_rsvd_in
		self.cancel = cancel
		self.reason = reason
		self.time = time
		self.month = month
		self.day_of_month = day_of_month

	def __str__(self):
		return ""

class ShutdownClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getShutdown(self):
		"""
		Retrieve the shutdown identified by the specified identifier
		
		Returns:
			An instance of the Shutdown class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified shutdown does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('shutdown')
		return deserialize_Shutdown_json(payload)

	def putShutdown(self, shutdown):
		"""
		Replace the object shutdown
		
		Args:
			shutdown An instance of the Shutdown class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['shutdown']=serialize_Shutdown_json(shutdown)
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

	def deleteShutdown(self):
		"""
		Remove the shutdown identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified shutdown does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllShutdownsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitShutdown(self, shutdown):
		"""
		Create the object shutdown
		
		Args:
			shutdown An instance of the Shutdown class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['shutdown']=serialize_Shutdown_json(shutdown)
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

	def getAllShutdowns(self):
		"""
		Retrieve all shutdown objects currently pending in the system
		
		Returns:
			A list of Shutdown objects
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
			payload= data.get('shutdownList')
		return deserialize_list_Shutdown_json(payload)

