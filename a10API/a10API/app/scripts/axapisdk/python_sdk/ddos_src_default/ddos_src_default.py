########################################################################################################################
# File name: ddos_src_default.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/src/default',
]

def deserialize_Ddos_src_default_l4_type__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	result = Ddos_src_default_l4_type__template(tcp=tcp, udp=udp)
	return result

def deserialize_Ddos_src_default_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	deny = data.get('deny')
	glid = data.get('glid')
	template = deserialize_Ddos_src_default_l4_type__template_json(data.get('template'))
	result = Ddos_src_default_l4_type(protocol=protocol, deny=deny, glid=glid, template=template)
	return result

def deserialize_list_Ddos_src_default_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_default_l4_type_json(item))
	return list(container)

def deserialize_Ddos_src_default_app_type__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns = data.get('dns')
	http = data.get('http')
	ssl_l4 = data.get('ssl-l4')
	result = Ddos_src_default_app_type__template(dns=dns, http=http, ssl_l4=ssl_l4)
	return result

def deserialize_Ddos_src_default_app_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	template = deserialize_Ddos_src_default_app_type__template_json(data.get('template'))
	result = Ddos_src_default_app_type(protocol=protocol, template=template)
	return result

def deserialize_list_Ddos_src_default_app_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_default_app_type_json(item))
	return list(container)

def deserialize_Default_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default_address_type = data.get('default-address-type')
	disable = data.get('disable')
	age = data.get('age')
	l4_typelist = deserialize_list_Ddos_src_default_l4_type_json(data.get('l4-typeList'))
	app_typelist = deserialize_list_Ddos_src_default_app_type_json(data.get('app-typeList'))
	result = Default(default_address_type=default_address_type, disable=disable, age=age, l4_typelist=l4_typelist, app_typelist=app_typelist)
	return result

def serialize_Ddos_src_default_l4_type__template_json(obj):
	output = OrderedDict()
	if obj.tcp is not None:
		output['tcp'] = obj.tcp
	if obj.udp is not None:
		output['udp'] = obj.udp
	return output

def serialize_Ddos_src_default_l4_type_json(obj):
	output = OrderedDict()
	output['protocol'] = obj.protocol
	if obj.deny is not None:
		output['deny'] = obj.deny
	if obj.glid is not None:
		output['glid'] = obj.glid
	if obj.template is not None:
		output['template'] = serialize_Ddos_src_default_l4_type__template_json(obj.template)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ddos_src_default_l4_type_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_src_default_l4_type_json(item))
	return output

def serialize_Ddos_src_default_app_type__template_json(obj):
	output = OrderedDict()
	if obj.dns is not None:
		output['dns'] = obj.dns
	if obj.http is not None:
		output['http'] = obj.http
	if obj.ssl_l4 is not None:
		output['ssl-l4'] = obj.ssl_l4
	return output

def serialize_Ddos_src_default_app_type_json(obj):
	output = OrderedDict()
	output['protocol'] = obj.protocol
	if obj.template is not None:
		output['template'] = serialize_Ddos_src_default_app_type__template_json(obj.template)
	return output

def serialize_list_Ddos_src_default_app_type_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_src_default_app_type_json(item))
	return output

def serialize_Default_json(obj):
	output = OrderedDict()
	output['default-address-type'] = obj.default_address_type
	if obj.disable is not None:
		output['disable'] = obj.disable
	if obj.age is not None:
		output['age'] = obj.age
	if obj.l4_typelist is not None:
		output['l4-typeList'] = serialize_list_Ddos_src_default_l4_type_json(obj.l4_typelist)
	if obj.app_typelist is not None:
		output['app-typeList'] = serialize_list_Ddos_src_default_app_type_json(obj.app_typelist)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Default_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Default_json(item))
	return list(container)

class Default(AxapiObject):
	__metaclass__ = StructMeta 
	default_address_type = Enum(['ip', 'ipv6'])
	disable=PosRangedInteger(0, 1)
	age=PosRangedInteger(5, 1023)
	def __init__(self, default_address_type, disable=None, age=None, l4_typelist=None, app_typelist=None):
		self.default_address_type = default_address_type
		self.disable = disable
		self.age = age
		self.l4_typelist = l4_typelist
		self.app_typelist = app_typelist

	def __str__(self):
		return str(self.default_address_type)

class Ddos_src_default_l4_type__template(AxapiObject):
	__metaclass__ = StructMeta 
	tcp=SizedString(1, 255)
	udp=SizedString(1, 255)
	def __init__(self, tcp=None, udp=None):
		self.tcp = tcp
		self.udp = udp

	def __str__(self):
		return ""

class Ddos_src_default_l4_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['tcp', 'udp', 'icmp', 'other'])
	deny=PosRangedInteger(0, 1)
	glid=PosRangedInteger(1, 32000)
	def __init__(self, protocol, deny=None, glid=None, template=None):
		self.protocol = protocol
		self.deny = deny
		self.glid = glid
		self.template = template

	def __str__(self):
		return str(self.protocol)

class Default_default_address_type(AxapiObject):
	__metaclass__ = StructMeta 
	default_address_type = Enum(['ip', 'ipv6'])
	def __init__(self, default_address_type):
		self.default_address_type = default_address_type

	def __str__(self):
		return str(self.default_address_type)

class Ddos_src_default_app_type__template(AxapiObject):
	__metaclass__ = StructMeta 
	dns=SizedString(1, 255)
	http=SizedString(1, 255)
	ssl_l4=SizedString(1, 255)
	def __init__(self, dns=None, http=None, ssl_l4=None):
		self.dns = dns
		self.http = http
		self.ssl_l4 = ssl_l4

	def __str__(self):
		return ""

class Ddos_src_default_app_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'ssl-l4'])
	def __init__(self, protocol, template=None):
		self.protocol = protocol
		self.template = template

	def __str__(self):
		return str(self.protocol)

class DdosSrcDefaultClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosSrcDefault(self, default_default_address_type):
		"""
		Retrieve the default identified by the specified identifier
		
		Args:
			default_default_address_type Default_default_address_type
		
		Returns:
			An instance of the Default class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(default_default_address_type) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified default does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('default')
		return deserialize_Default_json(payload)

	def putDdosSrcDefault(self, default_default_address_type, default):
		"""
		Replace the object default
		
		Args:
			default_default_address_type Default_default_address_type
			default An instance of the Default class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['default']=serialize_Default_json(default)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(default_default_address_type) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosSrcDefault(self, default_default_address_type):
		"""
		Remove the default identified by the specified identifier from the system
		
		Args:
			default_default_address_type Default_default_address_type
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(default_default_address_type) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified default does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosSrcDefaultsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosSrcDefault(self, default):
		"""
		Create the object default
		
		Args:
			default An instance of the Default class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['default']=serialize_Default_json(default)
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

	def getAllDdosSrcDefaults(self):
		"""
		Retrieve all default objects currently pending in the system
		
		Returns:
			A list of Default objects
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
			payload= data.get('defaultList')
		return deserialize_list_Default_json(payload)

