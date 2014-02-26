########################################################################################################################
# File name: interface_loopback_ipv6.py
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
	'https://axapi.a10networks.com/axapi/v3/interface/loopback/ipv6',
]

def deserialize_Interface_loopback_ipv6_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	anycast = data.get('anycast')
	link_local = data.get('link-local')
	result = Interface_loopback_ipv6_address_cfg(ipv6_addr=ipv6_addr, anycast=anycast, link_local=link_local)
	return result

def deserialize_list_Interface_loopback_ipv6_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_loopback_ipv6_address_cfg_json(item))
	return list(container)

def deserialize_Ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_cfg = deserialize_list_Interface_loopback_ipv6_address_cfg_json(data.get('address-cfg'))
	ipv6_enable = data.get('ipv6-enable')
	result = Ipv6(address_cfg=address_cfg, ipv6_enable=ipv6_enable)
	return result

def serialize_Interface_loopback_ipv6_address_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv6_addr is not None:
		output['ipv6-addr'] = obj.ipv6_addr
	if obj.anycast is not None:
		output['anycast'] = obj.anycast
	if obj.link_local is not None:
		output['link-local'] = obj.link_local
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Interface_loopback_ipv6_address_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_loopback_ipv6_address_cfg_json(item))
	return output

def serialize_Ipv6_json(obj):
	output = OrderedDict()
	if obj.address_cfg is not None:
		output['address-cfg'] = serialize_list_Interface_loopback_ipv6_address_cfg_json(obj.address_cfg)
	if obj.ipv6_enable is not None:
		output['ipv6-enable'] = obj.ipv6_enable
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

class Ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_enable=PosRangedInteger(0, 1)
	def __init__(self, address_cfg=None, ipv6_enable=None):
		self.address_cfg = address_cfg
		self.ipv6_enable = ipv6_enable

	def __str__(self):
		return ""

class Interface_loopback_ipv6_address_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	anycast=PosRangedInteger(0, 1)
	link_local=PosRangedInteger(0, 1)
	def __init__(self, ipv6_addr=None, anycast=None, link_local=None):
		self.ipv6_addr = ipv6_addr
		self.anycast = anycast
		self.link_local = link_local

	def __str__(self):
		return ""

class InterfaceLoopbackIpv6Client(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getInterfaceLoopbackIpv6(self):
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

	def putInterfaceLoopbackIpv6(self, ipv6):
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

	def deleteInterfaceLoopbackIpv6(self):
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

class AllInterfaceLoopbackIpv6sClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitInterfaceLoopbackIpv6(self, ipv6):
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

	def getAllInterfaceLoopbackIpv6s(self):
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

