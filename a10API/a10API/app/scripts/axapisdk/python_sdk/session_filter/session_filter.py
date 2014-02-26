########################################################################################################################
# File name: session_filter.py
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
	'https://axapi.a10networks.com/axapi/v3/session-filter',
]

def deserialize_Session_filter_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	ipv6 = data.get('ipv6')
	sip = data.get('sip')
	source_addr = data.get('source-addr')
	source_port = data.get('source-port')
	dest_addr = data.get('dest-addr')
	dport1 = data.get('dport1')
	dest_mask = data.get('dest-mask')
	dport2 = data.get('dport2')
	result = Session_filter(name=name, ipv6=ipv6, sip=sip, source_addr=source_addr, source_port=source_port, dest_addr=dest_addr, dport1=dport1, dest_mask=dest_mask, dport2=dport2)
	return result

def serialize_Session_filter_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	if obj.ipv6 is not None:
		output['ipv6'] = obj.ipv6
	if obj.sip is not None:
		output['sip'] = obj.sip
	if obj.source_addr is not None:
		output['source-addr'] = obj.source_addr
	if obj.source_port is not None:
		output['source-port'] = obj.source_port
	if obj.dest_addr is not None:
		output['dest-addr'] = obj.dest_addr
	if obj.dport1 is not None:
		output['dport1'] = obj.dport1
	if obj.dest_mask is not None:
		output['dest-mask'] = obj.dest_mask
	if obj.dport2 is not None:
		output['dport2'] = obj.dport2
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Session_filter_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Session_filter_json(item))
	return list(container)

class Session_filter(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 31)
	ipv6=PosRangedInteger(0, 1)
	sip=PosRangedInteger(0, 1)
	source_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	source_port=PosRangedInteger(1, 65535)
	dest_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	dport1=PosRangedInteger(1, 65535)
	dest_mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	dport2=PosRangedInteger(1, 65535)
	def __init__(self, name=None, ipv6=None, sip=None, source_addr=None, source_port=None, dest_addr=None, dport1=None, dest_mask=None, dport2=None):
		self.name = name
		self.ipv6 = ipv6
		self.sip = sip
		self.source_addr = source_addr
		self.source_port = source_port
		self.dest_addr = dest_addr
		self.dport1 = dport1
		self.dest_mask = dest_mask
		self.dport2 = dport2

	def __str__(self):
		return ""

class SessionfilterClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSessionfilter(self):
		"""
		Retrieve the session_filter identified by the specified identifier
		
		Returns:
			An instance of the Session_filter class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified session_filter does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('session-filter')
		return deserialize_Session_filter_json(payload)

	def putSessionfilter(self, session_filter):
		"""
		Replace the object session_filter
		
		Args:
			session_filter An instance of the Session_filter class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['session-filter']=serialize_Session_filter_json(session_filter)
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

	def deleteSessionfilter(self):
		"""
		Remove the session_filter identified by the specified identifier from the
		system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified session_filter does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSessionfiltersClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSessionfilter(self, session_filter):
		"""
		Create the object session_filter
		
		Args:
			session_filter An instance of the Session_filter class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['session-filter']=serialize_Session_filter_json(session_filter)
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

	def getAllSessionfilters(self):
		"""
		Retrieve all session_filter objects currently pending in the system
		
		Returns:
			A list of Session_filter objects
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
			payload= data.get('session-filterList')
		return deserialize_list_Session_filter_json(payload)

