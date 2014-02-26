########################################################################################################################
# File name: ddos_geo_location_load.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/geo-location/load',
]

def deserialize_Ddos_geo_location_load_load_file_config_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	load_file_name = data.get('load-file-name')
	result = Ddos_geo_location_load_load_file_config(load_file_name=load_file_name)
	return result

def deserialize_list_Ddos_geo_location_load_load_file_config_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_geo_location_load_load_file_config_json(item))
	return list(container)

def deserialize_Load_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	load_file_config = deserialize_list_Ddos_geo_location_load_load_file_config_json(data.get('load-file-config'))
	iana = data.get('iana')
	result = Load(load_file_config=load_file_config, iana=iana)
	return result

def serialize_Ddos_geo_location_load_load_file_config_json(obj):
	output = OrderedDict()
	if obj.load_file_name is not None:
		output['load-file-name'] = obj.load_file_name
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ddos_geo_location_load_load_file_config_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_geo_location_load_load_file_config_json(item))
	return output

def serialize_Load_json(obj):
	output = OrderedDict()
	if obj.load_file_config is not None:
		output['load-file-config'] = serialize_list_Ddos_geo_location_load_load_file_config_json(obj.load_file_config)
	if obj.iana is not None:
		output['iana'] = obj.iana
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Load_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Load_json(item))
	return list(container)

class Load(AxapiObject):
	__metaclass__ = StructMeta 
	iana=PosRangedInteger(0, 1)
	def __init__(self, load_file_config=None, iana=None):
		self.load_file_config = load_file_config
		self.iana = iana

	def __str__(self):
		return ""

class Ddos_geo_location_load_load_file_config(AxapiObject):
	__metaclass__ = StructMeta 
	load_file_name=SizedString(1, 255)
	def __init__(self, load_file_name=None):
		self.load_file_name = load_file_name

	def __str__(self):
		return ""

class DdosGeolocationLoadClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosGeolocationLoad(self):
		"""
		Retrieve the load identified by the specified identifier
		
		Returns:
			An instance of the Load class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified load does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('load')
		return deserialize_Load_json(payload)

	def putDdosGeolocationLoad(self, load):
		"""
		Replace the object load
		
		Args:
			load An instance of the Load class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['load']=serialize_Load_json(load)
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

	def deleteDdosGeolocationLoad(self):
		"""
		Remove the load identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified load does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosGeolocationLoadsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosGeolocationLoad(self, load):
		"""
		Create the object load
		
		Args:
			load An instance of the Load class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['load']=serialize_Load_json(load)
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

	def getAllDdosGeolocationLoads(self):
		"""
		Retrieve all load objects currently pending in the system
		
		Returns:
			A list of Load objects
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
			payload= data.get('loadList')
		return deserialize_list_Load_json(payload)

