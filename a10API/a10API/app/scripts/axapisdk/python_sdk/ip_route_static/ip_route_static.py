########################################################################################################################
# File name: ip_route_static.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/route/static',
]

def deserialize_Ip_route_static_bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_ip = data.get('local-ip')
	nexthop_ip = data.get('nexthop-ip')
	result = Ip_route_static_bfd(local_ip=local_ip, nexthop_ip=nexthop_ip)
	return result

def deserialize_list_Ip_route_static_bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_route_static_bfd_json(item))
	return list(container)

def deserialize_Static_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bfdlist = deserialize_list_Ip_route_static_bfd_json(data.get('bfdList'))
	result = Static(bfdlist=bfdlist)
	return result

class Static(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, bfdlist=None):
		self.bfdlist = bfdlist

	def __str__(self):
		return ""

class Ip_route_static_bfd(AxapiObject):
	__metaclass__ = StructMeta 
	local_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	nexthop_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, local_ip, nexthop_ip):
		self.local_ip = local_ip
		self.nexthop_ip = nexthop_ip

	def __str__(self):
		return str(self.local_ip) + '+' + str(self.nexthop_ip)

class IpRouteStaticClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpRouteStatic(self):
		"""
		Retrieve the static identified by the specified identifier
		
		Returns:
			An instance of the Static class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified static does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('static')
		return deserialize_Static_json(payload)

