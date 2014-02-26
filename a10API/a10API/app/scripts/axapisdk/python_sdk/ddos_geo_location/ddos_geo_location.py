########################################################################################################################
# File name: ddos_geo_location.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/geo-location',
]

def deserialize_Ddos_geo_location_load_file_config_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	load_file_name = data.get('load-file-name')
	result = Ddos_geo_location_load_file_config(load_file_name=load_file_name)
	return result

def deserialize_list_Ddos_geo_location_load_file_config_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_geo_location_load_file_config_json(item))
	return list(container)

def deserialize_Geo_location__load_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	load_file_config = deserialize_list_Ddos_geo_location_load_file_config_json(data.get('load-file-config'))
	iana = data.get('iana')
	result = Geo_location__load(load_file_config=load_file_config, iana=iana)
	return result

def deserialize_Geo_location__delete_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	delete_file_name = data.get('delete-file-name')
	delete_all = data.get('delete-all')
	result = Geo_location__delete(delete_file_name=delete_file_name, delete_all=delete_all)
	return result

def deserialize_Geo_location_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	load = deserialize_Geo_location__load_json(data.get('load'))
	delete = deserialize_Geo_location__delete_json(data.get('delete'))
	result = Geo_location(load=load, delete=delete)
	return result

class Geo_location__load(AxapiObject):
	__metaclass__ = StructMeta 
	iana=PosRangedInteger(0, 1)
	def __init__(self, load_file_config=None, iana=None):
		self.load_file_config = load_file_config
		self.iana = iana

	def __str__(self):
		return ""

class Geo_location__delete(AxapiObject):
	__metaclass__ = StructMeta 
	delete_file_name=SizedString(1, 255)
	delete_all=PosRangedInteger(0, 1)
	def __init__(self, delete_file_name=None, delete_all=None):
		self.delete_file_name = delete_file_name
		self.delete_all = delete_all

	def __str__(self):
		return ""

class Geo_location(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, load=None, delete=None):
		self.load = load
		self.delete = delete

	def __str__(self):
		return ""

class Ddos_geo_location_load_file_config(AxapiObject):
	__metaclass__ = StructMeta 
	load_file_name=SizedString(1, 255)
	def __init__(self, load_file_name=None):
		self.load_file_name = load_file_name

	def __str__(self):
		return ""

class DdosGeolocationClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosGeolocation(self):
		"""
		Retrieve the geo_location identified by the specified identifier
		
		Returns:
			An instance of the Geo_location class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified geo_location does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('geo-location')
		return deserialize_Geo_location_json(payload)

