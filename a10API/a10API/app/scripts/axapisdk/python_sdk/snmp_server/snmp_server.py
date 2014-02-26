########################################################################################################################
# File name: snmp_server.py
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
	'https://axapi.a10networks.com/axapi/v3/snmp-server',
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

def deserialize_Snmp_server__enable__traps_json(obj):
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
	result = Snmp_server__enable__traps(all=all, lldp=lldp, snmp=snmp, ha=ha, system=system, network=network)
	return result

def deserialize_Snmp_server__enable_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	service = data.get('service')
	traps = deserialize_Snmp_server__enable__traps_json(data.get('traps'))
	result = Snmp_server__enable(service=service, traps=traps)
	return result

def deserialize_Snmp_server__contact_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	contact_name = data.get('contact-name')
	result = Snmp_server__contact(contact_name=contact_name)
	return result

def deserialize_Snmp_server__location_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	loc = data.get('loc')
	result = Snmp_server__location(loc=loc)
	return result

def deserialize_Snmp_server__cpu_usage_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	cpulimit = data.get('cpulimit')
	result = Snmp_server__cpu_usage_limit(cpulimit=cpulimit)
	return result

def deserialize_Snmp_server_community_read_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	user = data.get('user')
	oid = data.get('oid')
	remote = data.get('remote')
	ipv4_mask = data.get('ipv4-mask')
	result = Snmp_server_community_read(user=user, oid=oid, remote=remote, ipv4_mask=ipv4_mask)
	return result

def deserialize_list_Snmp_server_community_read_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Snmp_server_community_read_json(item))
	return list(container)

def deserialize_Snmp_server__community_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	read = deserialize_list_Snmp_server_community_read_json(data.get('read'))
	result = Snmp_server__community(read=read)
	return result

def deserialize_Snmp_server_host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	hostname = data.get('hostname')
	ipv6_host = data.get('ipv6-host')
	version = data.get('version')
	comm = data.get('comm')
	udp_port = data.get('udp-port')
	result = Snmp_server_host(hostname=hostname, ipv6_host=ipv6_host, version=version, comm=comm, udp_port=udp_port)
	return result

def deserialize_list_Snmp_server_host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Snmp_server_host_json(item))
	return list(container)

def deserialize_Snmp_server_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable = deserialize_Snmp_server__enable_json(data.get('enable'))
	contact = deserialize_Snmp_server__contact_json(data.get('contact'))
	location = deserialize_Snmp_server__location_json(data.get('location'))
	cpu_usage_limit = deserialize_Snmp_server__cpu_usage_limit_json(data.get('cpu-usage-limit'))
	community = deserialize_Snmp_server__community_json(data.get('community'))
	host = deserialize_list_Snmp_server_host_json(data.get('host'))
	result = Snmp_server(enable=enable, contact=contact, location=location, cpu_usage_limit=cpu_usage_limit, community=community, host=host)
	return result

class Snmp_server__enable__traps(AxapiObject):
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

class Snmp_server__enable(AxapiObject):
	__metaclass__ = StructMeta 
	service=PosRangedInteger(0, 1)
	def __init__(self, service=None, traps=None):
		self.service = service
		self.traps = traps

	def __str__(self):
		return ""

class Snmp_server__contact(AxapiObject):
	__metaclass__ = StructMeta 
	contact_name=SizedString(1, 255)
	def __init__(self, contact_name=None):
		self.contact_name = contact_name

	def __str__(self):
		return ""

class Snmp_server__location(AxapiObject):
	__metaclass__ = StructMeta 
	loc=SizedString(1, 255)
	def __init__(self, loc=None):
		self.loc = loc

	def __str__(self):
		return ""

class Snmp_server__cpu_usage_limit(AxapiObject):
	__metaclass__ = StructMeta 
	cpulimit=PosRangedInteger(0, 20)
	def __init__(self, cpulimit=None):
		self.cpulimit = cpulimit

	def __str__(self):
		return ""

class Snmp_server__community(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, read=None):
		self.read = read

	def __str__(self):
		return ""

class Snmp_server(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, enable=None, contact=None, location=None, cpu_usage_limit=None, community=None, host=None):
		self.enable = enable
		self.contact = contact
		self.location = location
		self.cpu_usage_limit = cpu_usage_limit
		self.community = community
		self.host = host

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

class Snmp_server_community_read(AxapiObject):
	__metaclass__ = StructMeta 
	user=SizedString(1, 31)
	oid=PosRangedInteger(0, 1)
	remote = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv4_mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, user, oid=None, remote=None, ipv4_mask=None):
		self.user = user
		self.oid = oid
		self.remote = remote
		self.ipv4_mask = ipv4_mask

	def __str__(self):
		return str(self.user)

class Snmp_server_host(AxapiObject):
	__metaclass__ = StructMeta 
	hostname=SizedString(1, 31)
	ipv6_host=SizedString(1, 255)
	version = Enum(['v1', 'v2c'])
	comm=SizedString(1, 31)
	udp_port=PosRangedInteger(1, 65535)
	def __init__(self, hostname, ipv6_host, version=None, comm=None, udp_port=None):
		self.hostname = hostname
		self.ipv6_host = ipv6_host
		self.version = version
		self.comm = comm
		self.udp_port = udp_port

	def __str__(self):
		return str(self.hostname) + '+' + str(self.ipv6_host)

class SnmpserverClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSnmpserver(self):
		"""
		Retrieve the snmp_server identified by the specified identifier
		
		Returns:
			An instance of the Snmp_server class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified snmp_server does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('snmp-server')
		return deserialize_Snmp_server_json(payload)

