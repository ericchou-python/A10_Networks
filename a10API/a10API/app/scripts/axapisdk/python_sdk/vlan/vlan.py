########################################################################################################################
# File name: vlan.py
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
	'https://axapi.a10networks.com/axapi/v3/vlan',
]

def deserialize_Vlan_untagged_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	untagged_ethernet_start = data.get('untagged-ethernet-start')
	untagged_ethernet_end = data.get('untagged-ethernet-end')
	result = Vlan_untagged_eth_cfg(untagged_ethernet_start=untagged_ethernet_start, untagged_ethernet_end=untagged_ethernet_end)
	return result

def deserialize_list_Vlan_untagged_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vlan_untagged_eth_cfg_json(item))
	return list(container)

def deserialize_Vlan_untagged_trunk_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	untagged_trunk_start = data.get('untagged-trunk-start')
	untagged_trunk_end = data.get('untagged-trunk-end')
	result = Vlan_untagged_trunk_cfg(untagged_trunk_start=untagged_trunk_start, untagged_trunk_end=untagged_trunk_end)
	return result

def deserialize_list_Vlan_untagged_trunk_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vlan_untagged_trunk_cfg_json(item))
	return list(container)

def deserialize_Vlan__untagged_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	untagged_eth_cfg = deserialize_list_Vlan_untagged_eth_cfg_json(data.get('untagged-eth-cfg'))
	untagged_trunk_cfg = deserialize_list_Vlan_untagged_trunk_cfg_json(data.get('untagged-trunk-cfg'))
	result = Vlan__untagged(untagged_eth_cfg=untagged_eth_cfg, untagged_trunk_cfg=untagged_trunk_cfg)
	return result

def deserialize_Vlan_tagged_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tagged_ethernet_start = data.get('tagged-ethernet-start')
	tagged_ethernet_end = data.get('tagged-ethernet-end')
	result = Vlan_tagged_eth_cfg(tagged_ethernet_start=tagged_ethernet_start, tagged_ethernet_end=tagged_ethernet_end)
	return result

def deserialize_list_Vlan_tagged_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vlan_tagged_eth_cfg_json(item))
	return list(container)

def deserialize_Vlan_tagged_trunk_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tagged_trunk_start = data.get('tagged-trunk-start')
	tagged_trunk_end = data.get('tagged-trunk-end')
	result = Vlan_tagged_trunk_cfg(tagged_trunk_start=tagged_trunk_start, tagged_trunk_end=tagged_trunk_end)
	return result

def deserialize_list_Vlan_tagged_trunk_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vlan_tagged_trunk_cfg_json(item))
	return list(container)

def deserialize_Vlan__tagged_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tagged_eth_cfg = deserialize_list_Vlan_tagged_eth_cfg_json(data.get('tagged-eth-cfg'))
	tagged_trunk_cfg = deserialize_list_Vlan_tagged_trunk_cfg_json(data.get('tagged-trunk-cfg'))
	result = Vlan__tagged(tagged_eth_cfg=tagged_eth_cfg, tagged_trunk_cfg=tagged_trunk_cfg)
	return result

def deserialize_Vlan__router_interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ve = data.get('ve')
	name = data.get('name')
	result = Vlan__router_interface(ve=ve, name=name)
	return result

def deserialize_Vlan_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	vlan_num = data.get('vlan-num')
	untagged = deserialize_Vlan__untagged_json(data.get('untagged'))
	tagged = deserialize_Vlan__tagged_json(data.get('tagged'))
	router_interface = deserialize_Vlan__router_interface_json(data.get('router-interface'))
	result = Vlan(vlan_num=vlan_num, untagged=untagged, tagged=tagged, router_interface=router_interface)
	return result

