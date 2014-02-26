########################################################################################################################
# File name: link_startup_config.py
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
	'https://axapi.a10networks.com/axapi/v3/link/startup-config',
]

def deserialize_Startup_config__default_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default = data.get('default')
	file_name = data.get('file-name')
	primary = data.get('primary')
	secondary = data.get('secondary')
	result = Startup_config__default_cfg(default=default, file_name=file_name, primary=primary, secondary=secondary)
	return result

def deserialize_Startup_config_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default_cfg = deserialize_Startup_config__default_cfg_json(data.get('default-cfg'))
	result = Startup_config(default_cfg=default_cfg)
	return result

def serialize_Startup_config__default_cfg_json(obj):
	output = OrderedDict()
	if obj.default is not None:
		output['default'] = obj.default
	if obj.file_name is not None:
		output['file-name'] = obj.file_name
	if obj.primary is not None:
		output['primary'] = obj.primary
	if obj.secondary is not None:
		output['secondary'] = obj.secondary
	return output

def serialize_Startup_config_json(obj):
	output = OrderedDict()
	if obj.default_cfg is not None:
		output['default-cfg'] = serialize_Startup_config__default_cfg_json(obj.default_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Startup_config_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Startup_config_json(item))
	return list(container)

class Startup_config__default_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	default=PosRangedInteger(0, 1)
	file_name=SizedString(1, 31)
	primary=PosRangedInteger(0, 1)
	secondary=PosRangedInteger(0, 1)
	def __init__(self, default=None, file_name=None, primary=None, secondary=None):
		self.default = default
		self.file_name = file_name
		self.primary = primary
		self.secondary = secondary

	def __str__(self):
		return ""

class Startup_config(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, default_cfg=None):
		self.default_cfg = default_cfg

	def __str__(self):
		return ""

class LinkStartupconfigClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLinkStartupconfig(self):
		"""
		Retrieve the startup_config identified by the specified identifier
		
		Returns:
			An instance of the Startup_config class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified startup_config does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('startup-config')
		return deserialize_Startup_config_json(payload)

	def putLinkStartupconfig(self, startup_config):
		"""
		Replace the object startup_config
		
		Args:
			startup_config An instance of the Startup_config class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['startup-config']=serialize_Startup_config_json(startup_config)
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

	def deleteLinkStartupconfig(self):
		"""
		Remove the startup_config identified by the specified identifier from the
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
		errors = {500: 'An unexpected runtime exception', 404: 'Specified startup_config does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllLinkStartupconfigsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitLinkStartupconfig(self, startup_config):
		"""
		Create the object startup_config
		
		Args:
			startup_config An instance of the Startup_config class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['startup-config']=serialize_Startup_config_json(startup_config)
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

	def getAllLinkStartupconfigs(self):
		"""
		Retrieve all startup_config objects currently pending in the system
		
		Returns:
			A list of Startup_config objects
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
			payload= data.get('startup-configList')
		return deserialize_list_Startup_config_json(payload)

