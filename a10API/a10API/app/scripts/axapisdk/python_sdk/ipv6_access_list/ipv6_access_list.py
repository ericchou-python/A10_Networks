########################################################################################################################
# File name: ipv6_access_list.py
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
	'https://axapi.a10networks.com/axapi/v3/ipv6/access-list',
]

def deserialize_Ipv6_access_list_rules__icmp_cfg__icmp_src_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_from_icmp = data.get('any-from-icmp')
	host_from_icmp = data.get('host-from-icmp')
	subnet_from_icmp = data.get('subnet-from-icmp')
	result = Ipv6_access_list_rules__icmp_cfg__icmp_src_cfg(any_from_icmp=any_from_icmp, host_from_icmp=host_from_icmp, subnet_from_icmp=subnet_from_icmp)
	return result

def deserialize_Ipv6_access_list_rules__icmp_cfg__code_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_code = data.get('any-code')
	icmp_code = data.get('icmp-code')
	result = Ipv6_access_list_rules__icmp_cfg__code(any_code=any_code, icmp_code=icmp_code)
	return result

def deserialize_Ipv6_access_list_rules__icmp_cfg__type__type_code_json(obj):
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
	result = Ipv6_access_list_rules__icmp_cfg__type__type_code(type_any_code=type_any_code, type_icmp_code=type_icmp_code, host_type_code=host_type_code, subnet_type_code=subnet_type_code)
	return result

def deserialize_Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(obj):
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
	result = Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code(dest_un_any_code=dest_un_any_code, dest_un_icmp_code=dest_un_icmp_code, addr_unreachable=addr_unreachable, admin_prohibited=admin_prohibited, no_route=no_route, not_neighbour=not_neighbour, port_unreachable=port_unreachable)
	return result

def deserialize_Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dest_unreachable = data.get('dest-unreachable')
	dest_un_code = deserialize_Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(data.get('dest-un-code'))
	dest_un_any_src = data.get('dest-un-any-src')
	dest_un_host_src = data.get('dest-un-host-src')
	dest_un_subnet_src = data.get('dest-un-subnet-src')
	result = Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg(dest_unreachable=dest_unreachable, dest_un_code=dest_un_code, dest_un_any_src=dest_un_any_src, dest_un_host_src=dest_un_host_src, dest_un_subnet_src=dest_un_subnet_src)
	return result

def deserialize_Ipv6_access_list_rules__icmp_cfg__type_json(obj):
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
	type_code = deserialize_Ipv6_access_list_rules__icmp_cfg__type__type_code_json(data.get('type-code'))
	dest_unreach_cfg = deserialize_Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg_json(data.get('dest-unreach-cfg'))
	result = Ipv6_access_list_rules__icmp_cfg__type(icmp_type=icmp_type, any_type=any_type, echo_reply=echo_reply, echo_request=echo_request, packet_too_big=packet_too_big, param_prob=param_prob, time_exceeded=time_exceeded, type_code=type_code, dest_unreach_cfg=dest_unreach_cfg)
	return result

def deserialize_Ipv6_access_list_rules__icmp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp = data.get('icmp')
	icmp_src_cfg = deserialize_Ipv6_access_list_rules__icmp_cfg__icmp_src_cfg_json(data.get('icmp-src-cfg'))
	code = deserialize_Ipv6_access_list_rules__icmp_cfg__code_json(data.get('code'))
	type = deserialize_Ipv6_access_list_rules__icmp_cfg__type_json(data.get('type'))
	result = Ipv6_access_list_rules__icmp_cfg(icmp=icmp, icmp_src_cfg=icmp_src_cfg, code=code, type=type)
	return result

def deserialize_Ipv6_access_list_rules__src_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_from_ip = data.get('any-from-ip')
	host_from_ip = data.get('host-from-ip')
	subnet_from_ip = data.get('subnet-from-ip')
	result = Ipv6_access_list_rules__src_ip_cfg(any_from_ip=any_from_ip, host_from_ip=host_from_ip, subnet_from_ip=subnet_from_ip)
	return result

def deserialize_Ipv6_access_list_rules__dst_ip_cfg_json(obj):
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
	result = Ipv6_access_list_rules__dst_ip_cfg(any_to_ip=any_to_ip, host_to_ip=host_to_ip, subnet_to_ip=subnet_to_ip, fragments=fragments, vlan=vlan, dscp=dscp, log=log, transparent_session_only=transparent_session_only)
	return result

