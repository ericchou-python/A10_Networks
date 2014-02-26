########################################################################################################################
# File name: ntp.py
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
	'https://axapi.a10networks.com/axapi/v3/ntp',
]

def deserialize_Ntp_auth_key__key_cfg__type_cfg__hex_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	hex_key_string = data.get('hex-key-string')
	hex_encrypted = data.get('hex-encrypted')
	result = Ntp_auth_key__key_cfg__type_cfg__hex(hex_key_string=hex_key_string, hex_encrypted=hex_encrypted)
	return result

def deserialize_Ntp_auth_key__key_cfg__type_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type = data.get('type')
	hex = deserialize_Ntp_auth_key__key_cfg__type_cfg__hex_json(data.get('hex'))
	key_string = data.get('key-string')
	encrypted = data.get('encrypted')
	result = Ntp_auth_key__key_cfg__type_cfg(type=type, hex=hex, key_string=key_string, encrypted=encrypted)
	return result

def deserialize_Ntp_auth_key__key_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key = data.get('key')
	type_cfg = deserialize_Ntp_auth_key__key_cfg__type_cfg_json(data.get('type-cfg'))
	result = Ntp_auth_key__key_cfg(key=key, type_cfg=type_cfg)
	return result

def deserialize_Ntp_auth_key_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key_cfg = deserialize_Ntp_auth_key__key_cfg_json(data.get('key-cfg'))
	result = Ntp_auth_key(key_cfg=key_cfg)
	return result

def deserialize_list_Ntp_auth_key_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ntp_auth_key_json(item))
	return list(container)

def deserialize_Ntp_trusted_key_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key = data.get('key')
	result = Ntp_trusted_key(key=key)
	return result

def deserialize_list_Ntp_trusted_key_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ntp_trusted_key_json(item))
	return list(container)

def deserialize_Ntp_server__key_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key = data.get('key')
	prefer = data.get('prefer')
	action = data.get('action')
	result = Ntp_server__key_cfg(key=key, prefer=prefer, action=action)
	return result

def deserialize_Ntp_server_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	host = data.get('host')
	hostname = data.get('hostname')
	key_cfg = deserialize_Ntp_server__key_cfg_json(data.get('key-cfg'))
	result = Ntp_server(ipv6_addr=ipv6_addr, host=host, hostname=hostname, key_cfg=key_cfg)
	return result

def deserialize_list_Ntp_server_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ntp_server_json(item))
	return list(container)

def deserialize_Ntp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	auth_keylist = deserialize_list_Ntp_auth_key_json(data.get('auth-keyList'))
	trusted_keylist = deserialize_list_Ntp_trusted_key_json(data.get('trusted-keyList'))
	serverlist = deserialize_list_Ntp_server_json(data.get('serverList'))
	result = Ntp(auth_keylist=auth_keylist, trusted_keylist=trusted_keylist, serverlist=serverlist)
	return result

class Ntp(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, auth_keylist=None, trusted_keylist=None, serverlist=None):
		self.auth_keylist = auth_keylist
		self.trusted_keylist = trusted_keylist
		self.serverlist = serverlist

	def __str__(self):
		return ""

class Ntp_auth_key__key_cfg__type_cfg__hex(AxapiObject):
	__metaclass__ = StructMeta 
	hex_key_string=SizedString(21, 40)
	hex_encrypted=SizedString(1, 255)
	def __init__(self, hex_key_string, hex_encrypted):
		self.hex_key_string = hex_key_string
		self.hex_encrypted = hex_encrypted

	def __str__(self):
		return str(self.hex_key_string) + '+' + str(self.hex_encrypted)

class Ntp_auth_key__key_cfg__type_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	type = Enum([])
	key_string=SizedString(1, 20)
	encrypted=SizedString(1, 255)
	def __init__(self, type, hex, key_string, encrypted):
		self.type = type
		self.hex = hex
		self.key_string = key_string
		self.encrypted = encrypted

	def __str__(self):
		return str(self.type) + '+' + str(self.hex) + '+' + str(self.key_string) + '+' + str(self.encrypted)

class Ntp_auth_key__key_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	key=PosRangedInteger(1, 65535)
	def __init__(self, key, type_cfg=None):
		self.key = key
		self.type_cfg = type_cfg

	def __str__(self):
		return str(self.key)

class Ntp_auth_key(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, key_cfg):
		self.key_cfg = key_cfg

	def __str__(self):
		return str(self.key_cfg)

class Ntp_trusted_key(AxapiObject):
	__metaclass__ = StructMeta 
	key=PosRangedInteger(1, 65535)
	def __init__(self, key):
		self.key = key

	def __str__(self):
		return str(self.key)

class Ntp_server__key_cfg(AxapiObject):
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

class Ntp_server(AxapiObject):
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

class NtpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getNtp(self):
		"""
		Retrieve the ntp identified by the specified identifier
		
		Returns:
			An instance of the Ntp class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ntp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ntp')
		return deserialize_Ntp_json(payload)

