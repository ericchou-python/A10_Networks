########################################################################################################################
# File name: enable_management_service_https.py
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
	'https://axapi.a10networks.com/axapi/v3/enable-management/service/https',
]

def deserialize_Enable_management_service_https_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet_start = data.get('ethernet-start')
	ethernet_end = data.get('ethernet-end')
	result = Enable_management_service_https_eth_cfg(ethernet_start=ethernet_start, ethernet_end=ethernet_end)
	return result

def deserialize_list_Enable_management_service_https_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Enable_management_service_https_eth_cfg_json(item))
	return list(container)

def deserialize_Enable_management_service_https_ve_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ve_start = data.get('ve-start')
	ve_end = data.get('ve-end')
	result = Enable_management_service_https_ve_cfg(ve_start=ve_start, ve_end=ve_end)
	return result

def deserialize_list_Enable_management_service_https_ve_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Enable_management_service_https_ve_cfg_json(item))
	return list(container)

def deserialize_Https_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	eth_cfg = deserialize_list_Enable_management_service_https_eth_cfg_json(data.get('eth-cfg'))
	ve_cfg = deserialize_list_Enable_management_service_https_ve_cfg_json(data.get('ve-cfg'))
	result = Https(eth_cfg=eth_cfg, ve_cfg=ve_cfg)
	return result

def serialize_Enable_management_service_https_eth_cfg_json(obj):
	output = OrderedDict()
	if obj.ethernet_start is not None:
		output['ethernet-start'] = obj.ethernet_start
	if obj.ethernet_end is not None:
		output['ethernet-end'] = obj.ethernet_end
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Enable_management_service_https_eth_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Enable_management_service_https_eth_cfg_json(item))
	return output

def serialize_Enable_management_service_https_ve_cfg_json(obj):
	output = OrderedDict()
	if obj.ve_start is not None:
		output['ve-start'] = obj.ve_start
	if obj.ve_end is not None:
		output['ve-end'] = obj.ve_end
	return output

def serialize_list_Enable_management_service_https_ve_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Enable_management_service_https_ve_cfg_json(item))
	return output

def serialize_Https_json(obj):
	output = OrderedDict()
	if obj.eth_cfg is not None:
		output['eth-cfg'] = serialize_list_Enable_management_service_https_eth_cfg_json(obj.eth_cfg)
	if obj.ve_cfg is not None:
		output['ve-cfg'] = serialize_list_Enable_management_service_https_ve_cfg_json(obj.ve_cfg)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Https_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Https_json(item))
	return list(container)

class Https(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, eth_cfg=None, ve_cfg=None):
		self.eth_cfg = eth_cfg
		self.ve_cfg = ve_cfg

	def __str__(self):
		return ""

class Enable_management_service_https_eth_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet_start=PosRangedInteger(1, 2048)
	ethernet_end=PosRangedInteger(1, 2048)
	def __init__(self, ethernet_start=None, ethernet_end=None):
		self.ethernet_start = ethernet_start
		self.ethernet_end = ethernet_end

	def __str__(self):
		return ""

class Enable_management_service_https_ve_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ve_start=PosRangedInteger(1, 4094)
	ve_end=PosRangedInteger(1, 4094)
	def __init__(self, ve_start=None, ve_end=None):
		self.ve_start = ve_start
		self.ve_end = ve_end

	def __str__(self):
		return ""

class EnablemanagementServiceHttpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getEnablemanagementServiceHttps(self):
		"""
		Retrieve the https identified by the specified identifier
		
		Returns:
			An instance of the Https class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified https does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('https')
		return deserialize_Https_json(payload)

	def putEnablemanagementServiceHttps(self, https):
		"""
		Replace the object https
		
		Args:
			https An instance of the Https class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['https']=serialize_Https_json(https)
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

	def deleteEnablemanagementServiceHttps(self):
		"""
		Remove the https identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified https does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllEnablemanagementServiceHttpssClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitEnablemanagementServiceHttps(self, https):
		"""
		Create the object https
		
		Args:
			https An instance of the Https class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['https']=serialize_Https_json(https)
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

	def getAllEnablemanagementServiceHttpss(self):
		"""
		Retrieve all https objects currently pending in the system
		
		Returns:
			A list of Https objects
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
			payload= data.get('httpsList')
		return deserialize_list_Https_json(payload)

