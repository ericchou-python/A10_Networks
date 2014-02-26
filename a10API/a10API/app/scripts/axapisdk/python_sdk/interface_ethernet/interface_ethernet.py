########################################################################################################################
# File name: interface_ethernet.py
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
	'https://axapi.a10networks.com/axapi/v3/interface/ethernet',
]

def deserialize_Ethernet__snmp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	snmp_server = data.get('snmp-server')
	trap_source = data.get('trap-source')
	result = Ethernet__snmp_cfg(snmp_server=snmp_server, trap_source=trap_source)
	return result

def deserialize_Ethernet__icmp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp_rate_limit = data.get('icmp-rate-limit')
	normal_val = data.get('normal-val')
	lockup = data.get('lockup')
	lockup_period = data.get('lockup-period')
	result = Ethernet__icmp_cfg(icmp_rate_limit=icmp_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
	return result

def deserialize_Ethernet__icmpv6_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmpv6_rate_limit = data.get('icmpv6-rate-limit')
	normal_val = data.get('normal-val')
	lockup = data.get('lockup')
	lockup_period = data.get('lockup-period')
	result = Ethernet__icmpv6_cfg(icmpv6_rate_limit=icmpv6_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
	return result

def deserialize_Interface_ethernet_monitor_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	monitor = data.get('monitor')
	monitor_vlan = data.get('monitor-vlan')
	result = Interface_ethernet_monitor_cfg(monitor=monitor, monitor_vlan=monitor_vlan)
	return result

def deserialize_list_Interface_ethernet_monitor_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_ethernet_monitor_cfg_json(item))
	return list(container)

def deserialize_Ethernet__lldp__enable_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	rt_enable = data.get('rt-enable')
	rx = data.get('rx')
	tx = data.get('tx')
	result = Ethernet__lldp__enable_cfg(rt_enable=rt_enable, rx=rx, tx=tx)
	return result

def deserialize_Ethernet__lldp__notification_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	notification = data.get('notification')
	notif_enable = data.get('notif-enable')
	result = Ethernet__lldp__notification_cfg(notification=notification, notif_enable=notif_enable)
	return result

def deserialize_Ethernet__lldp__tx_dot1_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tx_dot1_tlvs = data.get('tx-dot1-tlvs')
	link_aggregation = data.get('link-aggregation')
	vlan = data.get('vlan')
	result = Ethernet__lldp__tx_dot1_cfg(tx_dot1_tlvs=tx_dot1_tlvs, link_aggregation=link_aggregation, vlan=vlan)
	return result

def deserialize_Ethernet__lldp__tx_tlvs_cfg_json(obj):
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
	result = Ethernet__lldp__tx_tlvs_cfg(tx_tlvs=tx_tlvs, management_address=management_address, port_description=port_description, system_capabilities=system_capabilities, system_description=system_description, system_name=system_name)
	return result

def deserialize_Ethernet__lldp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable_cfg = deserialize_Ethernet__lldp__enable_cfg_json(data.get('enable-cfg'))
	notification_cfg = deserialize_Ethernet__lldp__notification_cfg_json(data.get('notification-cfg'))
	tx_dot1_cfg = deserialize_Ethernet__lldp__tx_dot1_cfg_json(data.get('tx-dot1-cfg'))
	tx_tlvs_cfg = deserialize_Ethernet__lldp__tx_tlvs_cfg_json(data.get('tx-tlvs-cfg'))
	result = Ethernet__lldp(enable_cfg=enable_cfg, notification_cfg=notification_cfg, tx_dot1_cfg=tx_dot1_cfg, tx_tlvs_cfg=tx_tlvs_cfg)
	return result

def deserialize_Ethernet__lacp__trunk_cfg__mode_cfg_json(obj):
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
	result = Ethernet__lacp__trunk_cfg__mode_cfg(mode=mode, mode_admin=mode_admin, mode_admin_uni=mode_admin_uni, mode_uni=mode_uni, mode_uni_admin=mode_uni_admin)
	return result

def deserialize_Ethernet__lacp__trunk_cfg__admin_key_cfg_json(obj):
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
	result = Ethernet__lacp__trunk_cfg__admin_key_cfg(admin_key=admin_key, admin_uni=admin_uni, admin_uni_mode=admin_uni_mode, admin_mode=admin_mode, admin_mode_uni=admin_mode_uni)
	return result

def deserialize_Ethernet__lacp__trunk_cfg__unidirectional_cfg_json(obj):
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
	result = Ethernet__lacp__trunk_cfg__unidirectional_cfg(unidirectional_detection=unidirectional_detection, uni_admin=uni_admin, uni_admin_mode=uni_admin_mode, uni_mode=uni_mode, uni_mode_admin=uni_mode_admin)
	return result

def deserialize_Ethernet__lacp__trunk_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk = data.get('trunk')
	mode_cfg = deserialize_Ethernet__lacp__trunk_cfg__mode_cfg_json(data.get('mode-cfg'))
	admin_key_cfg = deserialize_Ethernet__lacp__trunk_cfg__admin_key_cfg_json(data.get('admin-key-cfg'))
	unidirectional_cfg = deserialize_Ethernet__lacp__trunk_cfg__unidirectional_cfg_json(data.get('unidirectional-cfg'))
	result = Ethernet__lacp__trunk_cfg(trunk=trunk, mode_cfg=mode_cfg, admin_key_cfg=admin_key_cfg, unidirectional_cfg=unidirectional_cfg)
	return result

def deserialize_Ethernet__lacp__udld_timeout_cfg__fast_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	udld_fast_timeout = data.get('udld-fast-timeout')
	result = Ethernet__lacp__udld_timeout_cfg__fast(udld_fast_timeout=udld_fast_timeout)
	return result

def deserialize_Ethernet__lacp__udld_timeout_cfg__slow_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	udld_slow_timeout = data.get('udld-slow-timeout')
	result = Ethernet__lacp__udld_timeout_cfg__slow(udld_slow_timeout=udld_slow_timeout)
	return result

def deserialize_Ethernet__lacp__udld_timeout_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	udld_timeout = data.get('udld-timeout')
	fast = deserialize_Ethernet__lacp__udld_timeout_cfg__fast_json(data.get('fast'))
	slow = deserialize_Ethernet__lacp__udld_timeout_cfg__slow_json(data.get('slow'))
	result = Ethernet__lacp__udld_timeout_cfg(udld_timeout=udld_timeout, fast=fast, slow=slow)
	return result

def deserialize_Ethernet__lacp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk_cfg = deserialize_Ethernet__lacp__trunk_cfg_json(data.get('trunk-cfg'))
	port_priority = data.get('port-priority')
	timeout = data.get('timeout')
	udld_timeout_cfg = deserialize_Ethernet__lacp__udld_timeout_cfg_json(data.get('udld-timeout-cfg'))
	result = Ethernet__lacp(trunk_cfg=trunk_cfg, port_priority=port_priority, timeout=timeout, udld_timeout_cfg=udld_timeout_cfg)
	return result

def deserialize_Ethernet__ddos_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	outside = data.get('outside')
	inside = data.get('inside')
	result = Ethernet__ddos(outside=outside, inside=inside)
	return result

def deserialize_Interface_ethernet_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4_address = data.get('ipv4-address')
	ipv4_netmask = data.get('ipv4-netmask')
	result = Interface_ethernet_ip_cfg(ipv4_address=ipv4_address, ipv4_netmask=ipv4_netmask)
	return result

def deserialize_list_Interface_ethernet_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_ethernet_ip_cfg_json(item))
	return list(container)

