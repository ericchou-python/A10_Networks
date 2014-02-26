########################################################################################################################
# File name: interface_ethernet_lacp.py
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
	'https://axapi.a10networks.com/axapi/v3/interface/ethernet/lacp',
]

def deserialize_Lacp__trunk_cfg__mode_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	mode = data.get('mode')
	mode_admin = data.get('mode-admin')
	mode_admin_uni = data.get('mode-admin-uni')
	mode_uni = data.get('mode-uni')
	mode_uni_admin = data.get('mode-uni-admin')
	result = Lacp__trunk_cfg__mode_cfg(mode=mode, mode_admin=mode_admin, mode_admin_uni=mode_admin_uni, mode_uni=mode_uni, mode_uni_admin=mode_uni_admin)
	return result

def deserialize_Lacp__trunk_cfg__admin_key_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	admin_key = data.get('admin-key')
	admin_uni = data.get('admin-uni')
	admin_uni_mode = data.get('admin-uni-mode')
	admin_mode = data.get('admin-mode')
	admin_mode_uni = data.get('admin-mode-uni')
	result = Lacp__trunk_cfg__admin_key_cfg(admin_key=admin_key, admin_uni=admin_uni, admin_uni_mode=admin_uni_mode, admin_mode=admin_mode, admin_mode_uni=admin_mode_uni)
	return result

def deserialize_Lacp__trunk_cfg__unidirectional_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	unidirectional_detection = data.get('unidirectional-detection')
	uni_admin = data.get('uni-admin')
	uni_admin_mode = data.get('uni-admin-mode')
	uni_mode = data.get('uni-mode')
	uni_mode_admin = data.get('uni-mode-admin')
	result = Lacp__trunk_cfg__unidirectional_cfg(unidirectional_detection=unidirectional_detection, uni_admin=uni_admin, uni_admin_mode=uni_admin_mode, uni_mode=uni_mode, uni_mode_admin=uni_mode_admin)
	return result

def deserialize_Lacp__trunk_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk = data.get('trunk')
	mode_cfg = deserialize_Lacp__trunk_cfg__mode_cfg_json(data.get('mode-cfg'))
	admin_key_cfg = deserialize_Lacp__trunk_cfg__admin_key_cfg_json(data.get('admin-key-cfg'))
	unidirectional_cfg = deserialize_Lacp__trunk_cfg__unidirectional_cfg_json(data.get('unidirectional-cfg'))
	result = Lacp__trunk_cfg(trunk=trunk, mode_cfg=mode_cfg, admin_key_cfg=admin_key_cfg, unidirectional_cfg=unidirectional_cfg)
	return result

def deserialize_Lacp__udld_timeout_cfg__fast_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	udld_fast_timeout = data.get('udld-fast-timeout')
	result = Lacp__udld_timeout_cfg__fast(udld_fast_timeout=udld_fast_timeout)
	return result

def deserialize_Lacp__udld_timeout_cfg__slow_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	udld_slow_timeout = data.get('udld-slow-timeout')
	result = Lacp__udld_timeout_cfg__slow(udld_slow_timeout=udld_slow_timeout)
	return result

def deserialize_Lacp__udld_timeout_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	udld_timeout = data.get('udld-timeout')
	fast = deserialize_Lacp__udld_timeout_cfg__fast_json(data.get('fast'))
	slow = deserialize_Lacp__udld_timeout_cfg__slow_json(data.get('slow'))
	result = Lacp__udld_timeout_cfg(udld_timeout=udld_timeout, fast=fast, slow=slow)
	return result

def deserialize_Lacp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk_cfg = deserialize_Lacp__trunk_cfg_json(data.get('trunk-cfg'))
	port_priority = data.get('port-priority')
	timeout = data.get('timeout')
	udld_timeout_cfg = deserialize_Lacp__udld_timeout_cfg_json(data.get('udld-timeout-cfg'))
	result = Lacp(trunk_cfg=trunk_cfg, port_priority=port_priority, timeout=timeout, udld_timeout_cfg=udld_timeout_cfg)
	return result

def serialize_Lacp__trunk_cfg__mode_cfg_json(obj):
	output = OrderedDict()
	if obj.mode is not None:
		output['mode'] = obj.mode
	if obj.mode_admin is not None:
		output['mode-admin'] = obj.mode_admin
	if obj.mode_admin_uni is not None:
		output['mode-admin-uni'] = obj.mode_admin_uni
	if obj.mode_uni is not None:
		output['mode-uni'] = obj.mode_uni
	if obj.mode_uni_admin is not None:
		output['mode-uni-admin'] = obj.mode_uni_admin
	return output