def serialize_Vlan_untagged_eth_cfg_json(obj):
	output = OrderedDict()
	if obj.untagged_ethernet_start is not None:
		output['untagged-ethernet-start'] = obj.untagged_ethernet_start
	if obj.untagged_ethernet_end is not None:
		output['untagged-ethernet-end'] = obj.untagged_ethernet_end
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Vlan_untagged_eth_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vlan_untagged_eth_cfg_json(item))
	return output

def serialize_Vlan_untagged_trunk_cfg_json(obj):
	output = OrderedDict()
	if obj.untagged_trunk_start is not None:
		output['untagged-trunk-start'] = obj.untagged_trunk_start
	if obj.untagged_trunk_end is not None:
		output['untagged-trunk-end'] = obj.untagged_trunk_end
	return output

def serialize_list_Vlan_untagged_trunk_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vlan_untagged_trunk_cfg_json(item))
	return output

def serialize_Vlan__untagged_json(obj):
	output = OrderedDict()
	if obj.untagged_eth_cfg is not None:
		output['untagged-eth-cfg'] = serialize_list_Vlan_untagged_eth_cfg_json(obj.untagged_eth_cfg)
	if obj.untagged_trunk_cfg is not None:
		output['untagged-trunk-cfg'] = serialize_list_Vlan_untagged_trunk_cfg_json(obj.untagged_trunk_cfg)
	return output

def serialize_Vlan_tagged_eth_cfg_json(obj):
	output = OrderedDict()
	if obj.tagged_ethernet_start is not None:
		output['tagged-ethernet-start'] = obj.tagged_ethernet_start
	if obj.tagged_ethernet_end is not None:
		output['tagged-ethernet-end'] = obj.tagged_ethernet_end
	return output

def serialize_list_Vlan_tagged_eth_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vlan_tagged_eth_cfg_json(item))
	return output

def serialize_Vlan_tagged_trunk_cfg_json(obj):
	output = OrderedDict()
	if obj.tagged_trunk_start is not None:
		output['tagged-trunk-start'] = obj.tagged_trunk_start
	if obj.tagged_trunk_end is not None:
		output['tagged-trunk-end'] = obj.tagged_trunk_end
	return output

def serialize_list_Vlan_tagged_trunk_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vlan_tagged_trunk_cfg_json(item))
	return output

def serialize_Vlan__tagged_json(obj):
	output = OrderedDict()
	if obj.tagged_eth_cfg is not None:
		output['tagged-eth-cfg'] = serialize_list_Vlan_tagged_eth_cfg_json(obj.tagged_eth_cfg)
	if obj.tagged_trunk_cfg is not None:
		output['tagged-trunk-cfg'] = serialize_list_Vlan_tagged_trunk_cfg_json(obj.tagged_trunk_cfg)
	return output

def serialize_Vlan__router_interface_json(obj):
	output = OrderedDict()
	if obj.ve is not None:
		output['ve'] = obj.ve
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Vlan_json(obj):
	output = OrderedDict()
	output['vlan-num'] = obj.vlan_num
	if obj.untagged is not None:
		output['untagged'] = serialize_Vlan__untagged_json(obj.untagged)
	if obj.tagged is not None:
		output['tagged'] = serialize_Vlan__tagged_json(obj.tagged)
	if obj.router_interface is not None:
		output['router-interface'] = serialize_Vlan__router_interface_json(obj.router_interface)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Vlan_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vlan_json(item))
	return list(container)

class Vlan__untagged(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, untagged_eth_cfg=None, untagged_trunk_cfg=None):
		self.untagged_eth_cfg = untagged_eth_cfg
		self.untagged_trunk_cfg = untagged_trunk_cfg

	def __str__(self):
		return ""

class Vlan__tagged(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, tagged_eth_cfg=None, tagged_trunk_cfg=None):
		self.tagged_eth_cfg = tagged_eth_cfg
		self.tagged_trunk_cfg = tagged_trunk_cfg

	def __str__(self):
		return ""

