########################################################################################################################
# File name: ip_nat_inside_source_static.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/nat/inside/source/static',
]

def deserialize_Static_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	src_address = data.get('src-address')
	nat_address = data.get('nat-address')
	vrid = data.get('vrid')
	result = Static(src_address=src_address, nat_address=nat_address, vrid=vrid)
	return result

def serialize_Static_json(obj):
	output = OrderedDict()
	output['src-address'] = obj.src_address
	output['nat-address'] = obj.nat_address
	if obj.vrid is not None:
		output['vrid'] = obj.vrid
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Static_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Static_json(item))
	return list(container)

class Static_src_address_nat_address(AxapiObject):
	__metaclass__ = StructMeta 
	src_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	nat_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, src_address, nat_address):
		self.src_address = src_address
		self.nat_address = nat_address

	def __str__(self):
		return str(self.src_address) + '+' + str(self.nat_address)

class Static(AxapiObject):
	__metaclass__ = StructMeta 
	src_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	nat_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	vrid=PosRangedInteger(1, 31)
	def __init__(self, src_address, nat_address, vrid=None):
		self.src_address = src_address
		self.nat_address = nat_address
		self.vrid = vrid

	def __str__(self):
		return str(self.src_address) + '+' + str(self.nat_address)

class IpNatInsideSourceStaticClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpNatInsideSourceStatic(self, static_src_address_nat_address):
		"""
		Retrieve the static identified by the specified identifier
		
		Args:
			static_src_address_nat_address Static_src_address_nat_address
		
		Returns:
			An instance of the Static class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(static_src_address_nat_address) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified static does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('static')
		return deserialize_Static_json(payload)

	def putIpNatInsideSourceStatic(self, static_src_address_nat_address, static):
		"""
		Replace the object static
		
		Args:
			static_src_address_nat_address Static_src_address_nat_address
			static An instance of the Static class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['static']=serialize_Static_json(static)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(static_src_address_nat_address) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpNatInsideSourceStatic(self, static_src_address_nat_address):
		"""
		Remove the static identified by the specified identifier from the system
		
		Args:
			static_src_address_nat_address Static_src_address_nat_address
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(static_src_address_nat_address) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified static does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpNatInsideSourceStaticsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpNatInsideSourceStatic(self, static):
		"""
		Create the object static
		
		Args:
			static An instance of the Static class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['static']=serialize_Static_json(static)
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

	def getAllIpNatInsideSourceStatics(self):
		"""
		Retrieve all static objects currently pending in the system
		
		Returns:
			A list of Static objects
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
			payload= data.get('staticList')
		return deserialize_list_Static_json(payload)

