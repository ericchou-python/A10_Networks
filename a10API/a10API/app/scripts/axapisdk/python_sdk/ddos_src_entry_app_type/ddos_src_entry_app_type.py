########################################################################################################################
# File name: ddos_src_entry_app_type.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/src/entry/app-type',
]

def deserialize_App_type__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ssl_l4 = data.get('ssl-l4')
	dns = data.get('dns')
	http = data.get('http')
	result = App_type__template(ssl_l4=ssl_l4, dns=dns, http=http)
	return result

def deserialize_App_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	template = deserialize_App_type__template_json(data.get('template'))
	result = App_type(protocol=protocol, template=template)
	return result

def serialize_App_type__template_json(obj):
	output = OrderedDict()
	if obj.ssl_l4 is not None:
		output['ssl-l4'] = obj.ssl_l4
	if obj.dns is not None:
		output['dns'] = obj.dns
	if obj.http is not None:
		output['http'] = obj.http
	return output

def serialize_App_type_json(obj):
	output = OrderedDict()
	output['protocol'] = obj.protocol
	if obj.template is not None:
		output['template'] = serialize_App_type__template_json(obj.template)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_App_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_App_type_json(item))
	return list(container)

class App_type_protocol(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'ssl-l4'])
	def __init__(self, protocol):
		self.protocol = protocol

	def __str__(self):
		return str(self.protocol)

class App_type__template(AxapiObject):
	__metaclass__ = StructMeta 
	ssl_l4=SizedString(1, 255)
	dns=SizedString(1, 255)
	http=SizedString(1, 255)
	def __init__(self, ssl_l4=None, dns=None, http=None):
		self.ssl_l4 = ssl_l4
		self.dns = dns
		self.http = http

	def __str__(self):
		return ""

class App_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'ssl-l4'])
	def __init__(self, protocol, template=None):
		self.protocol = protocol
		self.template = template

	def __str__(self):
		return str(self.protocol)

class DdosSrcEntryApptypeClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosSrcEntryApptype(self, app_type_protocol):
		"""
		Retrieve the app_type identified by the specified identifier
		
		Args:
			app_type_protocol App_type_protocol
		
		Returns:
			An instance of the App_type class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(app_type_protocol) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified app_type does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('app-type')
		return deserialize_App_type_json(payload)

	def putDdosSrcEntryApptype(self, app_type_protocol, app_type):
		"""
		Replace the object app_type
		
		Args:
			app_type_protocol App_type_protocol
			app_type An instance of the App_type class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['app-type']=serialize_App_type_json(app_type)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(app_type_protocol) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosSrcEntryApptype(self, app_type_protocol):
		"""
		Remove the app_type identified by the specified identifier from the system
		
		Args:
			app_type_protocol App_type_protocol
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(app_type_protocol) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified app_type does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosSrcEntryApptypesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosSrcEntryApptype(self, app_type):
		"""
		Create the object app_type
		
		Args:
			app_type An instance of the App_type class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['app-type']=serialize_App_type_json(app_type)
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

	def getAllDdosSrcEntryApptypes(self):
		"""
		Retrieve all app_type objects currently pending in the system
		
		Returns:
			A list of App_type objects
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
			payload= data.get('app-typeList')
		return deserialize_list_App_type_json(payload)

