########################################################################################################################
# File name: router_bgp_redistribute.py
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
	'https://axapi.a10networks.com/axapi/v3/router/bgp/redistribute',
]

def deserialize_Redistribute__connected_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	connected = data.get('connected')
	route_map = data.get('route-map')
	result = Redistribute__connected_cfg(connected=connected, route_map=route_map)
	return result

def deserialize_Redistribute__floating_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	route_map = data.get('route-map')
	result = Redistribute__floating_ip_cfg(route_map=route_map)
	return result

def deserialize_Redistribute__ip_nat_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_nat = data.get('ip-nat')
	route_map = data.get('route-map')
	result = Redistribute__ip_nat_cfg(ip_nat=ip_nat, route_map=route_map)
	return result

def deserialize_Redistribute__ip_nat_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_nat_list = data.get('ip-nat-list')
	route_map = data.get('route-map')
	result = Redistribute__ip_nat_list_cfg(ip_nat_list=ip_nat_list, route_map=route_map)
	return result

def deserialize_Redistribute__isis_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	route_map = data.get('route-map')
	result = Redistribute__isis_cfg(route_map=route_map)
	return result

def deserialize_Redistribute__kernel_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	kernel = data.get('kernel')
	route_map = data.get('route-map')
	result = Redistribute__kernel_cfg(kernel=kernel, route_map=route_map)
	return result

def deserialize_Redistribute__ospf_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ospf = data.get('ospf')
	route_map = data.get('route-map')
	result = Redistribute__ospf_cfg(ospf=ospf, route_map=route_map)
	return result

def deserialize_Redistribute__rip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	route_map = data.get('route-map')
	result = Redistribute__rip_cfg(route_map=route_map)
	return result

def deserialize_Redistribute__static_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	static = data.get('static')
	route_map = data.get('route-map')
	result = Redistribute__static_cfg(static=static, route_map=route_map)
	return result

def deserialize_Redistribute_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	connected_cfg = deserialize_Redistribute__connected_cfg_json(data.get('connected-cfg'))
	floating_ip_cfg = deserialize_Redistribute__floating_ip_cfg_json(data.get('floating-ip-cfg'))
	ip_nat_cfg = deserialize_Redistribute__ip_nat_cfg_json(data.get('ip-nat-cfg'))
	ip_nat_list_cfg = deserialize_Redistribute__ip_nat_list_cfg_json(data.get('ip-nat-list-cfg'))
	isis_cfg = deserialize_Redistribute__isis_cfg_json(data.get('isis-cfg'))
	kernel_cfg = deserialize_Redistribute__kernel_cfg_json(data.get('kernel-cfg'))
	ospf_cfg = deserialize_Redistribute__ospf_cfg_json(data.get('ospf-cfg'))
	rip_cfg = deserialize_Redistribute__rip_cfg_json(data.get('rip-cfg'))
	static_cfg = deserialize_Redistribute__static_cfg_json(data.get('static-cfg'))
	result = Redistribute(connected_cfg=connected_cfg, floating_ip_cfg=floating_ip_cfg, ip_nat_cfg=ip_nat_cfg, ip_nat_list_cfg=ip_nat_list_cfg, isis_cfg=isis_cfg, kernel_cfg=kernel_cfg, ospf_cfg=ospf_cfg, rip_cfg=rip_cfg, static_cfg=static_cfg)
	return result

def serialize_Redistribute__connected_cfg_json(obj):
	output = OrderedDict()
	if obj.connected is not None:
		output['connected'] = obj.connected
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Redistribute__floating_ip_cfg_json(obj):
	output = OrderedDict()
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Redistribute__ip_nat_cfg_json(obj):
	output = OrderedDict()
	if obj.ip_nat is not None:
		output['ip-nat'] = obj.ip_nat
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Redistribute__ip_nat_list_cfg_json(obj):
	output = OrderedDict()
	if obj.ip_nat_list is not None:
		output['ip-nat-list'] = obj.ip_nat_list
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Redistribute__isis_cfg_json(obj):
	output = OrderedDict()
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Redistribute__kernel_cfg_json(obj):
	output = OrderedDict()
	if obj.kernel is not None:
		output['kernel'] = obj.kernel
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Redistribute__ospf_cfg_json(obj):
	output = OrderedDict()
	if obj.ospf is not None:
		output['ospf'] = obj.ospf
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Redistribute__rip_cfg_json(obj):
	output = OrderedDict()
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Redistribute__static_cfg_json(obj):
	output = OrderedDict()
	if obj.static is not None:
		output['static'] = obj.static
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Redistribute_json(obj):
	output = OrderedDict()
	if obj.connected_cfg is not None:
		output['connected-cfg'] = serialize_Redistribute__connected_cfg_json(obj.connected_cfg)
	if obj.floating_ip_cfg is not None:
		output['floating-ip-cfg'] = serialize_Redistribute__floating_ip_cfg_json(obj.floating_ip_cfg)
	if obj.ip_nat_cfg is not None:
		output['ip-nat-cfg'] = serialize_Redistribute__ip_nat_cfg_json(obj.ip_nat_cfg)
	if obj.ip_nat_list_cfg is not None:
		output['ip-nat-list-cfg'] = serialize_Redistribute__ip_nat_list_cfg_json(obj.ip_nat_list_cfg)
	if obj.isis_cfg is not None:
		output['isis-cfg'] = serialize_Redistribute__isis_cfg_json(obj.isis_cfg)
	if obj.kernel_cfg is not None:
		output['kernel-cfg'] = serialize_Redistribute__kernel_cfg_json(obj.kernel_cfg)
	if obj.ospf_cfg is not None:
		output['ospf-cfg'] = serialize_Redistribute__ospf_cfg_json(obj.ospf_cfg)
	if obj.rip_cfg is not None:
		output['rip-cfg'] = serialize_Redistribute__rip_cfg_json(obj.rip_cfg)
	if obj.static_cfg is not None:
		output['static-cfg'] = serialize_Redistribute__static_cfg_json(obj.static_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Redistribute_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Redistribute_json(item))
	return list(container)

