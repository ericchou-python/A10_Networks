########################################################################################################################
# File name: bootimage.py
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
	'https://axapi.a10networks.com/axapi/v3/bootimage',
]

def deserialize_Bootimage__cf_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	cf = data.get('cf')
	pri = data.get('pri')
	result = Bootimage__cf_cfg(cf=cf, pri=pri)
	return result

def deserialize_Bootimage__hd_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	hd = data.get('hd')
	pri = data.get('pri')
	sec = data.get('sec')
	result = Bootimage__hd_cfg(hd=hd, pri=pri, sec=sec)
	return result

def deserialize_Bootimage_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	cf_cfg = deserialize_Bootimage__cf_cfg_json(data.get('cf-cfg'))
	hd_cfg = deserialize_Bootimage__hd_cfg_json(data.get('hd-cfg'))
	result = Bootimage(cf_cfg=cf_cfg, hd_cfg=hd_cfg)
	return result

def serialize_Bootimage__cf_cfg_json(obj):
	output = OrderedDict()
	if obj.cf is not None:
		output['cf'] = obj.cf
	if obj.pri is not None:
		output['pri'] = obj.pri
	return output

def serialize_Bootimage__hd_cfg_json(obj):
	output = OrderedDict()
	if obj.hd is not None:
		output['hd'] = obj.hd
	if obj.pri is not None:
		output['pri'] = obj.pri
	if obj.sec is not None:
		output['sec'] = obj.sec
	return output

def serialize_Bootimage_json(obj):
	output = OrderedDict()
	if obj.cf_cfg is not None:
		output['cf-cfg'] = serialize_Bootimage__cf_cfg_json(obj.cf_cfg)
	if obj.hd_cfg is not None:
		output['hd-cfg'] = serialize_Bootimage__hd_cfg_json(obj.hd_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Bootimage_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Bootimage_json(item))
	return list(container)

class Bootimage__cf_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	cf=PosRangedInteger(0, 1)
	pri=PosRangedInteger(0, 1)
	def __init__(self, cf=None, pri=None):
		self.cf = cf
		self.pri = pri

	def __str__(self):
		return ""

class Bootimage__hd_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	hd=PosRangedInteger(0, 1)
	pri=PosInteger()
	sec=PosRangedInteger(0, 1)
	def __init__(self, hd=None, pri=None, sec=None):
		self.hd = hd
		self.pri = pri
		self.sec = sec

	def __str__(self):
		return ""

class Bootimage(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, cf_cfg=None, hd_cfg=None):
		self.cf_cfg = cf_cfg
		self.hd_cfg = hd_cfg

	def __str__(self):
		return ""

class BootimageClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getBootimage(self):
		"""
		Retrieve the bootimage identified by the specified identifier
		
		Returns:
			An instance of the Bootimage class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bootimage does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('bootimage')
		return deserialize_Bootimage_json(payload)

	def putBootimage(self, bootimage):
		"""
		Replace the object bootimage
		
		Args:
			bootimage An instance of the Bootimage class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bootimage']=serialize_Bootimage_json(bootimage)
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

	def deleteBootimage(self):
		"""
		Remove the bootimage identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bootimage does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllBootimagesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitBootimage(self, bootimage):
		"""
		Create the object bootimage
		
		Args:
			bootimage An instance of the Bootimage class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bootimage']=serialize_Bootimage_json(bootimage)
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

	def getAllBootimages(self):
		"""
		Retrieve all bootimage objects currently pending in the system
		
		Returns:
			A list of Bootimage objects
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
			payload= data.get('bootimageList')
		return deserialize_list_Bootimage_json(payload)