def deserialize_Ethernet__ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_cfg = deserialize_list_Interface_ethernet_ip_cfg_json(data.get('ip-cfg'))
	dhcp = data.get('dhcp')
	result = Ethernet__ip__address(ip_cfg=ip_cfg, dhcp=dhcp)
	return result

def deserialize_Ethernet__ip__nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	inside = data.get('inside')
	outside = data.get('outside')
	result = Ethernet__ip__nat(inside=inside, outside=outside)
	return result

def deserialize_Ethernet__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Ethernet__ip__address_json(data.get('address'))
	cache_spoofing_port = data.get('cache-spoofing-port')
	helper_address = data.get('helper-address')
	nat = deserialize_Ethernet__ip__nat_json(data.get('nat'))
	generate_membership_query = data.get('generate-membership-query')
	generate_membership_query_val = data.get('generate-membership-query-val')
	max_resp_time = data.get('max-resp-time')
	result = Ethernet__ip(address=address, cache_spoofing_port=cache_spoofing_port, helper_address=helper_address, nat=nat, generate_membership_query=generate_membership_query, generate_membership_query_val=generate_membership_query_val, max_resp_time=max_resp_time)
	return result

def deserialize_Interface_ethernet_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	anycast = data.get('anycast')
	link_local = data.get('link-local')
	result = Interface_ethernet_address_cfg(ipv6_addr=ipv6_addr, anycast=anycast, link_local=link_local)
	return result

def deserialize_list_Interface_ethernet_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_ethernet_address_cfg_json(item))
	return list(container)

def deserialize_Ethernet__ipv6__ndisc__router_adver__mtu_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_mtu = data.get('adver-mtu')
	adver_mtu_disable = data.get('adver-mtu-disable')
	result = Ethernet__ipv6__ndisc__router_adver__mtu(adver_mtu=adver_mtu, adver_mtu_disable=adver_mtu_disable)
	return result

def deserialize_Interface_ethernet_prefix_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	prefix = data.get('prefix')
	not_autonomous = data.get('not-autonomous')
	not_on_link = data.get('not-on-link')
	preferred_lifetime = data.get('preferred-lifetime')
	valid_lifetime = data.get('valid-lifetime')
	result = Interface_ethernet_prefix_cfg(prefix=prefix, not_autonomous=not_autonomous, not_on_link=not_on_link, preferred_lifetime=preferred_lifetime, valid_lifetime=valid_lifetime)
	return result

def deserialize_list_Interface_ethernet_prefix_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_ethernet_prefix_cfg_json(item))
	return list(container)

def deserialize_Ethernet__ipv6__ndisc__router_adver__vrid_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_vrid = data.get('adver-vrid')
	adver_vrid_default = data.get('adver-vrid-default')
	use_floating_ip = data.get('use-floating-ip')
	floating_ip = data.get('floating-ip')
	result = Ethernet__ipv6__ndisc__router_adver__vrid(adver_vrid=adver_vrid, adver_vrid_default=adver_vrid_default, use_floating_ip=use_floating_ip, floating_ip=floating_ip)
	return result

def deserialize_Ethernet__ipv6__ndisc__router_adver__ha_group_id_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_ha_group_id = data.get('adver-ha-group-id')
	ha_use_floating_ip = data.get('ha-use-floating-ip')
	ha_floating_ip = data.get('ha-floating-ip')
	result = Ethernet__ipv6__ndisc__router_adver__ha_group_id(adver_ha_group_id=adver_ha_group_id, ha_use_floating_ip=ha_use_floating_ip, ha_floating_ip=ha_floating_ip)
	return result

