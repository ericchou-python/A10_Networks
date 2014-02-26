########################################################################################################################
# File name: interface.py
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
	'https://axapi.a10networks.com/axapi/v3/interface',
]

def deserialize_Interface__management__access_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl_id = data.get('acl_id')
	acl_name = data.get('acl-name')
	inbound = data.get('inbound')
	result = Interface__management__access_list(acl_id=acl_id, acl_name=acl_name, inbound=inbound)
	return result

def deserialize_Interface__management__bcast_rate_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	rate = data.get('rate')
	result = Interface__management__bcast_rate_limit(rate=rate)
	return result

def deserialize_Interface__management__lldp__enable_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	rt_enable = data.get('rt-enable')
	rx = data.get('rx')
	tx = data.get('tx')
	result = Interface__management__lldp__enable_cfg(rt_enable=rt_enable, rx=rx, tx=tx)
	return result

def deserialize_Interface__management__lldp__notification_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	notification = data.get('notification')
	notif_enable = data.get('notif-enable')
	result = Interface__management__lldp__notification_cfg(notification=notification, notif_enable=notif_enable)
	return result

def deserialize_Interface__management__lldp__tx_dot1_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tx_dot1_tlvs = data.get('tx-dot1-tlvs')
	link_aggregation = data.get('link-aggregation')
	vlan = data.get('vlan')
	result = Interface__management__lldp__tx_dot1_cfg(tx_dot1_tlvs=tx_dot1_tlvs, link_aggregation=link_aggregation, vlan=vlan)
	return result

def deserialize_Interface__management__lldp__tx_tlvs_cfg_json(obj):
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
	result = Interface__management__lldp__tx_tlvs_cfg(tx_tlvs=tx_tlvs, management_address=management_address, port_description=port_description, system_capabilities=system_capabilities, system_description=system_description, system_name=system_name)
	return result

def deserialize_Interface__management__lldp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable_cfg = deserialize_Interface__management__lldp__enable_cfg_json(data.get('enable-cfg'))
	notification_cfg = deserialize_Interface__management__lldp__notification_cfg_json(data.get('notification-cfg'))
	tx_dot1_cfg = deserialize_Interface__management__lldp__tx_dot1_cfg_json(data.get('tx-dot1-cfg'))
	tx_tlvs_cfg = deserialize_Interface__management__lldp__tx_tlvs_cfg_json(data.get('tx-tlvs-cfg'))
	result = Interface__management__lldp(enable_cfg=enable_cfg, notification_cfg=notification_cfg, tx_dot1_cfg=tx_dot1_cfg, tx_tlvs_cfg=tx_tlvs_cfg)
	return result

def deserialize_Interface__management__ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val = data.get('address_val')
	netmask = data.get('netmask')
	dhcp = data.get('dhcp')
	result = Interface__management__ip__address(address_val=address_val, netmask=netmask, dhcp=dhcp)
	return result

def deserialize_Interface__management__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Interface__management__ip__address_json(data.get('address'))
	control_apps_use_mgmt_port = data.get('control-apps-use-mgmt-port')
	default_gateway = data.get('default-gateway')
	result = Interface__management__ip(address=address, control_apps_use_mgmt_port=control_apps_use_mgmt_port, default_gateway=default_gateway)
	return result

def deserialize_Interface__management__ipv6_json(obj):
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
	result = Interface__management__ipv6(ipv6_addr=ipv6_addr, v6_acl_name=v6_acl_name, inbound=inbound, default_v6_gw=default_v6_gw)
	return result

def deserialize_Interface__management_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	access_list = deserialize_Interface__management__access_list_json(data.get('access-list'))
	duplexity = data.get('duplexity')
	speed = data.get('speed')
	flow_control = data.get('flow-control')
	enable = data.get('enable')
	disable = data.get('disable')
	bcast_rate_limit = deserialize_Interface__management__bcast_rate_limit_json(data.get('bcast-rate-limit'))
	lldp = deserialize_Interface__management__lldp_json(data.get('lldp'))
	ip = deserialize_Interface__management__ip_json(data.get('ip'))
	ipv6 = deserialize_Interface__management__ipv6_json(data.get('ipv6'))
	result = Interface__management(access_list=access_list, duplexity=duplexity, speed=speed, flow_control=flow_control, enable=enable, disable=disable, bcast_rate_limit=bcast_rate_limit, lldp=lldp, ip=ip, ipv6=ipv6)
	return result

def deserialize_Interface_ethernet__snmp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	snmp_server = data.get('snmp-server')
	trap_source = data.get('trap-source')
	result = Interface_ethernet__snmp_cfg(snmp_server=snmp_server, trap_source=trap_source)
	return result

