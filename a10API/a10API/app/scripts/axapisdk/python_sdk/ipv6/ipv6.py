########################################################################################################################
# File name: ipv6.py
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
	'https://axapi.a10networks.com/axapi/v3/ipv6',
]

def deserialize_Ipv6_rules__icmp_cfg__icmp_src_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_from_icmp = data.get('any-from-icmp')
	host_from_icmp = data.get('host-from-icmp')
	subnet_from_icmp = data.get('subnet-from-icmp')
	result = Ipv6_rules__icmp_cfg__icmp_src_cfg(any_from_icmp=any_from_icmp, host_from_icmp=host_from_icmp, subnet_from_icmp=subnet_from_icmp)
	return result

def deserialize_Ipv6_rules__icmp_cfg__code_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_code = data.get('any-code')
	icmp_code = data.get('icmp-code')
	result = Ipv6_rules__icmp_cfg__code(any_code=any_code, icmp_code=icmp_code)
	return result

def deserialize_Ipv6_rules__icmp_cfg__type__type_code_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type_any_code = data.get('type-any-code')
	type_icmp_code = data.get('type-icmp-code')
	host_type_code = data.get('host-type-code')
	subnet_type_code = data.get('subnet-type-code')
	result = Ipv6_rules__icmp_cfg__type__type_code(type_any_code=type_any_code, type_icmp_code=type_icmp_code, host_type_code=host_type_code, subnet_type_code=subnet_type_code)
	return result

def deserialize_Ipv6_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dest_un_any_code = data.get('dest-un-any-code')
	dest_un_icmp_code = data.get('dest-un-icmp-code')
	addr_unreachable = data.get('addr-unreachable')
	admin_prohibited = data.get('admin-prohibited')
	no_route = data.get('no-route')
	not_neighbour = data.get('not-neighbour')
	port_unreachable = data.get('port-unreachable')
	result = Ipv6_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code(dest_un_any_code=dest_un_any_code, dest_un_icmp_code=dest_un_icmp_code, addr_unreachable=addr_unreachable, admin_prohibited=admin_prohibited, no_route=no_route, not_neighbour=not_neighbour, port_unreachable=port_unreachable)
	return result

def deserialize_Ipv6_rules__icmp_cfg__type__dest_unreach_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dest_unreachable = data.get('dest-unreachable')
	dest_un_code = deserialize_Ipv6_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(data.get('dest-un-code'))
	dest_un_any_src = data.get('dest-un-any-src')
	dest_un_host_src = data.get('dest-un-host-src')
	dest_un_subnet_src = data.get('dest-un-subnet-src')
	result = Ipv6_rules__icmp_cfg__type__dest_unreach_cfg(dest_unreachable=dest_unreachable, dest_un_code=dest_un_code, dest_un_any_src=dest_un_any_src, dest_un_host_src=dest_un_host_src, dest_un_subnet_src=dest_un_subnet_src)
	return result

def deserialize_Ipv6_rules__icmp_cfg__type_json(obj):
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
	packet_too_big = data.get('packet-too-big')
	param_prob = data.get('param-prob')
	time_exceeded = data.get('time-exceeded')
	type_code = deserialize_Ipv6_rules__icmp_cfg__type__type_code_json(data.get('type-code'))
	dest_unreach_cfg = deserialize_Ipv6_rules__icmp_cfg__type__dest_unreach_cfg_json(data.get('dest-unreach-cfg'))
	result = Ipv6_rules__icmp_cfg__type(icmp_type=icmp_type, any_type=any_type, echo_reply=echo_reply, echo_request=echo_request, packet_too_big=packet_too_big, param_prob=param_prob, time_exceeded=time_exceeded, type_code=type_code, dest_unreach_cfg=dest_unreach_cfg)
	return result

def deserialize_Ipv6_rules__icmp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp = data.get('icmp')
	icmp_src_cfg = deserialize_Ipv6_rules__icmp_cfg__icmp_src_cfg_json(data.get('icmp-src-cfg'))
	code = deserialize_Ipv6_rules__icmp_cfg__code_json(data.get('code'))
	type = deserialize_Ipv6_rules__icmp_cfg__type_json(data.get('type'))
	result = Ipv6_rules__icmp_cfg(icmp=icmp, icmp_src_cfg=icmp_src_cfg, code=code, type=type)
	return result

