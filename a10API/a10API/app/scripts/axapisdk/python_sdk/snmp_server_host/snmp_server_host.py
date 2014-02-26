########################################################################################################################
# File name: snmp_server_host.py
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
	'https://axapi.a10networks.com/axapi/v3/snmp-server/host',
]

def deserialize_Host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	hostname = data.get('hostname')
	ipv6_host = data.get('ipv6-host')
	version = data.get('version')
	comm = data.get('comm')
	udp_port = data.get('udp-port')
	result = Host(hostname=hostname, ipv6_host=ipv6_host, version=version, comm=comm, udp_port=udp_port)
	return result

def serialize_Host_json(obj):
	output = OrderedDict()
	output['hostname'] = obj.hostname
	output['ipv6-host'] = obj.ipv6_host
	if obj.version is not None:
		output['version'] = obj.version
	if obj.comm is not None:
		output['comm'] = obj.comm
	if obj.udp_port is not None:
		output['udp-port'] = obj.udp_port
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

class Host_hostname_hostname_ipv6_host(AxapiObject):
	__metaclass__ = StructMeta 
	hostname=SizedString(1, 31)
	ipv6_host=SizedString(1, 255)
	def __init__(self, hostname, ipv6_host):
		self.hostname = hostname
		self.ipv6_host = ipv6_host

	def __str__(self):
		return str(self.hostname) + '+' + str(self.ipv6_host)

class Host(AxapiObject):
	__metaclass__ = StructMeta 
	hostname=SizedString(1, 31)
	ipv6_host=SizedString(1, 255)
	version = Enum(['v1', 'v2c'])
	comm=SizedString(1, 31)
	udp_port=PosRangedInteger(1, 65535)
	def __init__(self, hostname, ipv6_host, version=None, comm=None, udp_port=None):
		self.hostname = hostname
		self.ipv6_host = ipv6_host
		self.version = version
		self.comm = comm
		self.udp_port = udp_port

	def __str__(self):
		return str(self.hostname) + '+' + str(self.ipv6_host)

class SnmpserverHostClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSnmpserverHost(self, host_hostname_hostname_ipv6_host):
		"""
		Retrieve the host identified by the specified identifier
		
		Args:
			host_hostname_hostname_ipv6_host Host_hostname_hostname_ipv6_host
		
		Returns:
			An instance of the Host class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(host_hostname_hostname_ipv6_host) .replace("/", "%2f") + query, headers=headers)
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

	def putSnmpserverHost(self, host_hostname_hostname_ipv6_host, host):
		"""
		Replace the object host
		
		Args:
			host_hostname_hostname_ipv6_host Host_hostname_hostname_ipv6_host
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
		conn.request('PUT', self.get_path() + '/' + str(host_hostname_hostname_ipv6_host) .replace("/", "%2f") + query, payload, headers)
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

	def deleteSnmpserverHost(self, host_hostname_hostname_ipv6_host):
		"""
		Remove the host identified by the specified identifier from the system
		
		Args:
			host_hostname_hostname_ipv6_host Host_hostname_hostname_ipv6_host
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(host_hostname_hostname_ipv6_host) .replace("/", "%2f") + query, headers=headers)
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

class AllSnmpserverHostsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSnmpserverHost(self, host):
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

	def getAllSnmpserverHosts(self):
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