def deserialize_Interface_ethernet__icmp_cfg_json(obj):
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
	result = Interface_ethernet__icmp_cfg(icmp_rate_limit=icmp_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
	return result

def deserialize_Interface_ethernet__icmpv6_cfg_json(obj):
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
	result = Interface_ethernet__icmpv6_cfg(icmpv6_rate_limit=icmpv6_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
	return result

def deserialize_Interface_monitor_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	monitor = data.get('monitor')
	monitor_vlan = data.get('monitor-vlan')
	result = Interface_monitor_cfg(monitor=monitor, monitor_vlan=monitor_vlan)
	return result

def deserialize_list_Interface_monitor_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_monitor_cfg_json(item))
	return list(container)

def deserialize_Interface_ethernet__lldp__enable_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	rt_enable = data.get('rt-enable')
	rx = data.get('rx')
	tx = data.get('tx')
	result = Interface_ethernet__lldp__enable_cfg(rt_enable=rt_enable, rx=rx, tx=tx)
	return result

def deserialize_Interface_ethernet__lldp__notification_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	notification = data.get('notification')
	notif_enable = data.get('notif-enable')
	result = Interface_ethernet__lldp__notification_cfg(notification=notification, notif_enable=notif_enable)
	return result

def deserialize_Interface_ethernet__lldp__tx_dot1_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tx_dot1_tlvs = data.get('tx-dot1-tlvs')
	link_aggregation = data.get('link-aggregation')
	vlan = data.get('vlan')
	result = Interface_ethernet__lldp__tx_dot1_cfg(tx_dot1_tlvs=tx_dot1_tlvs, link_aggregation=link_aggregation, vlan=vlan)
	return result

def deserialize_Interface_ethernet__lldp__tx_tlvs_cfg_json(obj):
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
	result = Interface_ethernet__lldp__tx_tlvs_cfg(tx_tlvs=tx_tlvs, management_address=management_address, port_description=port_description, system_capabilities=system_capabilities, system_description=system_description, system_name=system_name)
	return result

def deserialize_Interface_ethernet__lldp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable_cfg = deserialize_Interface_ethernet__lldp__enable_cfg_json(data.get('enable-cfg'))
	notification_cfg = deserialize_Interface_ethernet__lldp__notification_cfg_json(data.get('notification-cfg'))
	tx_dot1_cfg = deserialize_Interface_ethernet__lldp__tx_dot1_cfg_json(data.get('tx-dot1-cfg'))
	tx_tlvs_cfg = deserialize_Interface_ethernet__lldp__tx_tlvs_cfg_json(data.get('tx-tlvs-cfg'))
	result = Interface_ethernet__lldp(enable_cfg=enable_cfg, notification_cfg=notification_cfg, tx_dot1_cfg=tx_dot1_cfg, tx_tlvs_cfg=tx_tlvs_cfg)
	return result

def deserialize_Interface_ethernet__lacp__trunk_cfg__mode_cfg_json(obj):
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
	result = Interface_ethernet__lacp__trunk_cfg__mode_cfg(mode=mode, mode_admin=mode_admin, mode_admin_uni=mode_admin_uni, mode_uni=mode_uni, mode_uni_admin=mode_uni_admin)
	return result

def deserialize_Interface_ethernet__lacp__trunk_cfg__admin_key_cfg_json(obj):
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
	result = Interface_ethernet__lacp__trunk_cfg__admin_key_cfg(admin_key=admin_key, admin_uni=admin_uni, admin_uni_mode=admin_uni_mode, admin_mode=admin_mode, admin_mode_uni=admin_mode_uni)
	return result

def deserialize_Interface_ethernet__lacp__trunk_cfg__unidirectional_cfg_json(obj):
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
	result = Interface_ethernet__lacp__trunk_cfg__unidirectional_cfg(unidirectional_detection=unidirectional_detection, uni_admin=uni_admin, uni_admin_mode=uni_admin_mode, uni_mode=uni_mode, uni_mode_admin=uni_mode_admin)
	return result

def deserialize_Interface_ethernet__lacp__trunk_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk = data.get('trunk')
	mode_cfg = deserialize_Interface_ethernet__lacp__trunk_cfg__mode_cfg_json(data.get('mode-cfg'))
	admin_key_cfg = deserialize_Interface_ethernet__lacp__trunk_cfg__admin_key_cfg_json(data.get('admin-key-cfg'))
	unidirectional_cfg = deserialize_Interface_ethernet__lacp__trunk_cfg__unidirectional_cfg_json(data.get('unidirectional-cfg'))
	result = Interface_ethernet__lacp__trunk_cfg(trunk=trunk, mode_cfg=mode_cfg, admin_key_cfg=admin_key_cfg, unidirectional_cfg=unidirectional_cfg)
	return result

def deserialize_Interface_ethernet__lacp__udld_timeout_cfg__fast_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	udld_fast_timeout = data.get('udld-fast-timeout')
	result = Interface_ethernet__lacp__udld_timeout_cfg__fast(udld_fast_timeout=udld_fast_timeout)
	return result

def deserialize_Interface_ethernet__lacp__udld_timeout_cfg__slow_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	udld_slow_timeout = data.get('udld-slow-timeout')
	result = Interface_ethernet__lacp__udld_timeout_cfg__slow(udld_slow_timeout=udld_slow_timeout)
	return result

def deserialize_Interface_ethernet__lacp__udld_timeout_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	udld_timeout = data.get('udld-timeout')
	fast = deserialize_Interface_ethernet__lacp__udld_timeout_cfg__fast_json(data.get('fast'))
	slow = deserialize_Interface_ethernet__lacp__udld_timeout_cfg__slow_json(data.get('slow'))
	result = Interface_ethernet__lacp__udld_timeout_cfg(udld_timeout=udld_timeout, fast=fast, slow=slow)
	return result

def deserialize_Interface_ethernet__lacp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk_cfg = deserialize_Interface_ethernet__lacp__trunk_cfg_json(data.get('trunk-cfg'))
	port_priority = data.get('port-priority')
	timeout = data.get('timeout')
	udld_timeout_cfg = deserialize_Interface_ethernet__lacp__udld_timeout_cfg_json(data.get('udld-timeout-cfg'))
	result = Interface_ethernet__lacp(trunk_cfg=trunk_cfg, port_priority=port_priority, timeout=timeout, udld_timeout_cfg=udld_timeout_cfg)
	return result

def deserialize_Interface_ethernet__ddos_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	outside = data.get('outside')
	inside = data.get('inside')
	result = Interface_ethernet__ddos(outside=outside, inside=inside)
	return result

def deserialize_Interface_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4_address = data.get('ipv4-address')
	ipv4_netmask = data.get('ipv4-netmask')
	result = Interface_ip_cfg(ipv4_address=ipv4_address, ipv4_netmask=ipv4_netmask)
	return result

def deserialize_list_Interface_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_ip_cfg_json(item))
	return list(container)

def deserialize_Interface_ethernet__ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_cfg = deserialize_list_Interface_ip_cfg_json(data.get('ip-cfg'))
	dhcp = data.get('dhcp')
	result = Interface_ethernet__ip__address(ip_cfg=ip_cfg, dhcp=dhcp)
	return result

def deserialize_Interface_ethernet__ip__nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	inside = data.get('inside')
	outside = data.get('outside')
	result = Interface_ethernet__ip__nat(inside=inside, outside=outside)
	return result

def deserialize_Interface_ethernet__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Interface_ethernet__ip__address_json(data.get('address'))
	cache_spoofing_port = data.get('cache-spoofing-port')
	helper_address = data.get('helper-address')
	nat = deserialize_Interface_ethernet__ip__nat_json(data.get('nat'))
	generate_membership_query = data.get('generate-membership-query')
	generate_membership_query_val = data.get('generate-membership-query-val')
	max_resp_time = data.get('max-resp-time')
	result = Interface_ethernet__ip(address=address, cache_spoofing_port=cache_spoofing_port, helper_address=helper_address, nat=nat, generate_membership_query=generate_membership_query, generate_membership_query_val=generate_membership_query_val, max_resp_time=max_resp_time)
	return result