def deserialize_Ipv6_rules__src_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_from_ip = data.get('any-from-ip')
	host_from_ip = data.get('host-from-ip')
	subnet_from_ip = data.get('subnet-from-ip')
	result = Ipv6_rules__src_ip_cfg(any_from_ip=any_from_ip, host_from_ip=host_from_ip, subnet_from_ip=subnet_from_ip)
	return result

def deserialize_Ipv6_rules__dst_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_to_ip = data.get('any-to-ip')
	host_to_ip = data.get('host-to-ip')
	subnet_to_ip = data.get('subnet-to-ip')
	fragments = data.get('fragments')
	vlan = data.get('vlan')
	dscp = data.get('dscp')
	log = data.get('log')
	transparent_session_only = data.get('transparent-session-only')
	result = Ipv6_rules__dst_ip_cfg(any_to_ip=any_to_ip, host_to_ip=host_to_ip, subnet_to_ip=subnet_to_ip, fragments=fragments, vlan=vlan, dscp=dscp, log=log, transparent_session_only=transparent_session_only)
	return result

def deserialize_Ipv6_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(obj):
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
	result = Ipv6_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg(eq_src=eq_src, gt_src=gt_src, lt_src=lt_src, range_src=range_src, port_num_end_src=port_num_end_src)
	return result

def deserialize_Ipv6_rules__l4_cfg__l4_src_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_from_tcp = data.get('any-from-tcp')
	host_from_tcp = data.get('host-from-tcp')
	subnet_from_tcp = data.get('subnet-from-tcp')
	l4_src_port_cfg = deserialize_Ipv6_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(data.get('l4-src-port-cfg'))
	result = Ipv6_rules__l4_cfg__l4_src_cfg(any_from_tcp=any_from_tcp, host_from_tcp=host_from_tcp, subnet_from_tcp=subnet_from_tcp, l4_src_port_cfg=l4_src_port_cfg)
	return result

def deserialize_Ipv6_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(obj):
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
	result = Ipv6_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg(eq_dst=eq_dst, gt_dst=gt_dst, lt_dst=lt_dst, range_dst=range_dst, port_num_end_dst=port_num_end_dst)
	return result

def deserialize_Ipv6_rules__l4_cfg__l4_dst_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_to_tcp = data.get('any-to-tcp')
	host_to_tcp = data.get('host-to-tcp')
	subnet_to_tcp = data.get('subnet-to-tcp')
	l4_dst_port_cfg = deserialize_Ipv6_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(data.get('l4-dst-port-cfg'))
	result = Ipv6_rules__l4_cfg__l4_dst_cfg(any_to_tcp=any_to_tcp, host_to_tcp=host_to_tcp, subnet_to_tcp=subnet_to_tcp, l4_dst_port_cfg=l4_dst_port_cfg)
	return result

def deserialize_Ipv6_rules__l4_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	l4_src_cfg = deserialize_Ipv6_rules__l4_cfg__l4_src_cfg_json(data.get('l4-src-cfg'))
	l4_dst_cfg = deserialize_Ipv6_rules__l4_cfg__l4_dst_cfg_json(data.get('l4-dst-cfg'))
	tcp_fragments = data.get('tcp-fragments')
	vlan = data.get('vlan')
	dscp = data.get('dscp')
	established = data.get('established')
	log = data.get('log')
	transparent_session_only = data.get('transparent-session-only')
	result = Ipv6_rules__l4_cfg(tcp=tcp, udp=udp, l4_src_cfg=l4_src_cfg, l4_dst_cfg=l4_dst_cfg, tcp_fragments=tcp_fragments, vlan=vlan, dscp=dscp, established=established, log=log, transparent_session_only=transparent_session_only)
	return result

