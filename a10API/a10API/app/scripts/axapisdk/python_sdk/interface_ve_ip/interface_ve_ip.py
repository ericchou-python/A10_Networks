########################################################################################################################
# File name: interface_ve_ip.py
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
	'https://axapi.a10networks.com/axapi/v3/interface/ve/ip',
]

def deserialize_Interface_ve_ip_address_val_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val = data.get('address_val')
	netmask = data.get('netmask')
	result = Interface_ve_ip_address_val_cfg(address_val=address_val, netmask=netmask)
	return result

def deserialize_list_Interface_ve_ip_address_val_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_ve_ip_address_val_cfg_json(item))
	return list(container)

def deserialize_Ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val_cfg = deserialize_list_Interface_ve_ip_address_val_cfg_json(data.get('address_val-cfg'))
	dhcp = data.get('dhcp')
	result = Ip__address(address_val_cfg=address_val_cfg, dhcp=dhcp)
	return result

def deserialize_Ip__nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	inside = data.get('inside')
	outside = data.get('outside')
	result = Ip__nat(inside=inside, outside=outside)
	return result

def deserialize_Ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Ip__address_json(data.get('address'))
	helper_address = data.get('helper-address')
	nat = deserialize_Ip__nat_json(data.get('nat'))
	generate_membership_query = data.get('generate-membership-query')
	generate_membership_query_val = data.get('generate-membership-query-val')
	max_resp_time = data.get('max-resp-time')
	result = Ip(address=address, helper_address=helper_address, nat=nat, generate_membership_query=generate_membership_query, generate_membership_query_val=generate_membership_query_val, max_resp_time=max_resp_time)
	return result

def serialize_Interface_ve_ip_address_val_cfg_json(obj):
	output = OrderedDict()
	if obj.address_val is not None:
		output['address_val'] = obj.address_val
	if obj.netmask is not None:
		output['netmask'] = obj.netmask
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Interface_ve_ip_address_val_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_ve_ip_address_val_cfg_json(item))
	return output

def serialize_Ip__address_json(obj):
	output = OrderedDict()
	if obj.address_val_cfg is not None:
		output['address_val-cfg'] = serialize_list_Interface_ve_ip_address_val_cfg_json(obj.address_val_cfg)
	if obj.dhcp is not None:
		output['dhcp'] = obj.dhcp
	return output

def serialize_Ip__nat_json(obj):
	output = OrderedDict()
	if obj.inside is not None:
		output['inside'] = obj.inside
	if obj.outside is not None:
		output['outside'] = obj.outside
	return output

def serialize_Ip_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = serialize_Ip__address_json(obj.address)
	if obj.helper_address is not None:
		output['helper-address'] = obj.helper_address
	if obj.nat is not None:
		output['nat'] = serialize_Ip__nat_json(obj.nat)
	if obj.generate_membership_query is not None:
		output['generate-membership-query'] = obj.generate_membership_query
	if obj.generate_membership_query_val is not None:
		output['generate-membership-query-val'] = obj.generate_membership_query_val
	if obj.max_resp_time is not None:
		output['max-resp-time'] = obj.max_resp_time
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_json(item))
	return list(container)

class Ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	dhcp=PosRangedInteger(0, 1)
	def __init__(self, address_val_cfg=None, dhcp=None):
		self.address_val_cfg = address_val_cfg
		self.dhcp = dhcp

	def __str__(self):
		return ""

class Ip__nat(AxapiObject):
	__metaclass__ = StructMeta 
	inside=PosRangedInteger(0, 1)
	outside=PosRangedInteger(0, 1)
	def __init__(self, inside=None, outside=None):
		self.inside = inside
		self.outside = outside

	def __str__(self):
		return ""

class Ip(AxapiObject):
	__metaclass__ = StructMeta 
	helper_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	generate_membership_query=PosRangedInteger(0, 1)
	generate_membership_query_val=PosRangedInteger(1, 255)
	max_resp_time=PosRangedInteger(1, 255)
	def __init__(self, address=None, helper_address=None, nat=None, generate_membership_query=None, generate_membership_query_val=None, max_resp_time=None):
		self.address = address
		self.helper_address = helper_address
		self.nat = nat
		self.generate_membership_query = generate_membership_query
		self.generate_membership_query_val = generate_membership_query_val
		self.max_resp_time = max_resp_time

	def __str__(self):
		return ""

class Interface_ve_ip_address_val_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	address_val = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, address_val=None, netmask=None):
		self.address_val = address_val
		self.netmask = netmask

	def __str__(self):
		return ""

class InterfaceVeIpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getInterfaceVeIp(self):
		"""
		Retrieve the ip identified by the specified identifier
		
		Returns:
			An instance of the Ip class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ip does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ip')
		return deserialize_Ip_json(payload)

	def putInterfaceVeIp(self, ip):
		"""
		Replace the object ip
		
		Args:
			ip An instance of the Ip class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ip']=serialize_Ip_json(ip)
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

	def deleteInterfaceVeIp(self):
		"""
		Remove the ip identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ip does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllInterfaceVeIpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitInterfaceVeIp(self, ip):
		"""
		Create the object ip
		
		Args:
			ip An instance of the Ip class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ip']=serialize_Ip_json(ip)
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

	def getAllInterfaceVeIps(self):
		"""
		Retrieve all ip objects currently pending in the system
		
		Returns:
			A list of Ip objects
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
			payload= data.get('ipList')
		return deserialize_list_Ip_json(payload)

