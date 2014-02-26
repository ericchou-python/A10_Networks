########################################################################################################################
# File name: logging_host.py
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
	'https://axapi.a10networks.com/axapi/v3/logging/host',
]

def deserialize_Host__host_ipv4_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	host_ipv4 = data.get('host-ipv4')
	host_ipv6 = data.get('host-ipv6')
	port = data.get('port')
	tcp = data.get('tcp')
	udp = data.get('udp')
	use_mgmt_port = data.get('use-mgmt-port')
	use_data_port = data.get('use-data-port')
	result = Host__host_ipv4(host_ipv4=host_ipv4, host_ipv6=host_ipv6, port=port, tcp=tcp, udp=udp, use_mgmt_port=use_mgmt_port, use_data_port=use_data_port)
	return result

def deserialize_Host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	host_ipv4 = deserialize_Host__host_ipv4_json(data.get('host-ipv4'))
	result = Host(host_ipv4=host_ipv4)
	return result

def serialize_Host__host_ipv4_json(obj):
	output = OrderedDict()
	output['host-ipv4'] = obj.host_ipv4
	output['host-ipv6'] = obj.host_ipv6
	output['port'] = obj.port
	output['tcp'] = obj.tcp
	output['udp'] = obj.udp
	output['use-mgmt-port'] = obj.use_mgmt_port
	output['use-data-port'] = obj.use_data_port
	return output

def serialize_Host_json(obj):
	output = OrderedDict()
	output['host-ipv4'] = serialize_Host__host_ipv4_json(obj.host_ipv4)
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

class Host_host_ipv4_host_ipv4_host_ipv6__host_ipv4(AxapiObject):
	__metaclass__ = StructMeta 
	host_ipv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	host_ipv6=SizedString(1, 255)
	port=PosRangedInteger(1, 32767)
	tcp=PosRangedInteger(0, 1)
	udp=PosRangedInteger(0, 1)
	use_mgmt_port=PosRangedInteger(0, 1)
	use_data_port=PosRangedInteger(0, 1)
	def __init__(self, host_ipv4, host_ipv6, port, tcp, udp, use_mgmt_port, use_data_port):
		self.host_ipv4 = host_ipv4
		self.host_ipv6 = host_ipv6
		self.port = port
		self.tcp = tcp
		self.udp = udp
		self.use_mgmt_port = use_mgmt_port
		self.use_data_port = use_data_port

	def __str__(self):
		return str(self.host_ipv4) + '+' + str(self.host_ipv6) + '+' + str(self.port) + '+' + str(self.tcp) + '+' + str(self.udp) + '+' + str(self.use_mgmt_port) + '+' + str(self.use_data_port)

class Host_host_ipv4_host_ipv4_host_ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, host_ipv4):
		self.host_ipv4 = host_ipv4

	def __str__(self):
		return str(self.host_ipv4)

class Host__host_ipv4(AxapiObject):
	__metaclass__ = StructMeta 
	host_ipv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	host_ipv6=SizedString(1, 255)
	port=PosRangedInteger(1, 32767)
	tcp=PosRangedInteger(0, 1)
	udp=PosRangedInteger(0, 1)
	use_mgmt_port=PosRangedInteger(0, 1)
	use_data_port=PosRangedInteger(0, 1)
	def __init__(self, host_ipv4, host_ipv6, port, tcp, udp, use_mgmt_port, use_data_port):
		self.host_ipv4 = host_ipv4
		self.host_ipv6 = host_ipv6
		self.port = port
		self.tcp = tcp
		self.udp = udp
		self.use_mgmt_port = use_mgmt_port
		self.use_data_port = use_data_port

	def __str__(self):
		return str(self.host_ipv4) + '+' + str(self.host_ipv6) + '+' + str(self.port) + '+' + str(self.tcp) + '+' + str(self.udp) + '+' + str(self.use_mgmt_port) + '+' + str(self.use_data_port)

class Host(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, host_ipv4):
		self.host_ipv4 = host_ipv4

	def __str__(self):
		return str(self.host_ipv4)

class LoggingHostClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLoggingHost(self, host_host_ipv4_host_ipv4_host_ipv6):
		"""
		Retrieve the host identified by the specified identifier
		
		Args:
			host_host_ipv4_host_ipv4_host_ipv6 Host_host_ipv4_host_ipv4_host_ipv6
		
		Returns:
			An instance of the Host class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(host_host_ipv4_host_ipv4_host_ipv6) .replace("/", "%2f") + query, headers=headers)
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

	def putLoggingHost(self, host_host_ipv4_host_ipv4_host_ipv6, host):
		"""
		Replace the object host
		
		Args:
			host_host_ipv4_host_ipv4_host_ipv6 Host_host_ipv4_host_ipv4_host_ipv6
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
		conn.request('PUT', self.get_path() + '/' + str(host_host_ipv4_host_ipv4_host_ipv6) .replace("/", "%2f") + query, payload, headers)
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

	def deleteLoggingHost(self, host_host_ipv4_host_ipv4_host_ipv6):
		"""
		Remove the host identified by the specified identifier from the system
		
		Args:
			host_host_ipv4_host_ipv4_host_ipv6 Host_host_ipv4_host_ipv4_host_ipv6
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(host_host_ipv4_host_ipv4_host_ipv6) .replace("/", "%2f") + query, headers=headers)
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

class AllLoggingHostsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitLoggingHost(self, host):
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

	def getAllLoggingHosts(self):
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