def deserialize_Ipv6_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	seq_num = data.get('seq-num')
	action = data.get('action')
	remark = data.get('remark')
	icmp_cfg = deserialize_Ipv6_rules__icmp_cfg_json(data.get('icmp-cfg'))
	ipv6 = data.get('ipv6')
	src_ip_cfg = deserialize_Ipv6_rules__src_ip_cfg_json(data.get('src-ip-cfg'))
	dst_ip_cfg = deserialize_Ipv6_rules__dst_ip_cfg_json(data.get('dst-ip-cfg'))
	l4_cfg = deserialize_Ipv6_rules__l4_cfg_json(data.get('l4-cfg'))
	result = Ipv6_rules(seq_num=seq_num, action=action, remark=remark, icmp_cfg=icmp_cfg, ipv6=ipv6, src_ip_cfg=src_ip_cfg, dst_ip_cfg=dst_ip_cfg, l4_cfg=l4_cfg)
	return result

def deserialize_list_Ipv6_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_rules_json(item))
	return list(container)

def deserialize_Ipv6_access_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	rules = deserialize_list_Ipv6_rules_json(data.get('rules'))
	result = Ipv6_access_list(name=name, rules=rules)
	return result

def deserialize_list_Ipv6_access_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_access_list_json(item))
	return list(container)

def deserialize_Ipv6__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_address = data.get('ipv6-address')
	link_local = data.get('link-local')
	anycast = data.get('anycast')
	result = Ipv6__address(ipv6_address=ipv6_address, link_local=link_local, anycast=anycast)
	return result

def deserialize_Ipv6__default_gateway_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_default_gateway = data.get('ipv6-default-gateway')
	result = Ipv6__default_gateway(ipv6_default_gateway=ipv6_default_gateway)
	return result

def deserialize_Ipv6__frag__timeout_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timeout_val = data.get('timeout-val')
	result = Ipv6__frag__timeout(timeout_val=timeout_val)
	return result

def deserialize_Ipv6__frag_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timeout = deserialize_Ipv6__frag__timeout_json(data.get('timeout'))
	result = Ipv6__frag(timeout=timeout)
	return result

def deserialize_Ipv6__icmpv6__disable_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	redirect = data.get('redirect')
	unreachable = data.get('unreachable')
	result = Ipv6__icmpv6__disable(redirect=redirect, unreachable=unreachable)
	return result

def deserialize_Ipv6__icmpv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	disable = deserialize_Ipv6__icmpv6__disable_json(data.get('disable'))
	result = Ipv6__icmpv6(disable=disable)
	return result

def deserialize_Ipv6_neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	mac = data.get('mac')
	ethernet = data.get('ethernet')
	trunk = data.get('trunk')
	vlan = data.get('vlan')
	result = Ipv6_neighbor(ipv6_addr=ipv6_addr, mac=mac, ethernet=ethernet, trunk=trunk, vlan=vlan)
	return result

def deserialize_list_Ipv6_neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_neighbor_json(item))
	return list(container)

def deserialize_Ipv6_route_static_bfd_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ve_num = data.get('ve-num')
	nexthop_ipv6_ll = data.get('nexthop-ipv6-ll')
	result = Ipv6_route_static_bfd_ve(ve_num=ve_num, nexthop_ipv6_ll=nexthop_ipv6_ll)
	return result

def deserialize_list_Ipv6_route_static_bfd_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_route_static_bfd_ve_json(item))
	return list(container)

def deserialize_Ipv6_route_static_bfd_trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk_num = data.get('trunk-num')
	nexthop_ipv6_ll = data.get('nexthop-ipv6-ll')
	result = Ipv6_route_static_bfd_trunk(trunk_num=trunk_num, nexthop_ipv6_ll=nexthop_ipv6_ll)
	return result

def deserialize_list_Ipv6_route_static_bfd_trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_route_static_bfd_trunk_json(item))
	return list(container)

def deserialize_Ipv6_route_static_bfd_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	eth_num = data.get('eth-num')
	nexthop_ipv6_ll = data.get('nexthop-ipv6-ll')
	result = Ipv6_route_static_bfd_ethernet(eth_num=eth_num, nexthop_ipv6_ll=nexthop_ipv6_ll)
	return result

