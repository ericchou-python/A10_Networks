########################################################################################################################
# File name: vrrp_a_interface.py
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
	'https://axapi.a10networks.com/axapi/v3/vrrp-a/interface',
]

def deserialize_Interface__ethernet_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet = data.get('ethernet')
	router_interface = data.get('router-interface')
	server_interface = data.get('server-interface')
	both = data.get('both')
	vlan = data.get('vlan')
	no_heartbeat = data.get('no-heartbeat')
	result = Interface__ethernet_cfg(ethernet=ethernet, router_interface=router_interface, server_interface=server_interface, both=both, vlan=vlan, no_heartbeat=no_heartbeat)
	return result

def deserialize_Interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet_cfg = deserialize_Interface__ethernet_cfg_json(data.get('ethernet-cfg'))
	result = Interface(ethernet_cfg=ethernet_cfg)
	return result

def serialize_Interface__ethernet_cfg_json(obj):
	output = OrderedDict()
	output['ethernet'] = obj.ethernet
	if obj.router_interface is not None:
		output['router-interface'] = obj.router_interface
	if obj.server_interface is not None:
		output['server-interface'] = obj.server_interface
	if obj.both is not None:
		output['both'] = obj.both
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	if obj.no_heartbeat is not None:
		output['no-heartbeat'] = obj.no_heartbeat
	return output

def serialize_Interface_json(obj):
	output = OrderedDict()
	output['ethernet-cfg'] = serialize_Interface__ethernet_cfg_json(obj.ethernet_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_json(item))
	return list(container)

class Interface_ethernet_cfg__ethernet_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet=PosRangedInteger(1, 2048)
	router_interface=PosRangedInteger(0, 1)
	server_interface=PosRangedInteger(0, 1)
	both=PosRangedInteger(0, 1)
	vlan=PosRangedInteger(1, 4094)
	no_heartbeat=PosRangedInteger(0, 1)
	def __init__(self, ethernet, router_interface=None, server_interface=None, both=None, vlan=None, no_heartbeat=None):
		self.ethernet = ethernet
		self.router_interface = router_interface
		self.server_interface = server_interface
		self.both = both
		self.vlan = vlan
		self.no_heartbeat = no_heartbeat

	def __str__(self):
		return str(self.ethernet)

class Interface_ethernet_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ethernet_cfg):
		self.ethernet_cfg = ethernet_cfg

	def __str__(self):
		return str(self.ethernet_cfg)

class Interface__ethernet_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet=PosRangedInteger(1, 2048)
	router_interface=PosRangedInteger(0, 1)
	server_interface=PosRangedInteger(0, 1)
	both=PosRangedInteger(0, 1)
	vlan=PosRangedInteger(1, 4094)
	no_heartbeat=PosRangedInteger(0, 1)
	def __init__(self, ethernet, router_interface=None, server_interface=None, both=None, vlan=None, no_heartbeat=None):
		self.ethernet = ethernet
		self.router_interface = router_interface
		self.server_interface = server_interface
		self.both = both
		self.vlan = vlan
		self.no_heartbeat = no_heartbeat

	def __str__(self):
		return str(self.ethernet)

class Interface(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ethernet_cfg):
		self.ethernet_cfg = ethernet_cfg

	def __str__(self):
		return str(self.ethernet_cfg)

class VrrpaInterfaceClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getVrrpaInterface(self, interface_ethernet_cfg):
		"""
		Retrieve the interface identified by the specified identifier
		
		Args:
			interface_ethernet_cfg Interface_ethernet_cfg
		
		Returns:
			An instance of the Interface class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(interface_ethernet_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified interface does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('interface')
		return deserialize_Interface_json(payload)

	def putVrrpaInterface(self, interface_ethernet_cfg, interface):
		"""
		Replace the object interface
		
		Args:
			interface_ethernet_cfg Interface_ethernet_cfg
			interface An instance of the Interface class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['interface']=serialize_Interface_json(interface)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(interface_ethernet_cfg) .replace("/", "%2f") + query, payload, headers)
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

	def deleteVrrpaInterface(self, interface_ethernet_cfg):
		"""
		Remove the interface identified by the specified identifier from the system
		
		Args:
			interface_ethernet_cfg Interface_ethernet_cfg
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(interface_ethernet_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified interface does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllVrrpaInterfacesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitVrrpaInterface(self, interface):
		"""
		Create the object interface
		
		Args:
			interface An instance of the Interface class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['interface']=serialize_Interface_json(interface)
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

	def getAllVrrpaInterfaces(self):
		"""
		Retrieve all interface objects currently pending in the system
		
		Returns:
			A list of Interface objects
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
			payload= data.get('interfaceList')
		return deserialize_list_Interface_json(payload)

