########################################################################################################################
# File name: snmp_server_enable.py
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
	'https://axapi.a10networks.com/axapi/v3/snmp-server/enable',
]

def deserialize_Snmp_server_enable_traps_snmp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	all = data.get('all')
	linkdown = data.get('linkdown')
	linkup = data.get('linkup')
	result = Snmp_server_enable_traps_snmp(all=all, linkdown=linkdown, linkup=linkup)
	return result

def deserialize_list_Snmp_server_enable_traps_snmp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Snmp_server_enable_traps_snmp_json(item))
	return list(container)

def deserialize_Snmp_server_enable_traps_ha_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	all = data.get('all')
	active = data.get('active')
	active_active = data.get('active-active')
	standby = data.get('standby')
	vrrp = data.get('vrrp')
	result = Snmp_server_enable_traps_ha(all=all, active=active, active_active=active_active, standby=standby, vrrp=vrrp)
	return result

def deserialize_list_Snmp_server_enable_traps_ha_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Snmp_server_enable_traps_ha_json(item))
	return list(container)

def deserialize_Snmp_server_enable_traps_system_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	all = data.get('all')
	connection_resource_event = data.get('connection-resource-event')
	control_cpu_high = data.get('control-cpu-high')
	data_cpu_high = data.get('data-cpu-high')
	fan = data.get('fan')
	file_sys_read_only = data.get('file-sys-read-only')
	high_disk_use = data.get('high-disk-use')
	high_memory_use = data.get('high-memory-use')
	high_temp = data.get('high-temp')
	license_management = data.get('license-management')
	packet_drop = data.get('packet-drop')
	power = data.get('power')
	pri_disk = data.get('pri-disk')
	restart = data.get('restart')
	sec_disk = data.get('sec-disk')
	shutdown = data.get('shutdown')
	smp_resource_event = data.get('smp-resource-event')
	start = data.get('start')
	result = Snmp_server_enable_traps_system(all=all, connection_resource_event=connection_resource_event, control_cpu_high=control_cpu_high, data_cpu_high=data_cpu_high, fan=fan, file_sys_read_only=file_sys_read_only, high_disk_use=high_disk_use, high_memory_use=high_memory_use, high_temp=high_temp, license_management=license_management, packet_drop=packet_drop, power=power, pri_disk=pri_disk, restart=restart, sec_disk=sec_disk, shutdown=shutdown, smp_resource_event=smp_resource_event, start=start)
	return result

def deserialize_list_Snmp_server_enable_traps_system_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Snmp_server_enable_traps_system_json(item))
	return list(container)

def deserialize_Snmp_server_enable_traps_network_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk_port_threshold = data.get('trunk-port-threshold')
	result = Snmp_server_enable_traps_network(trunk_port_threshold=trunk_port_threshold)
	return result

def deserialize_list_Snmp_server_enable_traps_network_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Snmp_server_enable_traps_network_json(item))
	return list(container)

def deserialize_Enable__traps_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	all = data.get('all')
	lldp = data.get('lldp')
	snmp = deserialize_list_Snmp_server_enable_traps_snmp_json(data.get('snmp'))
	ha = deserialize_list_Snmp_server_enable_traps_ha_json(data.get('ha'))
	system = deserialize_list_Snmp_server_enable_traps_system_json(data.get('system'))
	network = deserialize_list_Snmp_server_enable_traps_network_json(data.get('network'))
	result = Enable__traps(all=all, lldp=lldp, snmp=snmp, ha=ha, system=system, network=network)
	return result

def deserialize_Enable_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	service = data.get('service')
	traps = deserialize_Enable__traps_json(data.get('traps'))
	result = Enable(service=service, traps=traps)
	return result

def serialize_Snmp_server_enable_traps_snmp_json(obj):
	output = OrderedDict()
	output['all'] = obj.all
	output['linkdown'] = obj.linkdown
	output['linkup'] = obj.linkup
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Snmp_server_enable_traps_snmp_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Snmp_server_enable_traps_snmp_json(item))
	return output

def serialize_Snmp_server_enable_traps_ha_json(obj):
	output = OrderedDict()
	output['all'] = obj.all
	output['active'] = obj.active
	output['active-active'] = obj.active_active
	output['standby'] = obj.standby
	output['vrrp'] = obj.vrrp
	return output