def deserialize_list_Ipv6_route_static_bfd_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_route_static_bfd_ethernet_json(item))
	return list(container)

def deserialize_Ipv6_route_static_bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_ipv6 = data.get('local-ipv6')
	nexthop_ipv6 = data.get('nexthop-ipv6')
	velist = deserialize_list_Ipv6_route_static_bfd_ve_json(data.get('veList'))
	trunklist = deserialize_list_Ipv6_route_static_bfd_trunk_json(data.get('trunkList'))
	ethernetlist = deserialize_list_Ipv6_route_static_bfd_ethernet_json(data.get('ethernetList'))
	result = Ipv6_route_static_bfd(local_ipv6=local_ipv6, nexthop_ipv6=nexthop_ipv6, velist=velist, trunklist=trunklist, ethernetlist=ethernetlist)
	return result

def deserialize_list_Ipv6_route_static_bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_route_static_bfd_json(item))
	return list(container)

def deserialize_Ipv6_route__static_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bfdlist = deserialize_list_Ipv6_route_static_bfd_json(data.get('bfdList'))
	result = Ipv6_route__static(bfdlist=bfdlist)
	return result

def deserialize_Ipv6_route_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_address = data.get('ipv6-address')
	nexthop = data.get('nexthop')
	distance = data.get('distance')
	static = deserialize_Ipv6_route__static_json(data.get('static'))
	result = Ipv6_route(ipv6_address=ipv6_address, nexthop=nexthop, distance=distance, static=static)
	return result

def deserialize_list_Ipv6_route_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_route_json(item))
	return list(container)

def deserialize_Ipv6_nat_pool__pool_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	gateway = data.get('gateway')
	vrid = data.get('vrid')
	ip_rr = data.get('ip-rr')
	result = Ipv6_nat_pool__pool_cfg(gateway=gateway, vrid=vrid, ip_rr=ip_rr)
	return result

def deserialize_Ipv6_nat_pool_json(obj):
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
	pool_cfg = deserialize_Ipv6_nat_pool__pool_cfg_json(data.get('pool-cfg'))
	result = Ipv6_nat_pool(pool_name=pool_name, start_address=start_address, end_address=end_address, netmask=netmask, pool_cfg=pool_cfg)
	return result

def deserialize_list_Ipv6_nat_pool_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_nat_pool_json(item))
	return list(container)

def deserialize_Ipv6__nat__inside__source_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	list = data.get('list')
	pool = data.get('pool')
	result = Ipv6__nat__inside__source(list=list, pool=pool)
	return result

def deserialize_Ipv6__nat__inside_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	source = deserialize_Ipv6__nat__inside__source_json(data.get('source'))
	result = Ipv6__nat__inside(source=source)
	return result

def deserialize_Ipv6__nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	poollist = deserialize_list_Ipv6_nat_pool_json(data.get('poolList'))
	inside = deserialize_Ipv6__nat__inside_json(data.get('inside'))
	result = Ipv6__nat(poollist=poollist, inside=inside)
	return result

def deserialize_Ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	access_listlist = deserialize_list_Ipv6_access_list_json(data.get('access-listList'))
	address = deserialize_Ipv6__address_json(data.get('address'))
	default_gateway = deserialize_Ipv6__default_gateway_json(data.get('default-gateway'))
	frag = deserialize_Ipv6__frag_json(data.get('frag'))
	icmpv6 = deserialize_Ipv6__icmpv6_json(data.get('icmpv6'))
	neighborlist = deserialize_list_Ipv6_neighbor_json(data.get('neighborList'))
	routelist = deserialize_list_Ipv6_route_json(data.get('routeList'))
	nat = deserialize_Ipv6__nat_json(data.get('nat'))
	result = Ipv6(access_listlist=access_listlist, address=address, default_gateway=default_gateway, frag=frag, icmpv6=icmpv6, neighborlist=neighborlist, routelist=routelist, nat=nat)
	return result

