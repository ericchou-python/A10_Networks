########################################################################################################################
# File name: router_bgp_address_family.py
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
	'https://axapi.a10networks.com/axapi/v3/router/bgp/address-family',
]

def deserialize_Router_bgp_address_family_ipv6_neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	result = Router_bgp_address_family_ipv6_neighbor()
	return result

def deserialize_list_Router_bgp_address_family_ipv6_neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_address_family_ipv6_neighbor_json(item))
	return list(container)

def deserialize_Address_family__ipv6__redistribute_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	result = Address_family__ipv6__redistribute()
	return result

def deserialize_Address_family__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	neighborlist = deserialize_list_Router_bgp_address_family_ipv6_neighbor_json(data.get('neighborList'))
	redistribute = deserialize_Address_family__ipv6__redistribute_json(data.get('redistribute'))
	result = Address_family__ipv6(neighborlist=neighborlist, redistribute=redistribute)
	return result

def deserialize_Address_family_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6 = deserialize_Address_family__ipv6_json(data.get('ipv6'))
	result = Address_family(ipv6=ipv6)
	return result

class Address_family__ipv6__redistribute(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class Address_family__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, neighborlist=None, redistribute=None):
		self.neighborlist = neighborlist
		self.redistribute = redistribute

	def __str__(self):
		return ""

class Address_family(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ipv6=None):
		self.ipv6 = ipv6

	def __str__(self):
		return ""

class Router_bgp_address_family_ipv6_neighbor(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class RouterBgpAddressfamilyClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRouterBgpAddressfamily(self):
		"""
		Retrieve the address_family identified by the specified identifier
		
		Returns:
			An instance of the Address_family class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified address_family does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('address-family')
		return deserialize_Address_family_json(payload)