def deserialize_Ipv6_access_list_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(obj):
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
	result = Ipv6_access_list_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg(eq_src=eq_src, gt_src=gt_src, lt_src=lt_src, range_src=range_src, port_num_end_src=port_num_end_src)
	return result

def deserialize_Ipv6_access_list_rules__l4_cfg__l4_src_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_from_tcp = data.get('any-from-tcp')
	host_from_tcp = data.get('host-from-tcp')
	subnet_from_tcp = data.get('subnet-from-tcp')
	l4_src_port_cfg = deserialize_Ipv6_access_list_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(data.get('l4-src-port-cfg'))
	result = Ipv6_access_list_rules__l4_cfg__l4_src_cfg(any_from_tcp=any_from_tcp, host_from_tcp=host_from_tcp, subnet_from_tcp=subnet_from_tcp, l4_src_port_cfg=l4_src_port_cfg)
	return result

def deserialize_Ipv6_access_list_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(obj):
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
	result = Ipv6_access_list_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg(eq_dst=eq_dst, gt_dst=gt_dst, lt_dst=lt_dst, range_dst=range_dst, port_num_end_dst=port_num_end_dst)
	return result

def deserialize_Ipv6_access_list_rules__l4_cfg__l4_dst_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_to_tcp = data.get('any-to-tcp')
	host_to_tcp = data.get('host-to-tcp')
	subnet_to_tcp = data.get('subnet-to-tcp')
	l4_dst_port_cfg = deserialize_Ipv6_access_list_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(data.get('l4-dst-port-cfg'))
	result = Ipv6_access_list_rules__l4_cfg__l4_dst_cfg(any_to_tcp=any_to_tcp, host_to_tcp=host_to_tcp, subnet_to_tcp=subnet_to_tcp, l4_dst_port_cfg=l4_dst_port_cfg)
	return result

def deserialize_Ipv6_access_list_rules__l4_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	l4_src_cfg = deserialize_Ipv6_access_list_rules__l4_cfg__l4_src_cfg_json(data.get('l4-src-cfg'))
	l4_dst_cfg = deserialize_Ipv6_access_list_rules__l4_cfg__l4_dst_cfg_json(data.get('l4-dst-cfg'))
	tcp_fragments = data.get('tcp-fragments')
	vlan = data.get('vlan')
	dscp = data.get('dscp')
	established = data.get('established')
	log = data.get('log')
	transparent_session_only = data.get('transparent-session-only')
	result = Ipv6_access_list_rules__l4_cfg(tcp=tcp, udp=udp, l4_src_cfg=l4_src_cfg, l4_dst_cfg=l4_dst_cfg, tcp_fragments=tcp_fragments, vlan=vlan, dscp=dscp, established=established, log=log, transparent_session_only=transparent_session_only)
	return result

def deserialize_Ipv6_access_list_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	seq_num = data.get('seq-num')
	action = data.get('action')
	remark = data.get('remark')
	icmp_cfg = deserialize_Ipv6_access_list_rules__icmp_cfg_json(data.get('icmp-cfg'))
	ipv6 = data.get('ipv6')
	src_ip_cfg = deserialize_Ipv6_access_list_rules__src_ip_cfg_json(data.get('src-ip-cfg'))
	dst_ip_cfg = deserialize_Ipv6_access_list_rules__dst_ip_cfg_json(data.get('dst-ip-cfg'))
	l4_cfg = deserialize_Ipv6_access_list_rules__l4_cfg_json(data.get('l4-cfg'))
	result = Ipv6_access_list_rules(seq_num=seq_num, action=action, remark=remark, icmp_cfg=icmp_cfg, ipv6=ipv6, src_ip_cfg=src_ip_cfg, dst_ip_cfg=dst_ip_cfg, l4_cfg=l4_cfg)
	return result

def deserialize_list_Ipv6_access_list_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ipv6_access_list_rules_json(item))
	return list(container)

def deserialize_Access_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	rules = deserialize_list_Ipv6_access_list_rules_json(data.get('rules'))
	result = Access_list(name=name, rules=rules)
	return result

def serialize_Ipv6_access_list_rules__icmp_cfg__icmp_src_cfg_json(obj):
	output = OrderedDict()
	if obj.any_from_icmp is not None:
		output['any-from-icmp'] = obj.any_from_icmp
	if obj.host_from_icmp is not None:
		output['host-from-icmp'] = obj.host_from_icmp
	if obj.subnet_from_icmp is not None:
		output['subnet-from-icmp'] = obj.subnet_from_icmp
	return output

