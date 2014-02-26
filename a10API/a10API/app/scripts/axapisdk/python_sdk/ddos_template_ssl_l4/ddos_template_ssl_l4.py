########################################################################################################################
# File name: ddos_template_ssl_l4.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/template/ssl-l4',
]

def deserialize_Ssl_l4_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ssl_l4_tmpl_name = data.get('ssl-l4-tmpl-name')
	action = data.get('action')
	disable = data.get('disable')
	renegotiation = data.get('renegotiation')
	request_rate_limit = data.get('request-rate-limit')
	result = Ssl_l4(ssl_l4_tmpl_name=ssl_l4_tmpl_name, action=action, disable=disable, renegotiation=renegotiation, request_rate_limit=request_rate_limit)
	return result

def serialize_Ssl_l4_json(obj):
	output = OrderedDict()
	output['ssl-l4-tmpl-name'] = obj.ssl_l4_tmpl_name
	if obj.action is not None:
		output['action'] = obj.action
	if obj.disable is not None:
		output['disable'] = obj.disable
	if obj.renegotiation is not None:
		output['renegotiation'] = obj.renegotiation
	if obj.request_rate_limit is not None:
		output['request-rate-limit'] = obj.request_rate_limit
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Ssl_l4_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ssl_l4_json(item))
	return list(container)

class Ssl_l4_ssl_l4_tmpl_name(AxapiObject):
	__metaclass__ = StructMeta 
	ssl_l4_tmpl_name=SizedString(1, 63)
	def __init__(self, ssl_l4_tmpl_name):
		self.ssl_l4_tmpl_name = ssl_l4_tmpl_name

	def __str__(self):
		return str(self.ssl_l4_tmpl_name)

class Ssl_l4(AxapiObject):
	__metaclass__ = StructMeta 
	ssl_l4_tmpl_name=SizedString(1, 63)
	action = Enum(['drop', 'reset'])
	disable=PosRangedInteger(0, 1)
	renegotiation=PosRangedInteger(0, 7)
	request_rate_limit=PosRangedInteger(1, 16000000)
	def __init__(self, ssl_l4_tmpl_name, action=None, disable=None, renegotiation=None, request_rate_limit=None):
		self.ssl_l4_tmpl_name = ssl_l4_tmpl_name
		self.action = action
		self.disable = disable
		self.renegotiation = renegotiation
		self.request_rate_limit = request_rate_limit

	def __str__(self):
		return str(self.ssl_l4_tmpl_name)

class DdosTemplateSsll4Client(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosTemplateSsll4(self, ssl_l4_ssl_l4_tmpl_name):
		"""
		Retrieve the ssl_l4 identified by the specified identifier
		
		Args:
			ssl_l4_ssl_l4_tmpl_name Ssl_l4_ssl_l4_tmpl_name
		
		Returns:
			An instance of the Ssl_l4 class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(ssl_l4_ssl_l4_tmpl_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ssl_l4 does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ssl-l4')
		return deserialize_Ssl_l4_json(payload)

	def putDdosTemplateSsll4(self, ssl_l4_ssl_l4_tmpl_name, ssl_l4):
		"""
		Replace the object ssl_l4
		
		Args:
			ssl_l4_ssl_l4_tmpl_name Ssl_l4_ssl_l4_tmpl_name
			ssl_l4 An instance of the Ssl_l4 class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ssl-l4']=serialize_Ssl_l4_json(ssl_l4)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(ssl_l4_ssl_l4_tmpl_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosTemplateSsll4(self, ssl_l4_ssl_l4_tmpl_name):
		"""
		Remove the ssl_l4 identified by the specified identifier from the system
		
		Args:
			ssl_l4_ssl_l4_tmpl_name Ssl_l4_ssl_l4_tmpl_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(ssl_l4_ssl_l4_tmpl_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ssl_l4 does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosTemplateSsll4sClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosTemplateSsll4(self, ssl_l4):
		"""
		Create the object ssl_l4
		
		Args:
			ssl_l4 An instance of the Ssl_l4 class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ssl-l4']=serialize_Ssl_l4_json(ssl_l4)
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

	def getAllDdosTemplateSsll4s(self):
		"""
		Retrieve all ssl_l4 objects currently pending in the system
		
		Returns:
			A list of Ssl_l4 objects
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
			payload= data.get('ssl-l4List')
		return deserialize_list_Ssl_l4_json(payload)

