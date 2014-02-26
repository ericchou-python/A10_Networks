########################################################################################################################
# File name: ntp_server.py
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
	'https://axapi.a10networks.com/axapi/v3/ntp/server',
]

def deserialize_Server__key_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key = data.get('key')
	prefer = data.get('prefer')
	action = data.get('action')
	result = Server__key_cfg(key=key, prefer=prefer, action=action)
	return result

def deserialize_Server_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	host = data.get('host')
	hostname = data.get('hostname')
	key_cfg = deserialize_Server__key_cfg_json(data.get('key-cfg'))
	result = Server(ipv6_addr=ipv6_addr, host=host, hostname=hostname, key_cfg=key_cfg)
	return result

def serialize_Server__key_cfg_json(obj):
	output = OrderedDict()
	if obj.key is not None:
		output['key'] = obj.key
	if obj.prefer is not None:
		output['prefer'] = obj.prefer
	if obj.action is not None:
		output['action'] = obj.action
	return output

def serialize_Server_json(obj):
	output = OrderedDict()
	output['ipv6-addr'] = obj.ipv6_addr
	output['host'] = obj.host
	output['hostname'] = obj.hostname
	if obj.key_cfg is not None:
		output['key-cfg'] = serialize_Server__key_cfg_json(obj.key_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Server_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Server_json(item))
	return list(container)

class Server_ipv6_addr_host_hostname(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	host = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	hostname=SizedString(1, 255)
	def __init__(self, ipv6_addr, host, hostname):
		self.ipv6_addr = ipv6_addr
		self.host = host
		self.hostname = hostname

	def __str__(self):
		return str(self.ipv6_addr) + '+' + str(self.host) + '+' + str(self.hostname)

class Server__key_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	key=PosRangedInteger(1, 65535)
	prefer=PosRangedInteger(0, 1)
	action = Enum(['enable', 'disable'])
	def __init__(self, key=None, prefer=None, action=None):
		self.key = key
		self.prefer = prefer
		self.action = action

	def __str__(self):
		return ""

class Server(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	host = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	hostname=SizedString(1, 255)
	def __init__(self, ipv6_addr, host, hostname, key_cfg=None):
		self.ipv6_addr = ipv6_addr
		self.host = host
		self.hostname = hostname
		self.key_cfg = key_cfg

	def __str__(self):
		return str(self.ipv6_addr) + '+' + str(self.host) + '+' + str(self.hostname)

class NtpServerClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getNtpServer(self, server_ipv6_addr_host_hostname):
		"""
		Retrieve the server identified by the specified identifier
		
		Args:
			server_ipv6_addr_host_hostname Server_ipv6_addr_host_hostname
		
		Returns:
			An instance of the Server class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(server_ipv6_addr_host_hostname) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified server does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('server')
		return deserialize_Server_json(payload)

	def putNtpServer(self, server_ipv6_addr_host_hostname, server):
		"""
		Replace the object server
		
		Args:
			server_ipv6_addr_host_hostname Server_ipv6_addr_host_hostname
			server An instance of the Server class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['server']=serialize_Server_json(server)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(server_ipv6_addr_host_hostname) .replace("/", "%2f") + query, payload, headers)
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

	def deleteNtpServer(self, server_ipv6_addr_host_hostname):
		"""
		Remove the server identified by the specified identifier from the system
		
		Args:
			server_ipv6_addr_host_hostname Server_ipv6_addr_host_hostname
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(server_ipv6_addr_host_hostname) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified server does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllNtpServersClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitNtpServer(self, server):
		"""
		Create the object server
		
		Args:
			server An instance of the Server class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['server']=serialize_Server_json(server)
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

	def getAllNtpServers(self):
		"""
		Retrieve all server objects currently pending in the system
		
		Returns:
			A list of Server objects
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
			payload= data.get('serverList')
		return deserialize_list_Server_json(payload)