class Vlan__router_interface(AxapiObject):
	__metaclass__ = StructMeta 
	ve=PosRangedInteger(2, 4094)
	name=SizedString(1, 63)
	def __init__(self, ve=None, name=None):
		self.ve = ve
		self.name = name

	def __str__(self):
		return ""

class Vlan(AxapiObject):
	__metaclass__ = StructMeta 
	vlan_num=PosRangedInteger(2, 4094)
	def __init__(self, vlan_num, untagged=None, tagged=None, router_interface=None):
		self.vlan_num = vlan_num
		self.untagged = untagged
		self.tagged = tagged
		self.router_interface = router_interface

	def __str__(self):
		return str(self.vlan_num)

class Vlan_untagged_eth_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	untagged_ethernet_start=PosRangedInteger(1, 2048)
	untagged_ethernet_end=PosRangedInteger(1, 2048)
	def __init__(self, untagged_ethernet_start=None, untagged_ethernet_end=None):
		self.untagged_ethernet_start = untagged_ethernet_start
		self.untagged_ethernet_end = untagged_ethernet_end

	def __str__(self):
		return ""

class Vlan_untagged_trunk_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	untagged_trunk_start=PosRangedInteger(1, 16)
	untagged_trunk_end=PosRangedInteger(1, 16)
	def __init__(self, untagged_trunk_start=None, untagged_trunk_end=None):
		self.untagged_trunk_start = untagged_trunk_start
		self.untagged_trunk_end = untagged_trunk_end

	def __str__(self):
		return ""

class Vlan_tagged_eth_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tagged_ethernet_start=PosRangedInteger(1, 2048)
	tagged_ethernet_end=PosRangedInteger(1, 2048)
	def __init__(self, tagged_ethernet_start=None, tagged_ethernet_end=None):
		self.tagged_ethernet_start = tagged_ethernet_start
		self.tagged_ethernet_end = tagged_ethernet_end

	def __str__(self):
		return ""

class Vlan_vlan_num(AxapiObject):
	__metaclass__ = StructMeta 
	vlan_num=PosRangedInteger(2, 4094)
	def __init__(self, vlan_num):
		self.vlan_num = vlan_num

	def __str__(self):
		return str(self.vlan_num)

class Vlan_tagged_trunk_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tagged_trunk_start=PosRangedInteger(1, 16)
	tagged_trunk_end=PosRangedInteger(1, 16)
	def __init__(self, tagged_trunk_start=None, tagged_trunk_end=None):
		self.tagged_trunk_start = tagged_trunk_start
		self.tagged_trunk_end = tagged_trunk_end

	def __str__(self):
		return ""

class VlanClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getVlan(self, vlan_vlan_num):
		"""
		Retrieve the vlan identified by the specified identifier
		
		Args:
			vlan_vlan_num Vlan_vlan_num
		
		Returns:
			An instance of the Vlan class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(vlan_vlan_num) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified vlan does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('vlan')
		return deserialize_Vlan_json(payload)

	def putVlan(self, vlan_vlan_num, vlan):
		"""
		Replace the object vlan
		
		Args:
			vlan_vlan_num Vlan_vlan_num
			vlan An instance of the Vlan class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['vlan']=serialize_Vlan_json(vlan)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(vlan_vlan_num) .replace("/", "%2f") + query, payload, headers)
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

	def deleteVlan(self, vlan_vlan_num):
		"""
		Remove the vlan identified by the specified identifier from the system
		
		Args:
			vlan_vlan_num Vlan_vlan_num
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(vlan_vlan_num) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified vlan does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllVlansClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitVlan(self, vlan):
		"""
		Create the object vlan
		
		Args:
			vlan An instance of the Vlan class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['vlan']=serialize_Vlan_json(vlan)
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

	def getAllVlans(self):
		"""
		Retrieve all vlan objects currently pending in the system
		
		Returns:
			A list of Vlan objects
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
			payload= data.get('vlanList')
		return deserialize_list_Vlan_json(payload)

