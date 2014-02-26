########################################################################################################################
# File name: system_per_vlan_limit.py
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
	'https://axapi.a10networks.com/axapi/v3/system/per-vlan-limit',
]

def deserialize_Per_vlan_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bcast = data.get('bcast')
	ipmcast = data.get('ipmcast')
	mcast = data.get('mcast')
	unknown_ucast = data.get('unknown-ucast')
	result = Per_vlan_limit(bcast=bcast, ipmcast=ipmcast, mcast=mcast, unknown_ucast=unknown_ucast)
	return result

def serialize_Per_vlan_limit_json(obj):
	output = OrderedDict()
	if obj.bcast is not None:
		output['bcast'] = obj.bcast
	if obj.ipmcast is not None:
		output['ipmcast'] = obj.ipmcast
	if obj.mcast is not None:
		output['mcast'] = obj.mcast
	if obj.unknown_ucast is not None:
		output['unknown-ucast'] = obj.unknown_ucast
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Per_vlan_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Per_vlan_limit_json(item))
	return list(container)

class Per_vlan_limit(AxapiObject):
	__metaclass__ = StructMeta 
	bcast=PosRangedInteger(1, 65535)
	ipmcast=PosRangedInteger(1, 65535)
	mcast=PosRangedInteger(1, 65535)
	unknown_ucast=PosRangedInteger(1, 65535)
	def __init__(self, bcast=None, ipmcast=None, mcast=None, unknown_ucast=None):
		self.bcast = bcast
		self.ipmcast = ipmcast
		self.mcast = mcast
		self.unknown_ucast = unknown_ucast

	def __str__(self):
		return ""

class SystemPervlanlimitClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSystemPervlanlimit(self):
		"""
		Retrieve the per_vlan_limit identified by the specified identifier
		
		Returns:
			An instance of the Per_vlan_limit class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified per_vlan_limit does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('per-vlan-limit')
		return deserialize_Per_vlan_limit_json(payload)

	def putSystemPervlanlimit(self, per_vlan_limit):
		"""
		Replace the object per_vlan_limit
		
		Args:
			per_vlan_limit An instance of the Per_vlan_limit class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['per-vlan-limit']=serialize_Per_vlan_limit_json(per_vlan_limit)
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

	def deleteSystemPervlanlimit(self):
		"""
		Remove the per_vlan_limit identified by the specified identifier from the
		system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified per_vlan_limit does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSystemPervlanlimitsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSystemPervlanlimit(self, per_vlan_limit):
		"""
		Create the object per_vlan_limit
		
		Args:
			per_vlan_limit An instance of the Per_vlan_limit class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['per-vlan-limit']=serialize_Per_vlan_limit_json(per_vlan_limit)
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

	def getAllSystemPervlanlimits(self):
		"""
		Retrieve all per_vlan_limit objects currently pending in the system
		
		Returns:
			A list of Per_vlan_limit objects
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
			payload= data.get('per-vlan-limitList')
		return deserialize_list_Per_vlan_limit_json(payload)

