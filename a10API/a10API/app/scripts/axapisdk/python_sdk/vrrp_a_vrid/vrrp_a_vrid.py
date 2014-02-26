########################################################################################################################
# File name: vrrp_a_vrid.py
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
	'https://axapi.a10networks.com/axapi/v3/vrrp-a/vrid',
]

def deserialize_Vrrp_a_vrid_ip_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_address = data.get('ip-address')
	result = Vrrp_a_vrid_ip_address_cfg(ip_address=ip_address)
	return result

def deserialize_list_Vrrp_a_vrid_ip_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrrp_a_vrid_ip_address_cfg_json(item))
	return list(container)

def deserialize_Vrrp_a_vrid_ipv6_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_address = data.get('ipv6-address')
	result = Vrrp_a_vrid_ipv6_address_cfg(ipv6_address=ipv6_address)
	return result

def deserialize_list_Vrrp_a_vrid_ipv6_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrrp_a_vrid_ipv6_address_cfg_json(item))
	return list(container)

def deserialize_Vrid__floating_ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_address_cfg = deserialize_list_Vrrp_a_vrid_ip_address_cfg_json(data.get('ip-address-cfg'))
	ipv6_address_cfg = deserialize_list_Vrrp_a_vrid_ipv6_address_cfg_json(data.get('ipv6-address-cfg'))
	result = Vrid__floating_ip(ip_address_cfg=ip_address_cfg, ipv6_address_cfg=ipv6_address_cfg)
	return result

def deserialize_Vrid__preempt_mode_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	threshhold = data.get('threshhold')
	disable = data.get('disable')
	result = Vrid__preempt_mode(threshhold=threshhold, disable=disable)
	return result

def deserialize_Vrrp_a_vrid_interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet = data.get('ethernet')
	priority_cost = data.get('priority-cost')
	result = Vrrp_a_vrid_interface(ethernet=ethernet, priority_cost=priority_cost)
	return result

def deserialize_list_Vrrp_a_vrid_interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrrp_a_vrid_interface_json(item))
	return list(container)

def deserialize_Vrid__tracking_options__trunk_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk = data.get('trunk')
	priority_cost = data.get('priority-cost')
	per_port_pri = data.get('per-port-pri')
	result = Vrid__tracking_options__trunk_cfg(trunk=trunk, priority_cost=priority_cost, per_port_pri=per_port_pri)
	return result

def deserialize_Vrid__tracking_options_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	interface = deserialize_list_Vrrp_a_vrid_interface_json(data.get('interface'))
	trunk_cfg = deserialize_Vrid__tracking_options__trunk_cfg_json(data.get('trunk-cfg'))
	vlan = data.get('vlan')
	timeout = data.get('timeout')
	priority_cost = data.get('priority-cost')
	result = Vrid__tracking_options(interface=interface, trunk_cfg=trunk_cfg, vlan=vlan, timeout=timeout, priority_cost=priority_cost)
	return result

def deserialize_Vrid_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	vrid_val = data.get('vrid-val')
	floating_ip = deserialize_Vrid__floating_ip_json(data.get('floating-ip'))
	preempt_mode = deserialize_Vrid__preempt_mode_json(data.get('preempt-mode'))
	priority = data.get('priority')
	tracking_options = deserialize_Vrid__tracking_options_json(data.get('tracking-options'))
	result = Vrid(vrid_val=vrid_val, floating_ip=floating_ip, preempt_mode=preempt_mode, priority=priority, tracking_options=tracking_options)
	return result

def serialize_Vrrp_a_vrid_ip_address_cfg_json(obj):
	output = OrderedDict()
	if obj.ip_address is not None:
		output['ip-address'] = obj.ip_address
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Vrrp_a_vrid_ip_address_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vrrp_a_vrid_ip_address_cfg_json(item))
	return output

def serialize_Vrrp_a_vrid_ipv6_address_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv6_address is not None:
		output['ipv6-address'] = obj.ipv6_address
	return output

def serialize_list_Vrrp_a_vrid_ipv6_address_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vrrp_a_vrid_ipv6_address_cfg_json(item))
	return output

def serialize_Vrid__floating_ip_json(obj):
	output = OrderedDict()
	if obj.ip_address_cfg is not None:
		output['ip-address-cfg'] = serialize_list_Vrrp_a_vrid_ip_address_cfg_json(obj.ip_address_cfg)
	if obj.ipv6_address_cfg is not None:
		output['ipv6-address-cfg'] = serialize_list_Vrrp_a_vrid_ipv6_address_cfg_json(obj.ipv6_address_cfg)
	return output

def serialize_Vrid__preempt_mode_json(obj):
	output = OrderedDict()
	if obj.threshhold is not None:
		output['threshhold'] = obj.threshhold
	if obj.disable is not None:
		output['disable'] = obj.disable
	return output

def serialize_Vrrp_a_vrid_interface_json(obj):
	output = OrderedDict()
	if obj.ethernet is not None:
		output['ethernet'] = obj.ethernet
	if obj.priority_cost is not None:
		output['priority-cost'] = obj.priority_cost
	return output

def serialize_list_Vrrp_a_vrid_interface_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vrrp_a_vrid_interface_json(item))
	return output