class Ipv6__address(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_address=SizedString(1, 255)
	link_local=PosRangedInteger(0, 1)
	anycast=PosRangedInteger(0, 1)
	def __init__(self, ipv6_address=None, link_local=None, anycast=None):
		self.ipv6_address = ipv6_address
		self.link_local = link_local
		self.anycast = anycast

	def __str__(self):
		return ""

class Ipv6__default_gateway(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_default_gateway=SizedString(1, 255)
	def __init__(self, ipv6_default_gateway=None):
		self.ipv6_default_gateway = ipv6_default_gateway

	def __str__(self):
		return ""

class Ipv6__frag__timeout(AxapiObject):
	__metaclass__ = StructMeta 
	timeout_val=PosRangedInteger(4, 16000)
	def __init__(self, timeout_val=None):
		self.timeout_val = timeout_val

	def __str__(self):
		return ""

class Ipv6__frag(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, timeout=None):
		self.timeout = timeout

	def __str__(self):
		return ""

class Ipv6__icmpv6__disable(AxapiObject):
	__metaclass__ = StructMeta 
	redirect=PosRangedInteger(0, 1)
	unreachable=PosRangedInteger(0, 1)
	def __init__(self, redirect=None, unreachable=None):
		self.redirect = redirect
		self.unreachable = unreachable

	def __str__(self):
		return ""

class Ipv6__icmpv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, disable=None):
		self.disable = disable

	def __str__(self):
		return ""

class Ipv6__nat__inside__source(AxapiObject):
	__metaclass__ = StructMeta 
	list=SizedString(1, 16)
	pool=SizedString(1, 63)
	def __init__(self, list=None, pool=None):
		self.list = list
		self.pool = pool

	def __str__(self):
		return ""

class Ipv6__nat__inside(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, source=None):
		self.source = source

	def __str__(self):
		return ""

class Ipv6__nat(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, poollist=None, inside=None):
		self.poollist = poollist
		self.inside = inside

	def __str__(self):
		return ""

class Ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, access_listlist=None, address=None, default_gateway=None, frag=None, icmpv6=None, neighborlist=None, routelist=None, nat=None):
		self.access_listlist = access_listlist
		self.address = address
		self.default_gateway = default_gateway
		self.frag = frag
		self.icmpv6 = icmpv6
		self.neighborlist = neighborlist
		self.routelist = routelist
		self.nat = nat

	def __str__(self):
		return ""

class Ipv6_access_list(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 16)
	def __init__(self, name, rules=None):
		self.name = name
		self.rules = rules

	def __str__(self):
		return str(self.name)

class Ipv6_rules__icmp_cfg__icmp_src_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	any_from_icmp=PosRangedInteger(0, 1)
	host_from_icmp=SizedString(1, 255)
	subnet_from_icmp=SizedString(1, 255)
	def __init__(self, any_from_icmp=None, host_from_icmp=None, subnet_from_icmp=None):
		self.any_from_icmp = any_from_icmp
		self.host_from_icmp = host_from_icmp
		self.subnet_from_icmp = subnet_from_icmp

	def __str__(self):
		return ""

class Ipv6_rules__icmp_cfg__code(AxapiObject):
	__metaclass__ = StructMeta 
	any_code=PosRangedInteger(0, 1)
	icmp_code=PosRangedInteger(0, 254)
	def __init__(self, any_code=None, icmp_code=None):
		self.any_code = any_code
		self.icmp_code = icmp_code

	def __str__(self):
		return ""

class Ipv6_rules__icmp_cfg__type__type_code(AxapiObject):
	__metaclass__ = StructMeta 
	type_any_code=PosRangedInteger(0, 1)
	type_icmp_code=PosRangedInteger(0, 254)
	host_type_code=SizedString(1, 255)
	subnet_type_code=SizedString(1, 255)
	def __init__(self, type_any_code=None, type_icmp_code=None, host_type_code=None, subnet_type_code=None):
		self.type_any_code = type_any_code
		self.type_icmp_code = type_icmp_code
		self.host_type_code = host_type_code
		self.subnet_type_code = subnet_type_code

	def __str__(self):
		return ""

