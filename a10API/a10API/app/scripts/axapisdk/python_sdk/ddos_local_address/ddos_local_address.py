########################################################################################################################
# File name: ddos_local_address.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/local-address',
]

def deserialize_Ddos_local_address_ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_addr = data.get('ip-addr')
	result = Ddos_local_address_ip(ip_addr=ip_addr)
	return result

def deserialize_list_Ddos_local_address_ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_local_address_ip_json(item))
	return list(container)

def deserialize_Ddos_local_address_ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	result = Ddos_local_address_ipv6(ipv6_addr=ipv6_addr)
	return result

def deserialize_list_Ddos_local_address_ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_local_address_ipv6_json(item))
	return list(container)

def deserialize_Local_address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	iplist = deserialize_list_Ddos_local_address_ip_json(data.get('ipList'))
	ipv6list = deserialize_list_Ddos_local_address_ipv6_json(data.get('ipv6List'))
	result = Local_address(iplist=iplist, ipv6list=ipv6list)
	return result

class Local_address(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, iplist=None, ipv6list=None):
		self.iplist = iplist
		self.ipv6list = ipv6list

	def __str__(self):
		return ""

class Ddos_local_address_ip(AxapiObject):
	__metaclass__ = StructMeta 
	ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ip_addr):
		self.ip_addr = ip_addr

	def __str__(self):
		return str(self.ip_addr)

class Ddos_local_address_ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	def __init__(self, ipv6_addr):
		self.ipv6_addr = ipv6_addr

	def __str__(self):
		return str(self.ipv6_addr)

class DdosLocaladdressClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosLocaladdress(self):
		"""
		Retrieve the local_address identified by the specified identifier
		
		Returns:
			An instance of the Local_address class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified local_address does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('local-address')
		return deserialize_Local_address_json(payload)

