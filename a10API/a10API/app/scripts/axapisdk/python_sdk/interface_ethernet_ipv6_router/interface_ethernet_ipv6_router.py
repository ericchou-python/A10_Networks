########################################################################################################################
# File name: interface_ethernet_ipv6_router.py
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
	'https://axapi.a10networks.com/axapi/v3/interface/ethernet/ipv6/router',
]

def deserialize_Router__isis_v6_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	isis_options = data.get('isis-options')
	result = Router__isis_v6_cfg(isis_options=isis_options)
	return result

def deserialize_Router__ospf_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	result = Router__ospf()
	return result

def deserialize_Router_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	isis_v6_cfg = deserialize_Router__isis_v6_cfg_json(data.get('isis-v6-cfg'))
	ospf = deserialize_Router__ospf_json(data.get('ospf'))
	result = Router(isis_v6_cfg=isis_v6_cfg, ospf=ospf)
	return result

def serialize_Router__isis_v6_cfg_json(obj):
	output = OrderedDict()
	if obj.isis_options is not None:
		output['isis-options'] = obj.isis_options
	return output

def serialize_Router__ospf_json(obj):
	output = OrderedDict()
	return output

def serialize_Router_json(obj):
	output = OrderedDict()
	if obj.isis_v6_cfg is not None:
		output['isis-v6-cfg'] = serialize_Router__isis_v6_cfg_json(obj.isis_v6_cfg)
	if obj.ospf is not None:
		output['ospf'] = serialize_Router__ospf_json(obj.ospf)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Router_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_json(item))
	return list(container)

class Router__isis_v6_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	isis_options=SizedString(1, 255)
	def __init__(self, isis_options=None):
		self.isis_options = isis_options

	def __str__(self):
		return ""

class Router__ospf(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class Router(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, isis_v6_cfg=None, ospf=None):
		self.isis_v6_cfg = isis_v6_cfg
		self.ospf = ospf

	def __str__(self):
		return ""

class InterfaceEthernetIpv6RouterClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getInterfaceEthernetIpv6Router(self):
		"""
		Retrieve the router identified by the specified identifier
		
		Returns:
			An instance of the Router class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified router does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('router')
		return deserialize_Router_json(payload)

	def putInterfaceEthernetIpv6Router(self, router):
		"""
		Replace the object router
		
		Args:
			router An instance of the Router class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['router']=serialize_Router_json(router)
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

	def deleteInterfaceEthernetIpv6Router(self):
		"""
		Remove the router identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified router does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllInterfaceEthernetIpv6RoutersClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitInterfaceEthernetIpv6Router(self, router):
		"""
		Create the object router
		
		Args:
			router An instance of the Router class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['router']=serialize_Router_json(router)
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

	def getAllInterfaceEthernetIpv6Routers(self):
		"""
		Retrieve all router objects currently pending in the system
		
		Returns:
			A list of Router objects
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
			payload= data.get('routerList')
		return deserialize_list_Router_json(payload)