class Ipv6_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code(AxapiObject):
	__metaclass__ = StructMeta 
	dest_un_any_code=PosRangedInteger(0, 1)
	dest_un_icmp_code=PosRangedInteger(0, 254)
	addr_unreachable=PosRangedInteger(0, 1)
	admin_prohibited=PosRangedInteger(0, 1)
	no_route=PosRangedInteger(0, 1)
	not_neighbour=PosRangedInteger(0, 1)
	port_unreachable=PosRangedInteger(0, 1)
	def __init__(self, dest_un_any_code=None, dest_un_icmp_code=None, addr_unreachable=None, admin_prohibited=None, no_route=None, not_neighbour=None, port_unreachable=None):
		self.dest_un_any_code = dest_un_any_code
		self.dest_un_icmp_code = dest_un_icmp_code
		self.addr_unreachable = addr_unreachable
		self.admin_prohibited = admin_prohibited
		self.no_route = no_route
		self.not_neighbour = not_neighbour
		self.port_unreachable = port_unreachable

	def __str__(self):
		return ""

class Ipv6_rules__icmp_cfg__type__dest_unreach_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dest_unreachable=PosRangedInteger(0, 1)
	dest_un_any_src=PosRangedInteger(0, 1)
	dest_un_host_src=SizedString(1, 255)
	dest_un_subnet_src=SizedString(1, 255)
	def __init__(self, dest_unreachable=None, dest_un_code=None, dest_un_any_src=None, dest_un_host_src=None, dest_un_subnet_src=None):
		self.dest_unreachable = dest_unreachable
		self.dest_un_code = dest_un_code
		self.dest_un_any_src = dest_un_any_src
		self.dest_un_host_src = dest_un_host_src
		self.dest_un_subnet_src = dest_un_subnet_src

	def __str__(self):
		return ""

class Ipv6_rules__icmp_cfg__type(AxapiObject):
	__metaclass__ = StructMeta 
	icmp_type=PosRangedInteger(0, 254)
	any_type=PosRangedInteger(0, 1)
	echo_reply=PosRangedInteger(0, 1)
	echo_request=PosRangedInteger(0, 1)
	packet_too_big=PosRangedInteger(0, 1)
	param_prob=PosRangedInteger(0, 1)
	time_exceeded=PosRangedInteger(0, 1)
	def __init__(self, icmp_type=None, any_type=None, echo_reply=None, echo_request=None, packet_too_big=None, param_prob=None, time_exceeded=None, type_code=None, dest_unreach_cfg=None):
		self.icmp_type = icmp_type
		self.any_type = any_type
		self.echo_reply = echo_reply
		self.echo_request = echo_request
		self.packet_too_big = packet_too_big
		self.param_prob = param_prob
		self.time_exceeded = time_exceeded
		self.type_code = type_code
		self.dest_unreach_cfg = dest_unreach_cfg

	def __str__(self):
		return ""

class Ipv6_rules__icmp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	icmp=PosRangedInteger(0, 1)
	def __init__(self, icmp=None, icmp_src_cfg=None, code=None, type=None):
		self.icmp = icmp
		self.icmp_src_cfg = icmp_src_cfg
		self.code = code
		self.type = type

	def __str__(self):
		return ""

class Ipv6_rules__src_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	any_from_ip=PosRangedInteger(0, 1)
	host_from_ip=SizedString(1, 255)
	subnet_from_ip=SizedString(1, 255)
	def __init__(self, any_from_ip=None, host_from_ip=None, subnet_from_ip=None):
		self.any_from_ip = any_from_ip
		self.host_from_ip = host_from_ip
		self.subnet_from_ip = subnet_from_ip

	def __str__(self):
		return ""

class Ipv6_rules__dst_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	any_to_ip=PosRangedInteger(0, 1)
	host_to_ip=SizedString(1, 255)
	subnet_to_ip=SizedString(1, 255)
	fragments=PosRangedInteger(0, 1)
	vlan=PosRangedInteger(1, 4094)
	dscp=PosRangedInteger(1, 63)
	log=PosRangedInteger(0, 1)
	transparent_session_only=PosRangedInteger(0, 1)
	def __init__(self, any_to_ip=None, host_to_ip=None, subnet_to_ip=None, fragments=None, vlan=None, dscp=None, log=None, transparent_session_only=None):
		self.any_to_ip = any_to_ip
		self.host_to_ip = host_to_ip
		self.subnet_to_ip = subnet_to_ip
		self.fragments = fragments
		self.vlan = vlan
		self.dscp = dscp
		self.log = log
		self.transparent_session_only = transparent_session_only

	def __str__(self):
		return ""

