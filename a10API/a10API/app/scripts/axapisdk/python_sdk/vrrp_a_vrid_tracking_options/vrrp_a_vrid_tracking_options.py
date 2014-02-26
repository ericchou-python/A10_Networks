########################################################################################################################
# File name: vrrp_a_vrid_tracking_options.py
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
	'https://axapi.a10networks.com/axapi/v3/vrrp-a/vrid/tracking-options',
]

def deserialize_Vrrp_a_vrid_tracking_options_interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet = data.get('ethernet')
	priority_cost = data.get('priority-cost')
	result = Vrrp_a_vrid_tracking_options_interface(ethernet=ethernet, priority_cost=priority_cost)
	return result

def deserialize_list_Vrrp_a_vrid_tracking_options_interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrrp_a_vrid_tracking_options_interface_json(item))
	return list(container)

def deserialize_Tracking_options__trunk_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk = data.get('trunk')
	priority_cost = data.get('priority-cost')
	per_port_pri = data.get('per-port-pri')
	result = Tracking_options__trunk_cfg(trunk=trunk, priority_cost=priority_cost, per_port_pri=per_port_pri)
	return result

def deserialize_Tracking_options_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	interface = deserialize_list_Vrrp_a_vrid_tracking_options_interface_json(data.get('interface'))
	trunk_cfg = deserialize_Tracking_options__trunk_cfg_json(data.get('trunk-cfg'))
	vlan = data.get('vlan')
	timeout = data.get('timeout')
	priority_cost = data.get('priority-cost')
	result = Tracking_options(interface=interface, trunk_cfg=trunk_cfg, vlan=vlan, timeout=timeout, priority_cost=priority_cost)
	return result

def serialize_Vrrp_a_vrid_tracking_options_interface_json(obj):
	output = OrderedDict()
	if obj.ethernet is not None:
		output['ethernet'] = obj.ethernet
	if obj.priority_cost is not None:
		output['priority-cost'] = obj.priority_cost
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Vrrp_a_vrid_tracking_options_interface_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vrrp_a_vrid_tracking_options_interface_json(item))
	return output

def serialize_Tracking_options__trunk_cfg_json(obj):
	output = OrderedDict()
	if obj.trunk is not None:
		output['trunk'] = obj.trunk
	if obj.priority_cost is not None:
		output['priority-cost'] = obj.priority_cost
	if obj.per_port_pri is not None:
		output['per-port-pri'] = obj.per_port_pri
	return output

def serialize_Tracking_options_json(obj):
	output = OrderedDict()
	if obj.interface is not None:
		output['interface'] = serialize_list_Vrrp_a_vrid_tracking_options_interface_json(obj.interface)
	if obj.trunk_cfg is not None:
		output['trunk-cfg'] = serialize_Tracking_options__trunk_cfg_json(obj.trunk_cfg)
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	if obj.timeout is not None:
		output['timeout'] = obj.timeout
	if obj.priority_cost is not None:
		output['priority-cost'] = obj.priority_cost
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Tracking_options_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Tracking_options_json(item))
	return list(container)

class Tracking_options__trunk_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	trunk=PosRangedInteger(1, 16)
	priority_cost=PosRangedInteger(1, 255)
	per_port_pri=PosRangedInteger(1, 255)
	def __init__(self, trunk=None, priority_cost=None, per_port_pri=None):
		self.trunk = trunk
		self.priority_cost = priority_cost
		self.per_port_pri = per_port_pri

	def __str__(self):
		return ""

class Tracking_options(AxapiObject):
	__metaclass__ = StructMeta 
	vlan=PosRangedInteger(2, 4094)
	timeout=PosRangedInteger(2, 600)
	priority_cost=PosRangedInteger(1, 255)
	def __init__(self, interface=None, trunk_cfg=None, vlan=None, timeout=None, priority_cost=None):
		self.interface = interface
		self.trunk_cfg = trunk_cfg
		self.vlan = vlan
		self.timeout = timeout
		self.priority_cost = priority_cost

	def __str__(self):
		return ""

class Vrrp_a_vrid_tracking_options_interface(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet=PosRangedInteger(1, 2048)
	priority_cost=PosRangedInteger(1, 255)
	def __init__(self, ethernet=None, priority_cost=None):
		self.ethernet = ethernet
		self.priority_cost = priority_cost

	def __str__(self):
		return ""

class VrrpaVridTrackingoptionsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getVrrpaVridTrackingoptions(self):
		"""
		Retrieve the tracking_options identified by the specified identifier
		
		Returns:
			An instance of the Tracking_options class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified tracking_options does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('tracking-options')
		return deserialize_Tracking_options_json(payload)

	def putVrrpaVridTrackingoptions(self, tracking_options):
		"""
		Replace the object tracking_options
		
		Args:
			tracking_options An instance of the Tracking_options class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['tracking-options']=serialize_Tracking_options_json(tracking_options)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + query, payload, headers)
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

	def deleteVrrpaVridTrackingoptions(self):
		"""
		Remove the tracking_options identified by the specified identifier from
		the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified tracking_options does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllVrrpaVridTrackingoptionssClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitVrrpaVridTrackingoptions(self, tracking_options):
		"""
		Create the object tracking_options
		
		Args:
			tracking_options An instance of the Tracking_options class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['tracking-options']=serialize_Tracking_options_json(tracking_options)
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

	def getAllVrrpaVridTrackingoptionss(self):
		"""
		Retrieve all tracking_options objects currently pending in the system
		
		Returns:
			A list of Tracking_options objects
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
			payload= data.get('tracking-optionsList')
		return deserialize_list_Tracking_options_json(payload)

