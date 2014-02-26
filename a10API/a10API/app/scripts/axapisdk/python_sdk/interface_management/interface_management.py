########################################################################################################################
# File name: interface_management.py
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
	'https://axapi.a10networks.com/axapi/v3/interface/management',
]

def deserialize_Management__access_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl_id = data.get('acl_id')
	acl_name = data.get('acl-name')
	inbound = data.get('inbound')
	result = Management__access_list(acl_id=acl_id, acl_name=acl_name, inbound=inbound)
	return result

def deserialize_Management__bcast_rate_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	rate = data.get('rate')
	result = Management__bcast_rate_limit(rate=rate)
	return result

def deserialize_Management__lldp__enable_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	rt_enable = data.get('rt-enable')
	rx = data.get('rx')
	tx = data.get('tx')
	result = Management__lldp__enable_cfg(rt_enable=rt_enable, rx=rx, tx=tx)
	return result

def deserialize_Management__lldp__notification_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	notification = data.get('notification')
	notif_enable = data.get('notif-enable')
	result = Management__lldp__notification_cfg(notification=notification, notif_enable=notif_enable)
	return result

def deserialize_Management__lldp__tx_dot1_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tx_dot1_tlvs = data.get('tx-dot1-tlvs')
	link_aggregation = data.get('link-aggregation')
	vlan = data.get('vlan')
	result = Management__lldp__tx_dot1_cfg(tx_dot1_tlvs=tx_dot1_tlvs, link_aggregation=link_aggregation, vlan=vlan)
	return result

def deserialize_Management__lldp__tx_tlvs_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tx_tlvs = data.get('tx-tlvs')
	management_address = data.get('management-address')
	port_description = data.get('port-description')
	system_capabilities = data.get('system-capabilities')
	system_description = data.get('system-description')
	system_name = data.get('system-name')
	result = Management__lldp__tx_tlvs_cfg(tx_tlvs=tx_tlvs, management_address=management_address, port_description=port_description, system_capabilities=system_capabilities, system_description=system_description, system_name=system_name)
	return result

def deserialize_Management__lldp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable_cfg = deserialize_Management__lldp__enable_cfg_json(data.get('enable-cfg'))
	notification_cfg = deserialize_Management__lldp__notification_cfg_json(data.get('notification-cfg'))
	tx_dot1_cfg = deserialize_Management__lldp__tx_dot1_cfg_json(data.get('tx-dot1-cfg'))
	tx_tlvs_cfg = deserialize_Management__lldp__tx_tlvs_cfg_json(data.get('tx-tlvs-cfg'))
	result = Management__lldp(enable_cfg=enable_cfg, notification_cfg=notification_cfg, tx_dot1_cfg=tx_dot1_cfg, tx_tlvs_cfg=tx_tlvs_cfg)
	return result

def deserialize_Management__ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val = data.get('address_val')
	netmask = data.get('netmask')
	dhcp = data.get('dhcp')
	result = Management__ip__address(address_val=address_val, netmask=netmask, dhcp=dhcp)
	return result

def deserialize_Management__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Management__ip__address_json(data.get('address'))
	control_apps_use_mgmt_port = data.get('control-apps-use-mgmt-port')
	default_gateway = data.get('default-gateway')
	result = Management__ip(address=address, control_apps_use_mgmt_port=control_apps_use_mgmt_port, default_gateway=default_gateway)
	return result

def deserialize_Management__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	v6_acl_name = data.get('v6-acl-name')
	inbound = data.get('inbound')
	default_v6_gw = data.get('default-v6-gw')
	result = Management__ipv6(ipv6_addr=ipv6_addr, v6_acl_name=v6_acl_name, inbound=inbound, default_v6_gw=default_v6_gw)
	return result

def deserialize_Management_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	access_list = deserialize_Management__access_list_json(data.get('access-list'))
	duplexity = data.get('duplexity')
	speed = data.get('speed')
	flow_control = data.get('flow-control')
	enable = data.get('enable')
	disable = data.get('disable')
	bcast_rate_limit = deserialize_Management__bcast_rate_limit_json(data.get('bcast-rate-limit'))
	lldp = deserialize_Management__lldp_json(data.get('lldp'))
	ip = deserialize_Management__ip_json(data.get('ip'))
	ipv6 = deserialize_Management__ipv6_json(data.get('ipv6'))
	result = Management(access_list=access_list, duplexity=duplexity, speed=speed, flow_control=flow_control, enable=enable, disable=disable, bcast_rate_limit=bcast_rate_limit, lldp=lldp, ip=ip, ipv6=ipv6)
	return result

def serialize_Management__access_list_json(obj):
	output = OrderedDict()
	if obj.acl_id is not None:
		output['acl_id'] = obj.acl_id
	if obj.acl_name is not None:
		output['acl-name'] = obj.acl_name
	if obj.inbound is not None:
		output['inbound'] = obj.inbound
	return output

def serialize_Management__bcast_rate_limit_json(obj):
	output = OrderedDict()
	if obj.rate is not None:
		output['rate'] = obj.rate
	return output

