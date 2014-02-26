########################################################################################################################
# File name: ldap_server_host.py
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
	'https://axapi.a10networks.com/axapi/v3/ldap-server/host',
]

def deserialize_Host__host_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	hostname = data.get('hostname')
	ipv6 = data.get('ipv6')
	result = Host__host_cfg(hostname=hostname, ipv6=ipv6)
	return result

def deserialize_Host__cn_cfg__port_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	port = data.get('port')
	ssl = data.get('ssl')
	timeout = data.get('timeout')
	result = Host__cn_cfg__port_cfg(port=port, ssl=ssl, timeout=timeout)
	return result

def deserialize_Host__cn_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	cn = data.get('cn')
	dn = data.get('dn')
	port_cfg = deserialize_Host__cn_cfg__port_cfg_json(data.get('port-cfg'))
	result = Host__cn_cfg(cn=cn, dn=dn, port_cfg=port_cfg)
	return result

def deserialize_Host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	host_cfg = deserialize_Host__host_cfg_json(data.get('host-cfg'))
	cn_cfg = deserialize_Host__cn_cfg_json(data.get('cn-cfg'))
	result = Host(host_cfg=host_cfg, cn_cfg=cn_cfg)
	return result

def serialize_Host__host_cfg_json(obj):
	output = OrderedDict()
	output['hostname'] = obj.hostname
	output['ipv6'] = obj.ipv6
	return output

def serialize_Host__cn_cfg__port_cfg_json(obj):
	output = OrderedDict()
	if obj.port is not None:
		output['port'] = obj.port
	if obj.ssl is not None:
		output['ssl'] = obj.ssl
	if obj.timeout is not None:
		output['timeout'] = obj.timeout
	return output

def serialize_Host__cn_cfg_json(obj):
	output = OrderedDict()
	output['cn'] = obj.cn
	output['dn'] = obj.dn
	if obj.port_cfg is not None:
		output['port-cfg'] = serialize_Host__cn_cfg__port_cfg_json(obj.port_cfg)
	return output

def serialize_Host_json(obj):
	output = OrderedDict()
	output['host-cfg'] = serialize_Host__host_cfg_json(obj.host_cfg)
	if obj.cn_cfg is not None:
		output['cn-cfg'] = serialize_Host__cn_cfg_json(obj.cn_cfg)
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

class Host_host_cfg_hostname_ipv6__host_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	hostname=SizedString(1, 31)
	ipv6=SizedString(1, 255)
	def __init__(self, hostname, ipv6):
		self.hostname = hostname
		self.ipv6 = ipv6

	def __str__(self):
		return str(self.hostname) + '+' + str(self.ipv6)

class Host_host_cfg_hostname_ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, host_cfg):
		self.host_cfg = host_cfg

	def __str__(self):
		return str(self.host_cfg)

class Host__host_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	hostname=SizedString(1, 31)
	ipv6=SizedString(1, 255)
	def __init__(self, hostname, ipv6):
		self.hostname = hostname
		self.ipv6 = ipv6

	def __str__(self):
		return str(self.hostname) + '+' + str(self.ipv6)

class Host__cn_cfg__port_cfg(AxapiObject):
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

class Host__cn_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	cn=SizedString(1, 31)
	dn=SizedString(1, 63)
	def __init__(self, cn, dn, port_cfg=None):
		self.cn = cn
		self.dn = dn
		self.port_cfg = port_cfg

	def __str__(self):
		return str(self.cn) + '+' + str(self.dn)

class Host(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, host_cfg, cn_cfg=None):
		self.host_cfg = host_cfg
		self.cn_cfg = cn_cfg

	def __str__(self):
		return str(self.host_cfg)

class LdapserverHostClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLdapserverHost(self, host_host_cfg_hostname_ipv6):
		"""
		Retrieve the host identified by the specified identifier
		
		Args:
			host_host_cfg_hostname_ipv6 Host_host_cfg_hostname_ipv6
		
		Returns:
			An instance of the Host class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(host_host_cfg_hostname_ipv6) .replace("/", "%2f") + query, headers=headers)
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

	def putLdapserverHost(self, host_host_cfg_hostname_ipv6, host):
		"""
		Replace the object host
		
		Args:
			host_host_cfg_hostname_ipv6 Host_host_cfg_hostname_ipv6
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
		conn.request('PUT', self.get_path() + '/' + str(host_host_cfg_hostname_ipv6) .replace("/", "%2f") + query, payload, headers)
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

	def deleteLdapserverHost(self, host_host_cfg_hostname_ipv6):
		"""
		Remove the host identified by the specified identifier from the system
		
		Args:
			host_host_cfg_hostname_ipv6 Host_host_cfg_hostname_ipv6
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(host_host_cfg_hostname_ipv6) .replace("/", "%2f") + query, headers=headers)
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

class AllLdapserverHostsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitLdapserverHost(self, host):
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

	def getAllLdapserverHosts(self):
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

