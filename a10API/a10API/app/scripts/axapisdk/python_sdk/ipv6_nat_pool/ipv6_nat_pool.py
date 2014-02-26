########################################################################################################################
# File name: ipv6_nat_pool.py
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
	'https://axapi.a10networks.com/axapi/v3/ipv6/nat/pool',
]

def deserialize_Pool__pool_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	gateway = data.get('gateway')
	vrid = data.get('vrid')
	ip_rr = data.get('ip-rr')
	result = Pool__pool_cfg(gateway=gateway, vrid=vrid, ip_rr=ip_rr)
	return result

def deserialize_Pool_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	pool_name = data.get('pool-name')
	start_address = data.get('start-address')
	end_address = data.get('end-address')
	netmask = data.get('netmask')
	pool_cfg = deserialize_Pool__pool_cfg_json(data.get('pool-cfg'))
	result = Pool(pool_name=pool_name, start_address=start_address, end_address=end_address, netmask=netmask, pool_cfg=pool_cfg)
	return result

def serialize_Pool__pool_cfg_json(obj):
	output = OrderedDict()
	if obj.gateway is not None:
		output['gateway'] = obj.gateway
	if obj.vrid is not None:
		output['vrid'] = obj.vrid
	if obj.ip_rr is not None:
		output['ip-rr'] = obj.ip_rr
	return output

def serialize_Pool_json(obj):
	output = OrderedDict()
	output['pool-name'] = obj.pool_name
	if obj.start_address is not None:
		output['start-address'] = obj.start_address
	if obj.end_address is not None:
		output['end-address'] = obj.end_address
	if obj.netmask is not None:
		output['netmask'] = obj.netmask
	if obj.pool_cfg is not None:
		output['pool-cfg'] = serialize_Pool__pool_cfg_json(obj.pool_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Pool_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Pool_json(item))
	return list(container)

class Pool_pool_name(AxapiObject):
	__metaclass__ = StructMeta 
	pool_name=SizedString(1, 63)
	def __init__(self, pool_name):
		self.pool_name = pool_name

	def __str__(self):
		return str(self.pool_name)

class Pool__pool_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	gateway=SizedString(1, 255)
	vrid=PosRangedInteger(1, 31)
	ip_rr=PosRangedInteger(0, 1)
	def __init__(self, gateway=None, vrid=None, ip_rr=None):
		self.gateway = gateway
		self.vrid = vrid
		self.ip_rr = ip_rr

	def __str__(self):
		return ""

class Pool(AxapiObject):
	__metaclass__ = StructMeta 
	pool_name=SizedString(1, 63)
	start_address=SizedString(1, 255)
	end_address=SizedString(1, 255)
	netmask=PosRangedInteger(64, 128)
	def __init__(self, pool_name, start_address=None, end_address=None, netmask=None, pool_cfg=None):
		self.pool_name = pool_name
		self.start_address = start_address
		self.end_address = end_address
		self.netmask = netmask
		self.pool_cfg = pool_cfg

	def __str__(self):
		return str(self.pool_name)

class Ipv6NatPoolClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpv6NatPool(self, pool_pool_name):
		"""
		Retrieve the pool identified by the specified identifier
		
		Args:
			pool_pool_name Pool_pool_name
		
		Returns:
			An instance of the Pool class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(pool_pool_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified pool does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('pool')
		return deserialize_Pool_json(payload)

	def putIpv6NatPool(self, pool_pool_name, pool):
		"""
		Replace the object pool
		
		Args:
			pool_pool_name Pool_pool_name
			pool An instance of the Pool class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['pool']=serialize_Pool_json(pool)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(pool_pool_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpv6NatPool(self, pool_pool_name):
		"""
		Remove the pool identified by the specified identifier from the system
		
		Args:
			pool_pool_name Pool_pool_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(pool_pool_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified pool does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpv6NatPoolsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpv6NatPool(self, pool):
		"""
		Create the object pool
		
		Args:
			pool An instance of the Pool class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['pool']=serialize_Pool_json(pool)
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

	def getAllIpv6NatPools(self):
		"""
		Retrieve all pool objects currently pending in the system
		
		Returns:
			A list of Pool objects
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
			payload= data.get('poolList')
		return deserialize_list_Pool_json(payload)