def deserialize_Ethernet__ipv6__ndisc__router_adver_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_enable = data.get('adver-enable')
	adver_disable = data.get('adver-disable')
	default_lifetime = data.get('default-lifetime')
	hop_limit = data.get('hop-limit')
	max_interval = data.get('max-interval')
	min_interval = data.get('min-interval')
	rate_limit = data.get('rate-limit')
	reachable_time = data.get('reachable-time')
	retransmit_timer = data.get('retransmit-timer')
	mtu = deserialize_Ethernet__ipv6__ndisc__router_adver__mtu_json(data.get('mtu'))
	prefix_cfg = deserialize_list_Interface_ethernet_prefix_cfg_json(data.get('prefix-cfg'))
	vrid = deserialize_Ethernet__ipv6__ndisc__router_adver__vrid_json(data.get('vrid'))
	ha_group_id = deserialize_Ethernet__ipv6__ndisc__router_adver__ha_group_id_json(data.get('ha-group-id'))
	result = Ethernet__ipv6__ndisc__router_adver(adver_enable=adver_enable, adver_disable=adver_disable, default_lifetime=default_lifetime, hop_limit=hop_limit, max_interval=max_interval, min_interval=min_interval, rate_limit=rate_limit, reachable_time=reachable_time, retransmit_timer=retransmit_timer, mtu=mtu, prefix_cfg=prefix_cfg, vrid=vrid, ha_group_id=ha_group_id)
	return result

def deserialize_Ethernet__ipv6__ndisc_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	router_adver = deserialize_Ethernet__ipv6__ndisc__router_adver_json(data.get('router-adver'))
	result = Ethernet__ipv6__ndisc(router_adver=router_adver)
	return result

def deserialize_Ethernet__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_cfg = deserialize_list_Interface_ethernet_address_cfg_json(data.get('address-cfg'))
	ipv6_enable = data.get('ipv6-enable')
	ndisc = deserialize_Ethernet__ipv6__ndisc_json(data.get('ndisc'))
	result = Ethernet__ipv6(address_cfg=address_cfg, ipv6_enable=ipv6_enable, ndisc=ndisc)
	return result

def deserialize_Ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ifnum = data.get('ifnum')
	name = data.get('name')
	l3_vlan_fwd_disable = data.get('l3-vlan-fwd-disable')
	load_interval = data.get('load-interval')
	mtu = data.get('mtu')
	snmp_cfg = deserialize_Ethernet__snmp_cfg_json(data.get('snmp-cfg'))
	duplexity = data.get('duplexity')
	speed = data.get('speed')
	flow_control = data.get('flow-control')
	enable = data.get('enable')
	disable = data.get('disable')
	icmp_cfg = deserialize_Ethernet__icmp_cfg_json(data.get('icmp-cfg'))
	icmpv6_cfg = deserialize_Ethernet__icmpv6_cfg_json(data.get('icmpv6-cfg'))
	monitor_cfg = deserialize_list_Interface_ethernet_monitor_cfg_json(data.get('monitor-cfg'))
	lldp = deserialize_Ethernet__lldp_json(data.get('lldp'))
	lacp = deserialize_Ethernet__lacp_json(data.get('lacp'))
	ddos = deserialize_Ethernet__ddos_json(data.get('ddos'))
	ip = deserialize_Ethernet__ip_json(data.get('ip'))
	ipv6 = deserialize_Ethernet__ipv6_json(data.get('ipv6'))
	result = Ethernet(ifnum=ifnum, name=name, l3_vlan_fwd_disable=l3_vlan_fwd_disable, load_interval=load_interval, mtu=mtu, snmp_cfg=snmp_cfg, duplexity=duplexity, speed=speed, flow_control=flow_control, enable=enable, disable=disable, icmp_cfg=icmp_cfg, icmpv6_cfg=icmpv6_cfg, monitor_cfg=monitor_cfg, lldp=lldp, lacp=lacp, ddos=ddos, ip=ip, ipv6=ipv6)
	return result

def serialize_Ethernet__snmp_cfg_json(obj):
	output = OrderedDict()
	if obj.snmp_server is not None:
		output['snmp-server'] = obj.snmp_server
	if obj.trap_source is not None:
		output['trap-source'] = obj.trap_source
	return output

def serialize_Ethernet__icmp_cfg_json(obj):
	output = OrderedDict()
	if obj.icmp_rate_limit is not None:
		output['icmp-rate-limit'] = obj.icmp_rate_limit
	if obj.normal_val is not None:
		output['normal-val'] = obj.normal_val
	if obj.lockup is not None:
		output['lockup'] = obj.lockup
	if obj.lockup_period is not None:
		output['lockup-period'] = obj.lockup_period
	return output

def serialize_Ethernet__icmpv6_cfg_json(obj):
	output = OrderedDict()
	if obj.icmpv6_rate_limit is not None:
		output['icmpv6-rate-limit'] = obj.icmpv6_rate_limit
	if obj.normal_val is not None:
		output['normal-val'] = obj.normal_val
	if obj.lockup is not None:
		output['lockup'] = obj.lockup
	if obj.lockup_period is not None:
		output['lockup-period'] = obj.lockup_period
	return output

def serialize_Interface_ethernet_monitor_cfg_json(obj):
	output = OrderedDict()
	if obj.monitor is not None:
		output['monitor'] = obj.monitor
	if obj.monitor_vlan is not None:
		output['monitor-vlan'] = obj.monitor_vlan
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Interface_ethernet_monitor_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_ethernet_monitor_cfg_json(item))
	return output

