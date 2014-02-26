########################################################################################################################
# File name: sflow_collector_ipv6.py
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
	'https://axapi.a10networks.com/axapi/v3/sflow/collector/ipv6',
]

def deserialize_Ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	addr = data.get('addr')
	port = data.get('port')
	result = Ipv6(addr=addr, port=port)
	return result

def serialize_Ipv6_json(obj):
	output = OrderedDict()
	output['addr'] = obj.addr
	output['port'] = obj.port
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_json(item))
	return list(container)

class Ipv6_addr_port(AxapiObject):
	__metaclass__ = StructMeta 
	addr=SizedString(1, 255)
	port=PosRangedInteger(1, 65535)
	def __init__(self, addr, port):
		self.addr = addr
		self.port = port

	def __str__(self):
		return str(self.addr) + '+' + str(self.port)

class Ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	addr=SizedString(1, 255)
	port=PosRangedInteger(1, 65535)
	def __init__(self, addr, port):
		self.addr = addr
		self.port = port

	def __str__(self):
		return str(self.addr) + '+' + str(self.port)

class SflowCollectorIpv6Client(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSflowCollectorIpv6(self, ipv6_addr_port):
		"""
		Retrieve the ipv6 identified by the specified identifier
		
		Args:
			ipv6_addr_port Ipv6_addr_port
		
		Returns:
			An instance of the Ipv6 class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(ipv6_addr_port) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ipv6 does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ipv6')
		return deserialize_Ipv6_json(payload)

	def putSflowCollectorIpv6(self, ipv6_addr_port, ipv6):
		"""
		Replace the object ipv6
		
		Args:
			ipv6_addr_port Ipv6_addr_port
			ipv6 An instance of the Ipv6 class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ipv6']=serialize_Ipv6_json(ipv6)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(ipv6_addr_port) .replace("/", "%2f") + query, payload, headers)
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

	def deleteSflowCollectorIpv6(self, ipv6_addr_port):
		"""
		Remove the ipv6 identified by the specified identifier from the system
		
		Args:
			ipv6_addr_port Ipv6_addr_port
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(ipv6_addr_port) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ipv6 does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSflowCollectorIpv6sClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSflowCollectorIpv6(self, ipv6):
		"""
		Create the object ipv6
		
		Args:
			ipv6 An instance of the Ipv6 class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ipv6']=serialize_Ipv6_json(ipv6)
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

	def getAllSflowCollectorIpv6s(self):
		"""
		Retrieve all ipv6 objects currently pending in the system
		
		Returns:
			A list of Ipv6 objects
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
			payload= data.get('ipv6List')
		return deserialize_list_Ipv6_json(payload)