class Ipv6_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	eq_src=PosRangedInteger(1, 65535)
	gt_src=PosRangedInteger(1, 65535)
	lt_src=PosRangedInteger(1, 65535)
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

class Ipv6_rules__l4_cfg__l4_src_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	any_from_tcp=PosRangedInteger(0, 1)
	host_from_tcp=SizedString(1, 255)
	subnet_from_tcp=SizedString(1, 255)
	def __init__(self, any_from_tcp=None, host_from_tcp=None, subnet_from_tcp=None, l4_src_port_cfg=None):
		self.any_from_tcp = any_from_tcp
		self.host_from_tcp = host_from_tcp
		self.subnet_from_tcp = subnet_from_tcp
		self.l4_src_port_cfg = l4_src_port_cfg

	def __str__(self):
		return ""

class Ipv6_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	eq_dst=PosRangedInteger(1, 65535)
	gt_dst=PosRangedInteger(1, 65535)
	lt_dst=PosRangedInteger(1, 65535)
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

class Ipv6_rules__l4_cfg__l4_dst_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	any_to_tcp=PosRangedInteger(0, 1)
	host_to_tcp=SizedString(1, 255)
	subnet_to_tcp=SizedString(1, 255)
	def __init__(self, any_to_tcp=None, host_to_tcp=None, subnet_to_tcp=None, l4_dst_port_cfg=None):
		self.any_to_tcp = any_to_tcp
		self.host_to_tcp = host_to_tcp
		self.subnet_to_tcp = subnet_to_tcp
		self.l4_dst_port_cfg = l4_dst_port_cfg

	def __str__(self):
		return ""

class Ipv6_rules__l4_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tcp=PosRangedInteger(0, 1)
	udp=PosRangedInteger(0, 1)
	tcp_fragments=PosRangedInteger(0, 1)
	vlan=PosRangedInteger(1, 4094)
	dscp=PosRangedInteger(1, 63)
	established=PosRangedInteger(0, 1)
	log=PosInteger()
	transparent_session_only=PosInteger()
	def __init__(self, tcp=None, udp=None, l4_src_cfg=None, l4_dst_cfg=None, tcp_fragments=None, vlan=None, dscp=None, established=None, log=None, transparent_session_only=None):
		self.tcp = tcp
		self.udp = udp
		self.l4_src_cfg = l4_src_cfg
		self.l4_dst_cfg = l4_dst_cfg
		self.tcp_fragments = tcp_fragments
		self.vlan = vlan
		self.dscp = dscp
		self.established = established
		self.log = log
		self.transparent_session_only = transparent_session_only

	def __str__(self):
		return ""

class Ipv6_rules(AxapiObject):
	__metaclass__ = StructMeta 
	seq_num=PosRangedInteger(1, 8192)
	action = Enum(['deny', 'permit', 'l3-vlan-fwd-disable'])
	remark=SizedString(1, 63)
	ipv6=PosRangedInteger(0, 1)
	def __init__(self, seq_num=None, action=None, remark=None, icmp_cfg=None, ipv6=None, src_ip_cfg=None, dst_ip_cfg=None, l4_cfg=None):
		self.seq_num = seq_num
		self.action = action
		self.remark = remark
		self.icmp_cfg = icmp_cfg
		self.ipv6 = ipv6
		self.src_ip_cfg = src_ip_cfg
		self.dst_ip_cfg = dst_ip_cfg
		self.l4_cfg = l4_cfg

	def __str__(self):
		return ""

