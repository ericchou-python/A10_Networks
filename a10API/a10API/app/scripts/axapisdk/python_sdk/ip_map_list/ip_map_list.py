########################################################################################################################
# File name: ip_map_list.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/map-list',
]

def deserialize_Map_list__name_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	file = data.get('file')
	result = Map_list__name_cfg(name=name, file=file)
	return result

def deserialize_Ip_map_list_local_start_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_start_ip = data.get('local-start-ip')
	global_start_ip = data.get('global-start-ip')
	count = data.get('count')
	result = Ip_map_list_local_start_cfg(local_start_ip=local_start_ip, global_start_ip=global_start_ip, count=count)
	return result

def deserialize_list_Ip_map_list_local_start_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_map_list_local_start_cfg_json(item))
	return list(container)

def deserialize_Map_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name_cfg = deserialize_Map_list__name_cfg_json(data.get('name-cfg'))
	local_start_cfg = deserialize_list_Ip_map_list_local_start_cfg_json(data.get('local-start-cfg'))
	result = Map_list(name_cfg=name_cfg, local_start_cfg=local_start_cfg)
	return result

def serialize_Map_list__name_cfg_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.file is not None:
		output['file'] = obj.file
	return output

def serialize_Ip_map_list_local_start_cfg_json(obj):
	output = OrderedDict()
	if obj.local_start_ip is not None:
		output['local-start-ip'] = obj.local_start_ip
	if obj.global_start_ip is not None:
		output['global-start-ip'] = obj.global_start_ip
	if obj.count is not None:
		output['count'] = obj.count
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ip_map_list_local_start_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_map_list_local_start_cfg_json(item))
	return output

def serialize_Map_list_json(obj):
	output = OrderedDict()
	output['name-cfg'] = serialize_Map_list__name_cfg_json(obj.name_cfg)
	if obj.local_start_cfg is not None:
		output['local-start-cfg'] = serialize_list_Ip_map_list_local_start_cfg_json(obj.local_start_cfg)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Map_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Map_list_json(item))
	return list(container)

class Map_list__name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	file=PosRangedInteger(0, 1)
	def __init__(self, name, file=None):
		self.name = name
		self.file = file

	def __str__(self):
		return str(self.name)

class Map_list(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, name_cfg, local_start_cfg=None):
		self.name_cfg = name_cfg
		self.local_start_cfg = local_start_cfg

	def __str__(self):
		return str(self.name_cfg)

class Map_list_name_cfg__name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	file=PosRangedInteger(0, 1)
	def __init__(self, name, file=None):
		self.name = name
		self.file = file

	def __str__(self):
		return str(self.name)

class Map_list_name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, name_cfg):
		self.name_cfg = name_cfg

	def __str__(self):
		return str(self.name_cfg)

class Ip_map_list_local_start_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	local_start_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	global_start_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	count=PosRangedInteger(1, 16777216)
	def __init__(self, local_start_ip=None, global_start_ip=None, count=None):
		self.local_start_ip = local_start_ip
		self.global_start_ip = global_start_ip
		self.count = count

	def __str__(self):
		return ""

class IpMaplistClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpMaplist(self, map_list_name_cfg):
		"""
		Retrieve the map_list identified by the specified identifier
		
		Args:
			map_list_name_cfg Map_list_name_cfg
		
		Returns:
			An instance of the Map_list class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(map_list_name_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified map_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('map-list')
		return deserialize_Map_list_json(payload)

	def putIpMaplist(self, map_list_name_cfg, map_list):
		"""
		Replace the object map_list
		
		Args:
			map_list_name_cfg Map_list_name_cfg
			map_list An instance of the Map_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['map-list']=serialize_Map_list_json(map_list)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(map_list_name_cfg) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpMaplist(self, map_list_name_cfg):
		"""
		Remove the map_list identified by the specified identifier from the system
		
		Args:
			map_list_name_cfg Map_list_name_cfg
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(map_list_name_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified map_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpMaplistsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpMaplist(self, map_list):
		"""
		Create the object map_list
		
		Args:
			map_list An instance of the Map_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['map-list']=serialize_Map_list_json(map_list)
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

	def getAllIpMaplists(self):
		"""
		Retrieve all map_list objects currently pending in the system
		
		Returns:
			A list of Map_list objects
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
			payload= data.get('map-listList')
		return deserialize_list_Map_list_json(payload)

