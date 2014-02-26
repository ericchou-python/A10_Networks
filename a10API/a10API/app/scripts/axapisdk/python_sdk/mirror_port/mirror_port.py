########################################################################################################################
# File name: mirror_port.py
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
	'https://axapi.a10networks.com/axapi/v3/mirror-port',
]

def deserialize_Mirror_port__ethernet_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	result = Mirror_port__ethernet_cfg()
	return result

def deserialize_Mirror_port_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet_cfg = deserialize_Mirror_port__ethernet_cfg_json(data.get('ethernet-cfg'))
	ethernet = data.get('ethernet')
	result = Mirror_port(ethernet_cfg=ethernet_cfg, ethernet=ethernet)
	return result

def serialize_Mirror_port__ethernet_cfg_json(obj):
	output = OrderedDict()
	return output

def serialize_Mirror_port_json(obj):
	output = OrderedDict()
	output['ethernet-cfg'] = serialize_Mirror_port__ethernet_cfg_json(obj.ethernet_cfg)
	output['ethernet'] = obj.ethernet
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Mirror_port_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Mirror_port_json(item))
	return list(container)

class Mirror_port_ethernet_cfg__ethernet_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class Mirror_port_ethernet_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ethernet_cfg):
		self.ethernet_cfg = ethernet_cfg

	def __str__(self):
		return str(self.ethernet_cfg)

class Mirror_port__ethernet_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class Mirror_port(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet=PosRangedInteger(1, 2048)
	def __init__(self, ethernet_cfg, ethernet):
		self.ethernet_cfg = ethernet_cfg
		self.ethernet = ethernet

	def __str__(self):
		return str(self.ethernet_cfg) + '+' + str(self.ethernet)

class MirrorportClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getMirrorport(self, mirror_port_ethernet_cfg):
		"""
		Retrieve the mirror_port identified by the specified identifier
		
		Args:
			mirror_port_ethernet_cfg Mirror_port_ethernet_cfg
		
		Returns:
			An instance of the Mirror_port class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(mirror_port_ethernet_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified mirror_port does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('mirror-port')
		return deserialize_Mirror_port_json(payload)

	def putMirrorport(self, mirror_port_ethernet_cfg, mirror_port):
		"""
		Replace the object mirror_port
		
		Args:
			mirror_port_ethernet_cfg Mirror_port_ethernet_cfg
			mirror_port An instance of the Mirror_port class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['mirror-port']=serialize_Mirror_port_json(mirror_port)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(mirror_port_ethernet_cfg) .replace("/", "%2f") + query, payload, headers)
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

	def deleteMirrorport(self, mirror_port_ethernet_cfg):
		"""
		Remove the mirror_port identified by the specified identifier from the system
		
		Args:
			mirror_port_ethernet_cfg Mirror_port_ethernet_cfg
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(mirror_port_ethernet_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified mirror_port does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllMirrorportsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitMirrorport(self, mirror_port):
		"""
		Create the object mirror_port
		
		Args:
			mirror_port An instance of the Mirror_port class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['mirror-port']=serialize_Mirror_port_json(mirror_port)
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

	def getAllMirrorports(self):
		"""
		Retrieve all mirror_port objects currently pending in the system
		
		Returns:
			A list of Mirror_port objects
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
			payload= data.get('mirror-portList')
		return deserialize_list_Mirror_port_json(payload)