def serialize_Management__lldp__enable_cfg_json(obj):
	output = OrderedDict()
	if obj.rt_enable is not None:
		output['rt-enable'] = obj.rt_enable
	if obj.rx is not None:
		output['rx'] = obj.rx
	if obj.tx is not None:
		output['tx'] = obj.tx
	return output

def serialize_Management__lldp__notification_cfg_json(obj):
	output = OrderedDict()
	if obj.notification is not None:
		output['notification'] = obj.notification
	if obj.notif_enable is not None:
		output['notif-enable'] = obj.notif_enable
	return output

def serialize_Management__lldp__tx_dot1_cfg_json(obj):
	output = OrderedDict()
	if obj.tx_dot1_tlvs is not None:
		output['tx-dot1-tlvs'] = obj.tx_dot1_tlvs
	if obj.link_aggregation is not None:
		output['link-aggregation'] = obj.link_aggregation
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	return output

def serialize_Management__lldp__tx_tlvs_cfg_json(obj):
	output = OrderedDict()
	if obj.tx_tlvs is not None:
		output['tx-tlvs'] = obj.tx_tlvs
	if obj.management_address is not None:
		output['management-address'] = obj.management_address
	if obj.port_description is not None:
		output['port-description'] = obj.port_description
	if obj.system_capabilities is not None:
		output['system-capabilities'] = obj.system_capabilities
	if obj.system_description is not None:
		output['system-description'] = obj.system_description
	if obj.system_name is not None:
		output['system-name'] = obj.system_name
	return output

def serialize_Management__lldp_json(obj):
	output = OrderedDict()
	if obj.enable_cfg is not None:
		output['enable-cfg'] = serialize_Management__lldp__enable_cfg_json(obj.enable_cfg)
	if obj.notification_cfg is not None:
		output['notification-cfg'] = serialize_Management__lldp__notification_cfg_json(obj.notification_cfg)
	if obj.tx_dot1_cfg is not None:
		output['tx-dot1-cfg'] = serialize_Management__lldp__tx_dot1_cfg_json(obj.tx_dot1_cfg)
	if obj.tx_tlvs_cfg is not None:
		output['tx-tlvs-cfg'] = serialize_Management__lldp__tx_tlvs_cfg_json(obj.tx_tlvs_cfg)
	return output

def serialize_Management__ip__address_json(obj):
	output = OrderedDict()
	if obj.address_val is not None:
		output['address_val'] = obj.address_val
	if obj.netmask is not None:
		output['netmask'] = obj.netmask
	if obj.dhcp is not None:
		output['dhcp'] = obj.dhcp
	return output

def serialize_Management__ip_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = serialize_Management__ip__address_json(obj.address)
	if obj.control_apps_use_mgmt_port is not None:
		output['control-apps-use-mgmt-port'] = obj.control_apps_use_mgmt_port
	if obj.default_gateway is not None:
		output['default-gateway'] = obj.default_gateway
	return output

def serialize_Management__ipv6_json(obj):
	output = OrderedDict()
	if obj.ipv6_addr is not None:
		output['ipv6-addr'] = obj.ipv6_addr
	if obj.v6_acl_name is not None:
		output['v6-acl-name'] = obj.v6_acl_name
	if obj.inbound is not None:
		output['inbound'] = obj.inbound
	if obj.default_v6_gw is not None:
		output['default-v6-gw'] = obj.default_v6_gw
	return output

def serialize_Management_json(obj):
	output = OrderedDict()
	if obj.access_list is not None:
		output['access-list'] = serialize_Management__access_list_json(obj.access_list)
	if obj.duplexity is not None:
		output['duplexity'] = obj.duplexity
	if obj.speed is not None:
		output['speed'] = obj.speed
	if obj.flow_control is not None:
		output['flow-control'] = obj.flow_control
	if obj.enable is not None:
		output['enable'] = obj.enable
	if obj.disable is not None:
		output['disable'] = obj.disable
	if obj.bcast_rate_limit is not None:
		output['bcast-rate-limit'] = serialize_Management__bcast_rate_limit_json(obj.bcast_rate_limit)
	if obj.lldp is not None:
		output['lldp'] = serialize_Management__lldp_json(obj.lldp)
	if obj.ip is not None:
		output['ip'] = serialize_Management__ip_json(obj.ip)
	if obj.ipv6 is not None:
		output['ipv6'] = serialize_Management__ipv6_json(obj.ipv6)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Management_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Management_json(item))
	return list(container)

class Management__access_list(AxapiObject):
	__metaclass__ = StructMeta 
	acl_id=PosRangedInteger(1, 199)
	acl_name=SizedString(1, 16)
	inbound=PosRangedInteger(0, 1)
	def __init__(self, acl_id=None, acl_name=None, inbound=None):
		self.acl_id = acl_id
		self.acl_name = acl_name
		self.inbound = inbound

	def __str__(self):
		return ""

class Management__bcast_rate_limit(AxapiObject):
	__metaclass__ = StructMeta 
	rate=PosRangedInteger(50, 5000)
	def __init__(self, rate=None):
		self.rate = rate

	def __str__(self):
		return ""

