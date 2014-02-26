########################################################################################################################
# File name: backup_store.py
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
	'https://axapi.a10networks.com/axapi/v3/backup/store',
]

def deserialize_Store__creat_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	create = data.get('create')
	store_name = data.get('store-name')
	remote_file = data.get('remote-file')
	result = Store__creat_cfg(create=create, store_name=store_name, remote_file=remote_file)
	return result

def deserialize_Store__delete_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	delete = data.get('delete')
	store_name_del = data.get('store-name-del')
	result = Store__delete_cfg(delete=delete, store_name_del=store_name_del)
	return result

def deserialize_Store_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	creat_cfg = deserialize_Store__creat_cfg_json(data.get('creat-cfg'))
	delete_cfg = deserialize_Store__delete_cfg_json(data.get('delete-cfg'))
	result = Store(creat_cfg=creat_cfg, delete_cfg=delete_cfg)
	return result

def serialize_Store__creat_cfg_json(obj):
	output = OrderedDict()
	if obj.create is not None:
		output['create'] = obj.create
	if obj.store_name is not None:
		output['store-name'] = obj.store_name
	if obj.remote_file is not None:
		output['remote-file'] = obj.remote_file
	return output

def serialize_Store__delete_cfg_json(obj):
	output = OrderedDict()
	if obj.delete is not None:
		output['delete'] = obj.delete
	if obj.store_name_del is not None:
		output['store-name-del'] = obj.store_name_del
	return output

def serialize_Store_json(obj):
	output = OrderedDict()
	if obj.creat_cfg is not None:
		output['creat-cfg'] = serialize_Store__creat_cfg_json(obj.creat_cfg)
	if obj.delete_cfg is not None:
		output['delete-cfg'] = serialize_Store__delete_cfg_json(obj.delete_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Store_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Store_json(item))
	return list(container)

class Store__creat_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	create=PosRangedInteger(0, 1)
	store_name=SizedString(1, 31)
	remote_file=SizedString(1, 255)
	def __init__(self, create=None, store_name=None, remote_file=None):
		self.create = create
		self.store_name = store_name
		self.remote_file = remote_file

	def __str__(self):
		return ""

class Store__delete_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	delete=PosRangedInteger(0, 1)
	store_name_del=SizedString(1, 31)
	def __init__(self, delete=None, store_name_del=None):
		self.delete = delete
		self.store_name_del = store_name_del

	def __str__(self):
		return ""

class Store(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, creat_cfg=None, delete_cfg=None):
		self.creat_cfg = creat_cfg
		self.delete_cfg = delete_cfg

	def __str__(self):
		return ""

class BackupStoreClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getBackupStore(self):
		"""
		Retrieve the store identified by the specified identifier
		
		Returns:
			An instance of the Store class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified store does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('store')
		return deserialize_Store_json(payload)

	def putBackupStore(self, store):
		"""
		Replace the object store
		
		Args:
			store An instance of the Store class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['store']=serialize_Store_json(store)
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

	def deleteBackupStore(self):
		"""
		Remove the store identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified store does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllBackupStoresClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitBackupStore(self, store):
		"""
		Create the object store
		
		Args:
			store An instance of the Store class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['store']=serialize_Store_json(store)
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

	def getAllBackupStores(self):
		"""
		Retrieve all store objects currently pending in the system
		
		Returns:
			A list of Store objects
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
			payload= data.get('storeList')
		return deserialize_list_Store_json(payload)

