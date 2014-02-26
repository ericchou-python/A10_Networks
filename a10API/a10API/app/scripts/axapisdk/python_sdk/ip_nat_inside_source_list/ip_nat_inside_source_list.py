########################################################################################################################
# File name: ip_nat_inside_source_list.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/nat/inside/source/list',
]

def deserialize_Ip_nat_inside_source_list_name_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl_name = data.get('acl-name')
	pool = data.get('pool')
	msl = data.get('msl')
	result = Ip_nat_inside_source_list_name(acl_name=acl_name, pool=pool, msl=msl)
	return result

def deserialize_list_Ip_nat_inside_source_list_name_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_inside_source_list_name_json(item))
	return list(container)

def deserialize_List_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl_id = data.get('acl-id')
	pool = data.get('pool')
	msl = data.get('msl')
	namelist = deserialize_list_Ip_nat_inside_source_list_name_json(data.get('nameList'))
	result = List(acl_id=acl_id, pool=pool, msl=msl, namelist=namelist)
	return result

def serialize_Ip_nat_inside_source_list_name_json(obj):
	output = OrderedDict()
	output['acl-name'] = obj.acl_name
	output['pool'] = obj.pool
	if obj.msl is not None:
		output['msl'] = obj.msl
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ip_nat_inside_source_list_name_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_nat_inside_source_list_name_json(item))
	return output

def serialize_List_json(obj):
	output = OrderedDict()
	output['acl-id'] = obj.acl_id
	output['pool'] = obj.pool
	if obj.msl is not None:
		output['msl'] = obj.msl
	if obj.namelist is not None:
		output['nameList'] = serialize_list_Ip_nat_inside_source_list_name_json(obj.namelist)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_List_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_List_json(item))
	return list(container)

class List(AxapiObject):
	__metaclass__ = StructMeta 
	acl_id=PosRangedInteger(1, 199)
	pool=SizedString(1, 255)
	msl=PosRangedInteger(1, 1800)
	def __init__(self, acl_id, pool, msl=None, namelist=None):
		self.acl_id = acl_id
		self.pool = pool
		self.msl = msl
		self.namelist = namelist

	def __str__(self):
		return str(self.acl_id) + '+' + str(self.pool)

class List_acl_id_pool(AxapiObject):
	__metaclass__ = StructMeta 
	acl_id=PosRangedInteger(1, 199)
	pool=SizedString(1, 255)
	def __init__(self, acl_id, pool):
		self.acl_id = acl_id
		self.pool = pool

	def __str__(self):
		return str(self.acl_id) + '+' + str(self.pool)

class Ip_nat_inside_source_list_name(AxapiObject):
	__metaclass__ = StructMeta 
	acl_name=SizedString(1, 16)
	pool=SizedString(1, 255)
	msl=PosRangedInteger(1, 1800)
	def __init__(self, acl_name, pool, msl=None):
		self.acl_name = acl_name
		self.pool = pool
		self.msl = msl

	def __str__(self):
		return str(self.acl_name) + '+' + str(self.pool)

class IpNatInsideSourceListClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpNatInsideSourceList(self, list_acl_id_pool):
		"""
		Retrieve the list identified by the specified identifier
		
		Args:
			list_acl_id_pool List_acl_id_pool
		
		Returns:
			An instance of the List class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(list_acl_id_pool) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('list')
		return deserialize_List_json(payload)

	def putIpNatInsideSourceList(self, list_acl_id_pool, list):
		"""
		Replace the object list
		
		Args:
			list_acl_id_pool List_acl_id_pool
			list An instance of the List class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['list']=serialize_List_json(list)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(list_acl_id_pool) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpNatInsideSourceList(self, list_acl_id_pool):
		"""
		Remove the list identified by the specified identifier from the system
		
		Args:
			list_acl_id_pool List_acl_id_pool
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(list_acl_id_pool) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpNatInsideSourceListsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpNatInsideSourceList(self, list):
		"""
		Create the object list
		
		Args:
			list An instance of the List class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['list']=serialize_List_json(list)
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

	def getAllIpNatInsideSourceLists(self):
		"""
		Retrieve all list objects currently pending in the system
		
		Returns:
			A list of List objects
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
			payload= data.get('listList')
		return deserialize_list_List_json(payload)

