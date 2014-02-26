########################################################################################################################
# File name: ip_nat_pool.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/nat/pool',
]

def deserialize_Pool__pool_name_cfg_json(obj):
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
	gateway = data.get('gateway')
	vrid = data.get('vrid')
	ip_rr = data.get('ip-rr')
	ha_use_all_ports = data.get('ha-use-all-ports')
	result = Pool__pool_name_cfg(pool_name=pool_name, start_address=start_address, end_address=end_address, netmask=netmask, gateway=gateway, vrid=vrid, ip_rr=ip_rr, ha_use_all_ports=ha_use_all_ports)
	return result

def deserialize_Pool_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	pool_name_cfg = deserialize_Pool__pool_name_cfg_json(data.get('pool-name-cfg'))
	result = Pool(pool_name_cfg=pool_name_cfg)
	return result

def serialize_Pool__pool_name_cfg_json(obj):
	output = OrderedDict()
	output['pool-name'] = obj.pool_name
	output['start-address'] = obj.start_address
	output['end-address'] = obj.end_address
	output['netmask'] = obj.netmask
	if obj.gateway is not None:
		output['gateway'] = obj.gateway
	if obj.vrid is not None:
		output['vrid'] = obj.vrid
	if obj.ip_rr is not None:
		output['ip-rr'] = obj.ip_rr
	if obj.ha_use_all_ports is not None:
		output['ha-use-all-ports'] = obj.ha_use_all_ports
	return output

def serialize_Pool_json(obj):
	output = OrderedDict()
	output['pool-name-cfg'] = serialize_Pool__pool_name_cfg_json(obj.pool_name_cfg)
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

class Pool_pool_name_cfg__pool_name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	pool_name=SizedString(1, 63)
	start_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	end_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	gateway = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	vrid=PosRangedInteger(1, 31)
	ip_rr=PosRangedInteger(0, 1)
	ha_use_all_ports=PosRangedInteger(0, 1)
	def __init__(self, pool_name, start_address, end_address, netmask, gateway=None, vrid=None, ip_rr=None, ha_use_all_ports=None):
		self.pool_name = pool_name
		self.start_address = start_address
		self.end_address = end_address
		self.netmask = netmask
		self.gateway = gateway
		self.vrid = vrid
		self.ip_rr = ip_rr
		self.ha_use_all_ports = ha_use_all_ports

	def __str__(self):
		return str(self.pool_name) + '+' + str(self.start_address) + '+' + str(self.end_address) + '+' + str(self.netmask)

class Pool_pool_name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, pool_name_cfg):
		self.pool_name_cfg = pool_name_cfg

	def __str__(self):
		return str(self.pool_name_cfg)

class Pool__pool_name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	pool_name=SizedString(1, 63)
	start_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	end_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	gateway = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	vrid=PosRangedInteger(1, 31)
	ip_rr=PosRangedInteger(0, 1)
	ha_use_all_ports=PosRangedInteger(0, 1)
	def __init__(self, pool_name, start_address, end_address, netmask, gateway=None, vrid=None, ip_rr=None, ha_use_all_ports=None):
		self.pool_name = pool_name
		self.start_address = start_address
		self.end_address = end_address
		self.netmask = netmask
		self.gateway = gateway
		self.vrid = vrid
		self.ip_rr = ip_rr
		self.ha_use_all_ports = ha_use_all_ports

	def __str__(self):
		return str(self.pool_name) + '+' + str(self.start_address) + '+' + str(self.end_address) + '+' + str(self.netmask)

class Pool(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, pool_name_cfg):
		self.pool_name_cfg = pool_name_cfg

	def __str__(self):
		return str(self.pool_name_cfg)

class IpNatPoolClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpNatPool(self, pool_pool_name_cfg):
		"""
		Retrieve the pool identified by the specified identifier
		
		Args:
			pool_pool_name_cfg Pool_pool_name_cfg
		
		Returns:
			An instance of the Pool class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(pool_pool_name_cfg) .replace("/", "%2f") + query, headers=headers)
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

	def putIpNatPool(self, pool_pool_name_cfg, pool):
		"""
		Replace the object pool
		
		Args:
			pool_pool_name_cfg Pool_pool_name_cfg
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
		conn.request('PUT', self.get_path() + '/' + str(pool_pool_name_cfg) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpNatPool(self, pool_pool_name_cfg):
		"""
		Remove the pool identified by the specified identifier from the system
		
		Args:
			pool_pool_name_cfg Pool_pool_name_cfg
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(pool_pool_name_cfg) .replace("/", "%2f") + query, headers=headers)
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

class AllIpNatPoolsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpNatPool(self, pool):
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

	def getAllIpNatPools(self):
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