class Redistribute__connected_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	connected=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, connected=None, route_map=None):
		self.connected = connected
		self.route_map = route_map

	def __str__(self):
		return ""

class Redistribute__floating_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	route_map=SizedString(1, 255)
	def __init__(self, route_map=None):
		self.route_map = route_map

	def __str__(self):
		return ""

class Redistribute__ip_nat_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip_nat=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, ip_nat=None, route_map=None):
		self.ip_nat = ip_nat
		self.route_map = route_map

	def __str__(self):
		return ""

class Redistribute__ip_nat_list_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip_nat_list=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, ip_nat_list=None, route_map=None):
		self.ip_nat_list = ip_nat_list
		self.route_map = route_map

	def __str__(self):
		return ""

class Redistribute__isis_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	route_map=SizedString(1, 255)
	def __init__(self, route_map=None):
		self.route_map = route_map

	def __str__(self):
		return ""

class Redistribute__kernel_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	kernel=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, kernel=None, route_map=None):
		self.kernel = kernel
		self.route_map = route_map

	def __str__(self):
		return ""

class Redistribute__ospf_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ospf=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, ospf=None, route_map=None):
		self.ospf = ospf
		self.route_map = route_map

	def __str__(self):
		return ""

class Redistribute__rip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	route_map=SizedString(1, 255)
	def __init__(self, route_map=None):
		self.route_map = route_map

	def __str__(self):
		return ""

class Redistribute__static_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	static=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, static=None, route_map=None):
		self.static = static
		self.route_map = route_map

	def __str__(self):
		return ""

class Redistribute(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, connected_cfg=None, floating_ip_cfg=None, ip_nat_cfg=None, ip_nat_list_cfg=None, isis_cfg=None, kernel_cfg=None, ospf_cfg=None, rip_cfg=None, static_cfg=None):
		self.connected_cfg = connected_cfg
		self.floating_ip_cfg = floating_ip_cfg
		self.ip_nat_cfg = ip_nat_cfg
		self.ip_nat_list_cfg = ip_nat_list_cfg
		self.isis_cfg = isis_cfg
		self.kernel_cfg = kernel_cfg
		self.ospf_cfg = ospf_cfg
		self.rip_cfg = rip_cfg
		self.static_cfg = static_cfg

	def __str__(self):
		return ""

class RouterBgpRedistributeClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRouterBgpRedistribute(self):
		"""
		Retrieve the redistribute identified by the specified identifier
		
		Returns:
			An instance of the Redistribute class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified redistribute does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('redistribute')
		return deserialize_Redistribute_json(payload)

	def putRouterBgpRedistribute(self, redistribute):
		"""
		Replace the object redistribute
		
		Args:
			redistribute An instance of the Redistribute class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['redistribute']=serialize_Redistribute_json(redistribute)
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

	def deleteRouterBgpRedistribute(self):
		"""
		Remove the redistribute identified by the specified identifier from the
		system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified redistribute does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllRouterBgpRedistributesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitRouterBgpRedistribute(self, redistribute):
		"""
		Create the object redistribute
		
		Args:
			redistribute An instance of the Redistribute class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['redistribute']=serialize_Redistribute_json(redistribute)
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

	def getAllRouterBgpRedistributes(self):
		"""
		Retrieve all redistribute objects currently pending in the system
		
		Returns:
			A list of Redistribute objects
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
			payload= data.get('redistributeList')
		return deserialize_list_Redistribute_json(payload)

