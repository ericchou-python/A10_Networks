########################################################################################################################
# File name: tacacs_server_host.py
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
	'https://axapi.a10networks.com/axapi/v3/tacacs-server/host',
]

def deserialize_Host__secret__port_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	port = data.get('port')
	timeout = data.get('timeout')
	result = Host__secret__port_cfg(port=port, timeout=timeout)
	return result

def deserialize_Host__secret_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	secret_value = data.get('secret-value')
	encrypted = data.get('encrypted')
	port_cfg = deserialize_Host__secret__port_cfg_json(data.get('port-cfg'))
	result = Host__secret(secret_value=secret_value, encrypted=encrypted, port_cfg=port_cfg)
	return result

def deserialize_Host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4_addr = data.get('ipv4-addr')
	ipv6_addr = data.get('ipv6-addr')
	hostname = data.get('hostname')
	secret = deserialize_Host__secret_json(data.get('secret'))
	result = Host(ipv4_addr=ipv4_addr, ipv6_addr=ipv6_addr, hostname=hostname, secret=secret)
	return result

def serialize_Host__secret__port_cfg_json(obj):
	output = OrderedDict()
	if obj.port is not None:
		output['port'] = obj.port
	if obj.timeout is not None:
		output['timeout'] = obj.timeout
	return output

def serialize_Host__secret_json(obj):
	output = OrderedDict()
	output['secret-value'] = obj.secret_value
	output['encrypted'] = obj.encrypted
	if obj.port_cfg is not None:
		output['port-cfg'] = serialize_Host__secret__port_cfg_json(obj.port_cfg)
	return output

def serialize_Host_json(obj):
	output = OrderedDict()
	output['ipv4-addr'] = obj.ipv4_addr
	output['ipv6-addr'] = obj.ipv6_addr
	output['hostname'] = obj.hostname
	output['secret'] = serialize_Host__secret_json(obj.secret)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Host_json(item))
	return list(container)

class Host_ipv4_addr_ipv4_addr_ipv6_addr_hostname(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6_addr=SizedString(1, 255)
	hostname=SizedString(1, 63)
	def __init__(self, ipv4_addr, ipv6_addr, hostname):
		self.ipv4_addr = ipv4_addr
		self.ipv6_addr = ipv6_addr
		self.hostname = hostname

	def __str__(self):
		return str(self.ipv4_addr) + '+' + str(self.ipv6_addr) + '+' + str(self.hostname)

class Host__secret__port_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	port=PosRangedInteger(1, 65535)
	timeout=PosRangedInteger(1, 12)
	def __init__(self, port=None, timeout=None):
		self.port = port
		self.timeout = timeout

	def __str__(self):
		return ""

class Host__secret(AxapiObject):
	__metaclass__ = StructMeta 
	secret_value=SizedString(1, 127)
	encrypted=SizedString(1, 255)
	def __init__(self, secret_value, encrypted, port_cfg=None):
		self.secret_value = secret_value
		self.encrypted = encrypted
		self.port_cfg = port_cfg

	def __str__(self):
		return str(self.secret_value) + '+' + str(self.encrypted)

class Host(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6_addr=SizedString(1, 255)
	hostname=SizedString(1, 63)
	def __init__(self, ipv4_addr, ipv6_addr, hostname, secret):
		self.ipv4_addr = ipv4_addr
		self.ipv6_addr = ipv6_addr
		self.hostname = hostname
		self.secret = secret

	def __str__(self):
		return str(self.ipv4_addr) + '+' + str(self.ipv6_addr) + '+' + str(self.hostname) + '+' + str(self.secret)

class TacacsserverHostClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getTacacsserverHost(self, host_ipv4_addr_ipv4_addr_ipv6_addr_hostname):
		"""
		Retrieve the host identified by the specified identifier
		
		Args:
			host_ipv4_addr_ipv4_addr_ipv6_addr_hostname Host_ipv4_addr_ipv4_addr_ipv6_addr_hostname
		
		Returns:
			An instance of the Host class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(host_ipv4_addr_ipv4_addr_ipv6_addr_hostname) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified host does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('host')
		return deserialize_Host_json(payload)

	def putTacacsserverHost(self, host_ipv4_addr_ipv4_addr_ipv6_addr_hostname, host):
		"""
		Replace the object host
		
		Args:
			host_ipv4_addr_ipv4_addr_ipv6_addr_hostname Host_ipv4_addr_ipv4_addr_ipv6_addr_hostname
			host An instance of the Host class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['host']=serialize_Host_json(host)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(host_ipv4_addr_ipv4_addr_ipv6_addr_hostname) .replace("/", "%2f") + query, payload, headers)
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

	def deleteTacacsserverHost(self, host_ipv4_addr_ipv4_addr_ipv6_addr_hostname):
		"""
		Remove the host identified by the specified identifier from the system
		
		Args:
			host_ipv4_addr_ipv4_addr_ipv6_addr_hostname Host_ipv4_addr_ipv4_addr_ipv6_addr_hostname
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(host_ipv4_addr_ipv4_addr_ipv6_addr_hostname) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified host does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllTacacsserverHostsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitTacacsserverHost(self, host):
		"""
		Create the object host
		
		Args:
			host An instance of the Host class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['host']=serialize_Host_json(host)
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

	def getAllTacacsserverHosts(self):
		"""
		Retrieve all host objects currently pending in the system
		
		Returns:
			A list of Host objects
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
			payload= data.get('hostList')
		return deserialize_list_Host_json(payload)

