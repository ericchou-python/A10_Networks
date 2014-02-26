########################################################################################################################
# File name: router_bgp_address_family_ipv6.py
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
	'https://axapi.a10networks.com/axapi/v3/router/bgp/address-family/ipv6',
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

def deserialize_Ipv6__redistribute_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	result = Ipv6__redistribute()
	return result

def deserialize_Ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	neighborlist = deserialize_list_Router_bgp_address_family_ipv6_neighbor_json(data.get('neighborList'))
	redistribute = deserialize_Ipv6__redistribute_json(data.get('redistribute'))
	result = Ipv6(neighborlist=neighborlist, redistribute=redistribute)
	return result

def serialize_Router_bgp_address_family_ipv6_neighbor_json(obj):
	output = OrderedDict()
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Router_bgp_address_family_ipv6_neighbor_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_address_family_ipv6_neighbor_json(item))
	return output

def serialize_Ipv6__redistribute_json(obj):
	output = OrderedDict()
	return output

def serialize_Ipv6_json(obj):
	output = OrderedDict()
	if obj.neighborlist is not None:
		output['neighborList'] = serialize_list_Router_bgp_address_family_ipv6_neighbor_json(obj.neighborlist)
	if obj.redistribute is not None:
		output['redistribute'] = serialize_Ipv6__redistribute_json(obj.redistribute)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_json(item))
	return list(container)

class Ipv6__redistribute(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class Ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, neighborlist=None, redistribute=None):
		self.neighborlist = neighborlist
		self.redistribute = redistribute

	def __str__(self):
		return ""

class Router_bgp_address_family_ipv6_neighbor(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class RouterBgpAddressfamilyIpv6Client(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRouterBgpAddressfamilyIpv6(self):
		"""
		Retrieve the ipv6 identified by the specified identifier
		
		Returns:
			An instance of the Ipv6 class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ipv6 does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ipv6')
		return deserialize_Ipv6_json(payload)

	def putRouterBgpAddressfamilyIpv6(self, ipv6):
		"""
		Replace the object ipv6
		
		Args:
			ipv6 An instance of the Ipv6 class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ipv6']=serialize_Ipv6_json(ipv6)
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

	def deleteRouterBgpAddressfamilyIpv6(self):
		"""
		Remove the ipv6 identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ipv6 does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllRouterBgpAddressfamilyIpv6sClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitRouterBgpAddressfamilyIpv6(self, ipv6):
		"""
		Create the object ipv6
		
		Args:
			ipv6 An instance of the Ipv6 class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ipv6']=serialize_Ipv6_json(ipv6)
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

	def getAllRouterBgpAddressfamilyIpv6s(self):
		"""
		Retrieve all ipv6 objects currently pending in the system
		
		Returns:
			A list of Ipv6 objects
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
			payload= data.get('ipv6List')
		return deserialize_list_Ipv6_json(payload)