def serialize_Vrid__tracking_options__trunk_cfg_json(obj):
	output = OrderedDict()
	if obj.trunk is not None:
		output['trunk'] = obj.trunk
	if obj.priority_cost is not None:
		output['priority-cost'] = obj.priority_cost
	if obj.per_port_pri is not None:
		output['per-port-pri'] = obj.per_port_pri
	return output

def serialize_Vrid__tracking_options_json(obj):
	output = OrderedDict()
	if obj.interface is not None:
		output['interface'] = serialize_list_Vrrp_a_vrid_interface_json(obj.interface)
	if obj.trunk_cfg is not None:
		output['trunk-cfg'] = serialize_Vrid__tracking_options__trunk_cfg_json(obj.trunk_cfg)
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	if obj.timeout is not None:
		output['timeout'] = obj.timeout
	if obj.priority_cost is not None:
		output['priority-cost'] = obj.priority_cost
	return output

def serialize_Vrid_json(obj):
	output = OrderedDict()
	output['vrid-val'] = obj.vrid_val
	if obj.floating_ip is not None:
		output['floating-ip'] = serialize_Vrid__floating_ip_json(obj.floating_ip)
	if obj.preempt_mode is not None:
		output['preempt-mode'] = serialize_Vrid__preempt_mode_json(obj.preempt_mode)
	if obj.priority is not None:
		output['priority'] = obj.priority
	if obj.tracking_options is not None:
		output['tracking-options'] = serialize_Vrid__tracking_options_json(obj.tracking_options)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Vrid_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrid_json(item))
	return list(container)

class Vrid__floating_ip(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ip_address_cfg=None, ipv6_address_cfg=None):
		self.ip_address_cfg = ip_address_cfg
		self.ipv6_address_cfg = ipv6_address_cfg

	def __str__(self):
		return ""

class Vrid__preempt_mode(AxapiObject):
	__metaclass__ = StructMeta 
	threshhold=PosRangedInteger(1, 255)
	disable=PosRangedInteger(0, 1)
	def __init__(self, threshhold=None, disable=None):
		self.threshhold = threshhold
		self.disable = disable

	def __str__(self):
		return ""

class Vrid__tracking_options__trunk_cfg(AxapiObject):
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

class Vrid__tracking_options(AxapiObject):
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

class Vrid(AxapiObject):
	__metaclass__ = StructMeta 
	vrid_val=PosRangedInteger(1, 1)
	priority=PosRangedInteger(1, 255)
	def __init__(self, vrid_val, floating_ip=None, preempt_mode=None, priority=None, tracking_options=None):
		self.vrid_val = vrid_val
		self.floating_ip = floating_ip
		self.preempt_mode = preempt_mode
		self.priority = priority
		self.tracking_options = tracking_options

	def __str__(self):
		return str(self.vrid_val)

class Vrrp_a_vrid_ip_address_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ip_address=None):
		self.ip_address = ip_address

	def __str__(self):
		return ""

class Vrrp_a_vrid_ipv6_address_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_address=SizedString(1, 255)
	def __init__(self, ipv6_address=None):
		self.ipv6_address = ipv6_address

	def __str__(self):
		return ""

class Vrid_vrid_val(AxapiObject):
	__metaclass__ = StructMeta 
	vrid_val=PosRangedInteger(1, 1)
	def __init__(self, vrid_val):
		self.vrid_val = vrid_val

	def __str__(self):
		return str(self.vrid_val)

class Vrrp_a_vrid_interface(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet=PosRangedInteger(1, 2048)
	priority_cost=PosRangedInteger(1, 255)
	def __init__(self, ethernet=None, priority_cost=None):
		self.ethernet = ethernet
		self.priority_cost = priority_cost

	def __str__(self):
		return ""

class VrrpaVridClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getVrrpaVrid(self, vrid_vrid_val):
		"""
		Retrieve the vrid identified by the specified identifier
		
		Args:
			vrid_vrid_val Vrid_vrid_val
		
		Returns:
			An instance of the Vrid class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(vrid_vrid_val) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified vrid does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('vrid')
		return deserialize_Vrid_json(payload)

	def putVrrpaVrid(self, vrid_vrid_val, vrid):
		"""
		Replace the object vrid
		
		Args:
			vrid_vrid_val Vrid_vrid_val
			vrid An instance of the Vrid class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['vrid']=serialize_Vrid_json(vrid)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(vrid_vrid_val) .replace("/", "%2f") + query, payload, headers)
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

	def deleteVrrpaVrid(self, vrid_vrid_val):
		"""
		Remove the vrid identified by the specified identifier from the system
		
		Args:
			vrid_vrid_val Vrid_vrid_val
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(vrid_vrid_val) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified vrid does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllVrrpaVridsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitVrrpaVrid(self, vrid):
		"""
		Create the object vrid
		
		Args:
			vrid An instance of the Vrid class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['vrid']=serialize_Vrid_json(vrid)
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

	def getAllVrrpaVrids(self):
		"""
		Retrieve all vrid objects currently pending in the system
		
		Returns:
			A list of Vrid objects
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
			payload= data.get('vridList')
		return deserialize_list_Vrid_json(payload)

