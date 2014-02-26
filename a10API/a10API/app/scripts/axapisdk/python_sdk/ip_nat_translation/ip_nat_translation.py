########################################################################################################################
# File name: ip_nat_translation.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/nat/translation',
]

def deserialize_Translation__icmp_timeout_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp_timeout_val = data.get('icmp-timeout-val')
	fast = data.get('fast')
	result = Translation__icmp_timeout(icmp_timeout_val=icmp_timeout_val, fast=fast)
	return result

def deserialize_Ip_nat_translation_service_timeout_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	service_type = data.get('service-type')
	port = data.get('port')
	timeout_val = data.get('timeout-val')
	fast = data.get('fast')
	result = Ip_nat_translation_service_timeout(service_type=service_type, port=port, timeout_val=timeout_val, fast=fast)
	return result

def deserialize_list_Ip_nat_translation_service_timeout_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_translation_service_timeout_json(item))
	return list(container)

def deserialize_Translation_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp_timeout = deserialize_Translation__icmp_timeout_json(data.get('icmp-timeout'))
	tcp_timeout = data.get('tcp-timeout')
	udp_timeout = data.get('udp-timeout')
	service_timeoutlist = deserialize_list_Ip_nat_translation_service_timeout_json(data.get('service-timeoutList'))
	result = Translation(icmp_timeout=icmp_timeout, tcp_timeout=tcp_timeout, udp_timeout=udp_timeout, service_timeoutlist=service_timeoutlist)
	return result

def serialize_Translation__icmp_timeout_json(obj):
	output = OrderedDict()
	if obj.icmp_timeout_val is not None:
		output['icmp-timeout-val'] = obj.icmp_timeout_val
	if obj.fast is not None:
		output['fast'] = obj.fast
	return output

def serialize_Ip_nat_translation_service_timeout_json(obj):
	output = OrderedDict()
	output['service-type'] = obj.service_type
	output['port'] = obj.port
	output['timeout-val'] = obj.timeout_val
	output['fast'] = obj.fast
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ip_nat_translation_service_timeout_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_nat_translation_service_timeout_json(item))
	return output

def serialize_Translation_json(obj):
	output = OrderedDict()
	if obj.icmp_timeout is not None:
		output['icmp-timeout'] = serialize_Translation__icmp_timeout_json(obj.icmp_timeout)
	if obj.tcp_timeout is not None:
		output['tcp-timeout'] = obj.tcp_timeout
	if obj.udp_timeout is not None:
		output['udp-timeout'] = obj.udp_timeout
	if obj.service_timeoutlist is not None:
		output['service-timeoutList'] = serialize_list_Ip_nat_translation_service_timeout_json(obj.service_timeoutlist)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Translation_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Translation_json(item))
	return list(container)

class Translation__icmp_timeout(AxapiObject):
	__metaclass__ = StructMeta 
	icmp_timeout_val=PosRangedInteger(2, 15000)
	fast=PosRangedInteger(0, 1)
	def __init__(self, icmp_timeout_val=None, fast=None):
		self.icmp_timeout_val = icmp_timeout_val
		self.fast = fast

	def __str__(self):
		return ""

class Translation(AxapiObject):
	__metaclass__ = StructMeta 
	tcp_timeout=PosRangedInteger(2, 15000)
	udp_timeout=PosRangedInteger(2, 15000)
	def __init__(self, icmp_timeout=None, tcp_timeout=None, udp_timeout=None, service_timeoutlist=None):
		self.icmp_timeout = icmp_timeout
		self.tcp_timeout = tcp_timeout
		self.udp_timeout = udp_timeout
		self.service_timeoutlist = service_timeoutlist

	def __str__(self):
		return ""

class Ip_nat_translation_service_timeout(AxapiObject):
	__metaclass__ = StructMeta 
	service_type = Enum(['tcp', 'udp'])
	port=PosRangedInteger(1, 65535)
	timeout_val=PosRangedInteger(2, 15000)
	fast=PosRangedInteger(0, 1)
	def __init__(self, service_type, port, timeout_val, fast):
		self.service_type = service_type
		self.port = port
		self.timeout_val = timeout_val
		self.fast = fast

	def __str__(self):
		return str(self.service_type) + '+' + str(self.port) + '+' + str(self.timeout_val) + '+' + str(self.fast)

class IpNatTranslationClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpNatTranslation(self):
		"""
		Retrieve the translation identified by the specified identifier
		
		Returns:
			An instance of the Translation class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified translation does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('translation')
		return deserialize_Translation_json(payload)

	def putIpNatTranslation(self, translation):
		"""
		Replace the object translation
		
		Args:
			translation An instance of the Translation class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['translation']=serialize_Translation_json(translation)
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

	def deleteIpNatTranslation(self):
		"""
		Remove the translation identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified translation does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpNatTranslationsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpNatTranslation(self, translation):
		"""
		Create the object translation
		
		Args:
			translation An instance of the Translation class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['translation']=serialize_Translation_json(translation)
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

	def getAllIpNatTranslations(self):
		"""
		Retrieve all translation objects currently pending in the system
		
		Returns:
			A list of Translation objects
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
			payload= data.get('translationList')
		return deserialize_list_Translation_json(payload)

