########################################################################################################################
# File name: accounting_exec.py
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
	'https://axapi.a10networks.com/axapi/v3/accounting/exec',
]

def deserialize_Exec_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	start_stop = data.get('start-stop')
	stop_only = data.get('stop-only')
	tacplus = data.get('tacplus')
	radius = data.get('radius')
	result = Exec(start_stop=start_stop, stop_only=stop_only, tacplus=tacplus, radius=radius)
	return result

def serialize_Exec_json(obj):
	output = OrderedDict()
	if obj.start_stop is not None:
		output['start-stop'] = obj.start_stop
	if obj.stop_only is not None:
		output['stop-only'] = obj.stop_only
	if obj.tacplus is not None:
		output['tacplus'] = obj.tacplus
	if obj.radius is not None:
		output['radius'] = obj.radius
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Exec_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Exec_json(item))
	return list(container)

class Exec(AxapiObject):
	__metaclass__ = StructMeta 
	start_stop=PosRangedInteger(0, 1)
	stop_only=PosRangedInteger(0, 1)
	tacplus=PosRangedInteger(0, 1)
	radius=PosRangedInteger(0, 1)
	def __init__(self, start_stop=None, stop_only=None, tacplus=None, radius=None):
		self.start_stop = start_stop
		self.stop_only = stop_only
		self.tacplus = tacplus
		self.radius = radius

	def __str__(self):
		return ""

class AccountingExecClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getAccountingExec(self):
		"""
		Retrieve the exec identified by the specified identifier
		
		Returns:
			An instance of the Exec class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified exec does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('exec')
		return deserialize_Exec_json(payload)

	def putAccountingExec(self, py_kw_rsvd_exec):
		"""
		Replace the object exec
		
		Args:
			py_kw_rsvd_exec An instance of the Exec class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['exec']=serialize_Exec_json(py_kw_rsvd_exec)
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

	def deleteAccountingExec(self):
		"""
		Remove the exec identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified exec does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllAccountingExecsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitAccountingExec(self, py_kw_rsvd_exec):
		"""
		Create the object exec
		
		Args:
			py_kw_rsvd_exec An instance of the Exec class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['exec']=serialize_Exec_json(py_kw_rsvd_exec)
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

	def getAllAccountingExecs(self):
		"""
		Retrieve all exec objects currently pending in the system
		
		Returns:
			A list of Exec objects
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
			payload= data.get('execList')
		return deserialize_list_Exec_json(payload)