def serialize_Lacp__trunk_cfg__admin_key_cfg_json(obj):
	output = OrderedDict()
	if obj.admin_key is not None:
		output['admin-key'] = obj.admin_key
	if obj.admin_uni is not None:
		output['admin-uni'] = obj.admin_uni
	if obj.admin_uni_mode is not None:
		output['admin-uni-mode'] = obj.admin_uni_mode
	if obj.admin_mode is not None:
		output['admin-mode'] = obj.admin_mode
	if obj.admin_mode_uni is not None:
		output['admin-mode-uni'] = obj.admin_mode_uni
	return output

def serialize_Lacp__trunk_cfg__unidirectional_cfg_json(obj):
	output = OrderedDict()
	if obj.unidirectional_detection is not None:
		output['unidirectional-detection'] = obj.unidirectional_detection
	if obj.uni_admin is not None:
		output['uni-admin'] = obj.uni_admin
	if obj.uni_admin_mode is not None:
		output['uni-admin-mode'] = obj.uni_admin_mode
	if obj.uni_mode is not None:
		output['uni-mode'] = obj.uni_mode
	if obj.uni_mode_admin is not None:
		output['uni-mode-admin'] = obj.uni_mode_admin
	return output

def serialize_Lacp__trunk_cfg_json(obj):
	output = OrderedDict()
	if obj.trunk is not None:
		output['trunk'] = obj.trunk
	if obj.mode_cfg is not None:
		output['mode-cfg'] = serialize_Lacp__trunk_cfg__mode_cfg_json(obj.mode_cfg)
	if obj.admin_key_cfg is not None:
		output['admin-key-cfg'] = serialize_Lacp__trunk_cfg__admin_key_cfg_json(obj.admin_key_cfg)
	if obj.unidirectional_cfg is not None:
		output['unidirectional-cfg'] = serialize_Lacp__trunk_cfg__unidirectional_cfg_json(obj.unidirectional_cfg)
	return output

def serialize_Lacp__udld_timeout_cfg__fast_json(obj):
	output = OrderedDict()
	if obj.udld_fast_timeout is not None:
		output['udld-fast-timeout'] = obj.udld_fast_timeout
	return output

def serialize_Lacp__udld_timeout_cfg__slow_json(obj):
	output = OrderedDict()
	if obj.udld_slow_timeout is not None:
		output['udld-slow-timeout'] = obj.udld_slow_timeout
	return output

def serialize_Lacp__udld_timeout_cfg_json(obj):
	output = OrderedDict()
	if obj.udld_timeout is not None:
		output['udld-timeout'] = obj.udld_timeout
	if obj.fast is not None:
		output['fast'] = serialize_Lacp__udld_timeout_cfg__fast_json(obj.fast)
	if obj.slow is not None:
		output['slow'] = serialize_Lacp__udld_timeout_cfg__slow_json(obj.slow)
	return output

def serialize_Lacp_json(obj):
	output = OrderedDict()
	if obj.trunk_cfg is not None:
		output['trunk-cfg'] = serialize_Lacp__trunk_cfg_json(obj.trunk_cfg)
	if obj.port_priority is not None:
		output['port-priority'] = obj.port_priority
	if obj.timeout is not None:
		output['timeout'] = obj.timeout
	if obj.udld_timeout_cfg is not None:
		output['udld-timeout-cfg'] = serialize_Lacp__udld_timeout_cfg_json(obj.udld_timeout_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Lacp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Lacp_json(item))
	return list(container)

class Lacp__trunk_cfg__mode_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	mode = Enum(['active', 'passive'])
	mode_admin=PosRangedInteger(10000, 65535)
	mode_admin_uni=PosRangedInteger(0, 1)
	mode_uni=PosRangedInteger(0, 1)
	mode_uni_admin=PosRangedInteger(10000, 65535)
	def __init__(self, mode=None, mode_admin=None, mode_admin_uni=None, mode_uni=None, mode_uni_admin=None):
		self.mode = mode
		self.mode_admin = mode_admin
		self.mode_admin_uni = mode_admin_uni
		self.mode_uni = mode_uni
		self.mode_uni_admin = mode_uni_admin

	def __str__(self):
		return ""

