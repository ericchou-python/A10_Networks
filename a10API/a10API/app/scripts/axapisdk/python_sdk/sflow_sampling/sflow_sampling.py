########################################################################################################################
# File name: sflow_sampling.py
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
	'https://axapi.a10networks.com/axapi/v3/sflow/sampling',
]

def deserialize_Sflow_sampling_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	start = data.get('start')
	rate = data.get('rate')
	result = Sflow_sampling_ethernet(start=start, rate=rate)
	return result

def deserialize_list_Sflow_sampling_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_sampling_ethernet_json(item))
	return list(container)

def deserialize_Sflow_sampling_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	start = data.get('start')
	rate = data.get('rate')
	result = Sflow_sampling_ve(start=start, rate=rate)
	return result

def deserialize_list_Sflow_sampling_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_sampling_ve_json(item))
	return list(container)

def deserialize_Sampling_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernetlist = deserialize_list_Sflow_sampling_ethernet_json(data.get('ethernetList'))
	velist = deserialize_list_Sflow_sampling_ve_json(data.get('veList'))
	result = Sampling(ethernetlist=ethernetlist, velist=velist)
	return result

class Sampling(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ethernetlist=None, velist=None):
		self.ethernetlist = ethernetlist
		self.velist = velist

	def __str__(self):
		return ""

class Sflow_sampling_ethernet(AxapiObject):
	__metaclass__ = StructMeta 
	start=PosRangedInteger(1, 2048)
	rate=PosRangedInteger(10, 1000000)
	def __init__(self, start, rate=None):
		self.start = start
		self.rate = rate

	def __str__(self):
		return str(self.start)

class Sflow_sampling_ve(AxapiObject):
	__metaclass__ = StructMeta 
	start=PosRangedInteger(2, 4094)
	rate=PosRangedInteger(10, 1000000)
	def __init__(self, start, rate=None):
		self.start = start
		self.rate = rate

	def __str__(self):
		return str(self.start)

class SflowSamplingClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSflowSampling(self):
		"""
		Retrieve the sampling identified by the specified identifier
		
		Returns:
			An instance of the Sampling class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified sampling does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('sampling')
		return deserialize_Sampling_json(payload)

