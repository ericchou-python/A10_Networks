########################################################################################################################
# File name: ip.py
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
	'https://axapi.a10networks.com/axapi/v3/ip',
]

def deserialize_Ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_addr = data.get('ip_addr')
	ip_mask = data.get('ip_mask')
	result = Ip__address(ip_addr=ip_addr, ip_mask=ip_mask)
	return result

def deserialize_Ip__default_gateway_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	gateway_ip = data.get('gateway_ip')
	result = Ip__default_gateway(gateway_ip=gateway_ip)
	return result

def deserialize_Ip_access_list__icmp_cfg__icmp_src_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_src_icmp = data.get('any-src-icmp')
	host_src_icmp = data.get('host-src-icmp')
	subnet_src_icmp = data.get('subnet-src-icmp')
	mask_src_icmp = data.get('mask-src-icmp')
	result = Ip_access_list__icmp_cfg__icmp_src_cfg(any_src_icmp=any_src_icmp, host_src_icmp=host_src_icmp, subnet_src_icmp=subnet_src_icmp, mask_src_icmp=mask_src_icmp)
	return result

def deserialize_Ip_access_list__icmp_cfg__code_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_code = data.get('any-code')
	icmp_code = data.get('icmp-code')
	result = Ip_access_list__icmp_cfg__code(any_code=any_code, icmp_code=icmp_code)
	return result

def deserialize_Ip_access_list__icmp_cfg__type__type_code_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type_any_code = data.get('type-any-code')
	type_icmp_code = data.get('type-icmp-code')
	type_any_src = data.get('type-any-src')
	type_host_src = data.get('type-host-src')
	type_subnet_src = data.get('type-subnet-src')
	type_mask_src = data.get('type-mask-src')
	result = Ip_access_list__icmp_cfg__type__type_code(type_any_code=type_any_code, type_icmp_code=type_icmp_code, type_any_src=type_any_src, type_host_src=type_host_src, type_subnet_src=type_subnet_src, type_mask_src=type_mask_src)
	return result

def deserialize_Ip_access_list__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dest_un_any_code = data.get('dest-un-any-code')
	dest_un_icmp_code = data.get('dest-un-icmp-code')
	frag_required = data.get('frag-required')
	host_unreachable = data.get('host-unreachable')
	network_unreachable = data.get('network-unreachable')
	port_unreachable = data.get('port-unreachable')
	proto_unreachable = data.get('proto-unreachable')
	route_failed = data.get('route-failed')
	result = Ip_access_list__icmp_cfg__type__dest_unreach_cfg__dest_un_code(dest_un_any_code=dest_un_any_code, dest_un_icmp_code=dest_un_icmp_code, frag_required=frag_required, host_unreachable=host_unreachable, network_unreachable=network_unreachable, port_unreachable=port_unreachable, proto_unreachable=proto_unreachable, route_failed=route_failed)
	return result

def deserialize_Ip_access_list__icmp_cfg__type__dest_unreach_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dest_unreachable = data.get('dest-unreachable')
	dest_un_code = deserialize_Ip_access_list__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(data.get('dest-un-code'))
	dest_un_any_src = data.get('dest-un-any-src')
	dest_un_host_src = data.get('dest-un-host-src')
	dest_un_subnet_src = data.get('dest-un-subnet-src')
	dest_un_mask_src = data.get('dest-un-mask-src')
	result = Ip_access_list__icmp_cfg__type__dest_unreach_cfg(dest_unreachable=dest_unreachable, dest_un_code=dest_un_code, dest_un_any_src=dest_un_any_src, dest_un_host_src=dest_un_host_src, dest_un_subnet_src=dest_un_subnet_src, dest_un_mask_src=dest_un_mask_src)
	return result

def deserialize_Ip_access_list__icmp_cfg__type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp_type = data.get('icmp-type')
	any_type = data.get('any-type')
	echo_reply = data.get('echo-reply')
	echo_request = data.get('echo-request')
	info_reply = data.get('info-reply')
	info_request = data.get('info-request')
	mask_reply = data.get('mask-reply')
	mask_request = data.get('mask-request')
	parameter_problem = data.get('parameter-problem')
	redirect = data.get('redirect')
	source_quench = data.get('source-quench')
	time_exceeded = data.get('time-exceeded')
	timestamp = data.get('timestamp')
	timestamp_reply = data.get('timestamp-reply')
	type_code = deserialize_Ip_access_list__icmp_cfg__type__type_code_json(data.get('type-code'))
	dest_unreach_cfg = deserialize_Ip_access_list__icmp_cfg__type__dest_unreach_cfg_json(data.get('dest-unreach-cfg'))
	result = Ip_access_list__icmp_cfg__type(icmp_type=icmp_type, any_type=any_type, echo_reply=echo_reply, echo_request=echo_request, info_reply=info_reply, info_request=info_request, mask_reply=mask_reply, mask_request=mask_request, parameter_problem=parameter_problem, redirect=redirect, source_quench=source_quench, time_exceeded=time_exceeded, timestamp=timestamp, timestamp_reply=timestamp_reply, type_code=type_code, dest_unreach_cfg=dest_unreach_cfg)
	return result

