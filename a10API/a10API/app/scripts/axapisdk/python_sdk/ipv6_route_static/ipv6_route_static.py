########################################################################################################################
# File name: ipv6_route_static.py
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
	'https://axapi.a10networks.com/axapi/v3/ipv6/route/static',
]

def deserialize_Ipv6_route_static_bfd_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ve_num = data.get('ve-num')
	nexthop_ipv6_ll = data.get('nexthop-ipv6-ll')
	result = Ipv6_route_static_bfd_ve(ve_num=ve_num, nexthop_ipv6_ll=nexthop_ipv6_ll)
	return result

def deserialize_list_Ipv6_route_static_bfd_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_route_static_bfd_ve_json(item))
	return list(container)

def deserialize_Ipv6_route_static_bfd_trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk_num = data.get('trunk-num')
	nexthop_ipv6_ll = data.get('nexthop-ipv6-ll')
	result = Ipv6_route_static_bfd_trunk(trunk_num=trunk_num, nexthop_ipv6_ll=nexthop_ipv6_ll)
	return result

def deserialize_list_Ipv6_route_static_bfd_trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_route_static_bfd_trunk_json(item))
	return list(container)

def deserialize_Ipv6_route_static_bfd_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	eth_num = data.get('eth-num')
	nexthop_ipv6_ll = data.get('nexthop-ipv6-ll')
	result = Ipv6_route_static_bfd_ethernet(eth_num=eth_num, nexthop_ipv6_ll=nexthop_ipv6_ll)
	return result

def deserialize_list_Ipv6_route_static_bfd_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_route_static_bfd_ethernet_json(item))
	return list(container)

def deserialize_Ipv6_route_static_bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_ipv6 = data.get('local-ipv6')
	nexthop_ipv6 = data.get('nexthop-ipv6')
	velist = deserialize_list_Ipv6_route_static_bfd_ve_json(data.get('veList'))
	trunklist = deserialize_list_Ipv6_route_static_bfd_trunk_json(data.get('trunkList'))
	ethernetlist = deserialize_list_Ipv6_route_static_bfd_ethernet_json(data.get('ethernetList'))
	result = Ipv6_route_static_bfd(local_ipv6=local_ipv6, nexthop_ipv6=nexthop_ipv6, velist=velist, trunklist=trunklist, ethernetlist=ethernetlist)
	return result

def deserialize_list_Ipv6_route_static_bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_route_static_bfd_json(item))
	return list(container)

def deserialize_Static_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bfdlist = deserialize_list_Ipv6_route_static_bfd_json(data.get('bfdList'))
	result = Static(bfdlist=bfdlist)
	return result

class Static(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, bfdlist=None):
		self.bfdlist = bfdlist

	def __str__(self):
		return ""

class Ipv6_route_static_bfd(AxapiObject):
	__metaclass__ = StructMeta 
	local_ipv6=SizedString(1, 255)
	nexthop_ipv6=SizedString(1, 255)
	def __init__(self, local_ipv6, nexthop_ipv6, velist=None, trunklist=None, ethernetlist=None):
		self.local_ipv6 = local_ipv6
		self.nexthop_ipv6 = nexthop_ipv6
		self.velist = velist
		self.trunklist = trunklist
		self.ethernetlist = ethernetlist

	def __str__(self):
		return str(self.local_ipv6) + '+' + str(self.nexthop_ipv6)

class Ipv6_route_static_bfd_ve(AxapiObject):
	__metaclass__ = StructMeta 
	ve_num=PosInteger()
	nexthop_ipv6_ll=SizedString(1, 255)
	def __init__(self, ve_num, nexthop_ipv6_ll):
		self.ve_num = ve_num
		self.nexthop_ipv6_ll = nexthop_ipv6_ll

	def __str__(self):
		return str(self.ve_num) + '+' + str(self.nexthop_ipv6_ll)

class Ipv6_route_static_bfd_trunk(AxapiObject):
	__metaclass__ = StructMeta 
	trunk_num=PosInteger()
	nexthop_ipv6_ll=SizedString(1, 255)
	def __init__(self, trunk_num, nexthop_ipv6_ll):
		self.trunk_num = trunk_num
		self.nexthop_ipv6_ll = nexthop_ipv6_ll

	def __str__(self):
		return str(self.trunk_num) + '+' + str(self.nexthop_ipv6_ll)

class Ipv6_route_static_bfd_ethernet(AxapiObject):
	__metaclass__ = StructMeta 
	eth_num=PosInteger()
	nexthop_ipv6_ll=SizedString(1, 255)
	def __init__(self, eth_num, nexthop_ipv6_ll):
		self.eth_num = eth_num
		self.nexthop_ipv6_ll = nexthop_ipv6_ll

	def __str__(self):
		return str(self.eth_num) + '+' + str(self.nexthop_ipv6_ll)

class Ipv6RouteStaticClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpv6RouteStatic(self):
		"""
		Retrieve the static identified by the specified identifier
		
		Returns:
			An instance of the Static class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified static does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('static')
		return deserialize_Static_json(payload)

