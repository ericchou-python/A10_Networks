########################################################################################################################
# File name: ddos_use_default_route.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/use-default-route',
]

def deserialize_Ddos_use_default_route_ethernet_start_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet_start = data.get('ethernet-start')
	ethernet_end = data.get('ethernet-end')
	result = Ddos_use_default_route_ethernet_start_cfg(ethernet_start=ethernet_start, ethernet_end=ethernet_end)
	return result

def deserialize_list_Ddos_use_default_route_ethernet_start_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_use_default_route_ethernet_start_cfg_json(item))
	return list(container)

def deserialize_Use_default_route_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet_start_cfg = deserialize_list_Ddos_use_default_route_ethernet_start_cfg_json(data.get('ethernet-start-cfg'))
	result = Use_default_route(ethernet_start_cfg=ethernet_start_cfg)
	return result

def serialize_Ddos_use_default_route_ethernet_start_cfg_json(obj):
	output = OrderedDict()
	if obj.ethernet_start is not None:
		output['ethernet-start'] = obj.ethernet_start
	if obj.ethernet_end is not None:
		output['ethernet-end'] = obj.ethernet_end
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ddos_use_default_route_ethernet_start_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_use_default_route_ethernet_start_cfg_json(item))
	return output

def serialize_Use_default_route_json(obj):
	output = OrderedDict()
	if obj.ethernet_start_cfg is not None:
		output['ethernet-start-cfg'] = serialize_list_Ddos_use_default_route_ethernet_start_cfg_json(obj.ethernet_start_cfg)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Use_default_route_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Use_default_route_json(item))
	return list(container)

class Use_default_route(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ethernet_start_cfg=None):
		self.ethernet_start_cfg = ethernet_start_cfg

	def __str__(self):
		return ""

class Ddos_use_default_route_ethernet_start_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet_start=PosRangedInteger(1, 2048)
	ethernet_end=PosRangedInteger(1, 2048)
	def __init__(self, ethernet_start=None, ethernet_end=None):
		self.ethernet_start = ethernet_start
		self.ethernet_end = ethernet_end

	def __str__(self):
		return ""

class DdosUsedefaultrouteClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosUsedefaultroute(self):
		"""
		Retrieve the use_default_route identified by the specified identifier
		
		Returns:
			An instance of the Use_default_route class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified use_default_route does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('use-default-route')
		return deserialize_Use_default_route_json(payload)

	def putDdosUsedefaultroute(self, use_default_route):
		"""
		Replace the object use_default_route
		
		Args:
			use_default_route An instance of the Use_default_route class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['use-default-route']=serialize_Use_default_route_json(use_default_route)
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

	def deleteDdosUsedefaultroute(self):
		"""
		Remove the use_default_route identified by the specified identifier from
		the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified use_default_route does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosUsedefaultroutesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosUsedefaultroute(self, use_default_route):
		"""
		Create the object use_default_route
		
		Args:
			use_default_route An instance of the Use_default_route class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['use-default-route']=serialize_Use_default_route_json(use_default_route)
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

	def getAllDdosUsedefaultroutes(self):
		"""
		Retrieve all use_default_route objects currently pending in the system
		
		Returns:
			A list of Use_default_route objects
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
			payload= data.get('use-default-routeList')
		return deserialize_list_Use_default_route_json(payload)

