########################################################################################################################
# File name: sflow_collector.py
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
	'https://axapi.a10networks.com/axapi/v3/sflow/collector',
]

def deserialize_Sflow_collector_ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	addr = data.get('addr')
	port = data.get('port')
	result = Sflow_collector_ip(addr=addr, port=port)
	return result

def deserialize_list_Sflow_collector_ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_collector_ip_json(item))
	return list(container)

def deserialize_Sflow_collector_ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	addr = data.get('addr')
	port = data.get('port')
	result = Sflow_collector_ipv6(addr=addr, port=port)
	return result

def deserialize_list_Sflow_collector_ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_collector_ipv6_json(item))
	return list(container)

def deserialize_Collector_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	iplist = deserialize_list_Sflow_collector_ip_json(data.get('ipList'))
	ipv6list = deserialize_list_Sflow_collector_ipv6_json(data.get('ipv6List'))
	result = Collector(iplist=iplist, ipv6list=ipv6list)
	return result

class Collector(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, iplist=None, ipv6list=None):
		self.iplist = iplist
		self.ipv6list = ipv6list

	def __str__(self):
		return ""

class Sflow_collector_ip(AxapiObject):
	__metaclass__ = StructMeta 
	addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	port=PosRangedInteger(1, 65535)
	def __init__(self, addr, port):
		self.addr = addr
		self.port = port

	def __str__(self):
		return str(self.addr) + '+' + str(self.port)

class Sflow_collector_ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	addr=SizedString(1, 255)
	port=PosRangedInteger(1, 65535)
	def __init__(self, addr, port):
		self.addr = addr
		self.port = port

	def __str__(self):
		return str(self.addr) + '+' + str(self.port)

class SflowCollectorClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSflowCollector(self):
		"""
		Retrieve the collector identified by the specified identifier
		
		Returns:
			An instance of the Collector class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified collector does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('collector')
		return deserialize_Collector_json(payload)

