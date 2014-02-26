########################################################################################################################
# File name: ddos_dst_entry_src_dst_pair_app_type_src_dst.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/dst/entry/src-dst-pair/app-type-src-dst',
]

def deserialize_App_type_src_dst__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ssl_l4 = data.get('ssl-l4')
	dns = data.get('dns')
	http = data.get('http')
	result = App_type_src_dst__template(ssl_l4=ssl_l4, dns=dns, http=http)
	return result

def deserialize_App_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	template = deserialize_App_type_src_dst__template_json(data.get('template'))
	result = App_type_src_dst(protocol=protocol, template=template)
	return result

def serialize_App_type_src_dst__template_json(obj):
	output = OrderedDict()
	if obj.ssl_l4 is not None:
		output['ssl-l4'] = obj.ssl_l4
	if obj.dns is not None:
		output['dns'] = obj.dns
	if obj.http is not None:
		output['http'] = obj.http
	return output

def serialize_App_type_src_dst_json(obj):
	output = OrderedDict()
	output['protocol'] = obj.protocol
	if obj.template is not None:
		output['template'] = serialize_App_type_src_dst__template_json(obj.template)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_App_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_App_type_src_dst_json(item))
	return list(container)

class App_type_src_dst_protocol(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'ssl-l4'])
	def __init__(self, protocol):
		self.protocol = protocol

	def __str__(self):
		return str(self.protocol)

class App_type_src_dst__template(AxapiObject):
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

class App_type_src_dst(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'ssl-l4'])
	def __init__(self, protocol, template=None):
		self.protocol = protocol
		self.template = template

	def __str__(self):
		return str(self.protocol)

class DdosDstEntrySrcdstpairApptypesrcdstClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosDstEntrySrcdstpairApptypesrcdst(self, app_type_src_dst_protocol):
		"""
		Retrieve the app_type_src_dst identified by the specified identifier
		
		Args:
			app_type_src_dst_protocol App_type_src_dst_protocol
		
		Returns:
			An instance of the App_type_src_dst class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(app_type_src_dst_protocol) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified app_type_src_dst does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('app-type-src-dst')
		return deserialize_App_type_src_dst_json(payload)

	def putDdosDstEntrySrcdstpairApptypesrcdst(self, app_type_src_dst_protocol, app_type_src_dst):
		"""
		Replace the object app_type_src_dst
		
		Args:
			app_type_src_dst_protocol App_type_src_dst_protocol
			app_type_src_dst An instance of the App_type_src_dst class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['app-type-src-dst']=serialize_App_type_src_dst_json(app_type_src_dst)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(app_type_src_dst_protocol) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosDstEntrySrcdstpairApptypesrcdst(self, app_type_src_dst_protocol):
		"""
		Remove the app_type_src_dst identified by the specified identifier from
		the system
		
		Args:
			app_type_src_dst_protocol App_type_src_dst_protocol
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(app_type_src_dst_protocol) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified app_type_src_dst does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosDstEntrySrcdstpairApptypesrcdstsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosDstEntrySrcdstpairApptypesrcdst(self, app_type_src_dst):
		"""
		Create the object app_type_src_dst
		
		Args:
			app_type_src_dst An instance of the App_type_src_dst class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['app-type-src-dst']=serialize_App_type_src_dst_json(app_type_src_dst)
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

	def getAllDdosDstEntrySrcdstpairApptypesrcdsts(self):
		"""
		Retrieve all app_type_src_dst objects currently pending in the system
		
		Returns:
			A list of App_type_src_dst objects
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
			payload= data.get('app-type-src-dstList')
		return deserialize_list_App_type_src_dst_json(payload)