def serialize_Ethernet__lldp__enable_cfg_json(obj):
	output = OrderedDict()
	if obj.rt_enable is not None:
		output['rt-enable'] = obj.rt_enable
	if obj.rx is not None:
		output['rx'] = obj.rx
	if obj.tx is not None:
		output['tx'] = obj.tx
	return output

def serialize_Ethernet__lldp__notification_cfg_json(obj):
	output = OrderedDict()
	if obj.notification is not None:
		output['notification'] = obj.notification
	if obj.notif_enable is not None:
		output['notif-enable'] = obj.notif_enable
	return output

def serialize_Ethernet__lldp__tx_dot1_cfg_json(obj):
	output = OrderedDict()
	if obj.tx_dot1_tlvs is not None:
		output['tx-dot1-tlvs'] = obj.tx_dot1_tlvs
	if obj.link_aggregation is not None:
		output['link-aggregation'] = obj.link_aggregation
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	return output

def serialize_Ethernet__lldp__tx_tlvs_cfg_json(obj):
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

def serialize_Ethernet__lldp_json(obj):
	output = OrderedDict()
	if obj.enable_cfg is not None:
		output['enable-cfg'] = serialize_Ethernet__lldp__enable_cfg_json(obj.enable_cfg)
	if obj.notification_cfg is not None:
		output['notification-cfg'] = serialize_Ethernet__lldp__notification_cfg_json(obj.notification_cfg)
	if obj.tx_dot1_cfg is not None:
		output['tx-dot1-cfg'] = serialize_Ethernet__lldp__tx_dot1_cfg_json(obj.tx_dot1_cfg)
	if obj.tx_tlvs_cfg is not None:
		output['tx-tlvs-cfg'] = serialize_Ethernet__lldp__tx_tlvs_cfg_json(obj.tx_tlvs_cfg)
	return output

def serialize_Ethernet__lacp__trunk_cfg__mode_cfg_json(obj):
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

def serialize_Ethernet__lacp__trunk_cfg__admin_key_cfg_json(obj):
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

def serialize_Ethernet__lacp__trunk_cfg__unidirectional_cfg_json(obj):
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

def serialize_Ethernet__lacp__trunk_cfg_json(obj):
	output = OrderedDict()
	if obj.trunk is not None:
		output['trunk'] = obj.trunk
	if obj.mode_cfg is not None:
		output['mode-cfg'] = serialize_Ethernet__lacp__trunk_cfg__mode_cfg_json(obj.mode_cfg)
	if obj.admin_key_cfg is not None:
		output['admin-key-cfg'] = serialize_Ethernet__lacp__trunk_cfg__admin_key_cfg_json(obj.admin_key_cfg)
	if obj.unidirectional_cfg is not None:
		output['unidirectional-cfg'] = serialize_Ethernet__lacp__trunk_cfg__unidirectional_cfg_json(obj.unidirectional_cfg)
	return output

def serialize_Ethernet__lacp__udld_timeout_cfg__fast_json(obj):
	output = OrderedDict()
	if obj.udld_fast_timeout is not None:
		output['udld-fast-timeout'] = obj.udld_fast_timeout
	return output

def serialize_Ethernet__lacp__udld_timeout_cfg__slow_json(obj):
	output = OrderedDict()
	if obj.udld_slow_timeout is not None:
		output['udld-slow-timeout'] = obj.udld_slow_timeout
	return output

def serialize_Ethernet__lacp__udld_timeout_cfg_json(obj):
	output = OrderedDict()
	if obj.udld_timeout is not None:
		output['udld-timeout'] = obj.udld_timeout
	if obj.fast is not None:
		output['fast'] = serialize_Ethernet__lacp__udld_timeout_cfg__fast_json(obj.fast)
	if obj.slow is not None:
		output['slow'] = serialize_Ethernet__lacp__udld_timeout_cfg__slow_json(obj.slow)
	return output

def serialize_Ethernet__lacp_json(obj):
	output = OrderedDict()
	if obj.trunk_cfg is not None:
		output['trunk-cfg'] = serialize_Ethernet__lacp__trunk_cfg_json(obj.trunk_cfg)
	if obj.port_priority is not None:
		output['port-priority'] = obj.port_priority
	if obj.timeout is not None:
		output['timeout'] = obj.timeout
	if obj.udld_timeout_cfg is not None:
		output['udld-timeout-cfg'] = serialize_Ethernet__lacp__udld_timeout_cfg_json(obj.udld_timeout_cfg)
	return output

def serialize_Ethernet__ddos_json(obj):
	output = OrderedDict()
	if obj.outside is not None:
		output['outside'] = obj.outside
	if obj.inside is not None:
		output['inside'] = obj.inside
	return output

def serialize_Interface_ethernet_ip_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv4_address is not None:
		output['ipv4-address'] = obj.ipv4_address
	if obj.ipv4_netmask is not None:
		output['ipv4-netmask'] = obj.ipv4_netmask
	return output

def serialize_list_Interface_ethernet_ip_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_ethernet_ip_cfg_json(item))
	return output

def serialize_Ethernet__ip__address_json(obj):
	output = OrderedDict()
	if obj.ip_cfg is not None:
		output['ip-cfg'] = serialize_list_Interface_ethernet_ip_cfg_json(obj.ip_cfg)
	if obj.dhcp is not None:
		output['dhcp'] = obj.dhcp
	return output