def deserialize_Ip_access_list__icmp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp = data.get('icmp')
	icmp_src_cfg = deserialize_Ip_access_list__icmp_cfg__icmp_src_cfg_json(data.get('icmp-src-cfg'))
	code = deserialize_Ip_access_list__icmp_cfg__code_json(data.get('code'))
	type = deserialize_Ip_access_list__icmp_cfg__type_json(data.get('type'))
	result = Ip_access_list__icmp_cfg(icmp=icmp, icmp_src_cfg=icmp_src_cfg, code=code, type=type)
	return result

def deserialize_Ip_access_list__ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip = data.get('ip')
	any_src_ip = data.get('any-src-ip')
	host_src_ip = data.get('host-src-ip')
	subnet_src_ip = data.get('subnet-src-ip')
	mask_src_ip = data.get('mask-src-ip')
	result = Ip_access_list__ip_cfg(ip=ip, any_src_ip=any_src_ip, host_src_ip=host_src_ip, subnet_src_ip=subnet_src_ip, mask_src_ip=mask_src_ip)
	return result

def deserialize_Ip_access_list__any_code_any_source_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_code_any_src = data.get('any-code-any-src')
	any_code_host_src = data.get('any-code-host-src')
	any_code_subnet_src = data.get('any-code-subnet-src')
	any_code_mask_src = data.get('any-code-mask-src')
	result = Ip_access_list__any_code_any_source_cfg(any_code_any_src=any_code_any_src, any_code_host_src=any_code_host_src, any_code_subnet_src=any_code_subnet_src, any_code_mask_src=any_code_mask_src)
	return result

def deserialize_Ip_access_list__dst_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_dst_ip = data.get('any-dst-ip')
	host_dst_ip = data.get('host-dst-ip')
	subnet_dst_ip = data.get('subnet-dst-ip')
	mask_dst_ip = data.get('mask-dst-ip')
	fragments = data.get('fragments')
	vlan = data.get('vlan')
	dscp = data.get('dscp')
	log = data.get('log')
	result = Ip_access_list__dst_ip_cfg(any_dst_ip=any_dst_ip, host_dst_ip=host_dst_ip, subnet_dst_ip=subnet_dst_ip, mask_dst_ip=mask_dst_ip, fragments=fragments, vlan=vlan, dscp=dscp, log=log)
	return result

def deserialize_Ip_access_list__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	eq_src = data.get('eq-src')
	gt_src = data.get('gt-src')
	lt_src = data.get('lt-src')
	range_src = data.get('range-src')
	port_num_end_src = data.get('port-num-end-src')
	result = Ip_access_list__l4_cfg__l4_src_cfg__l4_src_port_cfg(eq_src=eq_src, gt_src=gt_src, lt_src=lt_src, range_src=range_src, port_num_end_src=port_num_end_src)
	return result

def deserialize_Ip_access_list__l4_cfg__l4_src_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_src_tcp = data.get('any-src-tcp')
	host_src_tcp = data.get('host-src-tcp')
	subnet_src_tcp = data.get('subnet-src-tcp')
	mask_src_tcp = data.get('mask-src-tcp')
	l4_src_port_cfg = deserialize_Ip_access_list__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(data.get('l4-src-port-cfg'))
	result = Ip_access_list__l4_cfg__l4_src_cfg(any_src_tcp=any_src_tcp, host_src_tcp=host_src_tcp, subnet_src_tcp=subnet_src_tcp, mask_src_tcp=mask_src_tcp, l4_src_port_cfg=l4_src_port_cfg)
	return result

def deserialize_Ip_access_list__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	eq_dst = data.get('eq-dst')
	gt_dst = data.get('gt-dst')
	lt_dst = data.get('lt-dst')
	range_dst = data.get('range-dst')
	port_num_end_dst = data.get('port-num-end-dst')
	result = Ip_access_list__l4_cfg__l4_dst_cfg__l4_dst_port_cfg(eq_dst=eq_dst, gt_dst=gt_dst, lt_dst=lt_dst, range_dst=range_dst, port_num_end_dst=port_num_end_dst)
	return result

def deserialize_Ip_access_list__l4_cfg__l4_dst_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_dst_tcp = data.get('any-dst-tcp')
	host_dst_tcp = data.get('host-dst-tcp')
	subnet_dst_tcp = data.get('subnet-dst-tcp')
	mask_dst_tcp = data.get('mask-dst-tcp')
	l4_dst_port_cfg = deserialize_Ip_access_list__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(data.get('l4-dst-port-cfg'))
	result = Ip_access_list__l4_cfg__l4_dst_cfg(any_dst_tcp=any_dst_tcp, host_dst_tcp=host_dst_tcp, subnet_dst_tcp=subnet_dst_tcp, mask_dst_tcp=mask_dst_tcp, l4_dst_port_cfg=l4_dst_port_cfg)
	return result

def deserialize_Ip_access_list__l4_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	l4_src_cfg = deserialize_Ip_access_list__l4_cfg__l4_src_cfg_json(data.get('l4-src-cfg'))
	l4_dst_cfg = deserialize_Ip_access_list__l4_cfg__l4_dst_cfg_json(data.get('l4-dst-cfg'))
	tcp_fragments = data.get('tcp-fragments')
	vlan = data.get('vlan')
	dscp = data.get('dscp')
	established = data.get('established')
	log = data.get('log')
	result = Ip_access_list__l4_cfg(tcp=tcp, udp=udp, l4_src_cfg=l4_src_cfg, l4_dst_cfg=l4_dst_cfg, tcp_fragments=tcp_fragments, vlan=vlan, dscp=dscp, established=established, log=log)
	return result

