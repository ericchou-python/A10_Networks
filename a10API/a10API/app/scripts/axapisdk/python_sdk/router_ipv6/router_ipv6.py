########################################################################################################################
# File name: router_ipv6.py
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
	'https://axapi.a10networks.com/axapi/v3/router/ipv6',
]

def deserialize_Router_ipv6_ospf_area_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	result = Router_ipv6_ospf_area()
	return result

def deserialize_list_Router_ipv6_ospf_area_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_ipv6_ospf_area_json(item))
	return list(container)

def deserialize_Router_ipv6_ospf__redistribute_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	result = Router_ipv6_ospf__redistribute()
	return result

def deserialize_Router_ipv6_ospf_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	arealist = deserialize_list_Router_ipv6_ospf_area_json(data.get('areaList'))
	redistribute = deserialize_Router_ipv6_ospf__redistribute_json(data.get('redistribute'))
	result = Router_ipv6_ospf(arealist=arealist, redistribute=redistribute)
	return result

def deserialize_list_Router_ipv6_ospf_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_ipv6_ospf_json(item))
	return list(container)

def deserialize_Ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ospflist = deserialize_list_Router_ipv6_ospf_json(data.get('ospfList'))
	result = Ipv6(ospflist=ospflist)
	return result

class Ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ospflist=None):
		self.ospflist = ospflist

	def __str__(self):
		return ""

class Router_ipv6_ospf__redistribute(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class Router_ipv6_ospf(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, arealist=None, redistribute=None):
		self.arealist = arealist
		self.redistribute = redistribute

	def __str__(self):
		return ""

class Router_ipv6_ospf_area(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class RouterIpv6Client(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRouterIpv6(self):
		"""
		Retrieve the ipv6 identified by the specified identifier
		
		Returns:
			An instance of the Ipv6 class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ipv6 does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ipv6')
		return deserialize_Ipv6_json(payload)