def serialize_Ethernet__ip__nat_json(obj):
	output = OrderedDict()
	if obj.inside is not None:
		output['inside'] = obj.inside
	if obj.outside is not None:
		output['outside'] = obj.outside
	return output

def serialize_Ethernet__ip_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = serialize_Ethernet__ip__address_json(obj.address)
	if obj.cache_spoofing_port is not None:
		output['cache-spoofing-port'] = obj.cache_spoofing_port
	if obj.helper_address is not None:
		output['helper-address'] = obj.helper_address
	if obj.nat is not None:
		output['nat'] = serialize_Ethernet__ip__nat_json(obj.nat)
	if obj.generate_membership_query is not None:
		output['generate-membership-query'] = obj.generate_membership_query
	if obj.generate_membership_query_val is not None:
		output['generate-membership-query-val'] = obj.generate_membership_query_val
	if obj.max_resp_time is not None:
		output['max-resp-time'] = obj.max_resp_time
	return output

def serialize_Interface_ethernet_address_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv6_addr is not None:
		output['ipv6-addr'] = obj.ipv6_addr
	if obj.anycast is not None:
		output['anycast'] = obj.anycast
	if obj.link_local is not None:
		output['link-local'] = obj.link_local
	return output

def serialize_list_Interface_ethernet_address_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_ethernet_address_cfg_json(item))
	return output

def serialize_Ethernet__ipv6__ndisc__router_adver__mtu_json(obj):
	output = OrderedDict()
	if obj.adver_mtu is not None:
		output['adver-mtu'] = obj.adver_mtu
	if obj.adver_mtu_disable is not None:
		output['adver-mtu-disable'] = obj.adver_mtu_disable
	return output

def serialize_Interface_ethernet_prefix_cfg_json(obj):
	output = OrderedDict()
	if obj.prefix is not None:
		output['prefix'] = obj.prefix
	if obj.not_autonomous is not None:
		output['not-autonomous'] = obj.not_autonomous
	if obj.not_on_link is not None:
		output['not-on-link'] = obj.not_on_link
	if obj.preferred_lifetime is not None:
		output['preferred-lifetime'] = obj.preferred_lifetime
	if obj.valid_lifetime is not None:
		output['valid-lifetime'] = obj.valid_lifetime
	return output

def serialize_list_Interface_ethernet_prefix_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_ethernet_prefix_cfg_json(item))
	return output

def serialize_Ethernet__ipv6__ndisc__router_adver__vrid_json(obj):
	output = OrderedDict()
	if obj.adver_vrid is not None:
		output['adver-vrid'] = obj.adver_vrid
	if obj.adver_vrid_default is not None:
		output['adver-vrid-default'] = obj.adver_vrid_default
	if obj.use_floating_ip is not None:
		output['use-floating-ip'] = obj.use_floating_ip
	if obj.floating_ip is not None:
		output['floating-ip'] = obj.floating_ip
	return output

def serialize_Ethernet__ipv6__ndisc__router_adver__ha_group_id_json(obj):
	output = OrderedDict()
	if obj.adver_ha_group_id is not None:
		output['adver-ha-group-id'] = obj.adver_ha_group_id
	if obj.ha_use_floating_ip is not None:
		output['ha-use-floating-ip'] = obj.ha_use_floating_ip
	if obj.ha_floating_ip is not None:
		output['ha-floating-ip'] = obj.ha_floating_ip
	return output

def serialize_Ethernet__ipv6__ndisc__router_adver_json(obj):
	output = OrderedDict()
	if obj.adver_enable is not None:
		output['adver-enable'] = obj.adver_enable
	if obj.adver_disable is not None:
		output['adver-disable'] = obj.adver_disable
	if obj.default_lifetime is not None:
		output['default-lifetime'] = obj.default_lifetime
	if obj.hop_limit is not None:
		output['hop-limit'] = obj.hop_limit
	if obj.max_interval is not None:
		output['max-interval'] = obj.max_interval
	if obj.min_interval is not None:
		output['min-interval'] = obj.min_interval
	if obj.rate_limit is not None:
		output['rate-limit'] = obj.rate_limit
	if obj.reachable_time is not None:
		output['reachable-time'] = obj.reachable_time
	if obj.retransmit_timer is not None:
		output['retransmit-timer'] = obj.retransmit_timer
	if obj.mtu is not None:
		output['mtu'] = serialize_Ethernet__ipv6__ndisc__router_adver__mtu_json(obj.mtu)
	if obj.prefix_cfg is not None:
		output['prefix-cfg'] = serialize_list_Interface_ethernet_prefix_cfg_json(obj.prefix_cfg)
	if obj.vrid is not None:
		output['vrid'] = serialize_Ethernet__ipv6__ndisc__router_adver__vrid_json(obj.vrid)
	if obj.ha_group_id is not None:
		output['ha-group-id'] = serialize_Ethernet__ipv6__ndisc__router_adver__ha_group_id_json(obj.ha_group_id)
	return output

def serialize_Ethernet__ipv6__ndisc_json(obj):
	output = OrderedDict()
	if obj.router_adver is not None:
		output['router-adver'] = serialize_Ethernet__ipv6__ndisc__router_adver_json(obj.router_adver)
	return output

def serialize_Ethernet__ipv6_json(obj):
	output = OrderedDict()
	if obj.address_cfg is not None:
		output['address-cfg'] = serialize_list_Interface_ethernet_address_cfg_json(obj.address_cfg)
	if obj.ipv6_enable is not None:
		output['ipv6-enable'] = obj.ipv6_enable
	if obj.ndisc is not None:
		output['ndisc'] = serialize_Ethernet__ipv6__ndisc_json(obj.ndisc)
	return output

