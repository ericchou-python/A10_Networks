########################################################################################################################
# File name: trunk.py
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
	'https://axapi.a10networks.com/axapi/v3/trunk',
]

def deserialize_Trunk_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet = data.get('ethernet')
	ethernet_to = data.get('ethernet-to')
	result = Trunk_eth_cfg(ethernet=ethernet, ethernet_to=ethernet_to)
	return result

def deserialize_list_Trunk_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Trunk_eth_cfg_json(item))
	return list(container)

def deserialize_Trunk_enable_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable_eth_start = data.get('enable-eth-start')
	enable_eth_end = data.get('enable-eth-end')
	result = Trunk_enable_eth_cfg(enable_eth_start=enable_eth_start, enable_eth_end=enable_eth_end)
	return result

def deserialize_list_Trunk_enable_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Trunk_enable_eth_cfg_json(item))
	return list(container)

def deserialize_Trunk__action_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	action = data.get('action')
	enable_eth_cfg = deserialize_list_Trunk_enable_eth_cfg_json(data.get('enable-eth-cfg'))
	result = Trunk__action_cfg(action=action, enable_eth_cfg=enable_eth_cfg)
	return result

def deserialize_Trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk_number = data.get('trunk-number')
	eth_cfg = deserialize_list_Trunk_eth_cfg_json(data.get('eth-cfg'))
	action_cfg = deserialize_Trunk__action_cfg_json(data.get('action-cfg'))
	name = data.get('name')
	ports_threshold = data.get('ports-threshold')
	ports_threshold_timer = data.get('ports-threshold-timer')
	result = Trunk(trunk_number=trunk_number, eth_cfg=eth_cfg, action_cfg=action_cfg, name=name, ports_threshold=ports_threshold, ports_threshold_timer=ports_threshold_timer)
	return result

def serialize_Trunk_eth_cfg_json(obj):
	output = OrderedDict()
	if obj.ethernet is not None:
		output['ethernet'] = obj.ethernet
	if obj.ethernet_to is not None:
		output['ethernet-to'] = obj.ethernet_to
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Trunk_eth_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Trunk_eth_cfg_json(item))
	return output

def serialize_Trunk_enable_eth_cfg_json(obj):
	output = OrderedDict()
	if obj.enable_eth_start is not None:
		output['enable-eth-start'] = obj.enable_eth_start
	if obj.enable_eth_end is not None:
		output['enable-eth-end'] = obj.enable_eth_end
	return output

def serialize_list_Trunk_enable_eth_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Trunk_enable_eth_cfg_json(item))
	return output

def serialize_Trunk__action_cfg_json(obj):
	output = OrderedDict()
	if obj.action is not None:
		output['action'] = obj.action
	if obj.enable_eth_cfg is not None:
		output['enable-eth-cfg'] = serialize_list_Trunk_enable_eth_cfg_json(obj.enable_eth_cfg)
	return output

def serialize_Trunk_json(obj):
	output = OrderedDict()
	output['trunk-number'] = obj.trunk_number
	if obj.eth_cfg is not None:
		output['eth-cfg'] = serialize_list_Trunk_eth_cfg_json(obj.eth_cfg)
	if obj.action_cfg is not None:
		output['action-cfg'] = serialize_Trunk__action_cfg_json(obj.action_cfg)
	if obj.name is not None:
		output['name'] = obj.name
	if obj.ports_threshold is not None:
		output['ports-threshold'] = obj.ports_threshold
	if obj.ports_threshold_timer is not None:
		output['ports-threshold-timer'] = obj.ports_threshold_timer
	return output

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

class Trunk__action_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	action = Enum(['enable', 'disable'])
	def __init__(self, action=None, enable_eth_cfg=None):
		self.action = action
		self.enable_eth_cfg = enable_eth_cfg

	def __str__(self):
		return ""

class Trunk(AxapiObject):
	__metaclass__ = StructMeta 
	trunk_number=PosRangedInteger(1, 16)
	name=SizedString(1, 63)
	ports_threshold=PosRangedInteger(2, 8)
	ports_threshold_timer=PosRangedInteger(1, 300)
	def __init__(self, trunk_number, eth_cfg=None, action_cfg=None, name=None, ports_threshold=None, ports_threshold_timer=None):
		self.trunk_number = trunk_number
		self.eth_cfg = eth_cfg
		self.action_cfg = action_cfg
		self.name = name
		self.ports_threshold = ports_threshold
		self.ports_threshold_timer = ports_threshold_timer

	def __str__(self):
		return str(self.trunk_number)

class Trunk_eth_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet=PosRangedInteger(1, 2048)
	ethernet_to=PosRangedInteger(1, 2048)
	def __init__(self, ethernet=None, ethernet_to=None):
		self.ethernet = ethernet
		self.ethernet_to = ethernet_to

	def __str__(self):
		return ""

class Trunk_trunk_number(AxapiObject):
	__metaclass__ = StructMeta 
	trunk_number=PosRangedInteger(1, 16)
	def __init__(self, trunk_number):
		self.trunk_number = trunk_number

	def __str__(self):
		return str(self.trunk_number)

class Trunk_enable_eth_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	enable_eth_start=PosRangedInteger(1, 2048)
	enable_eth_end=PosRangedInteger(1, 2048)
	def __init__(self, enable_eth_start=None, enable_eth_end=None):
		self.enable_eth_start = enable_eth_start
		self.enable_eth_end = enable_eth_end

	def __str__(self):
		return ""

class TrunkClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getTrunk(self, trunk_trunk_number):
		"""
		Retrieve the trunk identified by the specified identifier
		
		Args:
			trunk_trunk_number Trunk_trunk_number
		
		Returns:
			An instance of the Trunk class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(trunk_trunk_number) .replace("/", "%2f") + query, headers=headers)
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

	def putTrunk(self, trunk_trunk_number, trunk):
		"""
		Replace the object trunk
		
		Args:
			trunk_trunk_number Trunk_trunk_number
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
		conn.request('PUT', self.get_path() + '/' + str(trunk_trunk_number) .replace("/", "%2f") + query, payload, headers)
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

	def deleteTrunk(self, trunk_trunk_number):
		"""
		Remove the trunk identified by the specified identifier from the system
		
		Args:
			trunk_trunk_number Trunk_trunk_number
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(trunk_trunk_number) .replace("/", "%2f") + query, headers=headers)
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

class AllTrunksClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitTrunk(self, trunk):
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

	def getAllTrunks(self):
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

