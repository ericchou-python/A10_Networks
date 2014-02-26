########################################################################################################################
# File name: radius_server.py
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
	'https://axapi.a10networks.com/axapi/v3/radius-server',
]

def deserialize_Radius_server_host__secret__port_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	auth_port = data.get('auth-port')
	acct_port = data.get('acct-port')
	retransmit = data.get('retransmit')
	timeout = data.get('timeout')
	result = Radius_server_host__secret__port_cfg(auth_port=auth_port, acct_port=acct_port, retransmit=retransmit, timeout=timeout)
	return result

def deserialize_Radius_server_host__secret_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	secret_value = data.get('secret-value')
	encrypted = data.get('encrypted')
	port_cfg = deserialize_Radius_server_host__secret__port_cfg_json(data.get('port-cfg'))
	result = Radius_server_host__secret(secret_value=secret_value, encrypted=encrypted, port_cfg=port_cfg)
	return result

def deserialize_Radius_server_host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4 = data.get('ipv4')
	ipv6 = data.get('ipv6')
	hostname = data.get('hostname')
	secret = deserialize_Radius_server_host__secret_json(data.get('secret'))
	result = Radius_server_host(ipv4=ipv4, ipv6=ipv6, hostname=hostname, secret=secret)
	return result

def deserialize_list_Radius_server_host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Radius_server_host_json(item))
	return list(container)

def deserialize_Radius_server_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default_privilege_read_write = data.get('default-privilege-read-write')
	hostlist = deserialize_list_Radius_server_host_json(data.get('hostList'))
	result = Radius_server(default_privilege_read_write=default_privilege_read_write, hostlist=hostlist)
	return result

def serialize_Radius_server_host__secret__port_cfg_json(obj):
	output = OrderedDict()
	if obj.auth_port is not None:
		output['auth-port'] = obj.auth_port
	if obj.acct_port is not None:
		output['acct-port'] = obj.acct_port
	if obj.retransmit is not None:
		output['retransmit'] = obj.retransmit
	if obj.timeout is not None:
		output['timeout'] = obj.timeout
	return output

def serialize_Radius_server_host__secret_json(obj):
	output = OrderedDict()
	output['secret-value'] = obj.secret_value
	output['encrypted'] = obj.encrypted
	if obj.port_cfg is not None:
		output['port-cfg'] = serialize_Radius_server_host__secret__port_cfg_json(obj.port_cfg)
	return output

def serialize_Radius_server_host_json(obj):
	output = OrderedDict()
	output['ipv4'] = obj.ipv4
	output['ipv6'] = obj.ipv6
	output['hostname'] = obj.hostname
	output['secret'] = serialize_Radius_server_host__secret_json(obj.secret)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Radius_server_host_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Radius_server_host_json(item))
	return output

def serialize_Radius_server_json(obj):
	output = OrderedDict()
	if obj.default_privilege_read_write is not None:
		output['default-privilege-read-write'] = obj.default_privilege_read_write
	if obj.hostlist is not None:
		output['hostList'] = serialize_list_Radius_server_host_json(obj.hostlist)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Radius_server_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Radius_server_json(item))
	return list(container)

class Radius_server(AxapiObject):
	__metaclass__ = StructMeta 
	default_privilege_read_write=PosRangedInteger(0, 1)
	def __init__(self, default_privilege_read_write=None, hostlist=None):
		self.default_privilege_read_write = default_privilege_read_write
		self.hostlist = hostlist

	def __str__(self):
		return ""

class Radius_server_host__secret__port_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	auth_port=PosRangedInteger(1, 65535)
	acct_port=PosRangedInteger(1, 65535)
	retransmit=PosRangedInteger(0, 5)
	timeout=PosRangedInteger(1, 15)
	def __init__(self, auth_port=None, acct_port=None, retransmit=None, timeout=None):
		self.auth_port = auth_port
		self.acct_port = acct_port
		self.retransmit = retransmit
		self.timeout = timeout

	def __str__(self):
		return ""

class Radius_server_host__secret(AxapiObject):
	__metaclass__ = StructMeta 
	secret_value=SizedString(1, 128)
	encrypted=SizedString(1, 255)
	def __init__(self, secret_value, encrypted, port_cfg=None):
		self.secret_value = secret_value
		self.encrypted = encrypted
		self.port_cfg = port_cfg

	def __str__(self):
		return str(self.secret_value) + '+' + str(self.encrypted)

class Radius_server_host(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6=SizedString(1, 255)
	hostname=SizedString(1, 31)
	def __init__(self, ipv4, ipv6, hostname, secret):
		self.ipv4 = ipv4
		self.ipv6 = ipv6
		self.hostname = hostname
		self.secret = secret

	def __str__(self):
		return str(self.ipv4) + '+' + str(self.ipv6) + '+' + str(self.hostname) + '+' + str(self.secret)

class RadiusserverClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRadiusserver(self):
		"""
		Retrieve the radius_server identified by the specified identifier
		
		Returns:
			An instance of the Radius_server class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified radius_server does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('radius-server')
		return deserialize_Radius_server_json(payload)

	def putRadiusserver(self, radius_server):
		"""
		Replace the object radius_server
		
		Args:
			radius_server An instance of the Radius_server class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['radius-server']=serialize_Radius_server_json(radius_server)
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

	def deleteRadiusserver(self):
		"""
		Remove the radius_server identified by the specified identifier from the
		system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified radius_server does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllRadiusserversClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitRadiusserver(self, radius_server):
		"""
		Create the object radius_server
		
		Args:
			radius_server An instance of the Radius_server class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['radius-server']=serialize_Radius_server_json(radius_server)
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

	def getAllRadiusservers(self):
		"""
		Retrieve all radius_server objects currently pending in the system
		
		Returns:
			A list of Radius_server objects
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
			payload= data.get('radius-serverList')
		return deserialize_list_Radius_server_json(payload)