def deserialize_Interface_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	anycast = data.get('anycast')
	link_local = data.get('link-local')
	result = Interface_address_cfg(ipv6_addr=ipv6_addr, anycast=anycast, link_local=link_local)
	return result

def deserialize_list_Interface_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_address_cfg_json(item))
	return list(container)

def deserialize_Interface_ethernet__ipv6__ndisc__router_adver__mtu_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_mtu = data.get('adver-mtu')
	adver_mtu_disable = data.get('adver-mtu-disable')
	result = Interface_ethernet__ipv6__ndisc__router_adver__mtu(adver_mtu=adver_mtu, adver_mtu_disable=adver_mtu_disable)
	return result

def deserialize_Interface_prefix_cfg_json(obj):
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
	result = Interface_prefix_cfg(prefix=prefix, not_autonomous=not_autonomous, not_on_link=not_on_link, preferred_lifetime=preferred_lifetime, valid_lifetime=valid_lifetime)
	return result

def deserialize_list_Interface_prefix_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_prefix_cfg_json(item))
	return list(container)

def deserialize_Interface_ethernet__ipv6__ndisc__router_adver__vrid_json(obj):
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
	result = Interface_ethernet__ipv6__ndisc__router_adver__vrid(adver_vrid=adver_vrid, adver_vrid_default=adver_vrid_default, use_floating_ip=use_floating_ip, floating_ip=floating_ip)
	return result

def deserialize_Interface_ethernet__ipv6__ndisc__router_adver__ha_group_id_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_ha_group_id = data.get('adver-ha-group-id')
	ha_use_floating_ip = data.get('ha-use-floating-ip')
	ha_floating_ip = data.get('ha-floating-ip')
	result = Interface_ethernet__ipv6__ndisc__router_adver__ha_group_id(adver_ha_group_id=adver_ha_group_id, ha_use_floating_ip=ha_use_floating_ip, ha_floating_ip=ha_floating_ip)
	return result

def deserialize_Interface_ethernet__ipv6__ndisc__router_adver_json(obj):
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
	mtu = deserialize_Interface_ethernet__ipv6__ndisc__router_adver__mtu_json(data.get('mtu'))
	prefix_cfg = deserialize_list_Interface_prefix_cfg_json(data.get('prefix-cfg'))
	vrid = deserialize_Interface_ethernet__ipv6__ndisc__router_adver__vrid_json(data.get('vrid'))
	ha_group_id = deserialize_Interface_ethernet__ipv6__ndisc__router_adver__ha_group_id_json(data.get('ha-group-id'))
	result = Interface_ethernet__ipv6__ndisc__router_adver(adver_enable=adver_enable, adver_disable=adver_disable, default_lifetime=default_lifetime, hop_limit=hop_limit, max_interval=max_interval, min_interval=min_interval, rate_limit=rate_limit, reachable_time=reachable_time, retransmit_timer=retransmit_timer, mtu=mtu, prefix_cfg=prefix_cfg, vrid=vrid, ha_group_id=ha_group_id)
	return result

def deserialize_Interface_ethernet__ipv6__ndisc_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	router_adver = deserialize_Interface_ethernet__ipv6__ndisc__router_adver_json(data.get('router-adver'))
	result = Interface_ethernet__ipv6__ndisc(router_adver=router_adver)
	return result

def deserialize_Interface_ethernet__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_cfg = deserialize_list_Interface_address_cfg_json(data.get('address-cfg'))
	ipv6_enable = data.get('ipv6-enable')
	ndisc = deserialize_Interface_ethernet__ipv6__ndisc_json(data.get('ndisc'))
	result = Interface_ethernet__ipv6(address_cfg=address_cfg, ipv6_enable=ipv6_enable, ndisc=ndisc)
	return result

def deserialize_Interface_ethernet_json(obj):
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
	snmp_cfg = deserialize_Interface_ethernet__snmp_cfg_json(data.get('snmp-cfg'))
	duplexity = data.get('duplexity')
	speed = data.get('speed')
	flow_control = data.get('flow-control')
	enable = data.get('enable')
	disable = data.get('disable')
	icmp_cfg = deserialize_Interface_ethernet__icmp_cfg_json(data.get('icmp-cfg'))
	icmpv6_cfg = deserialize_Interface_ethernet__icmpv6_cfg_json(data.get('icmpv6-cfg'))
	monitor_cfg = deserialize_list_Interface_monitor_cfg_json(data.get('monitor-cfg'))
	lldp = deserialize_Interface_ethernet__lldp_json(data.get('lldp'))
	lacp = deserialize_Interface_ethernet__lacp_json(data.get('lacp'))
	ddos = deserialize_Interface_ethernet__ddos_json(data.get('ddos'))
	ip = deserialize_Interface_ethernet__ip_json(data.get('ip'))
	ipv6 = deserialize_Interface_ethernet__ipv6_json(data.get('ipv6'))
	result = Interface_ethernet(ifnum=ifnum, name=name, l3_vlan_fwd_disable=l3_vlan_fwd_disable, load_interval=load_interval, mtu=mtu, snmp_cfg=snmp_cfg, duplexity=duplexity, speed=speed, flow_control=flow_control, enable=enable, disable=disable, icmp_cfg=icmp_cfg, icmpv6_cfg=icmpv6_cfg, monitor_cfg=monitor_cfg, lldp=lldp, lacp=lacp, ddos=ddos, ip=ip, ipv6=ipv6)
	return result

def deserialize_list_Interface_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_ethernet_json(item))
	return list(container)

