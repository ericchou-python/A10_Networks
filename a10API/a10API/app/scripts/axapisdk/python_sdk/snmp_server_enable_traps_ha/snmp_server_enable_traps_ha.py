########################################################################################################################
# File name: snmp_server_enable_traps_ha.py
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
	'https://axapi.a10networks.com/axapi/v3/snmp-server/enable/traps/ha',
]

def deserialize_Ha_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	all = data.get('all')
	active = data.get('active')
	active_active = data.get('active-active')
	standby = data.get('standby')
	vrrp = data.get('vrrp')
	result = Ha(all=all, active=active, active_active=active_active, standby=standby, vrrp=vrrp)
	return result

def serialize_Ha_json(obj):
	output = OrderedDict()
	output['all'] = obj.all
	output['active'] = obj.active
	output['active-active'] = obj.active_active
	output['standby'] = obj.standby
	output['vrrp'] = obj.vrrp
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Ha_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ha_json(item))
	return list(container)

class Ha_all_all_active_active_active_standby_vrrp(AxapiObject):
	__metaclass__ = StructMeta 
	all=PosRangedInteger(0, 1)
	active=PosRangedInteger(0, 1)
	active_active=PosRangedInteger(0, 1)
	standby=PosRangedInteger(0, 1)
	vrrp=PosRangedInteger(0, 1)
	def __init__(self, all, active, active_active, standby, vrrp):
		self.all = all
		self.active = active
		self.active_active = active_active
		self.standby = standby
		self.vrrp = vrrp

	def __str__(self):
		return str(self.all) + '+' + str(self.active) + '+' + str(self.active_active) + '+' + str(self.standby) + '+' + str(self.vrrp)

class Ha(AxapiObject):
	__metaclass__ = StructMeta 
	all=PosRangedInteger(0, 1)
	active=PosRangedInteger(0, 1)
	active_active=PosRangedInteger(0, 1)
	standby=PosRangedInteger(0, 1)
	vrrp=PosRangedInteger(0, 1)
	def __init__(self, all, active, active_active, standby, vrrp):
		self.all = all
		self.active = active
		self.active_active = active_active
		self.standby = standby
		self.vrrp = vrrp

	def __str__(self):
		return str(self.all) + '+' + str(self.active) + '+' + str(self.active_active) + '+' + str(self.standby) + '+' + str(self.vrrp)

class SnmpserverEnableTrapsHaClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSnmpserverEnableTrapsHa(self, ha_all_all_active_active_active_standby_vrrp):
		"""
		Retrieve the ha identified by the specified identifier
		
		Args:
			ha_all_all_active_active_active_standby_vrrp Ha_all_all_active_active_active_standby_vrrp
		
		Returns:
			An instance of the Ha class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(ha_all_all_active_active_active_standby_vrrp) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ha does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ha')
		return deserialize_Ha_json(payload)

	def putSnmpserverEnableTrapsHa(self, ha_all_all_active_active_active_standby_vrrp, ha):
		"""
		Replace the object ha
		
		Args:
			ha_all_all_active_active_active_standby_vrrp Ha_all_all_active_active_active_standby_vrrp
			ha An instance of the Ha class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ha']=serialize_Ha_json(ha)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(ha_all_all_active_active_active_standby_vrrp) .replace("/", "%2f") + query, payload, headers)
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

	def deleteSnmpserverEnableTrapsHa(self, ha_all_all_active_active_active_standby_vrrp):
		"""
		Remove the ha identified by the specified identifier from the system
		
		Args:
			ha_all_all_active_active_active_standby_vrrp Ha_all_all_active_active_active_standby_vrrp
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(ha_all_all_active_active_active_standby_vrrp) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ha does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSnmpserverEnableTrapsHasClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSnmpserverEnableTrapsHa(self, ha):
		"""
		Create the object ha
		
		Args:
			ha An instance of the Ha class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ha']=serialize_Ha_json(ha)
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

	def getAllSnmpserverEnableTrapsHas(self):
		"""
		Retrieve all ha objects currently pending in the system
		
		Returns:
			A list of Ha objects
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
			payload= data.get('haList')
		return deserialize_list_Ha_json(payload)