def serialize_Ipv6_access_list_rules__icmp_cfg__code_json(obj):
	output = OrderedDict()
	if obj.any_code is not None:
		output['any-code'] = obj.any_code
	if obj.icmp_code is not None:
		output['icmp-code'] = obj.icmp_code
	return output

def serialize_Ipv6_access_list_rules__icmp_cfg__type__type_code_json(obj):
	output = OrderedDict()
	if obj.type_any_code is not None:
		output['type-any-code'] = obj.type_any_code
	if obj.type_icmp_code is not None:
		output['type-icmp-code'] = obj.type_icmp_code
	if obj.host_type_code is not None:
		output['host-type-code'] = obj.host_type_code
	if obj.subnet_type_code is not None:
		output['subnet-type-code'] = obj.subnet_type_code
	return output

def serialize_Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(obj):
	output = OrderedDict()
	if obj.dest_un_any_code is not None:
		output['dest-un-any-code'] = obj.dest_un_any_code
	if obj.dest_un_icmp_code is not None:
		output['dest-un-icmp-code'] = obj.dest_un_icmp_code
	if obj.addr_unreachable is not None:
		output['addr-unreachable'] = obj.addr_unreachable
	if obj.admin_prohibited is not None:
		output['admin-prohibited'] = obj.admin_prohibited
	if obj.no_route is not None:
		output['no-route'] = obj.no_route
	if obj.not_neighbour is not None:
		output['not-neighbour'] = obj.not_neighbour
	if obj.port_unreachable is not None:
		output['port-unreachable'] = obj.port_unreachable
	return output

def serialize_Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg_json(obj):
	output = OrderedDict()
	if obj.dest_unreachable is not None:
		output['dest-unreachable'] = obj.dest_unreachable
	if obj.dest_un_code is not None:
		output['dest-un-code'] = serialize_Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(obj.dest_un_code)
	if obj.dest_un_any_src is not None:
		output['dest-un-any-src'] = obj.dest_un_any_src
	if obj.dest_un_host_src is not None:
		output['dest-un-host-src'] = obj.dest_un_host_src
	if obj.dest_un_subnet_src is not None:
		output['dest-un-subnet-src'] = obj.dest_un_subnet_src
	return output

def serialize_Ipv6_access_list_rules__icmp_cfg__type_json(obj):
	output = OrderedDict()
	if obj.icmp_type is not None:
		output['icmp-type'] = obj.icmp_type
	if obj.any_type is not None:
		output['any-type'] = obj.any_type
	if obj.echo_reply is not None:
		output['echo-reply'] = obj.echo_reply
	if obj.echo_request is not None:
		output['echo-request'] = obj.echo_request
	if obj.packet_too_big is not None:
		output['packet-too-big'] = obj.packet_too_big
	if obj.param_prob is not None:
		output['param-prob'] = obj.param_prob
	if obj.time_exceeded is not None:
		output['time-exceeded'] = obj.time_exceeded
	if obj.type_code is not None:
		output['type-code'] = serialize_Ipv6_access_list_rules__icmp_cfg__type__type_code_json(obj.type_code)
	if obj.dest_unreach_cfg is not None:
		output['dest-unreach-cfg'] = serialize_Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg_json(obj.dest_unreach_cfg)
	return output

def serialize_Ipv6_access_list_rules__icmp_cfg_json(obj):
	output = OrderedDict()
	if obj.icmp is not None:
		output['icmp'] = obj.icmp
	if obj.icmp_src_cfg is not None:
		output['icmp-src-cfg'] = serialize_Ipv6_access_list_rules__icmp_cfg__icmp_src_cfg_json(obj.icmp_src_cfg)
	if obj.code is not None:
		output['code'] = serialize_Ipv6_access_list_rules__icmp_cfg__code_json(obj.code)
	if obj.type is not None:
		output['type'] = serialize_Ipv6_access_list_rules__icmp_cfg__type_json(obj.type)
	return output

def serialize_Ipv6_access_list_rules__src_ip_cfg_json(obj):
	output = OrderedDict()
	if obj.any_from_ip is not None:
		output['any-from-ip'] = obj.any_from_ip
	if obj.host_from_ip is not None:
		output['host-from-ip'] = obj.host_from_ip
	if obj.subnet_from_ip is not None:
		output['subnet-from-ip'] = obj.subnet_from_ip
	return output

