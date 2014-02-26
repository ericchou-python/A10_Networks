########################################################################################################################
# File name: ldap_server.py
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
	'https://axapi.a10networks.com/axapi/v3/ldap-server',
]

def deserialize_Ldap_server_host__host_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	hostname = data.get('hostname')
	ipv6 = data.get('ipv6')
	result = Ldap_server_host__host_cfg(hostname=hostname, ipv6=ipv6)
	return result

def deserialize_Ldap_server_host__cn_cfg__port_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	port = data.get('port')
	ssl = data.get('ssl')
	timeout = data.get('timeout')
	result = Ldap_server_host__cn_cfg__port_cfg(port=port, ssl=ssl, timeout=timeout)
	return result

def deserialize_Ldap_server_host__cn_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	cn = data.get('cn')
	dn = data.get('dn')
	port_cfg = deserialize_Ldap_server_host__cn_cfg__port_cfg_json(data.get('port-cfg'))
	result = Ldap_server_host__cn_cfg(cn=cn, dn=dn, port_cfg=port_cfg)
	return result

def deserialize_Ldap_server_host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	host_cfg = deserialize_Ldap_server_host__host_cfg_json(data.get('host-cfg'))
	cn_cfg = deserialize_Ldap_server_host__cn_cfg_json(data.get('cn-cfg'))
	result = Ldap_server_host(host_cfg=host_cfg, cn_cfg=cn_cfg)
	return result

def deserialize_list_Ldap_server_host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ldap_server_host_json(item))
	return list(container)

def deserialize_Ldap_server_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	hostlist = deserialize_list_Ldap_server_host_json(data.get('hostList'))
	result = Ldap_server(hostlist=hostlist)
	return result

class Ldap_server(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, hostlist=None):
		self.hostlist = hostlist

	def __str__(self):
		return ""

class Ldap_server_host__host_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	hostname=SizedString(1, 31)
	ipv6=SizedString(1, 255)
	def __init__(self, hostname, ipv6):
		self.hostname = hostname
		self.ipv6 = ipv6

	def __str__(self):
		return str(self.hostname) + '+' + str(self.ipv6)

class Ldap_server_host__cn_cfg__port_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	port=PosRangedInteger(1, 65535)
	ssl=PosRangedInteger(0, 1)
	timeout=PosRangedInteger(1, 60)
	def __init__(self, port=None, ssl=None, timeout=None):
		self.port = port
		self.ssl = ssl
		self.timeout = timeout

	def __str__(self):
		return ""

class Ldap_server_host__cn_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	cn=SizedString(1, 31)
	dn=SizedString(1, 63)
	def __init__(self, cn, dn, port_cfg=None):
		self.cn = cn
		self.dn = dn
		self.port_cfg = port_cfg

	def __str__(self):
		return str(self.cn) + '+' + str(self.dn)

class Ldap_server_host(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, host_cfg, cn_cfg=None):
		self.host_cfg = host_cfg
		self.cn_cfg = cn_cfg

	def __str__(self):
		return str(self.host_cfg)

class LdapserverClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLdapserver(self):
		"""
		Retrieve the ldap_server identified by the specified identifier
		
		Returns:
			An instance of the Ldap_server class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ldap_server does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ldap-server')
		return deserialize_Ldap_server_json(payload)

