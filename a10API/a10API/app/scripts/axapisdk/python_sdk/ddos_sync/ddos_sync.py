########################################################################################################################
# File name: ddos_sync.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/sync',
]

def deserialize_Ddos_sync_peer_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	peer_ip = data.get('peer-ip')
	result = Ddos_sync_peer_ip_cfg(peer_ip=peer_ip)
	return result

def deserialize_list_Ddos_sync_peer_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_sync_peer_ip_cfg_json(item))
	return list(container)

def deserialize_Sync_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable = data.get('enable')
	local_ip = data.get('local-ip')
	peer_ip_cfg = deserialize_list_Ddos_sync_peer_ip_cfg_json(data.get('peer-ip-cfg'))
	result = Sync(enable=enable, local_ip=local_ip, peer_ip_cfg=peer_ip_cfg)
	return result

def serialize_Ddos_sync_peer_ip_cfg_json(obj):
	output = OrderedDict()
	if obj.peer_ip is not None:
		output['peer-ip'] = obj.peer_ip
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ddos_sync_peer_ip_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_sync_peer_ip_cfg_json(item))
	return output

def serialize_Sync_json(obj):
	output = OrderedDict()
	if obj.enable is not None:
		output['enable'] = obj.enable
	if obj.local_ip is not None:
		output['local-ip'] = obj.local_ip
	if obj.peer_ip_cfg is not None:
		output['peer-ip-cfg'] = serialize_list_Ddos_sync_peer_ip_cfg_json(obj.peer_ip_cfg)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Sync_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sync_json(item))
	return list(container)

class Sync(AxapiObject):
	__metaclass__ = StructMeta 
	enable=PosRangedInteger(0, 1)
	local_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, enable=None, local_ip=None, peer_ip_cfg=None):
		self.enable = enable
		self.local_ip = local_ip
		self.peer_ip_cfg = peer_ip_cfg

	def __str__(self):
		return ""

class Ddos_sync_peer_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	peer_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, peer_ip=None):
		self.peer_ip = peer_ip

	def __str__(self):
		return ""

class DdosSyncClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosSync(self):
		"""
		Retrieve the sync identified by the specified identifier
		
		Returns:
			An instance of the Sync class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified sync does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('sync')
		return deserialize_Sync_json(payload)

	def putDdosSync(self, sync):
		"""
		Replace the object sync
		
		Args:
			sync An instance of the Sync class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['sync']=serialize_Sync_json(sync)
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

	def deleteDdosSync(self):
		"""
		Remove the sync identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified sync does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosSyncsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosSync(self, sync):
		"""
		Create the object sync
		
		Args:
			sync An instance of the Sync class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['sync']=serialize_Sync_json(sync)
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

	def getAllDdosSyncs(self):
		"""
		Retrieve all sync objects currently pending in the system
		
		Returns:
			A list of Sync objects
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
			payload= data.get('syncList')
		return deserialize_list_Sync_json(payload)