def serialize_Ipv6_access_list_rules__dst_ip_cfg_json(obj):
	output = OrderedDict()
	if obj.any_to_ip is not None:
		output['any-to-ip'] = obj.any_to_ip
	if obj.host_to_ip is not None:
		output['host-to-ip'] = obj.host_to_ip
	if obj.subnet_to_ip is not None:
		output['subnet-to-ip'] = obj.subnet_to_ip
	if obj.fragments is not None:
		output['fragments'] = obj.fragments
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	if obj.dscp is not None:
		output['dscp'] = obj.dscp
	if obj.log is not None:
		output['log'] = obj.log
	if obj.transparent_session_only is not None:
		output['transparent-session-only'] = obj.transparent_session_only
	return output

def serialize_Ipv6_access_list_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(obj):
	output = OrderedDict()
	if obj.eq_src is not None:
		output['eq-src'] = obj.eq_src
	if obj.gt_src is not None:
		output['gt-src'] = obj.gt_src
	if obj.lt_src is not None:
		output['lt-src'] = obj.lt_src
	if obj.range_src is not None:
		output['range-src'] = obj.range_src
	if obj.port_num_end_src is not None:
		output['port-num-end-src'] = obj.port_num_end_src
	return output

def serialize_Ipv6_access_list_rules__l4_cfg__l4_src_cfg_json(obj):
	output = OrderedDict()
	if obj.any_from_tcp is not None:
		output['any-from-tcp'] = obj.any_from_tcp
	if obj.host_from_tcp is not None:
		output['host-from-tcp'] = obj.host_from_tcp
	if obj.subnet_from_tcp is not None:
		output['subnet-from-tcp'] = obj.subnet_from_tcp
	if obj.l4_src_port_cfg is not None:
		output['l4-src-port-cfg'] = serialize_Ipv6_access_list_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(obj.l4_src_port_cfg)
	return output

def serialize_Ipv6_access_list_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(obj):
	output = OrderedDict()
	if obj.eq_dst is not None:
		output['eq-dst'] = obj.eq_dst
	if obj.gt_dst is not None:
		output['gt-dst'] = obj.gt_dst
	if obj.lt_dst is not None:
		output['lt-dst'] = obj.lt_dst
	if obj.range_dst is not None:
		output['range-dst'] = obj.range_dst
	if obj.port_num_end_dst is not None:
		output['port-num-end-dst'] = obj.port_num_end_dst
	return output

def serialize_Ipv6_access_list_rules__l4_cfg__l4_dst_cfg_json(obj):
	output = OrderedDict()
	if obj.any_to_tcp is not None:
		output['any-to-tcp'] = obj.any_to_tcp
	if obj.host_to_tcp is not None:
		output['host-to-tcp'] = obj.host_to_tcp
	if obj.subnet_to_tcp is not None:
		output['subnet-to-tcp'] = obj.subnet_to_tcp
	if obj.l4_dst_port_cfg is not None:
		output['l4-dst-port-cfg'] = serialize_Ipv6_access_list_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(obj.l4_dst_port_cfg)
	return output

def serialize_Ipv6_access_list_rules__l4_cfg_json(obj):
	output = OrderedDict()
	if obj.tcp is not None:
		output['tcp'] = obj.tcp
	if obj.udp is not None:
		output['udp'] = obj.udp
	if obj.l4_src_cfg is not None:
		output['l4-src-cfg'] = serialize_Ipv6_access_list_rules__l4_cfg__l4_src_cfg_json(obj.l4_src_cfg)
	if obj.l4_dst_cfg is not None:
		output['l4-dst-cfg'] = serialize_Ipv6_access_list_rules__l4_cfg__l4_dst_cfg_json(obj.l4_dst_cfg)
	if obj.tcp_fragments is not None:
		output['tcp-fragments'] = obj.tcp_fragments
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	if obj.dscp is not None:
		output['dscp'] = obj.dscp
	if obj.established is not None:
		output['established'] = obj.established
	if obj.log is not None:
		output['log'] = obj.log
	if obj.transparent_session_only is not None:
		output['transparent-session-only'] = obj.transparent_session_only
	return output