def deserialize_Interface_trunk__icmp_cfg_json(obj):
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
	result = Interface_trunk__icmp_cfg(icmp_rate_limit=icmp_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
	return result

def deserialize_Interface_trunk__icmpv6_cfg_json(obj):
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
	result = Interface_trunk__icmpv6_cfg(icmpv6_rate_limit=icmpv6_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
	return result

def deserialize_Interface_address_val_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val = data.get('address_val')
	netmask = data.get('netmask')
	result = Interface_address_val_cfg(address_val=address_val, netmask=netmask)
	return result

def deserialize_list_Interface_address_val_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_address_val_cfg_json(item))
	return list(container)

def deserialize_Interface_trunk__ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val_cfg = deserialize_list_Interface_address_val_cfg_json(data.get('address_val-cfg'))
	dhcp = data.get('dhcp')
	result = Interface_trunk__ip__address(address_val_cfg=address_val_cfg, dhcp=dhcp)
	return result

def deserialize_Interface_trunk__ip__nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	inside = data.get('inside')
	outside = data.get('outside')
	result = Interface_trunk__ip__nat(inside=inside, outside=outside)
	return result

def deserialize_Interface_trunk__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Interface_trunk__ip__address_json(data.get('address'))
	cache_spoofing_port = data.get('cache-spoofing-port')
	helper_address = data.get('helper-address')
	nat = deserialize_Interface_trunk__ip__nat_json(data.get('nat'))
	generate_membership_query = data.get('generate-membership-query')
	generate_membership_query_val = data.get('generate-membership-query-val')
	max_resp_time = data.get('max-resp-time')
	result = Interface_trunk__ip(address=address, cache_spoofing_port=cache_spoofing_port, helper_address=helper_address, nat=nat, generate_membership_query=generate_membership_query, generate_membership_query_val=generate_membership_query_val, max_resp_time=max_resp_time)
	return result

def deserialize_Interface_trunk__ipv6__nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	inside = data.get('inside')
	outside = data.get('outside')
	result = Interface_trunk__ipv6__nat(inside=inside, outside=outside)
	return result

def deserialize_Interface_trunk__ipv6__ndisc__router_adver__mtu_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_mtu = data.get('adver-mtu')
	adver_mtu_disable = data.get('adver-mtu-disable')
	result = Interface_trunk__ipv6__ndisc__router_adver__mtu(adver_mtu=adver_mtu, adver_mtu_disable=adver_mtu_disable)
	return result

def deserialize_Interface_trunk__ipv6__ndisc__router_adver__vrid_json(obj):
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
	result = Interface_trunk__ipv6__ndisc__router_adver__vrid(adver_vrid=adver_vrid, adver_vrid_default=adver_vrid_default, use_floating_ip=use_floating_ip, floating_ip=floating_ip)
	return result

def deserialize_Interface_trunk__ipv6__ndisc__router_adver__ha_group_id_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_ha_group_id = data.get('adver-ha-group-id')
	ha_use_floating_ip = data.get('ha-use-floating-ip')
	ha_floating_ip = data.get('ha-floating-ip')
	result = Interface_trunk__ipv6__ndisc__router_adver__ha_group_id(adver_ha_group_id=adver_ha_group_id, ha_use_floating_ip=ha_use_floating_ip, ha_floating_ip=ha_floating_ip)
	return result

def deserialize_Interface_trunk__ipv6__ndisc__router_adver_json(obj):
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
	mtu = deserialize_Interface_trunk__ipv6__ndisc__router_adver__mtu_json(data.get('mtu'))
	prefix_cfg = deserialize_list_Interface_prefix_cfg_json(data.get('prefix-cfg'))
	vrid = deserialize_Interface_trunk__ipv6__ndisc__router_adver__vrid_json(data.get('vrid'))
	ha_group_id = deserialize_Interface_trunk__ipv6__ndisc__router_adver__ha_group_id_json(data.get('ha-group-id'))
	result = Interface_trunk__ipv6__ndisc__router_adver(adver_enable=adver_enable, adver_disable=adver_disable, default_lifetime=default_lifetime, hop_limit=hop_limit, max_interval=max_interval, min_interval=min_interval, rate_limit=rate_limit, reachable_time=reachable_time, retransmit_timer=retransmit_timer, mtu=mtu, prefix_cfg=prefix_cfg, vrid=vrid, ha_group_id=ha_group_id)
	return result

def deserialize_Interface_trunk__ipv6__ndisc_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	router_adver = deserialize_Interface_trunk__ipv6__ndisc__router_adver_json(data.get('router-adver'))
	result = Interface_trunk__ipv6__ndisc(router_adver=router_adver)
	return result

def deserialize_Interface_trunk__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_cfg = deserialize_list_Interface_address_cfg_json(data.get('address-cfg'))
	ipv6_enable = data.get('ipv6-enable')
	nat = deserialize_Interface_trunk__ipv6__nat_json(data.get('nat'))
	ndisc = deserialize_Interface_trunk__ipv6__ndisc_json(data.get('ndisc'))
	result = Interface_trunk__ipv6(address_cfg=address_cfg, ipv6_enable=ipv6_enable, nat=nat, ndisc=ndisc)
	return result

def deserialize_Interface_trunk__ddos_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	outside = data.get('outside')
	inside = data.get('inside')
	result = Interface_trunk__ddos(outside=outside, inside=inside)
	return result

def deserialize_Interface_trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ifnum = data.get('ifnum')
	name = data.get('name')
	l3_vlan_fwd_disable = data.get('l3-vlan-fwd-disable')
	mtu = data.get('mtu')
	action = data.get('action')
	icmp_cfg = deserialize_Interface_trunk__icmp_cfg_json(data.get('icmp-cfg'))
	icmpv6_cfg = deserialize_Interface_trunk__icmpv6_cfg_json(data.get('icmpv6-cfg'))
	ip = deserialize_Interface_trunk__ip_json(data.get('ip'))
	ipv6 = deserialize_Interface_trunk__ipv6_json(data.get('ipv6'))
	ddos = deserialize_Interface_trunk__ddos_json(data.get('ddos'))
	result = Interface_trunk(ifnum=ifnum, name=name, l3_vlan_fwd_disable=l3_vlan_fwd_disable, mtu=mtu, action=action, icmp_cfg=icmp_cfg, icmpv6_cfg=icmpv6_cfg, ip=ip, ipv6=ipv6, ddos=ddos)
	return result

def deserialize_list_Interface_trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_trunk_json(item))
	return list(container)

def deserialize_Interface_ve__snmp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	snmp_server = data.get('snmp-server')
	trap_source = data.get('trap-source')
	result = Interface_ve__snmp_cfg(snmp_server=snmp_server, trap_source=trap_source)
	return result

