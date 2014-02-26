########################################################################################################################
# File name: ddos_dst_entry_ip_proto.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/dst/entry/ip-proto',
]

def deserialize_Ip_proto_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	port_num = data.get('port-num')
	deny = data.get('deny')
	glid = data.get('glid')
	result = Ip_proto(port_num=port_num, deny=deny, glid=glid)
	return result

def serialize_Ip_proto_json(obj):
	output = OrderedDict()
	output['port-num'] = obj.port_num
	if obj.deny is not None:
		output['deny'] = obj.deny
	if obj.glid is not None:
		output['glid'] = obj.glid
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Ip_proto_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_proto_json(item))
	return list(container)

class Ip_proto_port_num(AxapiObject):
	__metaclass__ = StructMeta 
	port_num=PosRangedInteger(1, 255)
	def __init__(self, port_num):
		self.port_num = port_num

	def __str__(self):
		return str(self.port_num)

class Ip_proto(AxapiObject):
	__metaclass__ = StructMeta 
	port_num=PosRangedInteger(1, 255)
	deny=PosRangedInteger(0, 1)
	glid=PosRangedInteger(1, 32000)
	def __init__(self, port_num, deny=None, glid=None):
		self.port_num = port_num
		self.deny = deny
		self.glid = glid

	def __str__(self):
		return str(self.port_num)

class DdosDstEntryIpprotoClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosDstEntryIpproto(self, ip_proto_port_num):
		"""
		Retrieve the ip_proto identified by the specified identifier
		
		Args:
			ip_proto_port_num Ip_proto_port_num
		
		Returns:
			An instance of the Ip_proto class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(ip_proto_port_num) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ip_proto does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ip-proto')
		return deserialize_Ip_proto_json(payload)

	def putDdosDstEntryIpproto(self, ip_proto_port_num, ip_proto):
		"""
		Replace the object ip_proto
		
		Args:
			ip_proto_port_num Ip_proto_port_num
			ip_proto An instance of the Ip_proto class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ip-proto']=serialize_Ip_proto_json(ip_proto)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(ip_proto_port_num) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosDstEntryIpproto(self, ip_proto_port_num):
		"""
		Remove the ip_proto identified by the specified identifier from the system
		
		Args:
			ip_proto_port_num Ip_proto_port_num
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(ip_proto_port_num) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ip_proto does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosDstEntryIpprotosClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosDstEntryIpproto(self, ip_proto):
		"""
		Create the object ip_proto
		
		Args:
			ip_proto An instance of the Ip_proto class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ip-proto']=serialize_Ip_proto_json(ip_proto)
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

	def getAllDdosDstEntryIpprotos(self):
		"""
		Retrieve all ip_proto objects currently pending in the system
		
		Returns:
			A list of Ip_proto objects
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
			payload= data.get('ip-protoList')
		return deserialize_list_Ip_proto_json(payload)