class Lacp__trunk_cfg__admin_key_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	admin_key=PosRangedInteger(10000, 65535)
	admin_uni=PosRangedInteger(0, 1)
	admin_uni_mode = Enum(['active', 'passive'])
	admin_mode = Enum(['active', 'passive'])
	admin_mode_uni=PosRangedInteger(0, 1)
	def __init__(self, admin_key=None, admin_uni=None, admin_uni_mode=None, admin_mode=None, admin_mode_uni=None):
		self.admin_key = admin_key
		self.admin_uni = admin_uni
		self.admin_uni_mode = admin_uni_mode
		self.admin_mode = admin_mode
		self.admin_mode_uni = admin_mode_uni

	def __str__(self):
		return ""

class Lacp__trunk_cfg__unidirectional_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	unidirectional_detection=PosRangedInteger(0, 1)
	uni_admin=PosRangedInteger(10000, 65535)
	uni_admin_mode = Enum(['active', 'passive'])
	uni_mode = Enum(['active', 'passive'])
	uni_mode_admin=PosRangedInteger(10000, 65535)
	def __init__(self, unidirectional_detection=None, uni_admin=None, uni_admin_mode=None, uni_mode=None, uni_mode_admin=None):
		self.unidirectional_detection = unidirectional_detection
		self.uni_admin = uni_admin
		self.uni_admin_mode = uni_admin_mode
		self.uni_mode = uni_mode
		self.uni_mode_admin = uni_mode_admin

	def __str__(self):
		return ""

class Lacp__trunk_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	trunk=PosRangedInteger(1, 16)
	def __init__(self, trunk=None, mode_cfg=None, admin_key_cfg=None, unidirectional_cfg=None):
		self.trunk = trunk
		self.mode_cfg = mode_cfg
		self.admin_key_cfg = admin_key_cfg
		self.unidirectional_cfg = unidirectional_cfg

	def __str__(self):
		return ""

class Lacp__udld_timeout_cfg__fast(AxapiObject):
	__metaclass__ = StructMeta 
	udld_fast_timeout=PosRangedInteger(100, 1000)
	def __init__(self, udld_fast_timeout=None):
		self.udld_fast_timeout = udld_fast_timeout

	def __str__(self):
		return ""

class Lacp__udld_timeout_cfg__slow(AxapiObject):
	__metaclass__ = StructMeta 
	udld_slow_timeout=PosRangedInteger(1, 60)
	def __init__(self, udld_slow_timeout=None):
		self.udld_slow_timeout = udld_slow_timeout

	def __str__(self):
		return ""

class Lacp__udld_timeout_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	udld_timeout=PosRangedInteger(0, 1)
	def __init__(self, udld_timeout=None, fast=None, slow=None):
		self.udld_timeout = udld_timeout
		self.fast = fast
		self.slow = slow

	def __str__(self):
		return ""

class Lacp(AxapiObject):
	__metaclass__ = StructMeta 
	port_priority=PosRangedInteger(1, 65535)
	timeout = Enum(['long', 'short'])
	def __init__(self, trunk_cfg=None, port_priority=None, timeout=None, udld_timeout_cfg=None):
		self.trunk_cfg = trunk_cfg
		self.port_priority = port_priority
		self.timeout = timeout
		self.udld_timeout_cfg = udld_timeout_cfg

	def __str__(self):
		return ""

class InterfaceEthernetLacpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getInterfaceEthernetLacp(self):
		"""
		Retrieve the lacp identified by the specified identifier
		
		Returns:
			An instance of the Lacp class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified lacp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('lacp')
		return deserialize_Lacp_json(payload)

	def putInterfaceEthernetLacp(self, lacp):
		"""
		Replace the object lacp
		
		Args:
			lacp An instance of the Lacp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['lacp']=serialize_Lacp_json(lacp)
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

	def deleteInterfaceEthernetLacp(self):
		"""
		Remove the lacp identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified lacp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllInterfaceEthernetLacpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitInterfaceEthernetLacp(self, lacp):
		"""
		Create the object lacp
		
		Args:
			lacp An instance of the Lacp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['lacp']=serialize_Lacp_json(lacp)
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

	def getAllInterfaceEthernetLacps(self):
		"""
		Retrieve all lacp objects currently pending in the system
		
		Returns:
			A list of Lacp objects
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
			payload= data.get('lacpList')
		return deserialize_list_Lacp_json(payload)

