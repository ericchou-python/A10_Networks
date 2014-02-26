########################################################################################################################
# File name: vlan_global.py
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
	'https://axapi.a10networks.com/axapi/v3/vlan-global',
]

def deserialize_Vlan_global_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable_def_vlan_l2_forwarding = data.get('enable-def-vlan-l2-forwarding')
	l3_vlan_fwd_disable = data.get('l3-vlan-fwd-disable')
	result = Vlan_global(enable_def_vlan_l2_forwarding=enable_def_vlan_l2_forwarding, l3_vlan_fwd_disable=l3_vlan_fwd_disable)
	return result

def serialize_Vlan_global_json(obj):
	output = OrderedDict()
	if obj.enable_def_vlan_l2_forwarding is not None:
		output['enable-def-vlan-l2-forwarding'] = obj.enable_def_vlan_l2_forwarding
	if obj.l3_vlan_fwd_disable is not None:
		output['l3-vlan-fwd-disable'] = obj.l3_vlan_fwd_disable
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Vlan_global_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vlan_global_json(item))
	return list(container)

class Vlan_global(AxapiObject):
	__metaclass__ = StructMeta 
	enable_def_vlan_l2_forwarding=PosRangedInteger(0, 1)
	l3_vlan_fwd_disable=PosRangedInteger(0, 1)
	def __init__(self, enable_def_vlan_l2_forwarding=None, l3_vlan_fwd_disable=None):
		self.enable_def_vlan_l2_forwarding = enable_def_vlan_l2_forwarding
		self.l3_vlan_fwd_disable = l3_vlan_fwd_disable

	def __str__(self):
		return ""

class VlanglobalClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getVlanglobal(self):
		"""
		Retrieve the vlan_global identified by the specified identifier
		
		Returns:
			An instance of the Vlan_global class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified vlan_global does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('vlan-global')
		return deserialize_Vlan_global_json(payload)

	def putVlanglobal(self, vlan_global):
		"""
		Replace the object vlan_global
		
		Args:
			vlan_global An instance of the Vlan_global class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['vlan-global']=serialize_Vlan_global_json(vlan_global)
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

	def deleteVlanglobal(self):
		"""
		Remove the vlan_global identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified vlan_global does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllVlanglobalsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitVlanglobal(self, vlan_global):
		"""
		Create the object vlan_global
		
		Args:
			vlan_global An instance of the Vlan_global class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['vlan-global']=serialize_Vlan_global_json(vlan_global)
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

	def getAllVlanglobals(self):
		"""
		Retrieve all vlan_global objects currently pending in the system
		
		Returns:
			A list of Vlan_global objects
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
			payload= data.get('vlan-globalList')
		return deserialize_list_Vlan_global_json(payload)