def serialize_list_Snmp_server_enable_traps_ha_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Snmp_server_enable_traps_ha_json(item))
	return output

def serialize_Snmp_server_enable_traps_system_json(obj):
	output = OrderedDict()
	output['all'] = obj.all
	output['connection-resource-event'] = obj.connection_resource_event
	output['control-cpu-high'] = obj.control_cpu_high
	output['data-cpu-high'] = obj.data_cpu_high
	output['fan'] = obj.fan
	output['file-sys-read-only'] = obj.file_sys_read_only
	output['high-disk-use'] = obj.high_disk_use
	output['high-memory-use'] = obj.high_memory_use
	output['high-temp'] = obj.high_temp
	output['license-management'] = obj.license_management
	output['packet-drop'] = obj.packet_drop
	output['power'] = obj.power
	output['pri-disk'] = obj.pri_disk
	output['restart'] = obj.restart
	output['sec-disk'] = obj.sec_disk
	output['shutdown'] = obj.shutdown
	output['smp-resource-event'] = obj.smp_resource_event
	output['start'] = obj.start
	return output

def serialize_list_Snmp_server_enable_traps_system_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Snmp_server_enable_traps_system_json(item))
	return output

def serialize_Snmp_server_enable_traps_network_json(obj):
	output = OrderedDict()
	output['trunk-port-threshold'] = obj.trunk_port_threshold
	return output

def serialize_list_Snmp_server_enable_traps_network_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Snmp_server_enable_traps_network_json(item))
	return output

def serialize_Enable__traps_json(obj):
	output = OrderedDict()
	if obj.all is not None:
		output['all'] = obj.all
	if obj.lldp is not None:
		output['lldp'] = obj.lldp
	if obj.snmp is not None:
		output['snmp'] = serialize_list_Snmp_server_enable_traps_snmp_json(obj.snmp)
	if obj.ha is not None:
		output['ha'] = serialize_list_Snmp_server_enable_traps_ha_json(obj.ha)
	if obj.system is not None:
		output['system'] = serialize_list_Snmp_server_enable_traps_system_json(obj.system)
	if obj.network is not None:
		output['network'] = serialize_list_Snmp_server_enable_traps_network_json(obj.network)
	return output

def serialize_Enable_json(obj):
	output = OrderedDict()
	if obj.service is not None:
		output['service'] = obj.service
	if obj.traps is not None:
		output['traps'] = serialize_Enable__traps_json(obj.traps)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Enable_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Enable_json(item))
	return list(container)

class Enable__traps(AxapiObject):
	__metaclass__ = StructMeta 
	all=PosRangedInteger(0, 1)
	lldp=PosRangedInteger(0, 1)
	def __init__(self, all=None, lldp=None, snmp=None, ha=None, system=None, network=None):
		self.all = all
		self.lldp = lldp
		self.snmp = snmp
		self.ha = ha
		self.system = system
		self.network = network

	def __str__(self):
		return ""

class Enable(AxapiObject):
	__metaclass__ = StructMeta 
	service=PosRangedInteger(0, 1)
	def __init__(self, service=None, traps=None):
		self.service = service
		self.traps = traps

	def __str__(self):
		return ""

class Snmp_server_enable_traps_snmp(AxapiObject):
	__metaclass__ = StructMeta 
	all=PosRangedInteger(0, 1)
	linkdown=PosRangedInteger(0, 1)
	linkup=PosRangedInteger(0, 1)
	def __init__(self, all, linkdown, linkup):
		self.all = all
		self.linkdown = linkdown
		self.linkup = linkup

	def __str__(self):
		return str(self.all) + '+' + str(self.linkdown) + '+' + str(self.linkup)

class Snmp_server_enable_traps_ha(AxapiObject):
	__metaclass__ = StructMeta 
	all=PosRangedInteger(0, 1)
	active=PosRangedInteger(0, 1)
	active_active=PosRangedInteger(0, 1)
	standby=PosRangedInteger(0, 1)
	vrrp=PosRangedInteger(0, 1)
	def __init__(self, all, active, active_active, standby, vrrp):
		self.all = all
		self.active = active
		self.active_active = active_active
		self.standby = standby
		self.vrrp = vrrp

	def __str__(self):
		return str(self.all) + '+' + str(self.active) + '+' + str(self.active_active) + '+' + str(self.standby) + '+' + str(self.vrrp)

