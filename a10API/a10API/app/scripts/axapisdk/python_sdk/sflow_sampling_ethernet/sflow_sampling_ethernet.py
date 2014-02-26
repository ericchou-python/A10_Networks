########################################################################################################################
# File name: sflow_sampling_ethernet.py
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
	'https://axapi.a10networks.com/axapi/v3/sflow/sampling/ethernet',
]

def deserialize_Ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	start = data.get('start')
	rate = data.get('rate')
	result = Ethernet(start=start, rate=rate)
	return result

def serialize_Ethernet_json(obj):
	output = OrderedDict()
	output['start'] = obj.start
	if obj.rate is not None:
		output['rate'] = obj.rate
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ethernet_json(item))
	return list(container)

class Ethernet_start(AxapiObject):
	__metaclass__ = StructMeta 
	start=PosRangedInteger(1, 2048)
	def __init__(self, start):
		self.start = start

	def __str__(self):
		return str(self.start)

class Ethernet(AxapiObject):
	__metaclass__ = StructMeta 
	start=PosRangedInteger(1, 2048)
	rate=PosRangedInteger(10, 1000000)
	def __init__(self, start, rate=None):
		self.start = start
		self.rate = rate

	def __str__(self):
		return str(self.start)

class SflowSamplingEthernetClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSflowSamplingEthernet(self, ethernet_start):
		"""
		Retrieve the ethernet identified by the specified identifier
		
		Args:
			ethernet_start Ethernet_start
		
		Returns:
			An instance of the Ethernet class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(ethernet_start) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ethernet does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ethernet')
		return deserialize_Ethernet_json(payload)

	def putSflowSamplingEthernet(self, ethernet_start, ethernet):
		"""
		Replace the object ethernet
		
		Args:
			ethernet_start Ethernet_start
			ethernet An instance of the Ethernet class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ethernet']=serialize_Ethernet_json(ethernet)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(ethernet_start) .replace("/", "%2f") + query, payload, headers)
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

	def deleteSflowSamplingEthernet(self, ethernet_start):
		"""
		Remove the ethernet identified by the specified identifier from the system
		
		Args:
			ethernet_start Ethernet_start
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(ethernet_start) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ethernet does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSflowSamplingEthernetsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSflowSamplingEthernet(self, ethernet):
		"""
		Create the object ethernet
		
		Args:
			ethernet An instance of the Ethernet class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ethernet']=serialize_Ethernet_json(ethernet)
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

	def getAllSflowSamplingEthernets(self):
		"""
		Retrieve all ethernet objects currently pending in the system
		
		Returns:
			A list of Ethernet objects
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
			payload= data.get('ethernetList')
		return deserialize_list_Ethernet_json(payload)

