########################################################################################################################
# File name: snmp_server_enable_traps_snmp.py
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
	'https://axapi.a10networks.com/axapi/v3/snmp-server/enable/traps/snmp',
]

def deserialize_Snmp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	all = data.get('all')
	linkdown = data.get('linkdown')
	linkup = data.get('linkup')
	result = Snmp(all=all, linkdown=linkdown, linkup=linkup)
	return result

def serialize_Snmp_json(obj):
	output = OrderedDict()
	output['all'] = obj.all
	output['linkdown'] = obj.linkdown
	output['linkup'] = obj.linkup
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Snmp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Snmp_json(item))
	return list(container)

class Snmp_all_all_linkdown_linkup(AxapiObject):
	__metaclass__ = StructMeta 
	all=PosRangedInteger(0, 1)
	linkdown=PosRangedInteger(0, 1)
	linkup=PosRangedInteger(0, 1)
	def __init__(self, all, linkdown, linkup):
		self.all = all
		self.linkdown = linkdown
		self.linkup = linkup

	def __str__(self):
		return str(self.all) + '+' + str(self.linkdown) + '+' + str(self.linkup)

class Snmp(AxapiObject):
	__metaclass__ = StructMeta 
	all=PosRangedInteger(0, 1)
	linkdown=PosRangedInteger(0, 1)
	linkup=PosRangedInteger(0, 1)
	def __init__(self, all, linkdown, linkup):
		self.all = all
		self.linkdown = linkdown
		self.linkup = linkup

	def __str__(self):
		return str(self.all) + '+' + str(self.linkdown) + '+' + str(self.linkup)

class SnmpserverEnableTrapsSnmpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSnmpserverEnableTrapsSnmp(self, snmp_all_all_linkdown_linkup):
		"""
		Retrieve the snmp identified by the specified identifier
		
		Args:
			snmp_all_all_linkdown_linkup Snmp_all_all_linkdown_linkup
		
		Returns:
			An instance of the Snmp class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(snmp_all_all_linkdown_linkup) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified snmp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('snmp')
		return deserialize_Snmp_json(payload)

	def putSnmpserverEnableTrapsSnmp(self, snmp_all_all_linkdown_linkup, snmp):
		"""
		Replace the object snmp
		
		Args:
			snmp_all_all_linkdown_linkup Snmp_all_all_linkdown_linkup
			snmp An instance of the Snmp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['snmp']=serialize_Snmp_json(snmp)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(snmp_all_all_linkdown_linkup) .replace("/", "%2f") + query, payload, headers)
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

	def deleteSnmpserverEnableTrapsSnmp(self, snmp_all_all_linkdown_linkup):
		"""
		Remove the snmp identified by the specified identifier from the system
		
		Args:
			snmp_all_all_linkdown_linkup Snmp_all_all_linkdown_linkup
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(snmp_all_all_linkdown_linkup) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified snmp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSnmpserverEnableTrapsSnmpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSnmpserverEnableTrapsSnmp(self, snmp):
		"""
		Create the object snmp
		
		Args:
			snmp An instance of the Snmp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['snmp']=serialize_Snmp_json(snmp)
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

	def getAllSnmpserverEnableTrapsSnmps(self):
		"""
		Retrieve all snmp objects currently pending in the system
		
		Returns:
			A list of Snmp objects
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
			payload= data.get('snmpList')
		return deserialize_list_Snmp_json(payload)

