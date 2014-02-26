########################################################################################################################
# File name: accounting.py
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
	'https://axapi.a10networks.com/axapi/v3/accounting',
]

def deserialize_Accounting__exec_json(obj):
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
	result = Accounting__exec(start_stop=start_stop, stop_only=stop_only, tacplus=tacplus, radius=radius)
	return result

def deserialize_Accounting_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	commands = data.get('commands')
	debug = data.get('debug')
	stop_only = data.get('stop-only')
	tacplus = data.get('tacplus')
	py_kw_rsvd_exec = deserialize_Accounting__exec_json(data.get('exec'))
	result = Accounting(commands=commands, debug=debug, stop_only=stop_only, tacplus=tacplus, py_kw_rsvd_exec=py_kw_rsvd_exec)
	return result

def serialize_Accounting__exec_json(obj):
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

def serialize_Accounting_json(obj):
	output = OrderedDict()
	if obj.commands is not None:
		output['commands'] = obj.commands
	if obj.debug is not None:
		output['debug'] = obj.debug
	if obj.stop_only is not None:
		output['stop-only'] = obj.stop_only
	if obj.tacplus is not None:
		output['tacplus'] = obj.tacplus
	if obj.py_kw_rsvd_exec is not None:
		output['exec'] = serialize_Accounting__exec_json(obj.py_kw_rsvd_exec)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Accounting_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Accounting_json(item))
	return list(container)

class Accounting__exec(AxapiObject):
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

class Accounting(AxapiObject):
	__metaclass__ = StructMeta 
	commands=PosRangedInteger(0, 15)
	debug=PosRangedInteger(1, 15)
	stop_only=PosRangedInteger(0, 1)
	tacplus=PosRangedInteger(0, 1)
	def __init__(self, commands=None, debug=None, stop_only=None, tacplus=None, py_kw_rsvd_exec=None):
		self.commands = commands
		self.debug = debug
		self.stop_only = stop_only
		self.tacplus = tacplus
		self.py_kw_rsvd_exec = py_kw_rsvd_exec

	def __str__(self):
		return ""

class AccountingClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getAccounting(self):
		"""
		Retrieve the accounting identified by the specified identifier
		
		Returns:
			An instance of the Accounting class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified accounting does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('accounting')
		return deserialize_Accounting_json(payload)

	def putAccounting(self, accounting):
		"""
		Replace the object accounting
		
		Args:
			accounting An instance of the Accounting class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['accounting']=serialize_Accounting_json(accounting)
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

	def deleteAccounting(self):
		"""
		Remove the accounting identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified accounting does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllAccountingsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitAccounting(self, accounting):
		"""
		Create the object accounting
		
		Args:
			accounting An instance of the Accounting class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['accounting']=serialize_Accounting_json(accounting)
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

	def getAllAccountings(self):
		"""
		Retrieve all accounting objects currently pending in the system
		
		Returns:
			A list of Accounting objects
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
			payload= data.get('accountingList')
		return deserialize_list_Accounting_json(payload)

