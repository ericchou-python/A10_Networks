########################################################################################################################
# File name: ip_tcp.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/tcp',
]

def deserialize_Tcp__syn_cookie_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	threshold = data.get('threshold')
	result = Tcp__syn_cookie(threshold=threshold)
	return result

def deserialize_Tcp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	syn_cookie = deserialize_Tcp__syn_cookie_json(data.get('syn-cookie'))
	result = Tcp(syn_cookie=syn_cookie)
	return result

def serialize_Tcp__syn_cookie_json(obj):
	output = OrderedDict()
	if obj.threshold is not None:
		output['threshold'] = obj.threshold
	return output

def serialize_Tcp_json(obj):
	output = OrderedDict()
	if obj.syn_cookie is not None:
		output['syn-cookie'] = serialize_Tcp__syn_cookie_json(obj.syn_cookie)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Tcp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Tcp_json(item))
	return list(container)

class Tcp__syn_cookie(AxapiObject):
	__metaclass__ = StructMeta 
	threshold=PosRangedInteger(1, 100)
	def __init__(self, threshold=None):
		self.threshold = threshold

	def __str__(self):
		return ""

class Tcp(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, syn_cookie=None):
		self.syn_cookie = syn_cookie

	def __str__(self):
		return ""

class IpTcpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpTcp(self):
		"""
		Retrieve the tcp identified by the specified identifier
		
		Returns:
			An instance of the Tcp class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified tcp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('tcp')
		return deserialize_Tcp_json(payload)

	def putIpTcp(self, tcp):
		"""
		Replace the object tcp
		
		Args:
			tcp An instance of the Tcp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['tcp']=serialize_Tcp_json(tcp)
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

	def deleteIpTcp(self):
		"""
		Remove the tcp identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified tcp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpTcpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpTcp(self, tcp):
		"""
		Create the object tcp
		
		Args:
			tcp An instance of the Tcp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['tcp']=serialize_Tcp_json(tcp)
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

	def getAllIpTcps(self):
		"""
		Retrieve all tcp objects currently pending in the system
		
		Returns:
			A list of Tcp objects
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
			payload= data.get('tcpList')
		return deserialize_list_Tcp_json(payload)