def deserialize_Interface_ve__icmp_cfg_json(obj):
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
	result = Interface_ve__icmp_cfg(icmp_rate_limit=icmp_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
	return result

def deserialize_Interface_ve__icmpv6_cfg_json(obj):
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
	result = Interface_ve__icmpv6_cfg(icmpv6_rate_limit=icmpv6_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
	return result

def deserialize_Interface_ve__ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val_cfg = deserialize_list_Interface_address_val_cfg_json(data.get('address_val-cfg'))
	dhcp = data.get('dhcp')
	result = Interface_ve__ip__address(address_val_cfg=address_val_cfg, dhcp=dhcp)
	return result

def deserialize_Interface_ve__ip__nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	inside = data.get('inside')
	outside = data.get('outside')
	result = Interface_ve__ip__nat(inside=inside, outside=outside)
	return result

def deserialize_Interface_ve__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Interface_ve__ip__address_json(data.get('address'))
	helper_address = data.get('helper-address')
	nat = deserialize_Interface_ve__ip__nat_json(data.get('nat'))
	generate_membership_query = data.get('generate-membership-query')
	generate_membership_query_val = data.get('generate-membership-query-val')
	max_resp_time = data.get('max-resp-time')
	result = Interface_ve__ip(address=address, helper_address=helper_address, nat=nat, generate_membership_query=generate_membership_query, generate_membership_query_val=generate_membership_query_val, max_resp_time=max_resp_time)
	return result

def deserialize_Interface_ve__ipv6__nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	inside = data.get('inside')
	outside = data.get('outside')
	result = Interface_ve__ipv6__nat(inside=inside, outside=outside)
	return result

def deserialize_Interface_ve__ipv6__ndisc__router_adver__mtu_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_mtu = data.get('adver-mtu')
	adver_mtu_disable = data.get('adver-mtu-disable')
	result = Interface_ve__ipv6__ndisc__router_adver__mtu(adver_mtu=adver_mtu, adver_mtu_disable=adver_mtu_disable)
	return result

def deserialize_Interface_ve__ipv6__ndisc__router_adver__vrid_json(obj):
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
	result = Interface_ve__ipv6__ndisc__router_adver__vrid(adver_vrid=adver_vrid, adver_vrid_default=adver_vrid_default, use_floating_ip=use_floating_ip, floating_ip=floating_ip)
	return result

def deserialize_Interface_ve__ipv6__ndisc__router_adver__ha_group_id_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_ha_group_id = data.get('adver-ha-group-id')
	ha_use_floating_ip = data.get('ha-use-floating-ip')
	ha_floating_ip = data.get('ha-floating-ip')
	result = Interface_ve__ipv6__ndisc__router_adver__ha_group_id(adver_ha_group_id=adver_ha_group_id, ha_use_floating_ip=ha_use_floating_ip, ha_floating_ip=ha_floating_ip)
	return result

def deserialize_Interface_ve__ipv6__ndisc__router_adver_json(obj):
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
	mtu = deserialize_Interface_ve__ipv6__ndisc__router_adver__mtu_json(data.get('mtu'))
	prefix_cfg = deserialize_list_Interface_prefix_cfg_json(data.get('prefix-cfg'))
	vrid = deserialize_Interface_ve__ipv6__ndisc__router_adver__vrid_json(data.get('vrid'))
	ha_group_id = deserialize_Interface_ve__ipv6__ndisc__router_adver__ha_group_id_json(data.get('ha-group-id'))
	result = Interface_ve__ipv6__ndisc__router_adver(adver_enable=adver_enable, adver_disable=adver_disable, default_lifetime=default_lifetime, hop_limit=hop_limit, max_interval=max_interval, min_interval=min_interval, rate_limit=rate_limit, reachable_time=reachable_time, retransmit_timer=retransmit_timer, mtu=mtu, prefix_cfg=prefix_cfg, vrid=vrid, ha_group_id=ha_group_id)
	return result

def deserialize_Interface_ve__ipv6__ndisc_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	router_adver = deserialize_Interface_ve__ipv6__ndisc__router_adver_json(data.get('router-adver'))
	result = Interface_ve__ipv6__ndisc(router_adver=router_adver)
	return result

def deserialize_Interface_ve__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_cfg = deserialize_list_Interface_address_cfg_json(data.get('address-cfg'))
	ipv6_enable = data.get('ipv6-enable')
	nat = deserialize_Interface_ve__ipv6__nat_json(data.get('nat'))
	ndisc = deserialize_Interface_ve__ipv6__ndisc_json(data.get('ndisc'))
	result = Interface_ve__ipv6(address_cfg=address_cfg, ipv6_enable=ipv6_enable, nat=nat, ndisc=ndisc)
	return result

def deserialize_Interface_ve__ddos_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	outside = data.get('outside')
	inside = data.get('inside')
	result = Interface_ve__ddos(outside=outside, inside=inside)
	return result

def deserialize_Interface_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ifnum = data.get('ifnum')
	name = data.get('name')
	l3_vlan_fwd_disable = data.get('l3-vlan-fwd-disable')
	mtu = data.get('mtu')
	snmp_cfg = deserialize_Interface_ve__snmp_cfg_json(data.get('snmp-cfg'))
	action = data.get('action')
	icmp_cfg = deserialize_Interface_ve__icmp_cfg_json(data.get('icmp-cfg'))
	icmpv6_cfg = deserialize_Interface_ve__icmpv6_cfg_json(data.get('icmpv6-cfg'))
	ip = deserialize_Interface_ve__ip_json(data.get('ip'))
	ipv6 = deserialize_Interface_ve__ipv6_json(data.get('ipv6'))
	ddos = deserialize_Interface_ve__ddos_json(data.get('ddos'))
	result = Interface_ve(ifnum=ifnum, name=name, l3_vlan_fwd_disable=l3_vlan_fwd_disable, mtu=mtu, snmp_cfg=snmp_cfg, action=action, icmp_cfg=icmp_cfg, icmpv6_cfg=icmpv6_cfg, ip=ip, ipv6=ipv6, ddos=ddos)
	return result

def deserialize_list_Interface_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_ve_json(item))
	return list(container)

def deserialize_Interface_loopback__snmp_server_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	snmp_server = data.get('snmp-server')
	trap_source = data.get('trap-source')
	result = Interface_loopback__snmp_server_cfg(snmp_server=snmp_server, trap_source=trap_source)
	return result

def deserialize_Interface_loopback__ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val_cfg = deserialize_list_Interface_address_val_cfg_json(data.get('address_val-cfg'))
	result = Interface_loopback__ip__address(address_val_cfg=address_val_cfg)
	return result

def deserialize_Interface_loopback__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Interface_loopback__ip__address_json(data.get('address'))
	result = Interface_loopback__ip(address=address)
	return result

def deserialize_Interface_loopback__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_cfg = deserialize_list_Interface_address_cfg_json(data.get('address-cfg'))
	ipv6_enable = data.get('ipv6-enable')
	result = Interface_loopback__ipv6(address_cfg=address_cfg, ipv6_enable=ipv6_enable)
	return result

def deserialize_Interface_loopback_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ifnum = data.get('ifnum')
	snmp_server_cfg = deserialize_Interface_loopback__snmp_server_cfg_json(data.get('snmp-server-cfg'))
	ip = deserialize_Interface_loopback__ip_json(data.get('ip'))
	ipv6 = deserialize_Interface_loopback__ipv6_json(data.get('ipv6'))
	result = Interface_loopback(ifnum=ifnum, snmp_server_cfg=snmp_server_cfg, ip=ip, ipv6=ipv6)
	return result

def deserialize_list_Interface_loopback_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_loopback_json(item))
	return list(container)

