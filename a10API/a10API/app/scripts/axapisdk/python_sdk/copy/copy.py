########################################################################################################################
# File name: copy.py
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
	'https://axapi.a10networks.com/axapi/v3/copy',
]

def deserialize_Copy_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	running_config = data.get('running-config')
	startup_config = data.get('startup-config')
	profile = data.get('profile')
	use_mgmt_port = data.get('use-mgmt-port')
	remote_file = data.get('remote-file')
	dest_profile = data.get('dest-profile')
	dest_use_mgmt_port = data.get('dest-use-mgmt-port')
	dest_remote_file = data.get('dest-remote-file')
	to_startup_config = data.get('to-startup-config')
	to_profile = data.get('to-profile')
	result = Copy(running_config=running_config, startup_config=startup_config, profile=profile, use_mgmt_port=use_mgmt_port, remote_file=remote_file, dest_profile=dest_profile, dest_use_mgmt_port=dest_use_mgmt_port, dest_remote_file=dest_remote_file, to_startup_config=to_startup_config, to_profile=to_profile)
	return result

def serialize_Copy_json(obj):
	output = OrderedDict()
	if obj.running_config is not None:
		output['running-config'] = obj.running_config
	if obj.startup_config is not None:
		output['startup-config'] = obj.startup_config
	if obj.profile is not None:
		output['profile'] = obj.profile
	if obj.use_mgmt_port is not None:
		output['use-mgmt-port'] = obj.use_mgmt_port
	if obj.remote_file is not None:
		output['remote-file'] = obj.remote_file
	if obj.dest_profile is not None:
		output['dest-profile'] = obj.dest_profile
	if obj.dest_use_mgmt_port is not None:
		output['dest-use-mgmt-port'] = obj.dest_use_mgmt_port
	if obj.dest_remote_file is not None:
		output['dest-remote-file'] = obj.dest_remote_file
	if obj.to_startup_config is not None:
		output['to-startup-config'] = obj.to_startup_config
	if obj.to_profile is not None:
		output['to-profile'] = obj.to_profile
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Copy_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Copy_json(item))
	return list(container)

class Copy(AxapiObject):
	__metaclass__ = StructMeta 
	running_config=PosRangedInteger(0, 1)
	startup_config=PosRangedInteger(0, 1)
	profile=SizedString(1, 31)
	use_mgmt_port=PosRangedInteger(0, 1)
	remote_file=SizedString(1, 255)
	dest_profile=SizedString(1, 31)
	dest_use_mgmt_port=PosRangedInteger(0, 1)
	dest_remote_file=SizedString(1, 255)
	to_startup_config=PosRangedInteger(0, 1)
	to_profile=SizedString(1, 31)
	def __init__(self, running_config=None, startup_config=None, profile=None, use_mgmt_port=None, remote_file=None, dest_profile=None, dest_use_mgmt_port=None, dest_remote_file=None, to_startup_config=None, to_profile=None):
		self.running_config = running_config
		self.startup_config = startup_config
		self.profile = profile
		self.use_mgmt_port = use_mgmt_port
		self.remote_file = remote_file
		self.dest_profile = dest_profile
		self.dest_use_mgmt_port = dest_use_mgmt_port
		self.dest_remote_file = dest_remote_file
		self.to_startup_config = to_startup_config
		self.to_profile = to_profile

	def __str__(self):
		return ""

class CopyClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getCopy(self):
		"""
		Retrieve the copy identified by the specified identifier
		
		Returns:
			An instance of the Copy class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified copy does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('copy')
		return deserialize_Copy_json(payload)

	def putCopy(self, copy):
		"""
		Replace the object copy
		
		Args:
			copy An instance of the Copy class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['copy']=serialize_Copy_json(copy)
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

	def deleteCopy(self):
		"""
		Remove the copy identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified copy does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllCopysClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitCopy(self, copy):
		"""
		Create the object copy
		
		Args:
			copy An instance of the Copy class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['copy']=serialize_Copy_json(copy)
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

	def getAllCopys(self):
		"""
		Retrieve all copy objects currently pending in the system
		
		Returns:
			A list of Copy objects
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
			payload= data.get('copyList')
		return deserialize_list_Copy_json(payload)

