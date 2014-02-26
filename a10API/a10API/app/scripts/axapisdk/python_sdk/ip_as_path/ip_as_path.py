########################################################################################################################
# File name: ip_as_path.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/as-path',
]

def deserialize_As_path__access_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	access_list = data.get('access-list')
	action = data.get('action')
	value = data.get('value')
	result = As_path__access_list_cfg(access_list=access_list, action=action, value=value)
	return result

def deserialize_As_path_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	access_list_cfg = deserialize_As_path__access_list_cfg_json(data.get('access-list-cfg'))
	result = As_path(access_list_cfg=access_list_cfg)
	return result

def serialize_As_path__access_list_cfg_json(obj):
	output = OrderedDict()
	output['access-list'] = obj.access_list
	output['action'] = obj.action
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_As_path_json(obj):
	output = OrderedDict()
	output['access-list-cfg'] = serialize_As_path__access_list_cfg_json(obj.access_list_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_As_path_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_As_path_json(item))
	return list(container)

class As_path_access_list_cfg__access_list_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	access_list=SizedString(1, 255)
	action = Enum(['deny', 'permit'])
	value=SizedString(0, 255)
	def __init__(self, access_list, action, value=None):
		self.access_list = access_list
		self.action = action
		self.value = value

	def __str__(self):
		return str(self.access_list) + '+' + str(self.action)

class As_path_access_list_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, access_list_cfg):
		self.access_list_cfg = access_list_cfg

	def __str__(self):
		return str(self.access_list_cfg)

class As_path__access_list_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	access_list=SizedString(1, 255)
	action = Enum(['deny', 'permit'])
	value=SizedString(0, 255)
	def __init__(self, access_list, action, value=None):
		self.access_list = access_list
		self.action = action
		self.value = value

	def __str__(self):
		return str(self.access_list) + '+' + str(self.action)

class As_path(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, access_list_cfg):
		self.access_list_cfg = access_list_cfg

	def __str__(self):
		return str(self.access_list_cfg)

class IpAspathClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpAspath(self, as_path_access_list_cfg):
		"""
		Retrieve the as_path identified by the specified identifier
		
		Args:
			as_path_access_list_cfg As_path_access_list_cfg
		
		Returns:
			An instance of the As_path class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(as_path_access_list_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified as_path does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('as-path')
		return deserialize_As_path_json(payload)

	def putIpAspath(self, as_path_access_list_cfg, as_path):
		"""
		Replace the object as_path
		
		Args:
			as_path_access_list_cfg As_path_access_list_cfg
			as_path An instance of the As_path class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['as-path']=serialize_As_path_json(as_path)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(as_path_access_list_cfg) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpAspath(self, as_path_access_list_cfg):
		"""
		Remove the as_path identified by the specified identifier from the system
		
		Args:
			as_path_access_list_cfg As_path_access_list_cfg
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(as_path_access_list_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified as_path does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpAspathsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpAspath(self, as_path):
		"""
		Create the object as_path
		
		Args:
			as_path An instance of the As_path class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['as-path']=serialize_As_path_json(as_path)
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

	def getAllIpAspaths(self):
		"""
		Retrieve all as_path objects currently pending in the system
		
		Returns:
			A list of As_path objects
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
			payload= data.get('as-pathList')
		return deserialize_list_As_path_json(payload)

