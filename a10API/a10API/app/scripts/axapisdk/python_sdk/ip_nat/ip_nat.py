########################################################################################################################
# File name: ip_nat.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/nat',
]

def deserialize_Ip_nat_pool__pool_name_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	pool_name = data.get('pool-name')
	start_address = data.get('start-address')
	end_address = data.get('end-address')
	netmask = data.get('netmask')
	gateway = data.get('gateway')
	vrid = data.get('vrid')
	ip_rr = data.get('ip-rr')
	ha_use_all_ports = data.get('ha-use-all-ports')
	result = Ip_nat_pool__pool_name_cfg(pool_name=pool_name, start_address=start_address, end_address=end_address, netmask=netmask, gateway=gateway, vrid=vrid, ip_rr=ip_rr, ha_use_all_ports=ha_use_all_ports)
	return result

def deserialize_Ip_nat_pool_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	pool_name_cfg = deserialize_Ip_nat_pool__pool_name_cfg_json(data.get('pool-name-cfg'))
	result = Ip_nat_pool(pool_name_cfg=pool_name_cfg)
	return result

def deserialize_list_Ip_nat_pool_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_pool_json(item))
	return list(container)

def deserialize_Ip_nat_pool_group_member_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	pool_name = data.get('pool-name')
	result = Ip_nat_pool_group_member(pool_name=pool_name)
	return result

def deserialize_list_Ip_nat_pool_group_member_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_pool_group_member_json(item))
	return list(container)

def deserialize_Ip_nat_pool_group_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	pool_group_name = data.get('pool-group-name')
	vrid = data.get('vrid')
	default = data.get('default')
	memberlist = deserialize_list_Ip_nat_pool_group_member_json(data.get('memberList'))
	result = Ip_nat_pool_group(pool_group_name=pool_group_name, vrid=vrid, default=default, memberlist=memberlist)
	return result

def deserialize_list_Ip_nat_pool_group_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_pool_group_json(item))
	return list(container)

def deserialize_Ip_nat_inside_source_list_name_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl_name = data.get('acl-name')
	pool = data.get('pool')
	msl = data.get('msl')
	result = Ip_nat_inside_source_list_name(acl_name=acl_name, pool=pool, msl=msl)
	return result

def deserialize_list_Ip_nat_inside_source_list_name_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_inside_source_list_name_json(item))
	return list(container)

def deserialize_Ip_nat_inside_source_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl_id = data.get('acl-id')
	pool = data.get('pool')
	msl = data.get('msl')
	namelist = deserialize_list_Ip_nat_inside_source_list_name_json(data.get('nameList'))
	result = Ip_nat_inside_source_list(acl_id=acl_id, pool=pool, msl=msl, namelist=namelist)
	return result

def deserialize_list_Ip_nat_inside_source_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_inside_source_list_json(item))
	return list(container)

def deserialize_Ip_nat_inside_source_static_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	src_address = data.get('src-address')
	nat_address = data.get('nat-address')
	vrid = data.get('vrid')
	result = Ip_nat_inside_source_static(src_address=src_address, nat_address=nat_address, vrid=vrid)
	return result

def deserialize_list_Ip_nat_inside_source_static_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_inside_source_static_json(item))
	return list(container)

def deserialize_Nat__inside__source_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	class_list = data.get('class-list')
	listlist = deserialize_list_Ip_nat_inside_source_list_json(data.get('listList'))
	staticlist = deserialize_list_Ip_nat_inside_source_static_json(data.get('staticList'))
	result = Nat__inside__source(class_list=class_list, listlist=listlist, staticlist=staticlist)
	return result

def deserialize_Nat__inside_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	source = deserialize_Nat__inside__source_json(data.get('source'))
	result = Nat__inside(source=source)
	return result

def deserialize_Ip_nat_template_logging__log__port_mappings_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	both = data.get('both')
	creation = data.get('creation')
	result = Ip_nat_template_logging__log__port_mappings(both=both, creation=creation)
	return result

def deserialize_Ip_nat_template_logging__log_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sessions = data.get('sessions')
	port_mappings = deserialize_Ip_nat_template_logging__log__port_mappings_json(data.get('port-mappings'))
	result = Ip_nat_template_logging__log(sessions=sessions, port_mappings=port_mappings)
	return result

def deserialize_Ip_nat_template_logging__source_port_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	source_port_num = data.get('source-port-num')
	any = data.get('any')
	result = Ip_nat_template_logging__source_port(source_port_num=source_port_num, any=any)
	return result