def serialize_Ethernet_json(obj):
	output = OrderedDict()
	output['ifnum'] = obj.ifnum
	if obj.name is not None:
		output['name'] = obj.name
	if obj.l3_vlan_fwd_disable is not None:
		output['l3-vlan-fwd-disable'] = obj.l3_vlan_fwd_disable
	if obj.load_interval is not None:
		output['load-interval'] = obj.load_interval
	if obj.mtu is not None:
		output['mtu'] = obj.mtu
	if obj.snmp_cfg is not None:
		output['snmp-cfg'] = serialize_Ethernet__snmp_cfg_json(obj.snmp_cfg)
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
	if obj.icmp_cfg is not None:
		output['icmp-cfg'] = serialize_Ethernet__icmp_cfg_json(obj.icmp_cfg)
	if obj.icmpv6_cfg is not None:
		output['icmpv6-cfg'] = serialize_Ethernet__icmpv6_cfg_json(obj.icmpv6_cfg)
	if obj.monitor_cfg is not None:
		output['monitor-cfg'] = serialize_list_Interface_ethernet_monitor_cfg_json(obj.monitor_cfg)
	if obj.lldp is not None:
		output['lldp'] = serialize_Ethernet__lldp_json(obj.lldp)
	if obj.lacp is not None:
		output['lacp'] = serialize_Ethernet__lacp_json(obj.lacp)
	if obj.ddos is not None:
		output['ddos'] = serialize_Ethernet__ddos_json(obj.ddos)
	if obj.ip is not None:
		output['ip'] = serialize_Ethernet__ip_json(obj.ip)
	if obj.ipv6 is not None:
		output['ipv6'] = serialize_Ethernet__ipv6_json(obj.ipv6)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ethernet_json(item))
	return list(container)

class Ethernet__snmp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	snmp_server=PosRangedInteger(0, 1)
	trap_source=PosRangedInteger(0, 1)
	def __init__(self, snmp_server=None, trap_source=None):
		self.snmp_server = snmp_server
		self.trap_source = trap_source

	def __str__(self):
		return ""

class Ethernet__icmp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	icmp_rate_limit=PosRangedInteger(0, 1)
	normal_val=PosRangedInteger(1, 65535)
	lockup=PosRangedInteger(1, 65535)
	lockup_period=PosRangedInteger(1, 16383)
	def __init__(self, icmp_rate_limit=None, normal_val=None, lockup=None, lockup_period=None):
		self.icmp_rate_limit = icmp_rate_limit
		self.normal_val = normal_val
		self.lockup = lockup
		self.lockup_period = lockup_period

	def __str__(self):
		return ""

class Ethernet__icmpv6_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	icmpv6_rate_limit=PosRangedInteger(0, 1)
	normal_val=PosRangedInteger(1, 65535)
	lockup=PosRangedInteger(1, 65535)
	lockup_period=PosRangedInteger(1, 16383)
	def __init__(self, icmpv6_rate_limit=None, normal_val=None, lockup=None, lockup_period=None):
		self.icmpv6_rate_limit = icmpv6_rate_limit
		self.normal_val = normal_val
		self.lockup = lockup
		self.lockup_period = lockup_period

	def __str__(self):
		return ""

class Ethernet__lldp__enable_cfg(AxapiObject):
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

class Ethernet__lldp__notification_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	notification=PosRangedInteger(0, 1)
	notif_enable=PosRangedInteger(0, 1)
	def __init__(self, notification=None, notif_enable=None):
		self.notification = notification
		self.notif_enable = notif_enable

	def __str__(self):
		return ""

class Ethernet__lldp__tx_dot1_cfg(AxapiObject):
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

class Ethernet__lldp__tx_tlvs_cfg(AxapiObject):
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

class Ethernet__lldp(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, enable_cfg=None, notification_cfg=None, tx_dot1_cfg=None, tx_tlvs_cfg=None):
		self.enable_cfg = enable_cfg
		self.notification_cfg = notification_cfg
		self.tx_dot1_cfg = tx_dot1_cfg
		self.tx_tlvs_cfg = tx_tlvs_cfg

	def __str__(self):
		return ""

class Ethernet__lacp__trunk_cfg__mode_cfg(AxapiObject):
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

class Ethernet__lacp__trunk_cfg__admin_key_cfg(AxapiObject):
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

class Ethernet__lacp__trunk_cfg__unidirectional_cfg(AxapiObject):
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

class Ethernet__lacp__trunk_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	trunk=PosRangedInteger(1, 16)
	def __init__(self, trunk=None, mode_cfg=None, admin_key_cfg=None, unidirectional_cfg=None):
		self.trunk = trunk
		self.mode_cfg = mode_cfg
		self.admin_key_cfg = admin_key_cfg
		self.unidirectional_cfg = unidirectional_cfg

	def __str__(self):
		return ""

class Ethernet__lacp__udld_timeout_cfg__fast(AxapiObject):
	__metaclass__ = StructMeta 
	udld_fast_timeout=PosRangedInteger(100, 1000)
	def __init__(self, udld_fast_timeout=None):
		self.udld_fast_timeout = udld_fast_timeout

	def __str__(self):
		return ""

