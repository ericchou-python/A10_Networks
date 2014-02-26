########################################################################################################################
# File name: ddos_src_entry.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/src/entry',
]

def deserialize_Ddos_src_entry_l4_type__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	result = Ddos_src_entry_l4_type__template(tcp=tcp, udp=udp)
	return result

def deserialize_Ddos_src_entry_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	action = data.get('action')
	glid = data.get('glid')
	template = deserialize_Ddos_src_entry_l4_type__template_json(data.get('template'))
	result = Ddos_src_entry_l4_type(protocol=protocol, action=action, glid=glid, template=template)
	return result

def deserialize_list_Ddos_src_entry_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_entry_l4_type_json(item))
	return list(container)

def deserialize_Ddos_src_entry_app_type__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ssl_l4 = data.get('ssl-l4')
	dns = data.get('dns')
	http = data.get('http')
	result = Ddos_src_entry_app_type__template(ssl_l4=ssl_l4, dns=dns, http=http)
	return result

def deserialize_Ddos_src_entry_app_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	template = deserialize_Ddos_src_entry_app_type__template_json(data.get('template'))
	result = Ddos_src_entry_app_type(protocol=protocol, template=template)
	return result

def deserialize_list_Ddos_src_entry_app_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_entry_app_type_json(item))
	return list(container)

def deserialize_Entry_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	src_entry_name = data.get('src-entry-name')
	ipv6_addr = data.get('ipv6-addr')
	ip_addr = data.get('ip-addr')
	subnet_ip_addr = data.get('subnet-ip-addr')
	subnet_ipv6_addr = data.get('subnet-ipv6-addr')
	l4_typelist = deserialize_list_Ddos_src_entry_l4_type_json(data.get('l4-typeList'))
	app_typelist = deserialize_list_Ddos_src_entry_app_type_json(data.get('app-typeList'))
	result = Entry(src_entry_name=src_entry_name, ipv6_addr=ipv6_addr, ip_addr=ip_addr, subnet_ip_addr=subnet_ip_addr, subnet_ipv6_addr=subnet_ipv6_addr, l4_typelist=l4_typelist, app_typelist=app_typelist)
	return result

def serialize_Ddos_src_entry_l4_type__template_json(obj):
	output = OrderedDict()
	if obj.tcp is not None:
		output['tcp'] = obj.tcp
	if obj.udp is not None:
		output['udp'] = obj.udp
	return output

def serialize_Ddos_src_entry_l4_type_json(obj):
	output = OrderedDict()
	output['protocol'] = obj.protocol
	if obj.action is not None:
		output['action'] = obj.action
	if obj.glid is not None:
		output['glid'] = obj.glid
	if obj.template is not None:
		output['template'] = serialize_Ddos_src_entry_l4_type__template_json(obj.template)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ddos_src_entry_l4_type_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_src_entry_l4_type_json(item))
	return output

def serialize_Ddos_src_entry_app_type__template_json(obj):
	output = OrderedDict()
	if obj.ssl_l4 is not None:
		output['ssl-l4'] = obj.ssl_l4
	if obj.dns is not None:
		output['dns'] = obj.dns
	if obj.http is not None:
		output['http'] = obj.http
	return output

def serialize_Ddos_src_entry_app_type_json(obj):
	output = OrderedDict()
	output['protocol'] = obj.protocol
	if obj.template is not None:
		output['template'] = serialize_Ddos_src_entry_app_type__template_json(obj.template)
	return output

def serialize_list_Ddos_src_entry_app_type_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_src_entry_app_type_json(item))
	return output