class Ipv6_neighbor(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	mac=SizedString(1, 17)
	ethernet=PosRangedInteger(1, 2048)
	trunk=PosRangedInteger(1, 16)
	vlan=PosRangedInteger(1, 4094)
	def __init__(self, ipv6_addr, mac, ethernet=None, trunk=None, vlan=None):
		self.ipv6_addr = ipv6_addr
		self.mac = mac
		self.ethernet = ethernet
		self.trunk = trunk
		self.vlan = vlan

	def __str__(self):
		return str(self.ipv6_addr) + '+' + str(self.mac)

class Ipv6_route__static(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, bfdlist=None):
		self.bfdlist = bfdlist

	def __str__(self):
		return ""

class Ipv6_route(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_address=SizedString(1, 255)
	nexthop=SizedString(1, 255)
	distance=PosRangedInteger(1, 255)
	def __init__(self, ipv6_address, nexthop, distance=None, static=None):
		self.ipv6_address = ipv6_address
		self.nexthop = nexthop
		self.distance = distance
		self.static = static

	def __str__(self):
		return str(self.ipv6_address) + '+' + str(self.nexthop)

class Ipv6_route_static_bfd(AxapiObject):
	__metaclass__ = StructMeta 
	local_ipv6=SizedString(1, 255)
	nexthop_ipv6=SizedString(1, 255)
	def __init__(self, local_ipv6, nexthop_ipv6, velist=None, trunklist=None, ethernetlist=None):
		self.local_ipv6 = local_ipv6
		self.nexthop_ipv6 = nexthop_ipv6
		self.velist = velist
		self.trunklist = trunklist
		self.ethernetlist = ethernetlist

	def __str__(self):
		return str(self.local_ipv6) + '+' + str(self.nexthop_ipv6)

class Ipv6_route_static_bfd_ve(AxapiObject):
	__metaclass__ = StructMeta 
	ve_num=PosInteger()
	nexthop_ipv6_ll=SizedString(1, 255)
	def __init__(self, ve_num, nexthop_ipv6_ll):
		self.ve_num = ve_num
		self.nexthop_ipv6_ll = nexthop_ipv6_ll

	def __str__(self):
		return str(self.ve_num) + '+' + str(self.nexthop_ipv6_ll)

class Ipv6_route_static_bfd_trunk(AxapiObject):
	__metaclass__ = StructMeta 
	trunk_num=PosInteger()
	nexthop_ipv6_ll=SizedString(1, 255)
	def __init__(self, trunk_num, nexthop_ipv6_ll):
		self.trunk_num = trunk_num
		self.nexthop_ipv6_ll = nexthop_ipv6_ll

	def __str__(self):
		return str(self.trunk_num) + '+' + str(self.nexthop_ipv6_ll)

class Ipv6_route_static_bfd_ethernet(AxapiObject):
	__metaclass__ = StructMeta 
	eth_num=PosInteger()
	nexthop_ipv6_ll=SizedString(1, 255)
	def __init__(self, eth_num, nexthop_ipv6_ll):
		self.eth_num = eth_num
		self.nexthop_ipv6_ll = nexthop_ipv6_ll

	def __str__(self):
		return str(self.eth_num) + '+' + str(self.nexthop_ipv6_ll)

class Ipv6_nat_pool__pool_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	gateway=SizedString(1, 255)
	vrid=PosRangedInteger(1, 31)
	ip_rr=PosRangedInteger(0, 1)
	def __init__(self, gateway=None, vrid=None, ip_rr=None):
		self.gateway = gateway
		self.vrid = vrid
		self.ip_rr = ip_rr

	def __str__(self):
		return ""

class Ipv6_nat_pool(AxapiObject):
	__metaclass__ = StructMeta 
	pool_name=SizedString(1, 63)
	start_address=SizedString(1, 255)
	end_address=SizedString(1, 255)
	netmask=PosRangedInteger(64, 128)
	def __init__(self, pool_name, start_address=None, end_address=None, netmask=None, pool_cfg=None):
		self.pool_name = pool_name
		self.start_address = start_address
		self.end_address = end_address
		self.netmask = netmask
		self.pool_cfg = pool_cfg

	def __str__(self):
		return str(self.pool_name)

class Ipv6Client(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpv6(self):
		"""
		Retrieve the ipv6 identified by the specified identifier
		
		Returns:
			An instance of the Ipv6 class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified ipv6 does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('ipv6')
		return deserialize_Ipv6_json(payload)

