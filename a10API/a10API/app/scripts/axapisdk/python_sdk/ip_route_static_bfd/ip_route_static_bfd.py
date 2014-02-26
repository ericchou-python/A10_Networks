########################################################################################################################
# File name: ip_route_static_bfd.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/route/static/bfd',
]

def deserialize_Bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_ip = data.get('local-ip')
	nexthop_ip = data.get('nexthop-ip')
	result = Bfd(local_ip=local_ip, nexthop_ip=nexthop_ip)
	return result

def serialize_Bfd_json(obj):
	output = OrderedDict()
	output['local-ip'] = obj.local_ip
	output['nexthop-ip'] = obj.nexthop_ip
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

class Bfd_local_ip_nexthop_ip(AxapiObject):
	__metaclass__ = StructMeta 
	local_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	nexthop_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, local_ip, nexthop_ip):
		self.local_ip = local_ip
		self.nexthop_ip = nexthop_ip

	def __str__(self):
		return str(self.local_ip) + '+' + str(self.nexthop_ip)

class Bfd(AxapiObject):
	__metaclass__ = StructMeta 
	local_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	nexthop_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, local_ip, nexthop_ip):
		self.local_ip = local_ip
		self.nexthop_ip = nexthop_ip

	def __str__(self):
		return str(self.local_ip) + '+' + str(self.nexthop_ip)

class IpRouteStaticBfdClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpRouteStaticBfd(self, bfd_local_ip_nexthop_ip):
		"""
		Retrieve the bfd identified by the specified identifier
		
		Args:
			bfd_local_ip_nexthop_ip Bfd_local_ip_nexthop_ip
		
		Returns:
			An instance of the Bfd class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(bfd_local_ip_nexthop_ip) .replace("/", "%2f") + query, headers=headers)
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

	def putIpRouteStaticBfd(self, bfd_local_ip_nexthop_ip, bfd):
		"""
		Replace the object bfd
		
		Args:
			bfd_local_ip_nexthop_ip Bfd_local_ip_nexthop_ip
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
		conn.request('PUT', self.get_path() + '/' + str(bfd_local_ip_nexthop_ip) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpRouteStaticBfd(self, bfd_local_ip_nexthop_ip):
		"""
		Remove the bfd identified by the specified identifier from the system
		
		Args:
			bfd_local_ip_nexthop_ip Bfd_local_ip_nexthop_ip
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(bfd_local_ip_nexthop_ip) .replace("/", "%2f") + query, headers=headers)
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

class AllIpRouteStaticBfdsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpRouteStaticBfd(self, bfd):
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

	def getAllIpRouteStaticBfds(self):
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