def serialize_Ipv6_access_list_rules_json(obj):
	output = OrderedDict()
	if obj.seq_num is not None:
		output['seq-num'] = obj.seq_num
	if obj.action is not None:
		output['action'] = obj.action
	if obj.remark is not None:
		output['remark'] = obj.remark
	if obj.icmp_cfg is not None:
		output['icmp-cfg'] = serialize_Ipv6_access_list_rules__icmp_cfg_json(obj.icmp_cfg)
	if obj.ipv6 is not None:
		output['ipv6'] = obj.ipv6
	if obj.src_ip_cfg is not None:
		output['src-ip-cfg'] = serialize_Ipv6_access_list_rules__src_ip_cfg_json(obj.src_ip_cfg)
	if obj.dst_ip_cfg is not None:
		output['dst-ip-cfg'] = serialize_Ipv6_access_list_rules__dst_ip_cfg_json(obj.dst_ip_cfg)
	if obj.l4_cfg is not None:
		output['l4-cfg'] = serialize_Ipv6_access_list_rules__l4_cfg_json(obj.l4_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ipv6_access_list_rules_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ipv6_access_list_rules_json(item))
	return output

def serialize_Access_list_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.rules is not None:
		output['rules'] = serialize_list_Ipv6_access_list_rules_json(obj.rules)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Access_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Access_list_json(item))
	return list(container)

class Access_list(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 16)
	def __init__(self, name, rules=None):
		self.name = name
		self.rules = rules

	def __str__(self):
		return str(self.name)

class Access_list_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 16)
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class Ipv6_access_list_rules__icmp_cfg__icmp_src_cfg(AxapiObject):
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

class Ipv6_access_list_rules__icmp_cfg__code(AxapiObject):
	__metaclass__ = StructMeta 
	any_code=PosRangedInteger(0, 1)
	icmp_code=PosRangedInteger(0, 254)
	def __init__(self, any_code=None, icmp_code=None):
		self.any_code = any_code
		self.icmp_code = icmp_code

	def __str__(self):
		return ""

class Ipv6_access_list_rules__icmp_cfg__type__type_code(AxapiObject):
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

class Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code(AxapiObject):
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

class Ipv6_access_list_rules__icmp_cfg__type__dest_unreach_cfg(AxapiObject):
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

class Ipv6_access_list_rules__icmp_cfg__type(AxapiObject):
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

class Ipv6_access_list_rules__icmp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	icmp=PosRangedInteger(0, 1)
	def __init__(self, icmp=None, icmp_src_cfg=None, code=None, type=None):
		self.icmp = icmp
		self.icmp_src_cfg = icmp_src_cfg
		self.code = code
		self.type = type

	def __str__(self):
		return ""

class Ipv6_access_list_rules__src_ip_cfg(AxapiObject):
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

class Ipv6_access_list_rules__dst_ip_cfg(AxapiObject):
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

class Ipv6_access_list_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg(AxapiObject):
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

class Ipv6_access_list_rules__l4_cfg__l4_src_cfg(AxapiObject):
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

class Ipv6_access_list_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg(AxapiObject):
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

class Ipv6_access_list_rules__l4_cfg__l4_dst_cfg(AxapiObject):
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

class Ipv6_access_list_rules__l4_cfg(AxapiObject):
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

class Ipv6_access_list_rules(AxapiObject):
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

class Ipv6AccesslistClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpv6Accesslist(self, access_list_name):
		"""
		Retrieve the access_list identified by the specified identifier
		
		Args:
			access_list_name Access_list_name
		
		Returns:
			An instance of the Access_list class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(access_list_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified access_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('access-list')
		return deserialize_Access_list_json(payload)

	def putIpv6Accesslist(self, access_list_name, access_list):
		"""
		Replace the object access_list
		
		Args:
			access_list_name Access_list_name
			access_list An instance of the Access_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['access-list']=serialize_Access_list_json(access_list)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(access_list_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpv6Accesslist(self, access_list_name):
		"""
		Remove the access_list identified by the specified identifier from the system
		
		Args:
			access_list_name Access_list_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(access_list_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified access_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpv6AccesslistsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpv6Accesslist(self, access_list):
		"""
		Create the object access_list
		
		Args:
			access_list An instance of the Access_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['access-list']=serialize_Access_list_json(access_list)
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

	def getAllIpv6Accesslists(self):
		"""
		Retrieve all access_list objects currently pending in the system
		
		Returns:
			A list of Access_list objects
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
			payload= data.get('access-listList')
		return deserialize_list_Access_list_json(payload)

