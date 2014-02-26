########################################################################################################################
# File name: tacacs_server.py
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
	'https://axapi.a10networks.com/axapi/v3/tacacs-server',
]

def deserialize_Tacacs_server_host__secret__port_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	port = data.get('port')
	timeout = data.get('timeout')
	result = Tacacs_server_host__secret__port_cfg(port=port, timeout=timeout)
	return result

def deserialize_Tacacs_server_host__secret_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	secret_value = data.get('secret-value')
	encrypted = data.get('encrypted')
	port_cfg = deserialize_Tacacs_server_host__secret__port_cfg_json(data.get('port-cfg'))
	result = Tacacs_server_host__secret(secret_value=secret_value, encrypted=encrypted, port_cfg=port_cfg)
	return result

def deserialize_Tacacs_server_host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4_addr = data.get('ipv4-addr')
	ipv6_addr = data.get('ipv6-addr')
	hostname = data.get('hostname')
	secret = deserialize_Tacacs_server_host__secret_json(data.get('secret'))
	result = Tacacs_server_host(ipv4_addr=ipv4_addr, ipv6_addr=ipv6_addr, hostname=hostname, secret=secret)
	return result

def deserialize_list_Tacacs_server_host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Tacacs_server_host_json(item))
	return list(container)

def deserialize_Tacacs_server_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	hostlist = deserialize_list_Tacacs_server_host_json(data.get('hostList'))
	result = Tacacs_server(hostlist=hostlist)
	return result

class Tacacs_server(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, hostlist=None):
		self.hostlist = hostlist

	def __str__(self):
		return ""

class Tacacs_server_host__secret__port_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	port=PosRangedInteger(1, 65535)
	timeout=PosRangedInteger(1, 12)
	def __init__(self, port=None, timeout=None):
		self.port = port
		self.timeout = timeout

	def __str__(self):
		return ""

class Tacacs_server_host__secret(AxapiObject):
	__metaclass__ = StructMeta 
	secret_value=SizedString(1, 127)
	encrypted=SizedString(1, 255)
	def __init__(self, secret_value, encrypted, port_cfg=None):
		self.secret_value = secret_value
		self.encrypted = encrypted
		self.port_cfg = port_cfg

	def __str__(self):
		return str(self.secret_value) + '+' + str(self.encrypted)

class Tacacs_server_host(AxapiObject):
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

class TacacsserverClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getTacacsserver(self):
		"""
		Retrieve the tacacs_server identified by the specified identifier
		
		Returns:
			An instance of the Tacacs_server class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified tacacs_server does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('tacacs-server')
		return deserialize_Tacacs_server_json(payload)

