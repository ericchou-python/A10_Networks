########################################################################################################################
# File name: service_group.py
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
	'https://axapi.a10networks.com/axapi/v3/service-group',
]

def deserialize_Service_group_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	protocol = data.get('protocol')
	protocol_tcp_start = data.get('protocol-tcp-start')
	protocol_tcp_end = data.get('protocol-tcp-end')
	protocol_udp_start = data.get('protocol-udp-start')
	protocol_udp_end = data.get('protocol-udp-end')
	ip_protocol = data.get('ip-protocol')
	result = Service_group(name=name, protocol=protocol, protocol_tcp_start=protocol_tcp_start, protocol_tcp_end=protocol_tcp_end, protocol_udp_start=protocol_udp_start, protocol_udp_end=protocol_udp_end, ip_protocol=ip_protocol)
	return result

def serialize_Service_group_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.protocol is not None:
		output['protocol'] = obj.protocol
	if obj.protocol_tcp_start is not None:
		output['protocol-tcp-start'] = obj.protocol_tcp_start
	if obj.protocol_tcp_end is not None:
		output['protocol-tcp-end'] = obj.protocol_tcp_end
	if obj.protocol_udp_start is not None:
		output['protocol-udp-start'] = obj.protocol_udp_start
	if obj.protocol_udp_end is not None:
		output['protocol-udp-end'] = obj.protocol_udp_end
	if obj.ip_protocol is not None:
		output['ip-protocol'] = obj.ip_protocol
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Service_group_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Service_group_json(item))
	return list(container)

class Service_group_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class Service_group(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	protocol=PosRangedInteger(0, 1)
	protocol_tcp_start=PosRangedInteger(1, 65534)
	protocol_tcp_end=PosRangedInteger(1, 65534)
	protocol_udp_start=PosRangedInteger(1, 65534)
	protocol_udp_end=PosRangedInteger(1, 65534)
	ip_protocol=PosRangedInteger(1, 255)
	def __init__(self, name, protocol=None, protocol_tcp_start=None, protocol_tcp_end=None, protocol_udp_start=None, protocol_udp_end=None, ip_protocol=None):
		self.name = name
		self.protocol = protocol
		self.protocol_tcp_start = protocol_tcp_start
		self.protocol_tcp_end = protocol_tcp_end
		self.protocol_udp_start = protocol_udp_start
		self.protocol_udp_end = protocol_udp_end
		self.ip_protocol = ip_protocol

	def __str__(self):
		return str(self.name)

class ServicegroupClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getServicegroup(self, service_group_name):
		"""
		Retrieve the service_group identified by the specified identifier
		
		Args:
			service_group_name Service_group_name
		
		Returns:
			An instance of the Service_group class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(service_group_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified service_group does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('service-group')
		return deserialize_Service_group_json(payload)

	def putServicegroup(self, service_group_name, service_group):
		"""
		Replace the object service_group
		
		Args:
			service_group_name Service_group_name
			service_group An instance of the Service_group class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['service-group']=serialize_Service_group_json(service_group)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(service_group_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteServicegroup(self, service_group_name):
		"""
		Remove the service_group identified by the specified identifier from the
		system
		
		Args:
			service_group_name Service_group_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(service_group_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified service_group does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllServicegroupsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitServicegroup(self, service_group):
		"""
		Create the object service_group
		
		Args:
			service_group An instance of the Service_group class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['service-group']=serialize_Service_group_json(service_group)
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

	def getAllServicegroups(self):
		"""
		Retrieve all service_group objects currently pending in the system
		
		Returns:
			A list of Service_group objects
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
			payload= data.get('service-groupList')
		return deserialize_list_Service_group_json(payload)