def deserialize_Ip_access_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	seq_num = data.get('seq-num')
	action = data.get('action')
	remark = data.get('remark')
	icmp_cfg = deserialize_Ip_access_list__icmp_cfg_json(data.get('icmp-cfg'))
	ip_cfg = deserialize_Ip_access_list__ip_cfg_json(data.get('ip-cfg'))
	any_code_any_source_cfg = deserialize_Ip_access_list__any_code_any_source_cfg_json(data.get('any-code-any-source-cfg'))
	dst_ip_cfg = deserialize_Ip_access_list__dst_ip_cfg_json(data.get('dst-ip-cfg'))
	l4_cfg = deserialize_Ip_access_list__l4_cfg_json(data.get('l4-cfg'))
	result = Ip_access_list(name=name, seq_num=seq_num, action=action, remark=remark, icmp_cfg=icmp_cfg, ip_cfg=ip_cfg, any_code_any_source_cfg=any_code_any_source_cfg, dst_ip_cfg=dst_ip_cfg, l4_cfg=l4_cfg)
	return result

def deserialize_list_Ip_access_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_access_list_json(item))
	return list(container)

def deserialize_Ip_mgmt_traffic__source_interface__loopback_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	loopback_num = data.get('loopback-num')
	result = Ip_mgmt_traffic__source_interface__loopback(loopback_num=loopback_num)
	return result

def deserialize_Ip_mgmt_traffic__source_interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	loopback = deserialize_Ip_mgmt_traffic__source_interface__loopback_json(data.get('loopback'))
	result = Ip_mgmt_traffic__source_interface(loopback=loopback)
	return result

def deserialize_Ip_mgmt_traffic_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	traffic_type = data.get('traffic-type')
	source_interface = deserialize_Ip_mgmt_traffic__source_interface_json(data.get('source-interface'))
	result = Ip_mgmt_traffic(traffic_type=traffic_type, source_interface=source_interface)
	return result

def deserialize_list_Ip_mgmt_traffic_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_mgmt_traffic_json(item))
	return list(container)

def deserialize_Ip__frag_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	buff = data.get('buff')
	max_reassembly_sessions = data.get('max-reassembly-sessions')
	timeout = data.get('timeout')
	result = Ip__frag(buff=buff, max_reassembly_sessions=max_reassembly_sessions, timeout=timeout)
	return result

def deserialize_Ip__tcp__syn_cookie_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	threshold = data.get('threshold')
	result = Ip__tcp__syn_cookie(threshold=threshold)
	return result

def deserialize_Ip__tcp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	syn_cookie = deserialize_Ip__tcp__syn_cookie_json(data.get('syn-cookie'))
	result = Ip__tcp(syn_cookie=syn_cookie)
	return result

def deserialize_Ip_route__ip_dest_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_dest_addr = data.get('ip_dest_addr')
	ip_mask = data.get('ip_mask')
	ip_next_hop = data.get('ip_next_hop')
	distance = data.get('distance')
	result = Ip_route__ip_dest_cfg(ip_dest_addr=ip_dest_addr, ip_mask=ip_mask, ip_next_hop=ip_next_hop, distance=distance)
	return result

def deserialize_Ip_route_static_bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_ip = data.get('local-ip')
	nexthop_ip = data.get('nexthop-ip')
	result = Ip_route_static_bfd(local_ip=local_ip, nexthop_ip=nexthop_ip)
	return result

def deserialize_list_Ip_route_static_bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_route_static_bfd_json(item))
	return list(container)

def deserialize_Ip_route__static_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bfdlist = deserialize_list_Ip_route_static_bfd_json(data.get('bfdList'))
	result = Ip_route__static(bfdlist=bfdlist)
	return result

def deserialize_Ip_route_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_dest_cfg = deserialize_Ip_route__ip_dest_cfg_json(data.get('ip-dest-cfg'))
	static = deserialize_Ip_route__static_json(data.get('static'))
	result = Ip_route(ip_dest_cfg=ip_dest_cfg, static=static)
	return result

def deserialize_list_Ip_route_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_route_json(item))
	return list(container)

def deserialize_Ip__dns__primary_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_v4_addr = data.get('ip-v4-addr')
	ip_v6_addr = data.get('ip-v6-addr')
	result = Ip__dns__primary(ip_v4_addr=ip_v4_addr, ip_v6_addr=ip_v6_addr)
	return result

def deserialize_Ip__dns__secondary_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_v4_addr = data.get('ip-v4-addr')
	ip_v6_addr = data.get('ip-v6-addr')
	result = Ip__dns__secondary(ip_v4_addr=ip_v4_addr, ip_v6_addr=ip_v6_addr)
	return result

def deserialize_Ip__dns__suffix_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	domain_name = data.get('domain-name')
	result = Ip__dns__suffix(domain_name=domain_name)
	return result

