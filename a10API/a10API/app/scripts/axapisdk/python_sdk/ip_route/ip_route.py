########################################################################################################################
# File name: ip_route.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/route',
]

def deserialize_Route__ip_dest_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_dest_addr = data.get('ip_dest_addr')
	ip_mask = data.get('ip_mask')
	ip_next_hop = data.get('ip_next_hop')
	distance = data.get('distance')
	result = Route__ip_dest_cfg(ip_dest_addr=ip_dest_addr, ip_mask=ip_mask, ip_next_hop=ip_next_hop, distance=distance)
	return result

def deserialize_Ip_route_static_bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_ip = data.get('local-ip')
	nexthop_ip = data.get('nexthop-ip')
	result = Ip_route_static_bfd(local_ip=local_ip, nexthop_ip=nexthop_ip)
	return result

def deserialize_list_Ip_route_static_bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_route_static_bfd_json(item))
	return list(container)

def deserialize_Route__static_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bfdlist = deserialize_list_Ip_route_static_bfd_json(data.get('bfdList'))
	result = Route__static(bfdlist=bfdlist)
	return result

def deserialize_Route_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_dest_cfg = deserialize_Route__ip_dest_cfg_json(data.get('ip-dest-cfg'))
	static = deserialize_Route__static_json(data.get('static'))
	result = Route(ip_dest_cfg=ip_dest_cfg, static=static)
	return result

def serialize_Route__ip_dest_cfg_json(obj):
	output = OrderedDict()
	output['ip_dest_addr'] = obj.ip_dest_addr
	output['ip_mask'] = obj.ip_mask
	output['ip_next_hop'] = obj.ip_next_hop
	if obj.distance is not None:
		output['distance'] = obj.distance
	return output

def serialize_Ip_route_static_bfd_json(obj):
	output = OrderedDict()
	output['local-ip'] = obj.local_ip
	output['nexthop-ip'] = obj.nexthop_ip
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ip_route_static_bfd_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_route_static_bfd_json(item))
	return output

def serialize_Route__static_json(obj):
	output = OrderedDict()
	if obj.bfdlist is not None:
		output['bfdList'] = serialize_list_Ip_route_static_bfd_json(obj.bfdlist)
	return output

def serialize_Route_json(obj):
	output = OrderedDict()
	output['ip-dest-cfg'] = serialize_Route__ip_dest_cfg_json(obj.ip_dest_cfg)
	if obj.static is not None:
		output['static'] = serialize_Route__static_json(obj.static)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Route_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Route_json(item))
	return list(container)

class Route__ip_dest_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip_dest_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_next_hop = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	distance=PosRangedInteger(1, 255)
	def __init__(self, ip_dest_addr, ip_mask, ip_next_hop, distance=None):
		self.ip_dest_addr = ip_dest_addr
		self.ip_mask = ip_mask
		self.ip_next_hop = ip_next_hop
		self.distance = distance

	def __str__(self):
		return str(self.ip_dest_addr) + '+' + str(self.ip_mask) + '+' + str(self.ip_next_hop)

class Route__static(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, bfdlist=None):
		self.bfdlist = bfdlist

	def __str__(self):
		return ""

class Route(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ip_dest_cfg, static=None):
		self.ip_dest_cfg = ip_dest_cfg
		self.static = static

	def __str__(self):
		return str(self.ip_dest_cfg)

class Route_ip_dest_cfg_ip_mask_ip_next_hop__ip_dest_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip_dest_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_next_hop = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	distance=PosRangedInteger(1, 255)
	def __init__(self, ip_dest_addr, ip_mask, ip_next_hop, distance=None):
		self.ip_dest_addr = ip_dest_addr
		self.ip_mask = ip_mask
		self.ip_next_hop = ip_next_hop
		self.distance = distance

	def __str__(self):
		return str(self.ip_dest_addr) + '+' + str(self.ip_mask) + '+' + str(self.ip_next_hop)

class Route_ip_dest_cfg_ip_mask_ip_next_hop(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ip_dest_cfg):
		self.ip_dest_cfg = ip_dest_cfg

	def __str__(self):
		return str(self.ip_dest_cfg)

class Ip_route_static_bfd(AxapiObject):
	__metaclass__ = StructMeta 
	local_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	nexthop_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, local_ip, nexthop_ip):
		self.local_ip = local_ip
		self.nexthop_ip = nexthop_ip

	def __str__(self):
		return str(self.local_ip) + '+' + str(self.nexthop_ip)

class IpRouteClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpRoute(self, route_ip_dest_cfg_ip_mask_ip_next_hop):
		"""
		Retrieve the route identified by the specified identifier
		
		Args:
			route_ip_dest_cfg_ip_mask_ip_next_hop Route_ip_dest_cfg_ip_mask_ip_next_hop
		
		Returns:
			An instance of the Route class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(route_ip_dest_cfg_ip_mask_ip_next_hop) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified route does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('route')
		return deserialize_Route_json(payload)

	def putIpRoute(self, route_ip_dest_cfg_ip_mask_ip_next_hop, route):
		"""
		Replace the object route
		
		Args:
			route_ip_dest_cfg_ip_mask_ip_next_hop Route_ip_dest_cfg_ip_mask_ip_next_hop
			route An instance of the Route class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['route']=serialize_Route_json(route)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(route_ip_dest_cfg_ip_mask_ip_next_hop) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpRoute(self, route_ip_dest_cfg_ip_mask_ip_next_hop):
		"""
		Remove the route identified by the specified identifier from the system
		
		Args:
			route_ip_dest_cfg_ip_mask_ip_next_hop Route_ip_dest_cfg_ip_mask_ip_next_hop
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(route_ip_dest_cfg_ip_mask_ip_next_hop) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified route does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpRoutesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpRoute(self, route):
		"""
		Create the object route
		
		Args:
			route An instance of the Route class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['route']=serialize_Route_json(route)
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

	def getAllIpRoutes(self):
		"""
		Retrieve all route objects currently pending in the system
		
		Returns:
			A list of Route objects
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
			payload= data.get('routeList')
		return deserialize_list_Route_json(payload)

