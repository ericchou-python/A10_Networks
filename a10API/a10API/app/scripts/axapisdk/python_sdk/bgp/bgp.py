########################################################################################################################
# File name: bgp.py
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
	'https://axapi.a10networks.com/axapi/v3/bgp',
]

def deserialize_Bgp__nexthop_trigger_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable = data.get('enable')
	delay = data.get('delay')
	result = Bgp__nexthop_trigger(enable=enable, delay=delay)
	return result

def deserialize_Bgp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	extended_asn_cap = data.get('extended-asn-cap')
	nexthop_trigger = deserialize_Bgp__nexthop_trigger_json(data.get('nexthop-trigger'))
	result = Bgp(extended_asn_cap=extended_asn_cap, nexthop_trigger=nexthop_trigger)
	return result

def serialize_Bgp__nexthop_trigger_json(obj):
	output = OrderedDict()
	if obj.enable is not None:
		output['enable'] = obj.enable
	if obj.delay is not None:
		output['delay'] = obj.delay
	return output

def serialize_Bgp_json(obj):
	output = OrderedDict()
	if obj.extended_asn_cap is not None:
		output['extended-asn-cap'] = obj.extended_asn_cap
	if obj.nexthop_trigger is not None:
		output['nexthop-trigger'] = serialize_Bgp__nexthop_trigger_json(obj.nexthop_trigger)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Bgp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Bgp_json(item))
	return list(container)

class Bgp__nexthop_trigger(AxapiObject):
	__metaclass__ = StructMeta 
	enable=PosRangedInteger(0, 1)
	delay=PosRangedInteger(1, 100)
	def __init__(self, enable=None, delay=None):
		self.enable = enable
		self.delay = delay

	def __str__(self):
		return ""

class Bgp(AxapiObject):
	__metaclass__ = StructMeta 
	extended_asn_cap=PosRangedInteger(0, 1)
	def __init__(self, extended_asn_cap=None, nexthop_trigger=None):
		self.extended_asn_cap = extended_asn_cap
		self.nexthop_trigger = nexthop_trigger

	def __str__(self):
		return ""

class BgpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getBgp(self):
		"""
		Retrieve the bgp identified by the specified identifier
		
		Returns:
			An instance of the Bgp class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bgp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('bgp')
		return deserialize_Bgp_json(payload)

	def putBgp(self, bgp):
		"""
		Replace the object bgp
		
		Args:
			bgp An instance of the Bgp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bgp']=serialize_Bgp_json(bgp)
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

	def deleteBgp(self):
		"""
		Remove the bgp identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bgp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllBgpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitBgp(self, bgp):
		"""
		Create the object bgp
		
		Args:
			bgp An instance of the Bgp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bgp']=serialize_Bgp_json(bgp)
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

	def getAllBgps(self):
		"""
		Retrieve all bgp objects currently pending in the system
		
		Returns:
			A list of Bgp objects
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
			payload= data.get('bgpList')
		return deserialize_list_Bgp_json(payload)

