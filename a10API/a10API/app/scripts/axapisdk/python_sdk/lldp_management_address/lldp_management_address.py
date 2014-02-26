########################################################################################################################
# File name: lldp_management_address.py
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
	'https://axapi.a10networks.com/axapi/v3/lldp/management-address',
]

def deserialize_Management_address__dns_cfg__interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet = data.get('ethernet')
	ve = data.get('ve')
	management = data.get('management')
	result = Management_address__dns_cfg__interface(ethernet=ethernet, ve=ve, management=management)
	return result

def deserialize_Management_address__dns_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns = data.get('dns')
	interface = deserialize_Management_address__dns_cfg__interface_json(data.get('interface'))
	result = Management_address__dns_cfg(dns=dns, interface=interface)
	return result

def deserialize_Management_address__ipv4_cfg__interface_ipv4_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4_eth = data.get('ipv4-eth')
	ipv4_ve = data.get('ipv4-ve')
	ipv4_mgmt = data.get('ipv4-mgmt')
	result = Management_address__ipv4_cfg__interface_ipv4(ipv4_eth=ipv4_eth, ipv4_ve=ipv4_ve, ipv4_mgmt=ipv4_mgmt)
	return result

def deserialize_Management_address__ipv4_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4 = data.get('ipv4')
	interface_ipv4 = deserialize_Management_address__ipv4_cfg__interface_ipv4_json(data.get('interface-ipv4'))
	result = Management_address__ipv4_cfg(ipv4=ipv4, interface_ipv4=interface_ipv4)
	return result

def deserialize_Management_address__ipv6_cfg__interface_ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_eth = data.get('ipv6-eth')
	ipv6_ve = data.get('ipv6-ve')
	ipv6_mgmt = data.get('ipv6-mgmt')
	result = Management_address__ipv6_cfg__interface_ipv6(ipv6_eth=ipv6_eth, ipv6_ve=ipv6_ve, ipv6_mgmt=ipv6_mgmt)
	return result

def deserialize_Management_address__ipv6_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6 = data.get('ipv6')
	interface_ipv6 = deserialize_Management_address__ipv6_cfg__interface_ipv6_json(data.get('interface-ipv6'))
	result = Management_address__ipv6_cfg(ipv6=ipv6, interface_ipv6=interface_ipv6)
	return result

def deserialize_Management_address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns_cfg = deserialize_Management_address__dns_cfg_json(data.get('dns-cfg'))
	ipv4_cfg = deserialize_Management_address__ipv4_cfg_json(data.get('ipv4-cfg'))
	ipv6_cfg = deserialize_Management_address__ipv6_cfg_json(data.get('ipv6-cfg'))
	result = Management_address(dns_cfg=dns_cfg, ipv4_cfg=ipv4_cfg, ipv6_cfg=ipv6_cfg)
	return result

def serialize_Management_address__dns_cfg__interface_json(obj):
	output = OrderedDict()
	if obj.ethernet is not None:
		output['ethernet'] = obj.ethernet
	if obj.ve is not None:
		output['ve'] = obj.ve
	if obj.management is not None:
		output['management'] = obj.management
	return output

def serialize_Management_address__dns_cfg_json(obj):
	output = OrderedDict()
	if obj.dns is not None:
		output['dns'] = obj.dns
	if obj.interface is not None:
		output['interface'] = serialize_Management_address__dns_cfg__interface_json(obj.interface)
	return output

def serialize_Management_address__ipv4_cfg__interface_ipv4_json(obj):
	output = OrderedDict()
	if obj.ipv4_eth is not None:
		output['ipv4-eth'] = obj.ipv4_eth
	if obj.ipv4_ve is not None:
		output['ipv4-ve'] = obj.ipv4_ve
	if obj.ipv4_mgmt is not None:
		output['ipv4-mgmt'] = obj.ipv4_mgmt
	return output

def serialize_Management_address__ipv4_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv4 is not None:
		output['ipv4'] = obj.ipv4
	if obj.interface_ipv4 is not None:
		output['interface-ipv4'] = serialize_Management_address__ipv4_cfg__interface_ipv4_json(obj.interface_ipv4)
	return output

def serialize_Management_address__ipv6_cfg__interface_ipv6_json(obj):
	output = OrderedDict()
	if obj.ipv6_eth is not None:
		output['ipv6-eth'] = obj.ipv6_eth
	if obj.ipv6_ve is not None:
		output['ipv6-ve'] = obj.ipv6_ve
	if obj.ipv6_mgmt is not None:
		output['ipv6-mgmt'] = obj.ipv6_mgmt
	return output