def deserialize_Interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	management = deserialize_Interface__management_json(data.get('management'))
	ethernetlist = deserialize_list_Interface_ethernet_json(data.get('ethernetList'))
	trunklist = deserialize_list_Interface_trunk_json(data.get('trunkList'))
	velist = deserialize_list_Interface_ve_json(data.get('veList'))
	loopbacklist = deserialize_list_Interface_loopback_json(data.get('loopbackList'))
	result = Interface(management=management, ethernetlist=ethernetlist, trunklist=trunklist, velist=velist, loopbacklist=loopbacklist)
	return result

class Interface__management__access_list(AxapiObject):
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

class Interface__management__bcast_rate_limit(AxapiObject):
	__metaclass__ = StructMeta 
	rate=PosRangedInteger(50, 5000)
	def __init__(self, rate=None):
		self.rate = rate

	def __str__(self):
		return ""

class Interface__management__lldp__enable_cfg(AxapiObject):
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

class Interface__management__lldp__notification_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	notification=PosRangedInteger(0, 1)
	notif_enable=PosRangedInteger(0, 1)
	def __init__(self, notification=None, notif_enable=None):
		self.notification = notification
		self.notif_enable = notif_enable

	def __str__(self):
		return ""

class Interface__management__lldp__tx_dot1_cfg(AxapiObject):
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

class Interface__management__lldp__tx_tlvs_cfg(AxapiObject):
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

class Interface__management__lldp(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, enable_cfg=None, notification_cfg=None, tx_dot1_cfg=None, tx_tlvs_cfg=None):
		self.enable_cfg = enable_cfg
		self.notification_cfg = notification_cfg
		self.tx_dot1_cfg = tx_dot1_cfg
		self.tx_tlvs_cfg = tx_tlvs_cfg

	def __str__(self):
		return ""

class Interface__management__ip__address(AxapiObject):
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

class Interface__management__ip(AxapiObject):
	__metaclass__ = StructMeta 
	control_apps_use_mgmt_port=PosRangedInteger(0, 1)
	default_gateway = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, address=None, control_apps_use_mgmt_port=None, default_gateway=None):
		self.address = address
		self.control_apps_use_mgmt_port = control_apps_use_mgmt_port
		self.default_gateway = default_gateway

	def __str__(self):
		return ""

class Interface__management__ipv6(AxapiObject):
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

class Interface__management(AxapiObject):
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

class Interface(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, management=None, ethernetlist=None, trunklist=None, velist=None, loopbacklist=None):
		self.management = management
		self.ethernetlist = ethernetlist
		self.trunklist = trunklist
		self.velist = velist
		self.loopbacklist = loopbacklist

	def __str__(self):
		return ""

class Interface_ethernet__snmp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	snmp_server=PosRangedInteger(0, 1)
	trap_source=PosRangedInteger(0, 1)
	def __init__(self, snmp_server=None, trap_source=None):
		self.snmp_server = snmp_server
		self.trap_source = trap_source

	def __str__(self):
		return ""

class Interface_ethernet__icmp_cfg(AxapiObject):
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

class Interface_ethernet__icmpv6_cfg(AxapiObject):
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

class Interface_ethernet__lldp__enable_cfg(AxapiObject):
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

class Interface_ethernet__lldp__notification_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	notification=PosRangedInteger(0, 1)
	notif_enable=PosRangedInteger(0, 1)
	def __init__(self, notification=None, notif_enable=None):
		self.notification = notification
		self.notif_enable = notif_enable

	def __str__(self):
		return ""

class Interface_ethernet__lldp__tx_dot1_cfg(AxapiObject):
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

class Interface_ethernet__lldp__tx_tlvs_cfg(AxapiObject):
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

class Interface_ethernet__lldp(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, enable_cfg=None, notification_cfg=None, tx_dot1_cfg=None, tx_tlvs_cfg=None):
		self.enable_cfg = enable_cfg
		self.notification_cfg = notification_cfg
		self.tx_dot1_cfg = tx_dot1_cfg
		self.tx_tlvs_cfg = tx_tlvs_cfg

	def __str__(self):
		return ""

class Interface_ethernet__lacp__trunk_cfg__mode_cfg(AxapiObject):
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

class Interface_ethernet__lacp__trunk_cfg__admin_key_cfg(AxapiObject):
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

class Interface_ethernet__lacp__trunk_cfg__unidirectional_cfg(AxapiObject):
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

class Interface_ethernet__lacp__trunk_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	trunk=PosRangedInteger(1, 16)
	def __init__(self, trunk=None, mode_cfg=None, admin_key_cfg=None, unidirectional_cfg=None):
		self.trunk = trunk
		self.mode_cfg = mode_cfg
		self.admin_key_cfg = admin_key_cfg
		self.unidirectional_cfg = unidirectional_cfg

	def __str__(self):
		return ""

class Interface_ethernet__lacp__udld_timeout_cfg__fast(AxapiObject):
	__metaclass__ = StructMeta 
	udld_fast_timeout=PosRangedInteger(100, 1000)
	def __init__(self, udld_fast_timeout=None):
		self.udld_fast_timeout = udld_fast_timeout

	def __str__(self):
		return ""

class Interface_ethernet__lacp__udld_timeout_cfg__slow(AxapiObject):
	__metaclass__ = StructMeta 
	udld_slow_timeout=PosRangedInteger(1, 60)
	def __init__(self, udld_slow_timeout=None):
		self.udld_slow_timeout = udld_slow_timeout

	def __str__(self):
		return ""

