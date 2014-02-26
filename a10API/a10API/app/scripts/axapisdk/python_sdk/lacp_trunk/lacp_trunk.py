########################################################################################################################
# File name: lacp_trunk.py
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
	'https://axapi.a10networks.com/axapi/v3/lacp-trunk',
]

def deserialize_Lacp_trunk_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	eth_start = data.get('eth-start')
	eth_end = data.get('eth-end')
	result = Lacp_trunk_eth_cfg(eth_start=eth_start, eth_end=eth_end)
	return result

def deserialize_list_Lacp_trunk_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Lacp_trunk_eth_cfg_json(item))
	return list(container)

def deserialize_Lacp_trunk__action_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	action = data.get('action')
	eth_cfg = deserialize_list_Lacp_trunk_eth_cfg_json(data.get('eth-cfg'))
	result = Lacp_trunk__action_cfg(action=action, eth_cfg=eth_cfg)
	return result

def deserialize_Lacp_trunk__ports_threshold_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	num_of_ports = data.get('num-of-ports')
	do_manual_recovery = data.get('do-manual-recovery')
	result = Lacp_trunk__ports_threshold(num_of_ports=num_of_ports, do_manual_recovery=do_manual_recovery)
	return result

def deserialize_Lacp_trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk_number = data.get('trunk-number')
	action_cfg = deserialize_Lacp_trunk__action_cfg_json(data.get('action-cfg'))
	ports_threshold = deserialize_Lacp_trunk__ports_threshold_json(data.get('ports-threshold'))
	ports_threshold_timer = data.get('ports-threshold-timer')
	result = Lacp_trunk(trunk_number=trunk_number, action_cfg=action_cfg, ports_threshold=ports_threshold, ports_threshold_timer=ports_threshold_timer)
	return result

def serialize_Lacp_trunk_eth_cfg_json(obj):
	output = OrderedDict()
	if obj.eth_start is not None:
		output['eth-start'] = obj.eth_start
	if obj.eth_end is not None:
		output['eth-end'] = obj.eth_end
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Lacp_trunk_eth_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Lacp_trunk_eth_cfg_json(item))
	return output

def serialize_Lacp_trunk__action_cfg_json(obj):
	output = OrderedDict()
	if obj.action is not None:
		output['action'] = obj.action
	if obj.eth_cfg is not None:
		output['eth-cfg'] = serialize_list_Lacp_trunk_eth_cfg_json(obj.eth_cfg)
	return output

def serialize_Lacp_trunk__ports_threshold_json(obj):
	output = OrderedDict()
	if obj.num_of_ports is not None:
		output['num-of-ports'] = obj.num_of_ports
	if obj.do_manual_recovery is not None:
		output['do-manual-recovery'] = obj.do_manual_recovery
	return output

def serialize_Lacp_trunk_json(obj):
	output = OrderedDict()
	output['trunk-number'] = obj.trunk_number
	if obj.action_cfg is not None:
		output['action-cfg'] = serialize_Lacp_trunk__action_cfg_json(obj.action_cfg)
	if obj.ports_threshold is not None:
		output['ports-threshold'] = serialize_Lacp_trunk__ports_threshold_json(obj.ports_threshold)
	if obj.ports_threshold_timer is not None:
		output['ports-threshold-timer'] = obj.ports_threshold_timer
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Lacp_trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Lacp_trunk_json(item))
	return list(container)

class Lacp_trunk__action_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	action = Enum(['enable-lacp', 'disable-lacp'])
	def __init__(self, action=None, eth_cfg=None):
		self.action = action
		self.eth_cfg = eth_cfg

	def __str__(self):
		return ""

class Lacp_trunk__ports_threshold(AxapiObject):
	__metaclass__ = StructMeta 
	num_of_ports=PosRangedInteger(2, 8)
	do_manual_recovery=PosRangedInteger(0, 1)
	def __init__(self, num_of_ports=None, do_manual_recovery=None):
		self.num_of_ports = num_of_ports
		self.do_manual_recovery = do_manual_recovery

	def __str__(self):
		return ""

class Lacp_trunk(AxapiObject):
	__metaclass__ = StructMeta 
	trunk_number=PosRangedInteger(1, 16)
	ports_threshold_timer=PosRangedInteger(1, 300)
	def __init__(self, trunk_number, action_cfg=None, ports_threshold=None, ports_threshold_timer=None):
		self.trunk_number = trunk_number
		self.action_cfg = action_cfg
		self.ports_threshold = ports_threshold
		self.ports_threshold_timer = ports_threshold_timer

	def __str__(self):
		return str(self.trunk_number)

class Lacp_trunk_trunk_number(AxapiObject):
	__metaclass__ = StructMeta 
	trunk_number=PosRangedInteger(1, 16)
	def __init__(self, trunk_number):
		self.trunk_number = trunk_number

	def __str__(self):
		return str(self.trunk_number)

class Lacp_trunk_eth_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	eth_start=PosRangedInteger(1, 2048)
	eth_end=PosRangedInteger(1, 2048)
	def __init__(self, eth_start=None, eth_end=None):
		self.eth_start = eth_start
		self.eth_end = eth_end

	def __str__(self):
		return ""

class LacptrunkClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLacptrunk(self, lacp_trunk_trunk_number):
		"""
		Retrieve the lacp_trunk identified by the specified identifier
		
		Args:
			lacp_trunk_trunk_number Lacp_trunk_trunk_number
		
		Returns:
			An instance of the Lacp_trunk class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(lacp_trunk_trunk_number) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified lacp_trunk does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('lacp-trunk')
		return deserialize_Lacp_trunk_json(payload)

	def putLacptrunk(self, lacp_trunk_trunk_number, lacp_trunk):
		"""
		Replace the object lacp_trunk
		
		Args:
			lacp_trunk_trunk_number Lacp_trunk_trunk_number
			lacp_trunk An instance of the Lacp_trunk class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['lacp-trunk']=serialize_Lacp_trunk_json(lacp_trunk)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(lacp_trunk_trunk_number) .replace("/", "%2f") + query, payload, headers)
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

	def deleteLacptrunk(self, lacp_trunk_trunk_number):
		"""
		Remove the lacp_trunk identified by the specified identifier from the system
		
		Args:
			lacp_trunk_trunk_number Lacp_trunk_trunk_number
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(lacp_trunk_trunk_number) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified lacp_trunk does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllLacptrunksClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitLacptrunk(self, lacp_trunk):
		"""
		Create the object lacp_trunk
		
		Args:
			lacp_trunk An instance of the Lacp_trunk class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['lacp-trunk']=serialize_Lacp_trunk_json(lacp_trunk)
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

	def getAllLacptrunks(self):
		"""
		Retrieve all lacp_trunk objects currently pending in the system
		
		Returns:
			A list of Lacp_trunk objects
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
			payload= data.get('lacp-trunkList')
		return deserialize_list_Lacp_trunk_json(payload)

