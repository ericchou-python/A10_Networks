########################################################################################################################
# File name: ddos_dst_entry_src_dst_pair.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/dst/entry/src-dst-pair',
]

def deserialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	result = Ddos_dst_entry_src_dst_pair_l4_type_src_dst__template(tcp=tcp, udp=udp)
	return result

def deserialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	glid = data.get('glid')
	template = deserialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst__template_json(data.get('template'))
	result = Ddos_dst_entry_src_dst_pair_l4_type_src_dst(protocol=protocol, glid=glid, template=template)
	return result

def deserialize_list_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(item))
	return list(container)

def deserialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ssl_l4 = data.get('ssl-l4')
	dns = data.get('dns')
	http = data.get('http')
	result = Ddos_dst_entry_src_dst_pair_app_type_src_dst__template(ssl_l4=ssl_l4, dns=dns, http=http)
	return result

def deserialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	template = deserialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst__template_json(data.get('template'))
	result = Ddos_dst_entry_src_dst_pair_app_type_src_dst(protocol=protocol, template=template)
	return result

def deserialize_list_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(item))
	return list(container)

def deserialize_Src_dst_pair_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	src = data.get('src')
	class_list_name = data.get('class-list-name')
	l4_type_src_dstlist = deserialize_list_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(data.get('l4-type-src-dstList'))
	app_type_src_dstlist = deserialize_list_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(data.get('app-type-src-dstList'))
	result = Src_dst_pair(src=src, class_list_name=class_list_name, l4_type_src_dstlist=l4_type_src_dstlist, app_type_src_dstlist=app_type_src_dstlist)
	return result

def serialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst__template_json(obj):
	output = OrderedDict()
	if obj.tcp is not None:
		output['tcp'] = obj.tcp
	if obj.udp is not None:
		output['udp'] = obj.udp
	return output

def serialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(obj):
	output = OrderedDict()
	output['protocol'] = obj.protocol
	if obj.glid is not None:
		output['glid'] = obj.glid
	if obj.template is not None:
		output['template'] = serialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst__template_json(obj.template)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(item))
	return output

def serialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst__template_json(obj):
	output = OrderedDict()
	if obj.ssl_l4 is not None:
		output['ssl-l4'] = obj.ssl_l4
	if obj.dns is not None:
		output['dns'] = obj.dns
	if obj.http is not None:
		output['http'] = obj.http
	return output

def serialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(obj):
	output = OrderedDict()
	output['protocol'] = obj.protocol
	if obj.template is not None:
		output['template'] = serialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst__template_json(obj.template)
	return output

def serialize_list_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(item))
	return output

def serialize_Src_dst_pair_json(obj):
	output = OrderedDict()
	output['src'] = obj.src
	if obj.class_list_name is not None:
		output['class-list-name'] = obj.class_list_name
	if obj.l4_type_src_dstlist is not None:
		output['l4-type-src-dstList'] = serialize_list_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(obj.l4_type_src_dstlist)
	if obj.app_type_src_dstlist is not None:
		output['app-type-src-dstList'] = serialize_list_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(obj.app_type_src_dstlist)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Src_dst_pair_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Src_dst_pair_json(item))
	return list(container)

class Src_dst_pair(AxapiObject):
	__metaclass__ = StructMeta 
	src = Enum(['default', 'class-list'])
	class_list_name=SizedString(1, 63)
	def __init__(self, src, class_list_name=None, l4_type_src_dstlist=None, app_type_src_dstlist=None):
		self.src = src
		self.class_list_name = class_list_name
		self.l4_type_src_dstlist = l4_type_src_dstlist
		self.app_type_src_dstlist = app_type_src_dstlist

	def __str__(self):
		return str(self.src)

class Ddos_dst_entry_src_dst_pair_l4_type_src_dst__template(AxapiObject):
	__metaclass__ = StructMeta 
	tcp=SizedString(1, 255)
	udp=SizedString(1, 255)
	def __init__(self, tcp=None, udp=None):
		self.tcp = tcp
		self.udp = udp

	def __str__(self):
		return ""

class Ddos_dst_entry_src_dst_pair_l4_type_src_dst(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['tcp', 'udp', 'icmp', 'other'])
	glid=PosRangedInteger(1, 32000)
	def __init__(self, protocol, glid=None, template=None):
		self.protocol = protocol
		self.glid = glid
		self.template = template

	def __str__(self):
		return str(self.protocol)

class Src_dst_pair_src(AxapiObject):
	__metaclass__ = StructMeta 
	src = Enum(['default', 'class-list'])
	def __init__(self, src):
		self.src = src

	def __str__(self):
		return str(self.src)

class Ddos_dst_entry_src_dst_pair_app_type_src_dst__template(AxapiObject):
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

class Ddos_dst_entry_src_dst_pair_app_type_src_dst(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'ssl-l4'])
	def __init__(self, protocol, template=None):
		self.protocol = protocol
		self.template = template

	def __str__(self):
		return str(self.protocol)

class DdosDstEntrySrcdstpairClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosDstEntrySrcdstpair(self, src_dst_pair_src):
		"""
		Retrieve the src_dst_pair identified by the specified identifier
		
		Args:
			src_dst_pair_src Src_dst_pair_src
		
		Returns:
			An instance of the Src_dst_pair class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(src_dst_pair_src) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified src_dst_pair does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('src-dst-pair')
		return deserialize_Src_dst_pair_json(payload)

	def putDdosDstEntrySrcdstpair(self, src_dst_pair_src, src_dst_pair):
		"""
		Replace the object src_dst_pair
		
		Args:
			src_dst_pair_src Src_dst_pair_src
			src_dst_pair An instance of the Src_dst_pair class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['src-dst-pair']=serialize_Src_dst_pair_json(src_dst_pair)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(src_dst_pair_src) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosDstEntrySrcdstpair(self, src_dst_pair_src):
		"""
		Remove the src_dst_pair identified by the specified identifier from the
		system
		
		Args:
			src_dst_pair_src Src_dst_pair_src
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(src_dst_pair_src) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified src_dst_pair does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosDstEntrySrcdstpairsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosDstEntrySrcdstpair(self, src_dst_pair):
		"""
		Create the object src_dst_pair
		
		Args:
			src_dst_pair An instance of the Src_dst_pair class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['src-dst-pair']=serialize_Src_dst_pair_json(src_dst_pair)
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

	def getAllDdosDstEntrySrcdstpairs(self):
		"""
		Retrieve all src_dst_pair objects currently pending in the system
		
		Returns:
			A list of Src_dst_pair objects
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
			payload= data.get('src-dst-pairList')
		return deserialize_list_Src_dst_pair_json(payload)

