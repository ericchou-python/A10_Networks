########################################################################################################################
# File name: ipv6_route_static_bfd_trunk.py
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
	'https://axapi.a10networks.com/axapi/v3/ipv6/route/static/bfd/trunk',
]

def deserialize_Trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk_num = data.get('trunk-num')
	nexthop_ipv6_ll = data.get('nexthop-ipv6-ll')
	result = Trunk(trunk_num=trunk_num, nexthop_ipv6_ll=nexthop_ipv6_ll)
	return result

def serialize_Trunk_json(obj):
	output = OrderedDict()
	output['trunk-num'] = obj.trunk_num
	output['nexthop-ipv6-ll'] = obj.nexthop_ipv6_ll
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Trunk_json(item))
	return list(container)

class Trunk_trunk_num_nexthop_ipv6_ll(AxapiObject):
	__metaclass__ = StructMeta 
	trunk_num=PosInteger()
	nexthop_ipv6_ll=SizedString(1, 255)
	def __init__(self, trunk_num, nexthop_ipv6_ll):
		self.trunk_num = trunk_num
		self.nexthop_ipv6_ll = nexthop_ipv6_ll

	def __str__(self):
		return str(self.trunk_num) + '+' + str(self.nexthop_ipv6_ll)

class Trunk(AxapiObject):
	__metaclass__ = StructMeta 
	trunk_num=PosInteger()
	nexthop_ipv6_ll=SizedString(1, 255)
	def __init__(self, trunk_num, nexthop_ipv6_ll):
		self.trunk_num = trunk_num
		self.nexthop_ipv6_ll = nexthop_ipv6_ll

	def __str__(self):
		return str(self.trunk_num) + '+' + str(self.nexthop_ipv6_ll)

class Ipv6RouteStaticBfdTrunkClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpv6RouteStaticBfdTrunk(self, trunk_trunk_num_nexthop_ipv6_ll):
		"""
		Retrieve the trunk identified by the specified identifier
		
		Args:
			trunk_trunk_num_nexthop_ipv6_ll Trunk_trunk_num_nexthop_ipv6_ll
		
		Returns:
			An instance of the Trunk class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(trunk_trunk_num_nexthop_ipv6_ll) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified trunk does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('trunk')
		return deserialize_Trunk_json(payload)

	def putIpv6RouteStaticBfdTrunk(self, trunk_trunk_num_nexthop_ipv6_ll, trunk):
		"""
		Replace the object trunk
		
		Args:
			trunk_trunk_num_nexthop_ipv6_ll Trunk_trunk_num_nexthop_ipv6_ll
			trunk An instance of the Trunk class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['trunk']=serialize_Trunk_json(trunk)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(trunk_trunk_num_nexthop_ipv6_ll) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpv6RouteStaticBfdTrunk(self, trunk_trunk_num_nexthop_ipv6_ll):
		"""
		Remove the trunk identified by the specified identifier from the system
		
		Args:
			trunk_trunk_num_nexthop_ipv6_ll Trunk_trunk_num_nexthop_ipv6_ll
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(trunk_trunk_num_nexthop_ipv6_ll) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified trunk does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpv6RouteStaticBfdTrunksClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpv6RouteStaticBfdTrunk(self, trunk):
		"""
		Create the object trunk
		
		Args:
			trunk An instance of the Trunk class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['trunk']=serialize_Trunk_json(trunk)
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

	def getAllIpv6RouteStaticBfdTrunks(self):
		"""
		Retrieve all trunk objects currently pending in the system
		
		Returns:
			A list of Trunk objects
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
			payload= data.get('trunkList')
		return deserialize_list_Trunk_json(payload)

