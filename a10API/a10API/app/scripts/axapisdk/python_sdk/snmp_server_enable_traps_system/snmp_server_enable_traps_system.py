########################################################################################################################
# File name: snmp_server_enable_traps_system.py
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
	'https://axapi.a10networks.com/axapi/v3/snmp-server/enable/traps/system',
]

def deserialize_System_json(obj):
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
	result = System(all=all, connection_resource_event=connection_resource_event, control_cpu_high=control_cpu_high, data_cpu_high=data_cpu_high, fan=fan, file_sys_read_only=file_sys_read_only, high_disk_use=high_disk_use, high_memory_use=high_memory_use, high_temp=high_temp, license_management=license_management, packet_drop=packet_drop, power=power, pri_disk=pri_disk, restart=restart, sec_disk=sec_disk, shutdown=shutdown, smp_resource_event=smp_resource_event, start=start)
	return result

def serialize_System_json(obj):
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

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_System_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_System_json(item))
	return list(container)

class System_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start(AxapiObject):
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

class System(AxapiObject):
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

class SnmpserverEnableTrapsSystemClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSnmpserverEnableTrapsSystem(self, system_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start):
		"""
		Retrieve the system identified by the specified identifier
		
		Args:
			system_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start System_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start
		
		Returns:
			An instance of the System class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(system_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified system does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('system')
		return deserialize_System_json(payload)

	def putSnmpserverEnableTrapsSystem(self, system_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start, system):
		"""
		Replace the object system
		
		Args:
			system_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start System_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start
			system An instance of the System class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['system']=serialize_System_json(system)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(system_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start) .replace("/", "%2f") + query, payload, headers)
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

	def deleteSnmpserverEnableTrapsSystem(self, system_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start):
		"""
		Remove the system identified by the specified identifier from the system
		
		Args:
			system_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start System_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(system_all_all_connection_resource_event_control_cpu_high_data_cpu_high_fan_file_sys_read_only_high_disk_use_high_memory_use_high_temp_license_management_packet_drop_power_pri_disk_restart_sec_disk_shutdown_smp_resource_event_start) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified system does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSnmpserverEnableTrapsSystemsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSnmpserverEnableTrapsSystem(self, system):
		"""
		Create the object system
		
		Args:
			system An instance of the System class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['system']=serialize_System_json(system)
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

	def getAllSnmpserverEnableTrapsSystems(self):
		"""
		Retrieve all system objects currently pending in the system
		
		Returns:
			A list of System objects
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
			payload= data.get('systemList')
		return deserialize_list_System_json(payload)