def serialize_Management_address__ipv6_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv6 is not None:
		output['ipv6'] = obj.ipv6
	if obj.interface_ipv6 is not None:
		output['interface-ipv6'] = serialize_Management_address__ipv6_cfg__interface_ipv6_json(obj.interface_ipv6)
	return output

def serialize_Management_address_json(obj):
	output = OrderedDict()
	if obj.dns_cfg is not None:
		output['dns-cfg'] = serialize_Management_address__dns_cfg_json(obj.dns_cfg)
	if obj.ipv4_cfg is not None:
		output['ipv4-cfg'] = serialize_Management_address__ipv4_cfg_json(obj.ipv4_cfg)
	if obj.ipv6_cfg is not None:
		output['ipv6-cfg'] = serialize_Management_address__ipv6_cfg_json(obj.ipv6_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Management_address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Management_address_json(item))
	return list(container)

class Management_address__dns_cfg__interface(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet=PosRangedInteger(1, 2048)
	ve=PosRangedInteger(1, 4094)
	management=PosRangedInteger(0, 1)
	def __init__(self, ethernet=None, ve=None, management=None):
		self.ethernet = ethernet
		self.ve = ve
		self.management = management

	def __str__(self):
		return ""

class Management_address__dns_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dns=SizedString(1, 31)
	def __init__(self, dns=None, interface=None):
		self.dns = dns
		self.interface = interface

	def __str__(self):
		return ""

class Management_address__ipv4_cfg__interface_ipv4(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4_eth=PosRangedInteger(1, 2048)
	ipv4_ve=PosRangedInteger(1, 4094)
	ipv4_mgmt=PosRangedInteger(0, 1)
	def __init__(self, ipv4_eth=None, ipv4_ve=None, ipv4_mgmt=None):
		self.ipv4_eth = ipv4_eth
		self.ipv4_ve = ipv4_ve
		self.ipv4_mgmt = ipv4_mgmt

	def __str__(self):
		return ""

class Management_address__ipv4_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ipv4=None, interface_ipv4=None):
		self.ipv4 = ipv4
		self.interface_ipv4 = interface_ipv4

	def __str__(self):
		return ""

class Management_address__ipv6_cfg__interface_ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_eth=PosRangedInteger(1, 2048)
	ipv6_ve=PosRangedInteger(1, 4094)
	ipv6_mgmt=PosRangedInteger(0, 1)
	def __init__(self, ipv6_eth=None, ipv6_ve=None, ipv6_mgmt=None):
		self.ipv6_eth = ipv6_eth
		self.ipv6_ve = ipv6_ve
		self.ipv6_mgmt = ipv6_mgmt

	def __str__(self):
		return ""

class Management_address__ipv6_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6=SizedString(1, 255)
	def __init__(self, ipv6=None, interface_ipv6=None):
		self.ipv6 = ipv6
		self.interface_ipv6 = interface_ipv6

	def __str__(self):
		return ""

class Management_address(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, dns_cfg=None, ipv4_cfg=None, ipv6_cfg=None):
		self.dns_cfg = dns_cfg
		self.ipv4_cfg = ipv4_cfg
		self.ipv6_cfg = ipv6_cfg

	def __str__(self):
		return ""

class LldpManagementaddressClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLldpManagementaddress(self):
		"""
		Retrieve the management_address identified by the specified identifier
		
		Returns:
			An instance of the Management_address class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified management_address does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('management-address')
		return deserialize_Management_address_json(payload)

	def putLldpManagementaddress(self, management_address):
		"""
		Replace the object management_address
		
		Args:
			management_address An instance of the Management_address class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['management-address']=serialize_Management_address_json(management_address)
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

	def deleteLldpManagementaddress(self):
		"""
		Remove the management_address identified by the specified identifier from
		the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified management_address does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllLldpManagementaddresssClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitLldpManagementaddress(self, management_address):
		"""
		Create the object management_address
		
		Args:
			management_address An instance of the Management_address class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['management-address']=serialize_Management_address_json(management_address)
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

	def getAllLldpManagementaddresss(self):
		"""
		Retrieve all management_address objects currently pending in the system
		
		Returns:
			A list of Management_address objects
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
			payload= data.get('management-addressList')
		return deserialize_list_Management_address_json(payload)

