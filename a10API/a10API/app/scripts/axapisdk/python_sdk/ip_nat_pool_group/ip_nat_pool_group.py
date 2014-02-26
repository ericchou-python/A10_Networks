########################################################################################################################
# File name: ip_nat_pool_group.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/nat/pool-group',
]

def deserialize_Ip_nat_pool_group_member_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	pool_name = data.get('pool-name')
	result = Ip_nat_pool_group_member(pool_name=pool_name)
	return result

def deserialize_list_Ip_nat_pool_group_member_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_pool_group_member_json(item))
	return list(container)

def deserialize_Pool_group_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	pool_group_name = data.get('pool-group-name')
	vrid = data.get('vrid')
	default = data.get('default')
	memberlist = deserialize_list_Ip_nat_pool_group_member_json(data.get('memberList'))
	result = Pool_group(pool_group_name=pool_group_name, vrid=vrid, default=default, memberlist=memberlist)
	return result

def serialize_Ip_nat_pool_group_member_json(obj):
	output = OrderedDict()
	output['pool-name'] = obj.pool_name
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ip_nat_pool_group_member_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_nat_pool_group_member_json(item))
	return output

def serialize_Pool_group_json(obj):
	output = OrderedDict()
	output['pool-group-name'] = obj.pool_group_name
	if obj.vrid is not None:
		output['vrid'] = obj.vrid
	if obj.default is not None:
		output['default'] = obj.default
	if obj.memberlist is not None:
		output['memberList'] = serialize_list_Ip_nat_pool_group_member_json(obj.memberlist)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Pool_group_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Pool_group_json(item))
	return list(container)

class Pool_group(AxapiObject):
	__metaclass__ = StructMeta 
	pool_group_name=SizedString(1, 63)
	vrid=PosRangedInteger(1, 31)
	default=PosRangedInteger(0, 1)
	def __init__(self, pool_group_name, vrid=None, default=None, memberlist=None):
		self.pool_group_name = pool_group_name
		self.vrid = vrid
		self.default = default
		self.memberlist = memberlist

	def __str__(self):
		return str(self.pool_group_name)

class Pool_group_pool_group_name(AxapiObject):
	__metaclass__ = StructMeta 
	pool_group_name=SizedString(1, 63)
	def __init__(self, pool_group_name):
		self.pool_group_name = pool_group_name

	def __str__(self):
		return str(self.pool_group_name)

class Ip_nat_pool_group_member(AxapiObject):
	__metaclass__ = StructMeta 
	pool_name=SizedString(1, 63)
	def __init__(self, pool_name):
		self.pool_name = pool_name

	def __str__(self):
		return str(self.pool_name)

class IpNatPoolgroupClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpNatPoolgroup(self, pool_group_pool_group_name):
		"""
		Retrieve the pool_group identified by the specified identifier
		
		Args:
			pool_group_pool_group_name Pool_group_pool_group_name
		
		Returns:
			An instance of the Pool_group class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(pool_group_pool_group_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified pool_group does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('pool-group')
		return deserialize_Pool_group_json(payload)

	def putIpNatPoolgroup(self, pool_group_pool_group_name, pool_group):
		"""
		Replace the object pool_group
		
		Args:
			pool_group_pool_group_name Pool_group_pool_group_name
			pool_group An instance of the Pool_group class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['pool-group']=serialize_Pool_group_json(pool_group)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(pool_group_pool_group_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpNatPoolgroup(self, pool_group_pool_group_name):
		"""
		Remove the pool_group identified by the specified identifier from the system
		
		Args:
			pool_group_pool_group_name Pool_group_pool_group_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(pool_group_pool_group_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified pool_group does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpNatPoolgroupsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpNatPoolgroup(self, pool_group):
		"""
		Create the object pool_group
		
		Args:
			pool_group An instance of the Pool_group class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['pool-group']=serialize_Pool_group_json(pool_group)
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

	def getAllIpNatPoolgroups(self):
		"""
		Retrieve all pool_group objects currently pending in the system
		
		Returns:
			A list of Pool_group objects
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
			payload= data.get('pool-groupList')
		return deserialize_list_Pool_group_json(payload)

