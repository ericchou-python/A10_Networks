########################################################################################################################
# File name: router_ipv6_ospf.py
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
	'https://axapi.a10networks.com/axapi/v3/router/ipv6/ospf',
]

def deserialize_Router_ipv6_ospf_area_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	result = Router_ipv6_ospf_area()
	return result

def deserialize_list_Router_ipv6_ospf_area_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_ipv6_ospf_area_json(item))
	return list(container)

def deserialize_Ospf__redistribute_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	result = Ospf__redistribute()
	return result

def deserialize_Ospf_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	arealist = deserialize_list_Router_ipv6_ospf_area_json(data.get('areaList'))
	redistribute = deserialize_Ospf__redistribute_json(data.get('redistribute'))
	result = Ospf(arealist=arealist, redistribute=redistribute)
	return result

def serialize_Router_ipv6_ospf_area_json(obj):
	output = OrderedDict()
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Router_ipv6_ospf_area_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_ipv6_ospf_area_json(item))
	return output

def serialize_Ospf__redistribute_json(obj):
	output = OrderedDict()
	return output

def serialize_Ospf_json(obj):
	output = OrderedDict()
	if obj.arealist is not None:
		output['areaList'] = serialize_list_Router_ipv6_ospf_area_json(obj.arealist)
	if obj.redistribute is not None:
		output['redistribute'] = serialize_Ospf__redistribute_json(obj.redistribute)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Ospf_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ospf_json(item))
	return list(container)

class Ospf__redistribute(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class Ospf(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, arealist=None, redistribute=None):
		self.arealist = arealist
		self.redistribute = redistribute

	def __str__(self):
		return ""

class Router_ipv6_ospf_area(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class RouterIpv6OspfClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRouterIpv6Ospf(self):
		"""
		Retrieve the ospf identified by the specified identifier
		
		Returns:
			An instance of the Ospf class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ospf does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ospf')
		return deserialize_Ospf_json(payload)

	def putRouterIpv6Ospf(self, ospf):
		"""
		Replace the object ospf
		
		Args:
			ospf An instance of the Ospf class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ospf']=serialize_Ospf_json(ospf)
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

	def deleteRouterIpv6Ospf(self):
		"""
		Remove the ospf identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ospf does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllRouterIpv6OspfsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitRouterIpv6Ospf(self, ospf):
		"""
		Create the object ospf
		
		Args:
			ospf An instance of the Ospf class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ospf']=serialize_Ospf_json(ospf)
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

	def getAllRouterIpv6Ospfs(self):
		"""
		Retrieve all ospf objects currently pending in the system
		
		Returns:
			A list of Ospf objects
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
			payload= data.get('ospfList')
		return deserialize_list_Ospf_json(payload)