class Management__lldp__enable_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	rt_enable=PosRangedInteger(0, 1)
	rx=PosRangedInteger(0, 1)
	tx=PosRangedInteger(0, 1)
	def __init__(self, rt_enable=None, rx=None, tx=None):
		self.rt_enable = rt_enable
		self.rx = rx
		self.tx = tx

	def __str__(self):
		return ""

class Management__lldp__notification_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	notification=PosRangedInteger(0, 1)
	notif_enable=PosRangedInteger(0, 1)
	def __init__(self, notification=None, notif_enable=None):
		self.notification = notification
		self.notif_enable = notif_enable

	def __str__(self):
		return ""

class Management__lldp__tx_dot1_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tx_dot1_tlvs=PosRangedInteger(0, 1)
	link_aggregation=PosRangedInteger(0, 1)
	vlan=PosRangedInteger(0, 1)
	def __init__(self, tx_dot1_tlvs=None, link_aggregation=None, vlan=None):
		self.tx_dot1_tlvs = tx_dot1_tlvs
		self.link_aggregation = link_aggregation
		self.vlan = vlan

	def __str__(self):
		return ""

class Management__lldp__tx_tlvs_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tx_tlvs=PosRangedInteger(0, 1)
	management_address=PosRangedInteger(0, 1)
	port_description=PosRangedInteger(0, 1)
	system_capabilities=PosRangedInteger(0, 1)
	system_description=PosRangedInteger(0, 1)
	system_name=PosRangedInteger(0, 1)
	def __init__(self, tx_tlvs=None, management_address=None, port_description=None, system_capabilities=None, system_description=None, system_name=None):
		self.tx_tlvs = tx_tlvs
		self.management_address = management_address
		self.port_description = port_description
		self.system_capabilities = system_capabilities
		self.system_description = system_description
		self.system_name = system_name

	def __str__(self):
		return ""

class Management__lldp(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, enable_cfg=None, notification_cfg=None, tx_dot1_cfg=None, tx_tlvs_cfg=None):
		self.enable_cfg = enable_cfg
		self.notification_cfg = notification_cfg
		self.tx_dot1_cfg = tx_dot1_cfg
		self.tx_tlvs_cfg = tx_tlvs_cfg

	def __str__(self):
		return ""

class Management__ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	address_val = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	dhcp=PosRangedInteger(0, 1)
	def __init__(self, address_val=None, netmask=None, dhcp=None):
		self.address_val = address_val
		self.netmask = netmask
		self.dhcp = dhcp

	def __str__(self):
		return ""

class Management__ip(AxapiObject):
	__metaclass__ = StructMeta 
	control_apps_use_mgmt_port=PosRangedInteger(0, 1)
	default_gateway = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, address=None, control_apps_use_mgmt_port=None, default_gateway=None):
		self.address = address
		self.control_apps_use_mgmt_port = control_apps_use_mgmt_port
		self.default_gateway = default_gateway

	def __str__(self):
		return ""

class Management__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	v6_acl_name=SizedString(1, 32)
	inbound=PosInteger()
	default_v6_gw=SizedString(1, 255)
	def __init__(self, ipv6_addr=None, v6_acl_name=None, inbound=None, default_v6_gw=None):
		self.ipv6_addr = ipv6_addr
		self.v6_acl_name = v6_acl_name
		self.inbound = inbound
		self.default_v6_gw = default_v6_gw

	def __str__(self):
		return ""

class Management(AxapiObject):
	__metaclass__ = StructMeta 
	duplexity = Enum(['Full', 'Half', 'auto'])
	speed = Enum(['10', '100', '1000', 'auto'])
	flow_control=PosRangedInteger(0, 1)
	enable=PosRangedInteger(0, 1)
	disable=PosRangedInteger(0, 1)
	def __init__(self, access_list=None, duplexity=None, speed=None, flow_control=None, enable=None, disable=None, bcast_rate_limit=None, lldp=None, ip=None, ipv6=None):
		self.access_list = access_list
		self.duplexity = duplexity
		self.speed = speed
		self.flow_control = flow_control
		self.enable = enable
		self.disable = disable
		self.bcast_rate_limit = bcast_rate_limit
		self.lldp = lldp
		self.ip = ip
		self.ipv6 = ipv6

	def __str__(self):
		return ""

class InterfaceManagementClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getInterfaceManagement(self):
		"""
		Retrieve the management identified by the specified identifier
		
		Returns:
			An instance of the Management class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified management does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('management')
		return deserialize_Management_json(payload)

	def putInterfaceManagement(self, management):
		"""
		Replace the object management
		
		Args:
			management An instance of the Management class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['management']=serialize_Management_json(management)
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

	def deleteInterfaceManagement(self):
		"""
		Remove the management identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified management does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllInterfaceManagementsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitInterfaceManagement(self, management):
		"""
		Create the object management
		
		Args:
			management An instance of the Management class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['management']=serialize_Management_json(management)
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

	def getAllInterfaceManagements(self):
		"""
		Retrieve all management objects currently pending in the system
		
		Returns:
			A list of Management objects
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
			payload= data.get('managementList')
		return deserialize_list_Management_json(payload)