def deserialize_Ip__dns_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	primary = deserialize_Ip__dns__primary_json(data.get('primary'))
	secondary = deserialize_Ip__dns__secondary_json(data.get('secondary'))
	suffix = deserialize_Ip__dns__suffix_json(data.get('suffix'))
	result = Ip__dns(primary=primary, secondary=secondary, suffix=suffix)
	return result

def deserialize_Ip__icmp__disable_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	redirect = data.get('redirect')
	unreachable = data.get('unreachable')
	result = Ip__icmp__disable(redirect=redirect, unreachable=unreachable)
	return result

def deserialize_Ip__icmp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	disable = deserialize_Ip__icmp__disable_json(data.get('disable'))
	result = Ip__icmp(disable=disable)
	return result

def deserialize_Ip_map_list__name_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	file = data.get('file')
	result = Ip_map_list__name_cfg(name=name, file=file)
	return result

def deserialize_Ip_local_start_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_start_ip = data.get('local-start-ip')
	global_start_ip = data.get('global-start-ip')
	count = data.get('count')
	result = Ip_local_start_cfg(local_start_ip=local_start_ip, global_start_ip=global_start_ip, count=count)
	return result

def deserialize_list_Ip_local_start_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_local_start_cfg_json(item))
	return list(container)

def deserialize_Ip_map_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name_cfg = deserialize_Ip_map_list__name_cfg_json(data.get('name-cfg'))
	local_start_cfg = deserialize_list_Ip_local_start_cfg_json(data.get('local-start-cfg'))
	result = Ip_map_list(name_cfg=name_cfg, local_start_cfg=local_start_cfg)
	return result

def deserialize_list_Ip_map_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_map_list_json(item))
	return list(container)

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

def deserialize_Ip__nat__inside__source_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	class_list = data.get('class-list')
	listlist = deserialize_list_Ip_nat_inside_source_list_json(data.get('listList'))
	staticlist = deserialize_list_Ip_nat_inside_source_static_json(data.get('staticList'))
	result = Ip__nat__inside__source(class_list=class_list, listlist=listlist, staticlist=staticlist)
	return result

def deserialize_Ip__nat__inside_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	source = deserialize_Ip__nat__inside__source_json(data.get('source'))
	result = Ip__nat__inside(source=source)
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

def deserialize_Ip__nat__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	logginglist = deserialize_list_Ip_nat_template_logging_json(data.get('loggingList'))
	result = Ip__nat__template(logginglist=logginglist)
	return result

def deserialize_Ip__nat__translation__icmp_timeout_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp_timeout_val = data.get('icmp-timeout-val')
	fast = data.get('fast')
	result = Ip__nat__translation__icmp_timeout(icmp_timeout_val=icmp_timeout_val, fast=fast)
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

def deserialize_Ip__nat__translation_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp_timeout = deserialize_Ip__nat__translation__icmp_timeout_json(data.get('icmp-timeout'))
	tcp_timeout = data.get('tcp-timeout')
	udp_timeout = data.get('udp-timeout')
	service_timeoutlist = deserialize_list_Ip_nat_translation_service_timeout_json(data.get('service-timeoutList'))
	result = Ip__nat__translation(icmp_timeout=icmp_timeout, tcp_timeout=tcp_timeout, udp_timeout=udp_timeout, service_timeoutlist=service_timeoutlist)
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

def deserialize_Ip__nat__alg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	pptp = data.get('pptp')
	result = Ip__nat__alg(pptp=pptp)
	return result

def deserialize_Ip__nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	poollist = deserialize_list_Ip_nat_pool_json(data.get('poolList'))
	pool_grouplist = deserialize_list_Ip_nat_pool_group_json(data.get('pool-groupList'))
	inside = deserialize_Ip__nat__inside_json(data.get('inside'))
	template = deserialize_Ip__nat__template_json(data.get('template'))
	translation = deserialize_Ip__nat__translation_json(data.get('translation'))
	range_listlist = deserialize_list_Ip_nat_range_list_json(data.get('range-listList'))
	alg = deserialize_Ip__nat__alg_json(data.get('alg'))
	result = Ip__nat(poollist=poollist, pool_grouplist=pool_grouplist, inside=inside, template=template, translation=translation, range_listlist=range_listlist, alg=alg)
	return result

def deserialize_Ip__nat_global_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	allow_static_host = data.get('allow-static-host')
	reset_idle_tcp_conn = data.get('reset-idle-tcp-conn')
	result = Ip__nat_global(allow_static_host=allow_static_host, reset_idle_tcp_conn=reset_idle_tcp_conn)
	return result

def deserialize_Ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Ip__address_json(data.get('address'))
	default_gateway = deserialize_Ip__default_gateway_json(data.get('default-gateway'))
	access_listlist = deserialize_list_Ip_access_list_json(data.get('access-listList'))
	mgmt_trafficlist = deserialize_list_Ip_mgmt_traffic_json(data.get('mgmt-trafficList'))
	frag = deserialize_Ip__frag_json(data.get('frag'))
	tcp = deserialize_Ip__tcp_json(data.get('tcp'))
	routelist = deserialize_list_Ip_route_json(data.get('routeList'))
	dns = deserialize_Ip__dns_json(data.get('dns'))
	icmp = deserialize_Ip__icmp_json(data.get('icmp'))
	map_listlist = deserialize_list_Ip_map_list_json(data.get('map-listList'))
	nat = deserialize_Ip__nat_json(data.get('nat'))
	nat_global = deserialize_Ip__nat_global_json(data.get('nat-global'))
	result = Ip(address=address, default_gateway=default_gateway, access_listlist=access_listlist, mgmt_trafficlist=mgmt_trafficlist, frag=frag, tcp=tcp, routelist=routelist, dns=dns, icmp=icmp, map_listlist=map_listlist, nat=nat, nat_global=nat_global)
	return result

class Ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ip_addr=None, ip_mask=None):
		self.ip_addr = ip_addr
		self.ip_mask = ip_mask

	def __str__(self):
		return ""

class Ip__default_gateway(AxapiObject):
	__metaclass__ = StructMeta 
	gateway_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, gateway_ip=None):
		self.gateway_ip = gateway_ip

	def __str__(self):
		return ""

class Ip__frag(AxapiObject):
	__metaclass__ = StructMeta 
	buff=PosRangedInteger(10000, 3000000)
	max_reassembly_sessions=PosRangedInteger(1, 200000)
	timeout=PosRangedInteger(4, 16000)
	def __init__(self, buff=None, max_reassembly_sessions=None, timeout=None):
		self.buff = buff
		self.max_reassembly_sessions = max_reassembly_sessions
		self.timeout = timeout

	def __str__(self):
		return ""

class Ip__tcp__syn_cookie(AxapiObject):
	__metaclass__ = StructMeta 
	threshold=PosRangedInteger(1, 100)
	def __init__(self, threshold=None):
		self.threshold = threshold

	def __str__(self):
		return ""

class Ip__tcp(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, syn_cookie=None):
		self.syn_cookie = syn_cookie

	def __str__(self):
		return ""

class Ip__dns__primary(AxapiObject):
	__metaclass__ = StructMeta 
	ip_v4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_v6_addr=SizedString(1, 255)
	def __init__(self, ip_v4_addr=None, ip_v6_addr=None):
		self.ip_v4_addr = ip_v4_addr
		self.ip_v6_addr = ip_v6_addr

	def __str__(self):
		return ""

class Ip__dns__secondary(AxapiObject):
	__metaclass__ = StructMeta 
	ip_v4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_v6_addr=SizedString(1, 255)
	def __init__(self, ip_v4_addr=None, ip_v6_addr=None):
		self.ip_v4_addr = ip_v4_addr
		self.ip_v6_addr = ip_v6_addr

	def __str__(self):
		return ""

class Ip__dns__suffix(AxapiObject):
	__metaclass__ = StructMeta 
	domain_name=SizedString(1, 32)
	def __init__(self, domain_name=None):
		self.domain_name = domain_name

	def __str__(self):
		return ""

class Ip__dns(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, primary=None, secondary=None, suffix=None):
		self.primary = primary
		self.secondary = secondary
		self.suffix = suffix

	def __str__(self):
		return ""

class Ip__icmp__disable(AxapiObject):
	__metaclass__ = StructMeta 
	redirect=PosRangedInteger(0, 1)
	unreachable=PosRangedInteger(0, 1)
	def __init__(self, redirect=None, unreachable=None):
		self.redirect = redirect
		self.unreachable = unreachable

	def __str__(self):
		return ""

class Ip__icmp(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, disable=None):
		self.disable = disable

	def __str__(self):
		return ""

class Ip__nat__inside__source(AxapiObject):
	__metaclass__ = StructMeta 
	class_list=SizedString(1, 63)
	def __init__(self, class_list=None, listlist=None, staticlist=None):
		self.class_list = class_list
		self.listlist = listlist
		self.staticlist = staticlist

	def __str__(self):
		return ""

class Ip__nat__inside(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, source=None):
		self.source = source

	def __str__(self):
		return ""

class Ip__nat__template(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, logginglist=None):
		self.logginglist = logginglist

	def __str__(self):
		return ""

class Ip__nat__translation__icmp_timeout(AxapiObject):
	__metaclass__ = StructMeta 
	icmp_timeout_val=PosRangedInteger(2, 15000)
	fast=PosRangedInteger(0, 1)
	def __init__(self, icmp_timeout_val=None, fast=None):
		self.icmp_timeout_val = icmp_timeout_val
		self.fast = fast

	def __str__(self):
		return ""

class Ip__nat__translation(AxapiObject):
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

class Ip__nat__alg(AxapiObject):
	__metaclass__ = StructMeta 
	pptp = Enum(['disable', 'enable'])
	def __init__(self, pptp=None):
		self.pptp = pptp

	def __str__(self):
		return ""

class Ip__nat(AxapiObject):
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

class Ip__nat_global(AxapiObject):
	__metaclass__ = StructMeta 
	allow_static_host=PosRangedInteger(0, 1)
	reset_idle_tcp_conn=PosRangedInteger(0, 1)
	def __init__(self, allow_static_host=None, reset_idle_tcp_conn=None):
		self.allow_static_host = allow_static_host
		self.reset_idle_tcp_conn = reset_idle_tcp_conn

	def __str__(self):
		return ""