class Interface_ethernet__lacp__udld_timeout_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	udld_timeout=PosRangedInteger(0, 1)
	def __init__(self, udld_timeout=None, fast=None, slow=None):
		self.udld_timeout = udld_timeout
		self.fast = fast
		self.slow = slow

	def __str__(self):
		return ""

class Interface_ethernet__lacp(AxapiObject):
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

class Interface_ethernet__ddos(AxapiObject):
	__metaclass__ = StructMeta 
	outside=PosRangedInteger(0, 1)
	inside=PosRangedInteger(0, 1)
	def __init__(self, outside=None, inside=None):
		self.outside = outside
		self.inside = inside

	def __str__(self):
		return ""

class Interface_ethernet__ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	dhcp=PosRangedInteger(0, 1)
	def __init__(self, ip_cfg=None, dhcp=None):
		self.ip_cfg = ip_cfg
		self.dhcp = dhcp

	def __str__(self):
		return ""

class Interface_ethernet__ip__nat(AxapiObject):
	__metaclass__ = StructMeta 
	inside=PosRangedInteger(0, 1)
	outside=PosRangedInteger(0, 1)
	def __init__(self, inside=None, outside=None):
		self.inside = inside
		self.outside = outside

	def __str__(self):
		return ""

class Interface_ethernet__ip(AxapiObject):
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

class Interface_ethernet__ipv6__ndisc__router_adver__mtu(AxapiObject):
	__metaclass__ = StructMeta 
	adver_mtu=PosRangedInteger(1200, 1500)
	adver_mtu_disable=PosRangedInteger(0, 1)
	def __init__(self, adver_mtu=None, adver_mtu_disable=None):
		self.adver_mtu = adver_mtu
		self.adver_mtu_disable = adver_mtu_disable

	def __str__(self):
		return ""

class Interface_ethernet__ipv6__ndisc__router_adver__vrid(AxapiObject):
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

class Interface_ethernet__ipv6__ndisc__router_adver__ha_group_id(AxapiObject):
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

class Interface_ethernet__ipv6__ndisc__router_adver(AxapiObject):
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

class Interface_ethernet__ipv6__ndisc(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, router_adver=None):
		self.router_adver = router_adver

	def __str__(self):
		return ""

class Interface_ethernet__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_enable=PosRangedInteger(0, 1)
	def __init__(self, address_cfg=None, ipv6_enable=None, ndisc=None):
		self.address_cfg = address_cfg
		self.ipv6_enable = ipv6_enable
		self.ndisc = ndisc

	def __str__(self):
		return ""

class Interface_ethernet(AxapiObject):
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

class Interface_monitor_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	monitor = Enum(['input', 'output', 'both'])
	monitor_vlan=PosRangedInteger(2, 4094)
	def __init__(self, monitor=None, monitor_vlan=None):
		self.monitor = monitor
		self.monitor_vlan = monitor_vlan

	def __str__(self):
		return ""

class Interface_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv4_netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ipv4_address=None, ipv4_netmask=None):
		self.ipv4_address = ipv4_address
		self.ipv4_netmask = ipv4_netmask

	def __str__(self):
		return ""

class Interface_address_cfg(AxapiObject):
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

class Interface_prefix_cfg(AxapiObject):
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

class Interface_trunk__icmp_cfg(AxapiObject):
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

class Interface_trunk__icmpv6_cfg(AxapiObject):
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

class Interface_trunk__ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	dhcp=PosRangedInteger(0, 1)
	def __init__(self, address_val_cfg=None, dhcp=None):
		self.address_val_cfg = address_val_cfg
		self.dhcp = dhcp

	def __str__(self):
		return ""

class Interface_trunk__ip__nat(AxapiObject):
	__metaclass__ = StructMeta 
	inside=PosRangedInteger(0, 1)
	outside=PosRangedInteger(0, 1)
	def __init__(self, inside=None, outside=None):
		self.inside = inside
		self.outside = outside

	def __str__(self):
		return ""

class Interface_trunk__ip(AxapiObject):
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

class Interface_trunk__ipv6__nat(AxapiObject):
	__metaclass__ = StructMeta 
	inside=PosRangedInteger(0, 1)
	outside=PosRangedInteger(0, 1)
	def __init__(self, inside=None, outside=None):
		self.inside = inside
		self.outside = outside

	def __str__(self):
		return ""

class Interface_trunk__ipv6__ndisc__router_adver__mtu(AxapiObject):
	__metaclass__ = StructMeta 
	adver_mtu=PosRangedInteger(1200, 1500)
	adver_mtu_disable=PosRangedInteger(0, 1)
	def __init__(self, adver_mtu=None, adver_mtu_disable=None):
		self.adver_mtu = adver_mtu
		self.adver_mtu_disable = adver_mtu_disable

	def __str__(self):
		return ""

class Interface_trunk__ipv6__ndisc__router_adver__vrid(AxapiObject):
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

class Interface_trunk__ipv6__ndisc__router_adver__ha_group_id(AxapiObject):
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

class Interface_trunk__ipv6__ndisc__router_adver(AxapiObject):
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

class Interface_trunk__ipv6__ndisc(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, router_adver=None):
		self.router_adver = router_adver

	def __str__(self):
		return ""

class Interface_trunk__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_enable=PosRangedInteger(0, 1)
	def __init__(self, address_cfg=None, ipv6_enable=None, nat=None, ndisc=None):
		self.address_cfg = address_cfg
		self.ipv6_enable = ipv6_enable
		self.nat = nat
		self.ndisc = ndisc

	def __str__(self):
		return ""

class Interface_trunk__ddos(AxapiObject):
	__metaclass__ = StructMeta 
	outside=PosRangedInteger(0, 1)
	inside=PosRangedInteger(0, 1)
	def __init__(self, outside=None, inside=None):
		self.outside = outside
		self.inside = inside

	def __str__(self):
		return ""

class Interface_trunk(AxapiObject):
	__metaclass__ = StructMeta 
	ifnum=PosInteger()
	name=SizedString(1, 32)
	l3_vlan_fwd_disable=PosRangedInteger(0, 1)
	mtu=PosRangedInteger(1200, 12000)
	action = Enum(['enable', 'disable'])
	def __init__(self, ifnum, name=None, l3_vlan_fwd_disable=None, mtu=None, action=None, icmp_cfg=None, icmpv6_cfg=None, ip=None, ipv6=None, ddos=None):
		self.ifnum = ifnum
		self.name = name
		self.l3_vlan_fwd_disable = l3_vlan_fwd_disable
		self.mtu = mtu
		self.action = action
		self.icmp_cfg = icmp_cfg
		self.icmpv6_cfg = icmpv6_cfg
		self.ip = ip
		self.ipv6 = ipv6
		self.ddos = ddos

	def __str__(self):
		return str(self.ifnum)