def deserialize_Ip_nat_template_logging_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	facility = data.get('facility')
	include_destination = data.get('include-destination')
	include_rip_rport = data.get('include-rip-rport')
	log = deserialize_Ip_nat_template_logging__log_json(data.get('log'))
	severity = data.get('severity')
	source_port = deserialize_Ip_nat_template_logging__source_port_json(data.get('source-port'))
	result = Ip_nat_template_logging(name=name, facility=facility, include_destination=include_destination, include_rip_rport=include_rip_rport, log=log, severity=severity, source_port=source_port)
	return result

def deserialize_list_Ip_nat_template_logging_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_template_logging_json(item))
	return list(container)

def deserialize_Nat__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	logginglist = deserialize_list_Ip_nat_template_logging_json(data.get('loggingList'))
	result = Nat__template(logginglist=logginglist)
	return result

def deserialize_Nat__translation__icmp_timeout_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp_timeout_val = data.get('icmp-timeout-val')
	fast = data.get('fast')
	result = Nat__translation__icmp_timeout(icmp_timeout_val=icmp_timeout_val, fast=fast)
	return result

def deserialize_Ip_nat_translation_service_timeout_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	service_type = data.get('service-type')
	port = data.get('port')
	timeout_val = data.get('timeout-val')
	fast = data.get('fast')
	result = Ip_nat_translation_service_timeout(service_type=service_type, port=port, timeout_val=timeout_val, fast=fast)
	return result

def deserialize_list_Ip_nat_translation_service_timeout_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_translation_service_timeout_json(item))
	return list(container)

def deserialize_Nat__translation_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp_timeout = deserialize_Nat__translation__icmp_timeout_json(data.get('icmp-timeout'))
	tcp_timeout = data.get('tcp-timeout')
	udp_timeout = data.get('udp-timeout')
	service_timeoutlist = deserialize_list_Ip_nat_translation_service_timeout_json(data.get('service-timeoutList'))
	result = Nat__translation(icmp_timeout=icmp_timeout, tcp_timeout=tcp_timeout, udp_timeout=udp_timeout, service_timeoutlist=service_timeoutlist)
	return result

def deserialize_Ip_nat_range_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	local_start_ipv4_addr = data.get('local-start-ipv4-addr')
	local_netmaskv4 = data.get('local-netmaskv4')
	global_start_ipv4_addr = data.get('global-start-ipv4-addr')
	global_netmaskv4 = data.get('global-netmaskv4')
	count = data.get('count')
	vrid = data.get('vrid')
	local_start_ipv6_addr = data.get('local-start-ipv6-addr')
	global_start_ipv6_addr = data.get('global-start-ipv6-addr')
	result = Ip_nat_range_list(name=name, local_start_ipv4_addr=local_start_ipv4_addr, local_netmaskv4=local_netmaskv4, global_start_ipv4_addr=global_start_ipv4_addr, global_netmaskv4=global_netmaskv4, count=count, vrid=vrid, local_start_ipv6_addr=local_start_ipv6_addr, global_start_ipv6_addr=global_start_ipv6_addr)
	return result

def deserialize_list_Ip_nat_range_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_range_list_json(item))
	return list(container)

def deserialize_Nat__alg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	pptp = data.get('pptp')
	result = Nat__alg(pptp=pptp)
	return result

def deserialize_Nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	poollist = deserialize_list_Ip_nat_pool_json(data.get('poolList'))
	pool_grouplist = deserialize_list_Ip_nat_pool_group_json(data.get('pool-groupList'))
	inside = deserialize_Nat__inside_json(data.get('inside'))
	template = deserialize_Nat__template_json(data.get('template'))
	translation = deserialize_Nat__translation_json(data.get('translation'))
	range_listlist = deserialize_list_Ip_nat_range_list_json(data.get('range-listList'))
	alg = deserialize_Nat__alg_json(data.get('alg'))
	result = Nat(poollist=poollist, pool_grouplist=pool_grouplist, inside=inside, template=template, translation=translation, range_listlist=range_listlist, alg=alg)
	return result

class Nat__inside__source(AxapiObject):
	__metaclass__ = StructMeta 
	class_list=SizedString(1, 63)
	def __init__(self, class_list=None, listlist=None, staticlist=None):
		self.class_list = class_list
		self.listlist = listlist
		self.staticlist = staticlist

	def __str__(self):
		return ""

class Nat__inside(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, source=None):
		self.source = source

	def __str__(self):
		return ""

class Nat__template(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, logginglist=None):
		self.logginglist = logginglist

	def __str__(self):
		return ""

