########################################################################################################################
# File name: sflow_polling.py
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
	'https://axapi.a10networks.com/axapi/v3/sflow/polling',
]

def deserialize_Polling__ddos_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	toggle = data.get('toggle')
	result = Polling__ddos(toggle=toggle)
	return result

def deserialize_Polling__http_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	toggle = data.get('toggle')
	result = Polling__http(toggle=toggle)
	return result

def deserialize_Polling__cpu_usage_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	toggle = data.get('toggle')
	result = Polling__cpu_usage(toggle=toggle)
	return result

def deserialize_Sflow_polling_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	start = data.get('start')
	interval = data.get('interval')
	result = Sflow_polling_ethernet(start=start, interval=interval)
	return result

def deserialize_list_Sflow_polling_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_polling_ethernet_json(item))
	return list(container)

def deserialize_Sflow_polling_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	start = data.get('start')
	interval = data.get('interval')
	result = Sflow_polling_ve(start=start, interval=interval)
	return result

def deserialize_list_Sflow_polling_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_polling_ve_json(item))
	return list(container)

def deserialize_Polling_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ddos = deserialize_Polling__ddos_json(data.get('ddos'))
	http = deserialize_Polling__http_json(data.get('http'))
	cpu_usage = deserialize_Polling__cpu_usage_json(data.get('cpu-usage'))
	ethernetlist = deserialize_list_Sflow_polling_ethernet_json(data.get('ethernetList'))
	velist = deserialize_list_Sflow_polling_ve_json(data.get('veList'))
	result = Polling(ddos=ddos, http=http, cpu_usage=cpu_usage, ethernetlist=ethernetlist, velist=velist)
	return result

class Polling__ddos(AxapiObject):
	__metaclass__ = StructMeta 
	toggle = Enum(['enable', 'disable'])
	def __init__(self, toggle=None):
		self.toggle = toggle

	def __str__(self):
		return ""

class Polling__http(AxapiObject):
	__metaclass__ = StructMeta 
	toggle = Enum(['enable', 'disable'])
	def __init__(self, toggle=None):
		self.toggle = toggle

	def __str__(self):
		return ""

class Polling__cpu_usage(AxapiObject):
	__metaclass__ = StructMeta 
	toggle = Enum(['enable', 'disable'])
	def __init__(self, toggle=None):
		self.toggle = toggle

	def __str__(self):
		return ""

class Polling(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ddos=None, http=None, cpu_usage=None, ethernetlist=None, velist=None):
		self.ddos = ddos
		self.http = http
		self.cpu_usage = cpu_usage
		self.ethernetlist = ethernetlist
		self.velist = velist

	def __str__(self):
		return ""

class Sflow_polling_ethernet(AxapiObject):
	__metaclass__ = StructMeta 
	start=PosRangedInteger(1, 2048)
	interval=PosRangedInteger(1, 200)
	def __init__(self, start, interval=None):
		self.start = start
		self.interval = interval

	def __str__(self):
		return str(self.start)

class Sflow_polling_ve(AxapiObject):
	__metaclass__ = StructMeta 
	start=PosRangedInteger(2, 4094)
	interval=PosRangedInteger(1, 200)
	def __init__(self, start, interval=None):
		self.start = start
		self.interval = interval

	def __str__(self):
		return str(self.start)

class SflowPollingClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSflowPolling(self):
		"""
		Retrieve the polling identified by the specified identifier
		
		Returns:
			An instance of the Polling class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified polling does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('polling')
		return deserialize_Polling_json(payload)