class Interface_address_val_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	address_val = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, address_val=None, netmask=None):
		self.address_val = address_val
		self.netmask = netmask

	def __str__(self):
		return ""

class Interface_ve__snmp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	snmp_server=PosRangedInteger(0, 1)
	trap_source=PosRangedInteger(0, 1)
	def __init__(self, snmp_server=None, trap_source=None):
		self.snmp_server = snmp_server
		self.trap_source = trap_source

	def __str__(self):
		return ""

class Interface_ve__icmp_cfg(AxapiObject):
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

class Interface_ve__icmpv6_cfg(AxapiObject):
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

class Interface_ve__ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	dhcp=PosRangedInteger(0, 1)
	def __init__(self, address_val_cfg=None, dhcp=None):
		self.address_val_cfg = address_val_cfg
		self.dhcp = dhcp

	def __str__(self):
		return ""

class Interface_ve__ip__nat(AxapiObject):
	__metaclass__ = StructMeta 
	inside=PosRangedInteger(0, 1)
	outside=PosRangedInteger(0, 1)
	def __init__(self, inside=None, outside=None):
		self.inside = inside
		self.outside = outside

	def __str__(self):
		return ""

class Interface_ve__ip(AxapiObject):
	__metaclass__ = StructMeta 
	helper_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	generate_membership_query=PosRangedInteger(0, 1)
	generate_membership_query_val=PosRangedInteger(1, 255)
	max_resp_time=PosRangedInteger(1, 255)
	def __init__(self, address=None, helper_address=None, nat=None, generate_membership_query=None, generate_membership_query_val=None, max_resp_time=None):
		self.address = address
		self.helper_address = helper_address
		self.nat = nat
		self.generate_membership_query = generate_membership_query
		self.generate_membership_query_val = generate_membership_query_val
		self.max_resp_time = max_resp_time

	def __str__(self):
		return ""

class Interface_ve__ipv6__nat(AxapiObject):
	__metaclass__ = StructMeta 
	inside=PosRangedInteger(0, 1)
	outside=PosRangedInteger(0, 1)
	def __init__(self, inside=None, outside=None):
		self.inside = inside
		self.outside = outside

	def __str__(self):
		return ""

class Interface_ve__ipv6__ndisc__router_adver__mtu(AxapiObject):
	__metaclass__ = StructMeta 
	adver_mtu=PosRangedInteger(1200, 1500)
	adver_mtu_disable=PosRangedInteger(0, 1)
	def __init__(self, adver_mtu=None, adver_mtu_disable=None):
		self.adver_mtu = adver_mtu
		self.adver_mtu_disable = adver_mtu_disable

	def __str__(self):
		return ""

class Interface_ve__ipv6__ndisc__router_adver__vrid(AxapiObject):
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

class Interface_ve__ipv6__ndisc__router_adver__ha_group_id(AxapiObject):
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

class Interface_ve__ipv6__ndisc__router_adver(AxapiObject):
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

class Interface_ve__ipv6__ndisc(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, router_adver=None):
		self.router_adver = router_adver

	def __str__(self):
		return ""

class Interface_ve__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_enable=PosRangedInteger(0, 1)
	def __init__(self, address_cfg=None, ipv6_enable=None, nat=None, ndisc=None):
		self.address_cfg = address_cfg
		self.ipv6_enable = ipv6_enable
		self.nat = nat
		self.ndisc = ndisc

	def __str__(self):
		return ""

class Interface_ve__ddos(AxapiObject):
	__metaclass__ = StructMeta 
	outside=PosRangedInteger(0, 1)
	inside=PosRangedInteger(0, 1)
	def __init__(self, outside=None, inside=None):
		self.outside = outside
		self.inside = inside

	def __str__(self):
		return ""

class Interface_ve(AxapiObject):
	__metaclass__ = StructMeta 
	ifnum=PosInteger()
	name=SizedString(1, 32)
	l3_vlan_fwd_disable=PosRangedInteger(0, 1)
	mtu=PosRangedInteger(1200, 12000)
	action = Enum(['enable', 'disable'])
	def __init__(self, ifnum, name=None, l3_vlan_fwd_disable=None, mtu=None, snmp_cfg=None, action=None, icmp_cfg=None, icmpv6_cfg=None, ip=None, ipv6=None, ddos=None):
		self.ifnum = ifnum
		self.name = name
		self.l3_vlan_fwd_disable = l3_vlan_fwd_disable
		self.mtu = mtu
		self.snmp_cfg = snmp_cfg
		self.action = action
		self.icmp_cfg = icmp_cfg
		self.icmpv6_cfg = icmpv6_cfg
		self.ip = ip
		self.ipv6 = ipv6
		self.ddos = ddos

	def __str__(self):
		return str(self.ifnum)

class Interface_loopback__snmp_server_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	snmp_server=PosRangedInteger(0, 1)
	trap_source=PosRangedInteger(0, 1)
	def __init__(self, snmp_server=None, trap_source=None):
		self.snmp_server = snmp_server
		self.trap_source = trap_source

	def __str__(self):
		return ""

class Interface_loopback__ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address_val_cfg=None):
		self.address_val_cfg = address_val_cfg

	def __str__(self):
		return ""

class Interface_loopback__ip(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address=None):
		self.address = address

	def __str__(self):
		return ""

class Interface_loopback__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_enable=PosRangedInteger(0, 1)
	def __init__(self, address_cfg=None, ipv6_enable=None):
		self.address_cfg = address_cfg
		self.ipv6_enable = ipv6_enable

	def __str__(self):
		return ""

class Interface_loopback(AxapiObject):
	__metaclass__ = StructMeta 
	ifnum=PosRangedInteger(0, 9)
	def __init__(self, ifnum, snmp_server_cfg=None, ip=None, ipv6=None):
		self.ifnum = ifnum
		self.snmp_server_cfg = snmp_server_cfg
		self.ip = ip
		self.ipv6 = ipv6

	def __str__(self):
		return str(self.ifnum)

class InterfaceClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getInterface(self):
		"""
		Retrieve the interface identified by the specified identifier
		
		Returns:
			An instance of the Interface class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
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

