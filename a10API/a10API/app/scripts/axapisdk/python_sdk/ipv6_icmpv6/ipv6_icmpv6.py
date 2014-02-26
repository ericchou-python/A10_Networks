########################################################################################################################
# File name: ipv6_icmpv6.py
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
	'https://axapi.a10networks.com/axapi/v3/ipv6/icmpv6',
]

def deserialize_Icmpv6__disable_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	redirect = data.get('redirect')
	unreachable = data.get('unreachable')
	result = Icmpv6__disable(redirect=redirect, unreachable=unreachable)
	return result

def deserialize_Icmpv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	disable = deserialize_Icmpv6__disable_json(data.get('disable'))
	result = Icmpv6(disable=disable)
	return result

def serialize_Icmpv6__disable_json(obj):
	output = OrderedDict()
	if obj.redirect is not None:
		output['redirect'] = obj.redirect
	if obj.unreachable is not None:
		output['unreachable'] = obj.unreachable
	return output

def serialize_Icmpv6_json(obj):
	output = OrderedDict()
	if obj.disable is not None:
		output['disable'] = serialize_Icmpv6__disable_json(obj.disable)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Icmpv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Icmpv6_json(item))
	return list(container)

class Icmpv6__disable(AxapiObject):
	__metaclass__ = StructMeta 
	redirect=PosRangedInteger(0, 1)
	unreachable=PosRangedInteger(0, 1)
	def __init__(self, redirect=None, unreachable=None):
		self.redirect = redirect
		self.unreachable = unreachable

	def __str__(self):
		return ""

class Icmpv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, disable=None):
		self.disable = disable

	def __str__(self):
		return ""

class Ipv6Icmpv6Client(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpv6Icmpv6(self):
		"""
		Retrieve the icmpv6 identified by the specified identifier
		
		Returns:
			An instance of the Icmpv6 class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified icmpv6 does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('icmpv6')
		return deserialize_Icmpv6_json(payload)

	def putIpv6Icmpv6(self, icmpv6):
		"""
		Replace the object icmpv6
		
		Args:
			icmpv6 An instance of the Icmpv6 class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['icmpv6']=serialize_Icmpv6_json(icmpv6)
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

	def deleteIpv6Icmpv6(self):
		"""
		Remove the icmpv6 identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified icmpv6 does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpv6Icmpv6sClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpv6Icmpv6(self, icmpv6):
		"""
		Create the object icmpv6
		
		Args:
			icmpv6 An instance of the Icmpv6 class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['icmpv6']=serialize_Icmpv6_json(icmpv6)
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

	def getAllIpv6Icmpv6s(self):
		"""
		Retrieve all icmpv6 objects currently pending in the system
		
		Returns:
			A list of Icmpv6 objects
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
			payload= data.get('icmpv6List')
		return deserialize_list_Icmpv6_json(payload)