class Ethernet__lacp__udld_timeout_cfg__slow(AxapiObject):
	__metaclass__ = StructMeta 
	udld_slow_timeout=PosRangedInteger(1, 60)
	def __init__(self, udld_slow_timeout=None):
		self.udld_slow_timeout = udld_slow_timeout

	def __str__(self):
		return ""

class Ethernet__lacp__udld_timeout_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	udld_timeout=PosRangedInteger(0, 1)
	def __init__(self, udld_timeout=None, fast=None, slow=None):
		self.udld_timeout = udld_timeout
		self.fast = fast
		self.slow = slow

	def __str__(self):
		return ""

class Ethernet__lacp(AxapiObject):
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

class Ethernet__ddos(AxapiObject):
	__metaclass__ = StructMeta 
	outside=PosRangedInteger(0, 1)
	inside=PosRangedInteger(0, 1)
	def __init__(self, outside=None, inside=None):
		self.outside = outside
		self.inside = inside

	def __str__(self):
		return ""

class Ethernet__ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	dhcp=PosRangedInteger(0, 1)
	def __init__(self, ip_cfg=None, dhcp=None):
		self.ip_cfg = ip_cfg
		self.dhcp = dhcp

	def __str__(self):
		return ""

class Ethernet__ip__nat(AxapiObject):
	__metaclass__ = StructMeta 
	inside=PosRangedInteger(0, 1)
	outside=PosRangedInteger(0, 1)
	def __init__(self, inside=None, outside=None):
		self.inside = inside
		self.outside = outside

	def __str__(self):
		return ""

class Ethernet__ip(AxapiObject):
	__metaclass__ = StructMeta 
	cache_spoofing_port=PosRangedInteger(0, 1)
	helper_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	generate_membership_query=PosRangedInteger(0, 1)
	generate_membership_query_val=PosRangedInteger(1, 255)
	max_resp_time=PosRangedInteger(1, 255)
	def __init__(self, address=None, cache_spoofing_port=None, helper_address=None, nat=None, generate_membership_query=None, generate_membership_query_val=None, max_resp_time=None):
		self.address = address
		self.cache_spoofing_port = cache_spoofing_port
		self.helper_address = helper_address
		self.nat = nat
		self.generate_membership_query = generate_membership_query
		self.generate_membership_query_val = generate_membership_query_val
		self.max_resp_time = max_resp_time

	def __str__(self):
		return ""

class Ethernet__ipv6__ndisc__router_adver__mtu(AxapiObject):
	__metaclass__ = StructMeta 
	adver_mtu=PosRangedInteger(1200, 1500)
	adver_mtu_disable=PosRangedInteger(0, 1)
	def __init__(self, adver_mtu=None, adver_mtu_disable=None):
		self.adver_mtu = adver_mtu
		self.adver_mtu_disable = adver_mtu_disable

	def __str__(self):
		return ""

class Ethernet__ipv6__ndisc__router_adver__vrid(AxapiObject):
	__metaclass__ = StructMeta 
	adver_vrid=PosRangedInteger(1, 31)
	adver_vrid_default=PosRangedInteger(0, 1)
	use_floating_ip=PosRangedInteger(0, 1)
	floating_ip=SizedString(1, 255)
	def __init__(self, adver_vrid=None, adver_vrid_default=None, use_floating_ip=None, floating_ip=None):
		self.adver_vrid = adver_vrid
		self.adver_vrid_default = adver_vrid_default
		self.use_floating_ip = use_floating_ip
		self.floating_ip = floating_ip

	def __str__(self):
		return ""

class Ethernet__ipv6__ndisc__router_adver__ha_group_id(AxapiObject):
	__metaclass__ = StructMeta 
	adver_ha_group_id=PosRangedInteger(1, 31)
	ha_use_floating_ip=PosRangedInteger(0, 1)
	ha_floating_ip=SizedString(1, 255)
	def __init__(self, adver_ha_group_id=None, ha_use_floating_ip=None, ha_floating_ip=None):
		self.adver_ha_group_id = adver_ha_group_id
		self.ha_use_floating_ip = ha_use_floating_ip
		self.ha_floating_ip = ha_floating_ip

	def __str__(self):
		return ""

class Ethernet__ipv6__ndisc__router_adver(AxapiObject):
	__metaclass__ = StructMeta 
	adver_enable=PosRangedInteger(0, 1)
	adver_disable=PosRangedInteger(0, 1)
	default_lifetime=PosRangedInteger(0, 9000)
	hop_limit=PosRangedInteger(1, 255)
	max_interval=PosRangedInteger(4, 1800)
	min_interval=PosRangedInteger(3, 1350)
	rate_limit=PosRangedInteger(1, 100000)
	reachable_time=PosRangedInteger(0, 3600000)
	retransmit_timer=PosRangedInteger(0, 4294967295)
	def __init__(self, adver_enable=None, adver_disable=None, default_lifetime=None, hop_limit=None, max_interval=None, min_interval=None, rate_limit=None, reachable_time=None, retransmit_timer=None, mtu=None, prefix_cfg=None, vrid=None, ha_group_id=None):
		self.adver_enable = adver_enable
		self.adver_disable = adver_disable
		self.default_lifetime = default_lifetime
		self.hop_limit = hop_limit
		self.max_interval = max_interval
		self.min_interval = min_interval
		self.rate_limit = rate_limit
		self.reachable_time = reachable_time
		self.retransmit_timer = retransmit_timer
		self.mtu = mtu
		self.prefix_cfg = prefix_cfg
		self.vrid = vrid
		self.ha_group_id = ha_group_id

	def __str__(self):
		return ""