class Snmp_server_enable_traps_system(AxapiObject):
	__metaclass__ = StructMeta 
	all=PosRangedInteger(0, 1)
	connection_resource_event=PosRangedInteger(0, 1)
	control_cpu_high=PosRangedInteger(0, 1)
	data_cpu_high=PosRangedInteger(0, 1)
	fan=PosRangedInteger(0, 1)
	file_sys_read_only=PosRangedInteger(0, 1)
	high_disk_use=PosRangedInteger(0, 1)
	high_memory_use=PosRangedInteger(0, 1)
	high_temp=PosRangedInteger(0, 1)
	license_management=PosRangedInteger(0, 1)
	packet_drop=PosRangedInteger(0, 1)
	power=PosRangedInteger(0, 1)
	pri_disk=PosRangedInteger(0, 1)
	restart=PosRangedInteger(0, 1)
	sec_disk=PosRangedInteger(0, 1)
	shutdown=PosRangedInteger(0, 1)
	smp_resource_event=PosRangedInteger(0, 1)
	start=PosRangedInteger(0, 1)
	def __init__(self, all, connection_resource_event, control_cpu_high, data_cpu_high, fan, file_sys_read_only, high_disk_use, high_memory_use, high_temp, license_management, packet_drop, power, pri_disk, restart, sec_disk, shutdown, smp_resource_event, start):
		self.all = all
		self.connection_resource_event = connection_resource_event
		self.control_cpu_high = control_cpu_high
		self.data_cpu_high = data_cpu_high
		self.fan = fan
		self.file_sys_read_only = file_sys_read_only
		self.high_disk_use = high_disk_use
		self.high_memory_use = high_memory_use
		self.high_temp = high_temp
		self.license_management = license_management
		self.packet_drop = packet_drop
		self.power = power
		self.pri_disk = pri_disk
		self.restart = restart
		self.sec_disk = sec_disk
		self.shutdown = shutdown
		self.smp_resource_event = smp_resource_event
		self.start = start

	def __str__(self):
		return str(self.all) + '+' + str(self.connection_resource_event) + '+' + str(self.control_cpu_high) + '+' + str(self.data_cpu_high) + '+' + str(self.fan) + '+' + str(self.file_sys_read_only) + '+' + str(self.high_disk_use) + '+' + str(self.high_memory_use) + '+' + str(self.high_temp) + '+' + str(self.license_management) + '+' + str(self.packet_drop) + '+' + str(self.power) + '+' + str(self.pri_disk) + '+' + str(self.restart) + '+' + str(self.sec_disk) + '+' + str(self.shutdown) + '+' + str(self.smp_resource_event) + '+' + str(self.start)

class Snmp_server_enable_traps_network(AxapiObject):
	__metaclass__ = StructMeta 
	trunk_port_threshold=PosRangedInteger(0, 1)
	def __init__(self, trunk_port_threshold):
		self.trunk_port_threshold = trunk_port_threshold

	def __str__(self):
		return str(self.trunk_port_threshold)

class SnmpserverEnableClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSnmpserverEnable(self):
		"""
		Retrieve the enable identified by the specified identifier
		
		Returns:
			An instance of the Enable class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified enable does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('enable')
		return deserialize_Enable_json(payload)

	def putSnmpserverEnable(self, enable):
		"""
		Replace the object enable
		
		Args:
			enable An instance of the Enable class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['enable']=serialize_Enable_json(enable)
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

	def deleteSnmpserverEnable(self):
		"""
		Remove the enable identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified enable does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSnmpserverEnablesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSnmpserverEnable(self, enable):
		"""
		Create the object enable
		
		Args:
			enable An instance of the Enable class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['enable']=serialize_Enable_json(enable)
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

	def getAllSnmpserverEnables(self):
		"""
		Retrieve all enable objects currently pending in the system
		
		Returns:
			A list of Enable objects
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
			payload= data.get('enableList')
		return deserialize_list_Enable_json(payload)