def serialize_Entry_json(obj):
	output = OrderedDict()
	output['src-entry-name'] = obj.src_entry_name
	if obj.ipv6_addr is not None:
		output['ipv6-addr'] = obj.ipv6_addr
	if obj.ip_addr is not None:
		output['ip-addr'] = obj.ip_addr
	if obj.subnet_ip_addr is not None:
		output['subnet-ip-addr'] = obj.subnet_ip_addr
	if obj.subnet_ipv6_addr is not None:
		output['subnet-ipv6-addr'] = obj.subnet_ipv6_addr
	if obj.l4_typelist is not None:
		output['l4-typeList'] = serialize_list_Ddos_src_entry_l4_type_json(obj.l4_typelist)
	if obj.app_typelist is not None:
		output['app-typeList'] = serialize_list_Ddos_src_entry_app_type_json(obj.app_typelist)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Entry_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Entry_json(item))
	return list(container)

class Entry(AxapiObject):
	__metaclass__ = StructMeta 
	src_entry_name=SizedString(1, 63)
	ipv6_addr=SizedString(1, 255)
	ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_ipv6_addr=SizedString(1, 255)
	def __init__(self, src_entry_name, ipv6_addr=None, ip_addr=None, subnet_ip_addr=None, subnet_ipv6_addr=None, l4_typelist=None, app_typelist=None):
		self.src_entry_name = src_entry_name
		self.ipv6_addr = ipv6_addr
		self.ip_addr = ip_addr
		self.subnet_ip_addr = subnet_ip_addr
		self.subnet_ipv6_addr = subnet_ipv6_addr
		self.l4_typelist = l4_typelist
		self.app_typelist = app_typelist

	def __str__(self):
		return str(self.src_entry_name)

class Ddos_src_entry_l4_type__template(AxapiObject):
	__metaclass__ = StructMeta 
	tcp=SizedString(1, 255)
	udp=SizedString(1, 255)
	def __init__(self, tcp=None, udp=None):
		self.tcp = tcp
		self.udp = udp

	def __str__(self):
		return ""

class Ddos_src_entry_l4_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['tcp', 'udp', 'icmp', 'other'])
	action = Enum(['permit', 'deny'])
	glid=PosRangedInteger(1, 32000)
	def __init__(self, protocol, action=None, glid=None, template=None):
		self.protocol = protocol
		self.action = action
		self.glid = glid
		self.template = template

	def __str__(self):
		return str(self.protocol)

class Entry_src_entry_name(AxapiObject):
	__metaclass__ = StructMeta 
	src_entry_name=SizedString(1, 63)
	def __init__(self, src_entry_name):
		self.src_entry_name = src_entry_name

	def __str__(self):
		return str(self.src_entry_name)

class Ddos_src_entry_app_type__template(AxapiObject):
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

class Ddos_src_entry_app_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'ssl-l4'])
	def __init__(self, protocol, template=None):
		self.protocol = protocol
		self.template = template

	def __str__(self):
		return str(self.protocol)

class DdosSrcEntryClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosSrcEntry(self, entry_src_entry_name):
		"""
		Retrieve the entry identified by the specified identifier
		
		Args:
			entry_src_entry_name Entry_src_entry_name
		
		Returns:
			An instance of the Entry class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(entry_src_entry_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified entry does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('entry')
		return deserialize_Entry_json(payload)

	def putDdosSrcEntry(self, entry_src_entry_name, entry):
		"""
		Replace the object entry
		
		Args:
			entry_src_entry_name Entry_src_entry_name
			entry An instance of the Entry class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['entry']=serialize_Entry_json(entry)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(entry_src_entry_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosSrcEntry(self, entry_src_entry_name):
		"""
		Remove the entry identified by the specified identifier from the system
		
		Args:
			entry_src_entry_name Entry_src_entry_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(entry_src_entry_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified entry does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosSrcEntrysClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosSrcEntry(self, entry):
		"""
		Create the object entry
		
		Args:
			entry An instance of the Entry class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['entry']=serialize_Entry_json(entry)
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

	def getAllDdosSrcEntrys(self):
		"""
		Retrieve all entry objects currently pending in the system
		
		Returns:
			A list of Entry objects
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
			payload= data.get('entryList')
		return deserialize_list_Entry_json(payload)