class Nat__translation__icmp_timeout(AxapiObject):
	__metaclass__ = StructMeta 
	icmp_timeout_val=PosRangedInteger(2, 15000)
	fast=PosRangedInteger(0, 1)
	def __init__(self, icmp_timeout_val=None, fast=None):
		self.icmp_timeout_val = icmp_timeout_val
		self.fast = fast

	def __str__(self):
		return ""

class Nat__translation(AxapiObject):
	__metaclass__ = StructMeta 
	tcp_timeout=PosRangedInteger(2, 15000)
	udp_timeout=PosRangedInteger(2, 15000)
	def __init__(self, icmp_timeout=None, tcp_timeout=None, udp_timeout=None, service_timeoutlist=None):
		self.icmp_timeout = icmp_timeout
		self.tcp_timeout = tcp_timeout
		self.udp_timeout = udp_timeout
		self.service_timeoutlist = service_timeoutlist

	def __str__(self):
		return ""

class Nat__alg(AxapiObject):
	__metaclass__ = StructMeta 
	pptp = Enum(['disable', 'enable'])
	def __init__(self, pptp=None):
		self.pptp = pptp

	def __str__(self):
		return ""

class Nat(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, poollist=None, pool_grouplist=None, inside=None, template=None, translation=None, range_listlist=None, alg=None):
		self.poollist = poollist
		self.pool_grouplist = pool_grouplist
		self.inside = inside
		self.template = template
		self.translation = translation
		self.range_listlist = range_listlist
		self.alg = alg

	def __str__(self):
		return ""

class Ip_nat_pool__pool_name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	pool_name=SizedString(1, 63)
	start_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	end_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	gateway = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	vrid=PosRangedInteger(1, 31)
	ip_rr=PosRangedInteger(0, 1)
	ha_use_all_ports=PosRangedInteger(0, 1)
	def __init__(self, pool_name, start_address, end_address, netmask, gateway=None, vrid=None, ip_rr=None, ha_use_all_ports=None):
		self.pool_name = pool_name
		self.start_address = start_address
		self.end_address = end_address
		self.netmask = netmask
		self.gateway = gateway
		self.vrid = vrid
		self.ip_rr = ip_rr
		self.ha_use_all_ports = ha_use_all_ports

	def __str__(self):
		return str(self.pool_name) + '+' + str(self.start_address) + '+' + str(self.end_address) + '+' + str(self.netmask)

class Ip_nat_pool(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, pool_name_cfg):
		self.pool_name_cfg = pool_name_cfg

	def __str__(self):
		return str(self.pool_name_cfg)

class Ip_nat_pool_group(AxapiObject):
	__metaclass__ = StructMeta 
	pool_group_name=SizedString(1, 63)
	vrid=PosRangedInteger(1, 31)
	default=PosRangedInteger(0, 1)
	def __init__(self, pool_group_name, vrid=None, default=None, memberlist=None):
		self.pool_group_name = pool_group_name
		self.vrid = vrid
		self.default = default
		self.memberlist = memberlist

	def __str__(self):
		return str(self.pool_group_name)

class Ip_nat_pool_group_member(AxapiObject):
	__metaclass__ = StructMeta 
	pool_name=SizedString(1, 63)
	def __init__(self, pool_name):
		self.pool_name = pool_name

	def __str__(self):
		return str(self.pool_name)

class Ip_nat_inside_source_list(AxapiObject):
	__metaclass__ = StructMeta 
	acl_id=PosRangedInteger(1, 199)
	pool=SizedString(1, 255)
	msl=PosRangedInteger(1, 1800)
	def __init__(self, acl_id, pool, msl=None, namelist=None):
		self.acl_id = acl_id
		self.pool = pool
		self.msl = msl
		self.namelist = namelist

	def __str__(self):
		return str(self.acl_id) + '+' + str(self.pool)

class Ip_nat_inside_source_list_name(AxapiObject):
	__metaclass__ = StructMeta 
	acl_name=SizedString(1, 16)
	pool=SizedString(1, 255)
	msl=PosRangedInteger(1, 1800)
	def __init__(self, acl_name, pool, msl=None):
		self.acl_name = acl_name
		self.pool = pool
		self.msl = msl

	def __str__(self):
		return str(self.acl_name) + '+' + str(self.pool)

