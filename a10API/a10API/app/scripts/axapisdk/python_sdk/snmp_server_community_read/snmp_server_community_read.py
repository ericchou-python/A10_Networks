########################################################################################################################
# File name: snmp_server_community_read.py
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
	'https://axapi.a10networks.com/axapi/v3/snmp-server/community/read',
]

def deserialize_Read_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	user = data.get('user')
	oid = data.get('oid')
	remote = data.get('remote')
	ipv4_mask = data.get('ipv4-mask')
	result = Read(user=user, oid=oid, remote=remote, ipv4_mask=ipv4_mask)
	return result

def serialize_Read_json(obj):
	output = OrderedDict()
	output['user'] = obj.user
	if obj.oid is not None:
		output['oid'] = obj.oid
	if obj.remote is not None:
		output['remote'] = obj.remote
	if obj.ipv4_mask is not None:
		output['ipv4-mask'] = obj.ipv4_mask
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Read_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Read_json(item))
	return list(container)

class Read_user(AxapiObject):
	__metaclass__ = StructMeta 
	user=SizedString(1, 31)
	def __init__(self, user):
		self.user = user

	def __str__(self):
		return str(self.user)

class Read(AxapiObject):
	__metaclass__ = StructMeta 
	user=SizedString(1, 31)
	oid=PosRangedInteger(0, 1)
	remote = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv4_mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, user, oid=None, remote=None, ipv4_mask=None):
		self.user = user
		self.oid = oid
		self.remote = remote
		self.ipv4_mask = ipv4_mask

	def __str__(self):
		return str(self.user)

class SnmpserverCommunityReadClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSnmpserverCommunityRead(self, read_user):
		"""
		Retrieve the read identified by the specified identifier
		
		Args:
			read_user Read_user
		
		Returns:
			An instance of the Read class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(read_user) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified read does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('read')
		return deserialize_Read_json(payload)

	def putSnmpserverCommunityRead(self, read_user, read):
		"""
		Replace the object read
		
		Args:
			read_user Read_user
			read An instance of the Read class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['read']=serialize_Read_json(read)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(read_user) .replace("/", "%2f") + query, payload, headers)
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

	def deleteSnmpserverCommunityRead(self, read_user):
		"""
		Remove the read identified by the specified identifier from the system
		
		Args:
			read_user Read_user
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(read_user) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified read does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSnmpserverCommunityReadsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSnmpserverCommunityRead(self, read):
		"""
		Create the object read
		
		Args:
			read An instance of the Read class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['read']=serialize_Read_json(read)
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

	def getAllSnmpserverCommunityReads(self):
		"""
		Retrieve all read objects currently pending in the system
		
		Returns:
			A list of Read objects
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
			payload= data.get('readList')
		return deserialize_list_Read_json(payload)

