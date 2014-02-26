########################################################################################################################
# File name: bfd.py
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
	'https://axapi.a10networks.com/axapi/v3/bfd',
]

def deserialize_Bfd__interval_cfg__min_rx_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	min_rx = data.get('min-rx')
	multiplier = data.get('multiplier')
	result = Bfd__interval_cfg__min_rx_cfg(min_rx=min_rx, multiplier=multiplier)
	return result

def deserialize_Bfd__interval_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	interval = data.get('interval')
	min_rx_cfg = deserialize_Bfd__interval_cfg__min_rx_cfg_json(data.get('min-rx-cfg'))
	result = Bfd__interval_cfg(interval=interval, min_rx_cfg=min_rx_cfg)
	return result

def deserialize_Bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	echo = data.get('echo')
	enable = data.get('enable')
	interval_cfg = deserialize_Bfd__interval_cfg_json(data.get('interval-cfg'))
	result = Bfd(echo=echo, enable=enable, interval_cfg=interval_cfg)
	return result

def serialize_Bfd__interval_cfg__min_rx_cfg_json(obj):
	output = OrderedDict()
	if obj.min_rx is not None:
		output['min-rx'] = obj.min_rx
	if obj.multiplier is not None:
		output['multiplier'] = obj.multiplier
	return output

def serialize_Bfd__interval_cfg_json(obj):
	output = OrderedDict()
	if obj.interval is not None:
		output['interval'] = obj.interval
	if obj.min_rx_cfg is not None:
		output['min-rx-cfg'] = serialize_Bfd__interval_cfg__min_rx_cfg_json(obj.min_rx_cfg)
	return output

def serialize_Bfd_json(obj):
	output = OrderedDict()
	if obj.echo is not None:
		output['echo'] = obj.echo
	if obj.enable is not None:
		output['enable'] = obj.enable
	if obj.interval_cfg is not None:
		output['interval-cfg'] = serialize_Bfd__interval_cfg_json(obj.interval_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Bfd_json(item))
	return list(container)

class Bfd__interval_cfg__min_rx_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	min_rx=PosRangedInteger(48, 1000)
	multiplier=PosRangedInteger(3, 50)
	def __init__(self, min_rx=None, multiplier=None):
		self.min_rx = min_rx
		self.multiplier = multiplier

	def __str__(self):
		return ""

class Bfd__interval_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	interval=PosRangedInteger(48, 1000)
	def __init__(self, interval=None, min_rx_cfg=None):
		self.interval = interval
		self.min_rx_cfg = min_rx_cfg

	def __str__(self):
		return ""

class Bfd(AxapiObject):
	__metaclass__ = StructMeta 
	echo=PosRangedInteger(0, 1)
	enable=PosRangedInteger(0, 1)
	def __init__(self, echo=None, enable=None, interval_cfg=None):
		self.echo = echo
		self.enable = enable
		self.interval_cfg = interval_cfg

	def __str__(self):
		return ""

class BfdClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getBfd(self):
		"""
		Retrieve the bfd identified by the specified identifier
		
		Returns:
			An instance of the Bfd class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bfd does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('bfd')
		return deserialize_Bfd_json(payload)

	def putBfd(self, bfd):
		"""
		Replace the object bfd
		
		Args:
			bfd An instance of the Bfd class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bfd']=serialize_Bfd_json(bfd)
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

	def deleteBfd(self):
		"""
		Remove the bfd identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bfd does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllBfdsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitBfd(self, bfd):
		"""
		Create the object bfd
		
		Args:
			bfd An instance of the Bfd class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bfd']=serialize_Bfd_json(bfd)
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

	def getAllBfds(self):
		"""
		Retrieve all bfd objects currently pending in the system
		
		Returns:
			A list of Bfd objects
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
			payload= data.get('bfdList')
		return deserialize_list_Bfd_json(payload)