class Ip_nat_inside_source_static(AxapiObject):
	__metaclass__ = StructMeta 
	src_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	nat_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	vrid=PosRangedInteger(1, 31)
	def __init__(self, src_address, nat_address, vrid=None):
		self.src_address = src_address
		self.nat_address = nat_address
		self.vrid = vrid

	def __str__(self):
		return str(self.src_address) + '+' + str(self.nat_address)

class Ip_nat_template_logging__log__port_mappings(AxapiObject):
	__metaclass__ = StructMeta 
	both=PosRangedInteger(0, 1)
	creation=PosRangedInteger(0, 1)
	def __init__(self, both, creation):
		self.both = both
		self.creation = creation

	def __str__(self):
		return str(self.both) + '+' + str(self.creation)

class Ip_nat_template_logging__log(AxapiObject):
	__metaclass__ = StructMeta 
	sessions=PosRangedInteger(0, 1)
	def __init__(self, sessions, port_mappings):
		self.sessions = sessions
		self.port_mappings = port_mappings

	def __str__(self):
		return str(self.sessions) + '+' + str(self.port_mappings)

class Ip_nat_template_logging__source_port(AxapiObject):
	__metaclass__ = StructMeta 
	source_port_num=PosRangedInteger(1, 65535)
	any=PosRangedInteger(0, 1)
	def __init__(self, source_port_num, any):
		self.source_port_num = source_port_num
		self.any = any

	def __str__(self):
		return str(self.source_port_num) + '+' + str(self.any)

class Ip_nat_template_logging(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	facility = Enum(['kernel', 'user', 'mail', 'daemon', 'security-authorization', 'syslog', 'line-printer', 'news', 'uucp', 'cron', 'security-authorization-private', 'ftp', 'ntp', 'audit', 'alert', 'clock', 'local0', 'local1', 'local2', 'local3', 'local4', 'local5', 'local6', 'local7'])
	include_destination=PosRangedInteger(0, 1)
	include_rip_rport=PosRangedInteger(0, 1)
	severity = Enum(['emergency', 'alert', 'critical', 'error', 'warning', 'notice', 'informational', 'debugging'])
	def __init__(self, name, facility=None, include_destination=None, include_rip_rport=None, log=None, severity=None, source_port=None):
		self.name = name
		self.facility = facility
		self.include_destination = include_destination
		self.include_rip_rport = include_rip_rport
		self.log = log
		self.severity = severity
		self.source_port = source_port

	def __str__(self):
		return str(self.name)

class Ip_nat_translation_service_timeout(AxapiObject):
	__metaclass__ = StructMeta 
	service_type = Enum(['tcp', 'udp'])
	port=PosRangedInteger(1, 65535)
	timeout_val=PosRangedInteger(2, 15000)
	fast=PosRangedInteger(0, 1)
	def __init__(self, service_type, port, timeout_val, fast):
		self.service_type = service_type
		self.port = port
		self.timeout_val = timeout_val
		self.fast = fast

	def __str__(self):
		return str(self.service_type) + '+' + str(self.port) + '+' + str(self.timeout_val) + '+' + str(self.fast)

class Ip_nat_range_list(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	local_start_ipv4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	local_netmaskv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	global_start_ipv4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	global_netmaskv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	count=PosRangedInteger(1, 200000)
	vrid=PosRangedInteger(1, 31)
	local_start_ipv6_addr=SizedString(1, 255)
	global_start_ipv6_addr=SizedString(1, 255)
	def __init__(self, name, local_start_ipv4_addr, local_netmaskv4, global_start_ipv4_addr, global_netmaskv4, count, local_start_ipv6_addr, global_start_ipv6_addr, vrid=None):
		self.name = name
		self.local_start_ipv4_addr = local_start_ipv4_addr
		self.local_netmaskv4 = local_netmaskv4
		self.global_start_ipv4_addr = global_start_ipv4_addr
		self.global_netmaskv4 = global_netmaskv4
		self.count = count
		self.vrid = vrid
		self.local_start_ipv6_addr = local_start_ipv6_addr
		self.global_start_ipv6_addr = global_start_ipv6_addr

	def __str__(self):
		return str(self.name) + '+' + str(self.local_start_ipv4_addr) + '+' + str(self.local_netmaskv4) + '+' + str(self.global_start_ipv4_addr) + '+' + str(self.global_netmaskv4) + '+' + str(self.count) + '+' + str(self.local_start_ipv6_addr) + '+' + str(self.global_start_ipv6_addr)

class IpNatClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpNat(self):
		"""
		Retrieve the nat identified by the specified identifier
		
		Returns:
			An instance of the Nat class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified nat does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('nat')
		return deserialize_Nat_json(payload)