class Ethernet__ipv6__ndisc(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, router_adver=None):
		self.router_adver = router_adver

	def __str__(self):
		return ""

class Ethernet__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_enable=PosRangedInteger(0, 1)
	def __init__(self, address_cfg=None, ipv6_enable=None, ndisc=None):
		self.address_cfg = address_cfg
		self.ipv6_enable = ipv6_enable
		self.ndisc = ndisc

	def __str__(self):
		return ""

class Ethernet(AxapiObject):
	__metaclass__ = StructMeta 
	ifnum=PosRangedInteger(1, 2048)
	name=SizedString(1, 32)
	l3_vlan_fwd_disable=PosRangedInteger(0, 1)
	load_interval=PosRangedInteger(5, 300)
	mtu=PosRangedInteger(1200, 12000)
	duplexity = Enum(['Full', 'Half', 'auto'])
	speed = Enum(['10', '100', '1000', 'auto'])
	flow_control=PosRangedInteger(0, 1)
	enable=PosRangedInteger(0, 1)
	disable=PosRangedInteger(0, 1)
	def __init__(self, ifnum, name=None, l3_vlan_fwd_disable=None, load_interval=None, mtu=None, snmp_cfg=None, duplexity=None, speed=None, flow_control=None, enable=None, disable=None, icmp_cfg=None, icmpv6_cfg=None, monitor_cfg=None, lldp=None, lacp=None, ddos=None, ip=None, ipv6=None):
		self.ifnum = ifnum
		self.name = name
		self.l3_vlan_fwd_disable = l3_vlan_fwd_disable
		self.load_interval = load_interval
		self.mtu = mtu
		self.snmp_cfg = snmp_cfg
		self.duplexity = duplexity
		self.speed = speed
		self.flow_control = flow_control
		self.enable = enable
		self.disable = disable
		self.icmp_cfg = icmp_cfg
		self.icmpv6_cfg = icmpv6_cfg
		self.monitor_cfg = monitor_cfg
		self.lldp = lldp
		self.lacp = lacp
		self.ddos = ddos
		self.ip = ip
		self.ipv6 = ipv6

	def __str__(self):
		return str(self.ifnum)

class Interface_ethernet_monitor_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	monitor = Enum(['input', 'output', 'both'])
	monitor_vlan=PosRangedInteger(2, 4094)
	def __init__(self, monitor=None, monitor_vlan=None):
		self.monitor = monitor
		self.monitor_vlan = monitor_vlan

	def __str__(self):
		return ""

class Interface_ethernet_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv4_netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ipv4_address=None, ipv4_netmask=None):
		self.ipv4_address = ipv4_address
		self.ipv4_netmask = ipv4_netmask

	def __str__(self):
		return ""

class Interface_ethernet_address_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	anycast=PosRangedInteger(0, 1)
	link_local=PosRangedInteger(0, 1)
	def __init__(self, ipv6_addr=None, anycast=None, link_local=None):
		self.ipv6_addr = ipv6_addr
		self.anycast = anycast
		self.link_local = link_local

	def __str__(self):
		return ""

class Ethernet_ifnum(AxapiObject):
	__metaclass__ = StructMeta 
	ifnum=PosRangedInteger(1, 2048)
	def __init__(self, ifnum):
		self.ifnum = ifnum

	def __str__(self):
		return str(self.ifnum)

class Interface_ethernet_prefix_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	prefix=SizedString(1, 255)
	not_autonomous=PosRangedInteger(0, 1)
	not_on_link=PosRangedInteger(0, 1)
	preferred_lifetime=PosRangedInteger(0, 4294967295)
	valid_lifetime=PosRangedInteger(0, 4294967295)
	def __init__(self, prefix=None, not_autonomous=None, not_on_link=None, preferred_lifetime=None, valid_lifetime=None):
		self.prefix = prefix
		self.not_autonomous = not_autonomous
		self.not_on_link = not_on_link
		self.preferred_lifetime = preferred_lifetime
		self.valid_lifetime = valid_lifetime

	def __str__(self):
		return ""

class InterfaceEthernetClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getInterfaceEthernet(self, ethernet_ifnum):
		"""
		Retrieve the ethernet identified by the specified identifier
		
		Args:
			ethernet_ifnum Ethernet_ifnum
		
		Returns:
			An instance of the Ethernet class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(ethernet_ifnum) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ethernet does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ethernet')
		return deserialize_Ethernet_json(payload)

	def putInterfaceEthernet(self, ethernet_ifnum, ethernet):
		"""
		Replace the object ethernet
		
		Args:
			ethernet_ifnum Ethernet_ifnum
			ethernet An instance of the Ethernet class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ethernet']=serialize_Ethernet_json(ethernet)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(ethernet_ifnum) .replace("/", "%2f") + query, payload, headers)
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

	def deleteInterfaceEthernet(self, ethernet_ifnum):
		"""
		Remove the ethernet identified by the specified identifier from the system
		
		Args:
			ethernet_ifnum Ethernet_ifnum
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(ethernet_ifnum) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ethernet does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllInterfaceEthernetsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitInterfaceEthernet(self, ethernet):
		"""
		Create the object ethernet
		
		Args:
			ethernet An instance of the Ethernet class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['ethernet']=serialize_Ethernet_json(ethernet)
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

	def getAllInterfaceEthernets(self):
		"""
		Retrieve all ethernet objects currently pending in the system
		
		Returns:
			A list of Ethernet objects
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
			payload= data.get('ethernetList')
		return deserialize_list_Ethernet_json(payload)

