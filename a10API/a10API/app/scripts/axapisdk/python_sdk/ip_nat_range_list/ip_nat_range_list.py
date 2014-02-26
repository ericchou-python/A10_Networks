########################################################################################################################
# File name: ip_nat_range_list.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/nat/range-list',
]

def deserialize_Range_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	local_start_ipv4_addr = data.get('local-start-ipv4-addr')
	local_netmaskv4 = data.get('local-netmaskv4')
	global_start_ipv4_addr = data.get('global-start-ipv4-addr')
	global_netmaskv4 = data.get('global-netmaskv4')
	count = data.get('count')
	vrid = data.get('vrid')
	local_start_ipv6_addr = data.get('local-start-ipv6-addr')
	global_start_ipv6_addr = data.get('global-start-ipv6-addr')
	result = Range_list(name=name, local_start_ipv4_addr=local_start_ipv4_addr, local_netmaskv4=local_netmaskv4, global_start_ipv4_addr=global_start_ipv4_addr, global_netmaskv4=global_netmaskv4, count=count, vrid=vrid, local_start_ipv6_addr=local_start_ipv6_addr, global_start_ipv6_addr=global_start_ipv6_addr)
	return result

def serialize_Range_list_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	output['local-start-ipv4-addr'] = obj.local_start_ipv4_addr
	output['local-netmaskv4'] = obj.local_netmaskv4
	output['global-start-ipv4-addr'] = obj.global_start_ipv4_addr
	output['global-netmaskv4'] = obj.global_netmaskv4
	output['count'] = obj.count
	if obj.vrid is not None:
		output['vrid'] = obj.vrid
	output['local-start-ipv6-addr'] = obj.local_start_ipv6_addr
	output['global-start-ipv6-addr'] = obj.global_start_ipv6_addr
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Range_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Range_list_json(item))
	return list(container)

class Range_list_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class Range_list(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	local_start_ipv4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	local_netmaskv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	global_start_ipv4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	global_netmaskv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	count=PosRangedInteger(1, 200000)
	vrid=PosRangedInteger(1, 31)
	local_start_ipv6_addr=SizedString(1, 255)
	global_start_ipv6_addr=SizedString(1, 255)
	def __init__(self, name, local_start_ipv4_addr, local_netmaskv4, global_start_ipv4_addr, global_netmaskv4, count, local_start_ipv6_addr, global_start_ipv6_addr, vrid=None):
		self.name = name
		self.local_start_ipv4_addr = local_start_ipv4_addr
		self.local_netmaskv4 = local_netmaskv4
		self.global_start_ipv4_addr = global_start_ipv4_addr
		self.global_netmaskv4 = global_netmaskv4
		self.count = count
		self.vrid = vrid
		self.local_start_ipv6_addr = local_start_ipv6_addr
		self.global_start_ipv6_addr = global_start_ipv6_addr

	def __str__(self):
		return str(self.name) + '+' + str(self.local_start_ipv4_addr) + '+' + str(self.local_netmaskv4) + '+' + str(self.global_start_ipv4_addr) + '+' + str(self.global_netmaskv4) + '+' + str(self.count) + '+' + str(self.local_start_ipv6_addr) + '+' + str(self.global_start_ipv6_addr)

class IpNatRangelistClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpNatRangelist(self, range_list_name):
		"""
		Retrieve the range_list identified by the specified identifier
		
		Args:
			range_list_name Range_list_name
		
		Returns:
			An instance of the Range_list class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(range_list_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified range_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('range-list')
		return deserialize_Range_list_json(payload)

	def putIpNatRangelist(self, range_list_name, range_list):
		"""
		Replace the object range_list
		
		Args:
			range_list_name Range_list_name
			range_list An instance of the Range_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['range-list']=serialize_Range_list_json(range_list)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(range_list_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpNatRangelist(self, range_list_name):
		"""
		Remove the range_list identified by the specified identifier from the system
		
		Args:
			range_list_name Range_list_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(range_list_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified range_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpNatRangelistsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpNatRangelist(self, range_list):
		"""
		Create the object range_list
		
		Args:
			range_list An instance of the Range_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['range-list']=serialize_Range_list_json(range_list)
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

	def getAllIpNatRangelists(self):
		"""
		Retrieve all range_list objects currently pending in the system
		
		Returns:
			A list of Range_list objects
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
			payload= data.get('range-listList')
		return deserialize_list_Range_list_json(payload)