class Ip(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address=None, default_gateway=None, access_listlist=None, mgmt_trafficlist=None, frag=None, tcp=None, routelist=None, dns=None, icmp=None, map_listlist=None, nat=None, nat_global=None):
		self.address = address
		self.default_gateway = default_gateway
		self.access_listlist = access_listlist
		self.mgmt_trafficlist = mgmt_trafficlist
		self.frag = frag
		self.tcp = tcp
		self.routelist = routelist
		self.dns = dns
		self.icmp = icmp
		self.map_listlist = map_listlist
		self.nat = nat
		self.nat_global = nat_global

	def __str__(self):
		return ""

class Ip_access_list__icmp_cfg__icmp_src_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	any_src_icmp=PosRangedInteger(0, 1)
	host_src_icmp = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_src_icmp = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	mask_src_icmp = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, any_src_icmp=None, host_src_icmp=None, subnet_src_icmp=None, mask_src_icmp=None):
		self.any_src_icmp = any_src_icmp
		self.host_src_icmp = host_src_icmp
		self.subnet_src_icmp = subnet_src_icmp
		self.mask_src_icmp = mask_src_icmp

	def __str__(self):
		return ""

class Ip_access_list__icmp_cfg__code(AxapiObject):
	__metaclass__ = StructMeta 
	any_code=PosRangedInteger(0, 1)
	icmp_code=PosRangedInteger(0, 254)
	def __init__(self, any_code=None, icmp_code=None):
		self.any_code = any_code
		self.icmp_code = icmp_code

	def __str__(self):
		return ""

class Ip_access_list__icmp_cfg__type__type_code(AxapiObject):
	__metaclass__ = StructMeta 
	type_any_code=PosRangedInteger(0, 1)
	type_icmp_code=PosRangedInteger(0, 254)
	type_any_src=PosRangedInteger(0, 1)
	type_host_src = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	type_subnet_src = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	type_mask_src = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, type_any_code=None, type_icmp_code=None, type_any_src=None, type_host_src=None, type_subnet_src=None, type_mask_src=None):
		self.type_any_code = type_any_code
		self.type_icmp_code = type_icmp_code
		self.type_any_src = type_any_src
		self.type_host_src = type_host_src
		self.type_subnet_src = type_subnet_src
		self.type_mask_src = type_mask_src

	def __str__(self):
		return ""

class Ip_access_list__icmp_cfg__type__dest_unreach_cfg__dest_un_code(AxapiObject):
	__metaclass__ = StructMeta 
	dest_un_any_code=PosRangedInteger(0, 1)
	dest_un_icmp_code=PosRangedInteger(0, 254)
	frag_required=PosRangedInteger(0, 1)
	host_unreachable=PosRangedInteger(0, 1)
	network_unreachable=PosRangedInteger(0, 1)
	port_unreachable=PosRangedInteger(0, 1)
	proto_unreachable=PosRangedInteger(0, 1)
	route_failed=PosRangedInteger(0, 1)
	def __init__(self, dest_un_any_code=None, dest_un_icmp_code=None, frag_required=None, host_unreachable=None, network_unreachable=None, port_unreachable=None, proto_unreachable=None, route_failed=None):
		self.dest_un_any_code = dest_un_any_code
		self.dest_un_icmp_code = dest_un_icmp_code
		self.frag_required = frag_required
		self.host_unreachable = host_unreachable
		self.network_unreachable = network_unreachable
		self.port_unreachable = port_unreachable
		self.proto_unreachable = proto_unreachable
		self.route_failed = route_failed

	def __str__(self):
		return ""

class Ip_access_list__icmp_cfg__type__dest_unreach_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dest_unreachable=PosRangedInteger(0, 1)
	dest_un_any_src=PosRangedInteger(0, 1)
	dest_un_host_src = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	dest_un_subnet_src = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	dest_un_mask_src = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, dest_unreachable=None, dest_un_code=None, dest_un_any_src=None, dest_un_host_src=None, dest_un_subnet_src=None, dest_un_mask_src=None):
		self.dest_unreachable = dest_unreachable
		self.dest_un_code = dest_un_code
		self.dest_un_any_src = dest_un_any_src
		self.dest_un_host_src = dest_un_host_src
		self.dest_un_subnet_src = dest_un_subnet_src
		self.dest_un_mask_src = dest_un_mask_src

	def __str__(self):
		return ""

class Ip_access_list__icmp_cfg__type(AxapiObject):
	__metaclass__ = StructMeta 
	icmp_type=PosRangedInteger(0, 254)
	any_type=PosRangedInteger(0, 1)
	echo_reply=PosRangedInteger(0, 1)
	echo_request=PosRangedInteger(0, 1)
	info_reply=PosRangedInteger(0, 1)
	info_request=PosRangedInteger(0, 1)
	mask_reply=PosRangedInteger(0, 1)
	mask_request=PosRangedInteger(0, 1)
	parameter_problem=PosRangedInteger(0, 1)
	redirect=PosRangedInteger(0, 1)
	source_quench=PosRangedInteger(0, 1)
	time_exceeded=PosRangedInteger(0, 1)
	timestamp=PosRangedInteger(0, 1)
	timestamp_reply=PosRangedInteger(0, 1)
	def __init__(self, icmp_type=None, any_type=None, echo_reply=None, echo_request=None, info_reply=None, info_request=None, mask_reply=None, mask_request=None, parameter_problem=None, redirect=None, source_quench=None, time_exceeded=None, timestamp=None, timestamp_reply=None, type_code=None, dest_unreach_cfg=None):
		self.icmp_type = icmp_type
		self.any_type = any_type
		self.echo_reply = echo_reply
		self.echo_request = echo_request
		self.info_reply = info_reply
		self.info_request = info_request
		self.mask_reply = mask_reply
		self.mask_request = mask_request
		self.parameter_problem = parameter_problem
		self.redirect = redirect
		self.source_quench = source_quench
		self.time_exceeded = time_exceeded
		self.timestamp = timestamp
		self.timestamp_reply = timestamp_reply
		self.type_code = type_code
		self.dest_unreach_cfg = dest_unreach_cfg

	def __str__(self):
		return ""

