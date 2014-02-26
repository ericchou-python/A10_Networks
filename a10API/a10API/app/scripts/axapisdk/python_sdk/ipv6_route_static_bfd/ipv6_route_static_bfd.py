########################################################################################################################
# File name: ipv6_route_static_bfd.py
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
	'https://axapi.a10networks.com/axapi/v3/ipv6/route/static/bfd',
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

def deserialize_Bfd_json(obj):
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
	result = Bfd(local_ipv6=local_ipv6, nexthop_ipv6=nexthop_ipv6, velist=velist, trunklist=trunklist, ethernetlist=ethernetlist)
	return result

def serialize_Ipv6_route_static_bfd_ve_json(obj):
	output = OrderedDict()
	output['ve-num'] = obj.ve_num
	output['nexthop-ipv6-ll'] = obj.nexthop_ipv6_ll
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ipv6_route_static_bfd_ve_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ipv6_route_static_bfd_ve_json(item))
	return output

def serialize_Ipv6_route_static_bfd_trunk_json(obj):
	output = OrderedDict()
	output['trunk-num'] = obj.trunk_num
	output['nexthop-ipv6-ll'] = obj.nexthop_ipv6_ll
	return output

def serialize_list_Ipv6_route_static_bfd_trunk_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ipv6_route_static_bfd_trunk_json(item))
	return output

def serialize_Ipv6_route_static_bfd_ethernet_json(obj):
	output = OrderedDict()
	output['eth-num'] = obj.eth_num
	output['nexthop-ipv6-ll'] = obj.nexthop_ipv6_ll
	return output

def serialize_list_Ipv6_route_static_bfd_ethernet_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ipv6_route_static_bfd_ethernet_json(item))
	return output

def serialize_Bfd_json(obj):
	output = OrderedDict()
	output['local-ipv6'] = obj.local_ipv6
	output['nexthop-ipv6'] = obj.nexthop_ipv6
	if obj.velist is not None:
		output['veList'] = serialize_list_Ipv6_route_static_bfd_ve_json(obj.velist)
	if obj.trunklist is not None:
		output['trunkList'] = serialize_list_Ipv6_route_static_bfd_trunk_json(obj.trunklist)
	if obj.ethernetlist is not None:
		output['ethernetList'] = serialize_list_Ipv6_route_static_bfd_ethernet_json(obj.ethernetlist)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Bfd_json(item))
	return list(container)

class Bfd(AxapiObject):
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

class Bfd_local_ipv6_local_ipv6_nexthop_ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	local_ipv6=SizedString(1, 255)
	nexthop_ipv6=SizedString(1, 255)
	def __init__(self, local_ipv6, nexthop_ipv6):
		self.local_ipv6 = local_ipv6
		self.nexthop_ipv6 = nexthop_ipv6

	def __str__(self):
		return str(self.local_ipv6) + '+' + str(self.nexthop_ipv6)

class Ipv6_route_static_bfd_ethernet(AxapiObject):
	__metaclass__ = StructMeta 
	eth_num=PosInteger()
	nexthop_ipv6_ll=SizedString(1, 255)
	def __init__(self, eth_num, nexthop_ipv6_ll):
		self.eth_num = eth_num
		self.nexthop_ipv6_ll = nexthop_ipv6_ll

	def __str__(self):
		return str(self.eth_num) + '+' + str(self.nexthop_ipv6_ll)

class Ipv6RouteStaticBfdClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpv6RouteStaticBfd(self, bfd_local_ipv6_local_ipv6_nexthop_ipv6):
		"""
		Retrieve the bfd identified by the specified identifier
		
		Args:
			bfd_local_ipv6_local_ipv6_nexthop_ipv6 Bfd_local_ipv6_local_ipv6_nexthop_ipv6
		
		Returns:
			An instance of the Bfd class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(bfd_local_ipv6_local_ipv6_nexthop_ipv6) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bfd does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('bfd')
		return deserialize_Bfd_json(payload)

	def putIpv6RouteStaticBfd(self, bfd_local_ipv6_local_ipv6_nexthop_ipv6, bfd):
		"""
		Replace the object bfd
		
		Args:
			bfd_local_ipv6_local_ipv6_nexthop_ipv6 Bfd_local_ipv6_local_ipv6_nexthop_ipv6
			bfd An instance of the Bfd class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bfd']=serialize_Bfd_json(bfd)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(bfd_local_ipv6_local_ipv6_nexthop_ipv6) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpv6RouteStaticBfd(self, bfd_local_ipv6_local_ipv6_nexthop_ipv6):
		"""
		Remove the bfd identified by the specified identifier from the system
		
		Args:
			bfd_local_ipv6_local_ipv6_nexthop_ipv6 Bfd_local_ipv6_local_ipv6_nexthop_ipv6
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(bfd_local_ipv6_local_ipv6_nexthop_ipv6) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bfd does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpv6RouteStaticBfdsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpv6RouteStaticBfd(self, bfd):
		"""
		Create the object bfd
		
		Args:
			bfd An instance of the Bfd class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bfd']=serialize_Bfd_json(bfd)
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

	def getAllIpv6RouteStaticBfds(self):
		"""
		Retrieve all bfd objects currently pending in the system
		
		Returns:
			A list of Bfd objects
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
			payload= data.get('bfdList')
		return deserialize_list_Bfd_json(payload)

