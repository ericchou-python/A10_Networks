########################################################################################################################
# File name: ddos_local_address_ip.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/local-address/ip',
]

def deserialize_Ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_addr = data.get('ip-addr')
	result = Ip(ip_addr=ip_addr)
	return result

def serialize_Ip_json(obj):
	output = OrderedDict()
	output['ip-addr'] = obj.ip_addr
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

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

class Ip_ip_addr_ip_addr(AxapiObject):
	__metaclass__ = StructMeta 
	ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ip_addr):
		self.ip_addr = ip_addr

	def __str__(self):
		return str(self.ip_addr)

class Ip(AxapiObject):
	__metaclass__ = StructMeta 
	ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ip_addr):
		self.ip_addr = ip_addr

	def __str__(self):
		return str(self.ip_addr)

class DdosLocaladdressIpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosLocaladdressIp(self, ip_ip_addr_ip_addr):
		"""
		Retrieve the ip identified by the specified identifier
		
		Args:
			ip_ip_addr_ip_addr Ip_ip_addr_ip_addr
		
		Returns:
			An instance of the Ip class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(ip_ip_addr_ip_addr) .replace("/", "%2f") + query, headers=headers)
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

	def putDdosLocaladdressIp(self, ip_ip_addr_ip_addr, ip):
		"""
		Replace the object ip
		
		Args:
			ip_ip_addr_ip_addr Ip_ip_addr_ip_addr
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
		conn.request('PUT', self.get_path() + '/' + str(ip_ip_addr_ip_addr) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosLocaladdressIp(self, ip_ip_addr_ip_addr):
		"""
		Remove the ip identified by the specified identifier from the system
		
		Args:
			ip_ip_addr_ip_addr Ip_ip_addr_ip_addr
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(ip_ip_addr_ip_addr) .replace("/", "%2f") + query, headers=headers)
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

class AllDdosLocaladdressIpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosLocaladdressIp(self, ip):
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

	def getAllDdosLocaladdressIps(self):
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