class Ip_access_list__icmp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	icmp=PosRangedInteger(0, 1)
	def __init__(self, icmp=None, icmp_src_cfg=None, code=None, type=None):
		self.icmp = icmp
		self.icmp_src_cfg = icmp_src_cfg
		self.code = code
		self.type = type

	def __str__(self):
		return ""

class Ip_access_list__ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip=PosRangedInteger(0, 1)
	any_src_ip=PosRangedInteger(0, 1)
	host_src_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_src_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	mask_src_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ip=None, any_src_ip=None, host_src_ip=None, subnet_src_ip=None, mask_src_ip=None):
		self.ip = ip
		self.any_src_ip = any_src_ip
		self.host_src_ip = host_src_ip
		self.subnet_src_ip = subnet_src_ip
		self.mask_src_ip = mask_src_ip

	def __str__(self):
		return ""

class Ip_access_list__any_code_any_source_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	any_code_any_src=PosRangedInteger(0, 1)
	any_code_host_src = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	any_code_subnet_src = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	any_code_mask_src = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, any_code_any_src=None, any_code_host_src=None, any_code_subnet_src=None, any_code_mask_src=None):
		self.any_code_any_src = any_code_any_src
		self.any_code_host_src = any_code_host_src
		self.any_code_subnet_src = any_code_subnet_src
		self.any_code_mask_src = any_code_mask_src

	def __str__(self):
		return ""

class Ip_access_list__dst_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	any_dst_ip=PosRangedInteger(0, 1)
	host_dst_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_dst_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	mask_dst_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	fragments=PosRangedInteger(0, 1)
	vlan=PosRangedInteger(1, 4094)
	dscp=PosRangedInteger(1, 63)
	log=PosRangedInteger(0, 1)
	def __init__(self, any_dst_ip=None, host_dst_ip=None, subnet_dst_ip=None, mask_dst_ip=None, fragments=None, vlan=None, dscp=None, log=None):
		self.any_dst_ip = any_dst_ip
		self.host_dst_ip = host_dst_ip
		self.subnet_dst_ip = subnet_dst_ip
		self.mask_dst_ip = mask_dst_ip
		self.fragments = fragments
		self.vlan = vlan
		self.dscp = dscp
		self.log = log

	def __str__(self):
		return ""

class Ip_access_list__l4_cfg__l4_src_cfg__l4_src_port_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	eq_src=PosRangedInteger(1, 65535)
	gt_src=PosRangedInteger(1, 65534)
	lt_src=PosRangedInteger(2, 65535)
	range_src=PosRangedInteger(1, 65535)
	port_num_end_src=PosRangedInteger(1, 65535)
	def __init__(self, eq_src=None, gt_src=None, lt_src=None, range_src=None, port_num_end_src=None):
		self.eq_src = eq_src
		self.gt_src = gt_src
		self.lt_src = lt_src
		self.range_src = range_src
		self.port_num_end_src = port_num_end_src

	def __str__(self):
		return ""

class Ip_access_list__l4_cfg__l4_src_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	any_src_tcp=PosRangedInteger(0, 1)
	host_src_tcp = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_src_tcp = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	mask_src_tcp = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, any_src_tcp=None, host_src_tcp=None, subnet_src_tcp=None, mask_src_tcp=None, l4_src_port_cfg=None):
		self.any_src_tcp = any_src_tcp
		self.host_src_tcp = host_src_tcp
		self.subnet_src_tcp = subnet_src_tcp
		self.mask_src_tcp = mask_src_tcp
		self.l4_src_port_cfg = l4_src_port_cfg

	def __str__(self):
		return ""

class Ip_access_list__l4_cfg__l4_dst_cfg__l4_dst_port_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	eq_dst=PosRangedInteger(1, 65535)
	gt_dst=PosRangedInteger(1, 65534)
	lt_dst=PosRangedInteger(2, 65535)
	range_dst=PosRangedInteger(1, 65535)
	port_num_end_dst=PosRangedInteger(1, 65535)
	def __init__(self, eq_dst=None, gt_dst=None, lt_dst=None, range_dst=None, port_num_end_dst=None):
		self.eq_dst = eq_dst
		self.gt_dst = gt_dst
		self.lt_dst = lt_dst
		self.range_dst = range_dst
		self.port_num_end_dst = port_num_end_dst

	def __str__(self):
		return ""

