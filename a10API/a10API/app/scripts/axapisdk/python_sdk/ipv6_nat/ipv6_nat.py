########################################################################################################################
# File name: ipv6_nat.py
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
	'https://axapi.a10networks.com/axapi/v3/ipv6/nat',
]

def deserialize_Ipv6_nat_pool__pool_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	gateway = data.get('gateway')
	vrid = data.get('vrid')
	ip_rr = data.get('ip-rr')
	result = Ipv6_nat_pool__pool_cfg(gateway=gateway, vrid=vrid, ip_rr=ip_rr)
	return result

def deserialize_Ipv6_nat_pool_json(obj):
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
	pool_cfg = deserialize_Ipv6_nat_pool__pool_cfg_json(data.get('pool-cfg'))
	result = Ipv6_nat_pool(pool_name=pool_name, start_address=start_address, end_address=end_address, netmask=netmask, pool_cfg=pool_cfg)
	return result

def deserialize_list_Ipv6_nat_pool_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_nat_pool_json(item))
	return list(container)

def deserialize_Nat__inside__source_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	list = data.get('list')
	pool = data.get('pool')
	result = Nat__inside__source(list=list, pool=pool)
	return result

def deserialize_Nat__inside_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	source = deserialize_Nat__inside__source_json(data.get('source'))
	result = Nat__inside(source=source)
	return result

def deserialize_Nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	poollist = deserialize_list_Ipv6_nat_pool_json(data.get('poolList'))
	inside = deserialize_Nat__inside_json(data.get('inside'))
	result = Nat(poollist=poollist, inside=inside)
	return result

class Nat__inside__source(AxapiObject):
	__metaclass__ = StructMeta 
	list=SizedString(1, 16)
	pool=SizedString(1, 63)
	def __init__(self, list=None, pool=None):
		self.list = list
		self.pool = pool

	def __str__(self):
		return ""

class Nat__inside(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, source=None):
		self.source = source

	def __str__(self):
		return ""

class Nat(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, poollist=None, inside=None):
		self.poollist = poollist
		self.inside = inside

	def __str__(self):
		return ""

class Ipv6_nat_pool__pool_cfg(AxapiObject):
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

class Ipv6_nat_pool(AxapiObject):
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

class Ipv6NatClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpv6Nat(self):
		"""
		Retrieve the nat identified by the specified identifier
		
		Returns:
			An instance of the Nat class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified nat does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('nat')
		return deserialize_Nat_json(payload)

