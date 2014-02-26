########################################################################################################################
# File name: ip_nat_inside_source.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/nat/inside/source',
]

def deserialize_Ip_nat_inside_source_list_name_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl_name = data.get('acl-name')
	pool = data.get('pool')
	msl = data.get('msl')
	result = Ip_nat_inside_source_list_name(acl_name=acl_name, pool=pool, msl=msl)
	return result

def deserialize_list_Ip_nat_inside_source_list_name_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_inside_source_list_name_json(item))
	return list(container)

def deserialize_Ip_nat_inside_source_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl_id = data.get('acl-id')
	pool = data.get('pool')
	msl = data.get('msl')
	namelist = deserialize_list_Ip_nat_inside_source_list_name_json(data.get('nameList'))
	result = Ip_nat_inside_source_list(acl_id=acl_id, pool=pool, msl=msl, namelist=namelist)
	return result

def deserialize_list_Ip_nat_inside_source_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_inside_source_list_json(item))
	return list(container)

def deserialize_Ip_nat_inside_source_static_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	src_address = data.get('src-address')
	nat_address = data.get('nat-address')
	vrid = data.get('vrid')
	result = Ip_nat_inside_source_static(src_address=src_address, nat_address=nat_address, vrid=vrid)
	return result

def deserialize_list_Ip_nat_inside_source_static_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_inside_source_static_json(item))
	return list(container)

def deserialize_Source_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	class_list = data.get('class-list')
	listlist = deserialize_list_Ip_nat_inside_source_list_json(data.get('listList'))
	staticlist = deserialize_list_Ip_nat_inside_source_static_json(data.get('staticList'))
	result = Source(class_list=class_list, listlist=listlist, staticlist=staticlist)
	return result

def serialize_Ip_nat_inside_source_list_name_json(obj):
	output = OrderedDict()
	output['acl-name'] = obj.acl_name
	output['pool'] = obj.pool
	if obj.msl is not None:
		output['msl'] = obj.msl
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ip_nat_inside_source_list_name_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_nat_inside_source_list_name_json(item))
	return output

def serialize_Ip_nat_inside_source_list_json(obj):
	output = OrderedDict()
	output['acl-id'] = obj.acl_id
	output['pool'] = obj.pool
	if obj.msl is not None:
		output['msl'] = obj.msl
	if obj.namelist is not None:
		output['nameList'] = serialize_list_Ip_nat_inside_source_list_name_json(obj.namelist)
	return output

def serialize_list_Ip_nat_inside_source_list_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_nat_inside_source_list_json(item))
	return output

def serialize_Ip_nat_inside_source_static_json(obj):
	output = OrderedDict()
	output['src-address'] = obj.src_address
	output['nat-address'] = obj.nat_address
	if obj.vrid is not None:
		output['vrid'] = obj.vrid
	return output

def serialize_list_Ip_nat_inside_source_static_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_nat_inside_source_static_json(item))
	return output

def serialize_Source_json(obj):
	output = OrderedDict()
	if obj.class_list is not None:
		output['class-list'] = obj.class_list
	if obj.listlist is not None:
		output['listList'] = serialize_list_Ip_nat_inside_source_list_json(obj.listlist)
	if obj.staticlist is not None:
		output['staticList'] = serialize_list_Ip_nat_inside_source_static_json(obj.staticlist)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Source_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Source_json(item))
	return list(container)

class Source(AxapiObject):
	__metaclass__ = StructMeta 
	class_list=SizedString(1, 63)
	def __init__(self, class_list=None, listlist=None, staticlist=None):
		self.class_list = class_list
		self.listlist = listlist
		self.staticlist = staticlist

	def __str__(self):
		return ""

class Ip_nat_inside_source_list(AxapiObject):
	__metaclass__ = StructMeta 
	acl_id=PosRangedInteger(1, 199)
	pool=SizedString(1, 255)
	msl=PosRangedInteger(1, 1800)
	def __init__(self, acl_id, pool, msl=None, namelist=None):
		self.acl_id = acl_id
		self.pool = pool
		self.msl = msl
		self.namelist = namelist

	def __str__(self):
		return str(self.acl_id) + '+' + str(self.pool)

class Ip_nat_inside_source_list_name(AxapiObject):
	__metaclass__ = StructMeta 
	acl_name=SizedString(1, 16)
	pool=SizedString(1, 255)
	msl=PosRangedInteger(1, 1800)
	def __init__(self, acl_name, pool, msl=None):
		self.acl_name = acl_name
		self.pool = pool
		self.msl = msl

	def __str__(self):
		return str(self.acl_name) + '+' + str(self.pool)

class Ip_nat_inside_source_static(AxapiObject):
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

class IpNatInsideSourceClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpNatInsideSource(self):
		"""
		Retrieve the source identified by the specified identifier
		
		Returns:
			An instance of the Source class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified source does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('source')
		return deserialize_Source_json(payload)

	def putIpNatInsideSource(self, source):
		"""
		Replace the object source
		
		Args:
			source An instance of the Source class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['source']=serialize_Source_json(source)
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

	def deleteIpNatInsideSource(self):
		"""
		Remove the source identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified source does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpNatInsideSourcesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpNatInsideSource(self, source):
		"""
		Create the object source
		
		Args:
			source An instance of the Source class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['source']=serialize_Source_json(source)
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

	def getAllIpNatInsideSources(self):
		"""
		Retrieve all source objects currently pending in the system
		
		Returns:
			A list of Source objects
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
			payload= data.get('sourceList')
		return deserialize_list_Source_json(payload)