class Ip_access_list__l4_cfg__l4_dst_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	any_dst_tcp=PosRangedInteger(0, 1)
	host_dst_tcp = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_dst_tcp = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	mask_dst_tcp = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, any_dst_tcp=None, host_dst_tcp=None, subnet_dst_tcp=None, mask_dst_tcp=None, l4_dst_port_cfg=None):
		self.any_dst_tcp = any_dst_tcp
		self.host_dst_tcp = host_dst_tcp
		self.subnet_dst_tcp = subnet_dst_tcp
		self.mask_dst_tcp = mask_dst_tcp
		self.l4_dst_port_cfg = l4_dst_port_cfg

	def __str__(self):
		return ""

class Ip_access_list__l4_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tcp=PosRangedInteger(0, 1)
	udp=PosRangedInteger(0, 1)
	tcp_fragments=PosRangedInteger(0, 1)
	vlan=PosRangedInteger(1, 4094)
	dscp=PosRangedInteger(1, 63)
	established=PosRangedInteger(0, 1)
	log=PosInteger()
	def __init__(self, tcp=None, udp=None, l4_src_cfg=None, l4_dst_cfg=None, tcp_fragments=None, vlan=None, dscp=None, established=None, log=None):
		self.tcp = tcp
		self.udp = udp
		self.l4_src_cfg = l4_src_cfg
		self.l4_dst_cfg = l4_dst_cfg
		self.tcp_fragments = tcp_fragments
		self.vlan = vlan
		self.dscp = dscp
		self.established = established
		self.log = log

	def __str__(self):
		return ""

class Ip_access_list(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 16)
	seq_num=PosRangedInteger(1, 8192)
	action = Enum(['deny', 'permit', 'l3-vlan-fwd-disable'])
	remark=SizedString(1, 63)
	def __init__(self, name, seq_num=None, action=None, remark=None, icmp_cfg=None, ip_cfg=None, any_code_any_source_cfg=None, dst_ip_cfg=None, l4_cfg=None):
		self.name = name
		self.seq_num = seq_num
		self.action = action
		self.remark = remark
		self.icmp_cfg = icmp_cfg
		self.ip_cfg = ip_cfg
		self.any_code_any_source_cfg = any_code_any_source_cfg
		self.dst_ip_cfg = dst_ip_cfg
		self.l4_cfg = l4_cfg

	def __str__(self):
		return str(self.name)

class Ip_mgmt_traffic__source_interface__loopback(AxapiObject):
	__metaclass__ = StructMeta 
	loopback_num=PosRangedInteger(1, 10)
	def __init__(self, loopback_num=None):
		self.loopback_num = loopback_num

	def __str__(self):
		return ""

class Ip_mgmt_traffic__source_interface(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, loopback=None):
		self.loopback = loopback

	def __str__(self):
		return ""

class Ip_mgmt_traffic(AxapiObject):
	__metaclass__ = StructMeta 
	traffic_type = Enum(['all', 'ftp', 'ntp', 'rcp', 'snmp', 'ssh', 'syslog', 'telnet', 'tftp', 'web'])
	def __init__(self, traffic_type, source_interface):
		self.traffic_type = traffic_type
		self.source_interface = source_interface

	def __str__(self):
		return str(self.traffic_type) + '+' + str(self.source_interface)

class Ip_route__ip_dest_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip_dest_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_next_hop = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	distance=PosRangedInteger(1, 255)
	def __init__(self, ip_dest_addr, ip_mask, ip_next_hop, distance=None):
		self.ip_dest_addr = ip_dest_addr
		self.ip_mask = ip_mask
		self.ip_next_hop = ip_next_hop
		self.distance = distance

	def __str__(self):
		return str(self.ip_dest_addr) + '+' + str(self.ip_mask) + '+' + str(self.ip_next_hop)

class Ip_route__static(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, bfdlist=None):
		self.bfdlist = bfdlist

	def __str__(self):
		return ""

class Ip_route(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ip_dest_cfg, static=None):
		self.ip_dest_cfg = ip_dest_cfg
		self.static = static

	def __str__(self):
		return str(self.ip_dest_cfg)

class Ip_route_static_bfd(AxapiObject):
	__metaclass__ = StructMeta 
	local_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	nexthop_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, local_ip, nexthop_ip):
		self.local_ip = local_ip
		self.nexthop_ip = nexthop_ip

	def __str__(self):
		return str(self.local_ip) + '+' + str(self.nexthop_ip)

class Ip_map_list__name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	file=PosRangedInteger(0, 1)
	def __init__(self, name, file=None):
		self.name = name
		self.file = file

	def __str__(self):
		return str(self.name)

class Ip_map_list(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, name_cfg, local_start_cfg=None):
		self.name_cfg = name_cfg
		self.local_start_cfg = local_start_cfg

	def __str__(self):
		return str(self.name_cfg)

class Ip_local_start_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	local_start_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	global_start_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	count=PosRangedInteger(1, 16777216)
	def __init__(self, local_start_ip=None, global_start_ip=None, count=None):
		self.local_start_ip = local_start_ip
		self.global_start_ip = global_start_ip
		self.count = count

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

class IpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIp(self):
		"""
		Retrieve the ip identified by the specified identifier
		
		Returns:
			An instance of the Ip class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ip does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ip')
		return deserialize_Ip_json(payload)

