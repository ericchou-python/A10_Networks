########################################################################################################################
# File name: access_list.py
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
	'https://axapi.a10networks.com/axapi/v3/access-list',
]

def deserialize_Access_list_rules__std_action_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	action = data.get('action')
	any = data.get('any')
	host = data.get('host')
	subnet = data.get('subnet')
	rev_subnet_mask = data.get('rev-subnet-mask')
	log = data.get('log')
	result = Access_list_rules__std_action_cfg(action=action, any=any, host=host, subnet=subnet, rev_subnet_mask=rev_subnet_mask, log=log)
	return result

def deserialize_Access_list_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	seq_num = data.get('seq-num')
	remark_std = data.get('remark-std')
	std_action_cfg = deserialize_Access_list_rules__std_action_cfg_json(data.get('std-action-cfg'))
	result = Access_list_rules(seq_num=seq_num, remark_std=remark_std, std_action_cfg=std_action_cfg)
	return result

def deserialize_list_Access_list_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Access_list_rules_json(item))
	return list(container)

def deserialize_Access_list__std_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	std = data.get('std')
	rules = deserialize_list_Access_list_rules_json(data.get('rules'))
	result = Access_list__std_cfg(std=std, rules=rules)
	return result

def deserialize_Access_list_ext_rules__icmp_cfg__icmp_src_cfg_json(obj):
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
	result = Access_list_ext_rules__icmp_cfg__icmp_src_cfg(any_src_icmp=any_src_icmp, host_src_icmp=host_src_icmp, subnet_src_icmp=subnet_src_icmp, mask_src_icmp=mask_src_icmp)
	return result

def deserialize_Access_list_ext_rules__icmp_cfg__code_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	any_code = data.get('any-code')
	icmp_code = data.get('icmp-code')
	result = Access_list_ext_rules__icmp_cfg__code(any_code=any_code, icmp_code=icmp_code)
	return result

def deserialize_Access_list_ext_rules__icmp_cfg__type__type_code_json(obj):
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
	result = Access_list_ext_rules__icmp_cfg__type__type_code(type_any_code=type_any_code, type_icmp_code=type_icmp_code, type_any_src=type_any_src, type_host_src=type_host_src, type_subnet_src=type_subnet_src, type_mask_src=type_mask_src)
	return result

def deserialize_Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(obj):
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
	result = Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code(dest_un_any_code=dest_un_any_code, dest_un_icmp_code=dest_un_icmp_code, frag_required=frag_required, host_unreachable=host_unreachable, network_unreachable=network_unreachable, port_unreachable=port_unreachable, proto_unreachable=proto_unreachable, route_failed=route_failed)
	return result

def deserialize_Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dest_unreachable = data.get('dest-unreachable')
	dest_un_code = deserialize_Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(data.get('dest-un-code'))
	dest_un_any_src = data.get('dest-un-any-src')
	dest_un_host_src = data.get('dest-un-host-src')
	dest_un_subnet_src = data.get('dest-un-subnet-src')
	dest_un_mask_src = data.get('dest-un-mask-src')
	result = Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg(dest_unreachable=dest_unreachable, dest_un_code=dest_un_code, dest_un_any_src=dest_un_any_src, dest_un_host_src=dest_un_host_src, dest_un_subnet_src=dest_un_subnet_src, dest_un_mask_src=dest_un_mask_src)
	return result

def deserialize_Access_list_ext_rules__icmp_cfg__type_json(obj):
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
	type_code = deserialize_Access_list_ext_rules__icmp_cfg__type__type_code_json(data.get('type-code'))
	dest_unreach_cfg = deserialize_Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg_json(data.get('dest-unreach-cfg'))
	result = Access_list_ext_rules__icmp_cfg__type(icmp_type=icmp_type, any_type=any_type, echo_reply=echo_reply, echo_request=echo_request, info_reply=info_reply, info_request=info_request, mask_reply=mask_reply, mask_request=mask_request, parameter_problem=parameter_problem, redirect=redirect, source_quench=source_quench, time_exceeded=time_exceeded, timestamp=timestamp, timestamp_reply=timestamp_reply, type_code=type_code, dest_unreach_cfg=dest_unreach_cfg)
	return result

def deserialize_Access_list_ext_rules__icmp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp = data.get('icmp')
	icmp_src_cfg = deserialize_Access_list_ext_rules__icmp_cfg__icmp_src_cfg_json(data.get('icmp-src-cfg'))
	code = deserialize_Access_list_ext_rules__icmp_cfg__code_json(data.get('code'))
	type = deserialize_Access_list_ext_rules__icmp_cfg__type_json(data.get('type'))
	result = Access_list_ext_rules__icmp_cfg(icmp=icmp, icmp_src_cfg=icmp_src_cfg, code=code, type=type)
	return result

def deserialize_Access_list_ext_rules__ip_cfg_json(obj):
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
	result = Access_list_ext_rules__ip_cfg(ip=ip, any_src_ip=any_src_ip, host_src_ip=host_src_ip, subnet_src_ip=subnet_src_ip, mask_src_ip=mask_src_ip)
	return result

def deserialize_Access_list_ext_rules__any_code_any_source_cfg_json(obj):
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
	result = Access_list_ext_rules__any_code_any_source_cfg(any_code_any_src=any_code_any_src, any_code_host_src=any_code_host_src, any_code_subnet_src=any_code_subnet_src, any_code_mask_src=any_code_mask_src)
	return result

def deserialize_Access_list_ext_rules__dst_ip_cfg_json(obj):
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
	result = Access_list_ext_rules__dst_ip_cfg(any_dst_ip=any_dst_ip, host_dst_ip=host_dst_ip, subnet_dst_ip=subnet_dst_ip, mask_dst_ip=mask_dst_ip, fragments=fragments, vlan=vlan, dscp=dscp, log=log)
	return result

def deserialize_Access_list_ext_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(obj):
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
	result = Access_list_ext_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg(eq_src=eq_src, gt_src=gt_src, lt_src=lt_src, range_src=range_src, port_num_end_src=port_num_end_src)
	return result

def deserialize_Access_list_ext_rules__l4_cfg__l4_src_cfg_json(obj):
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
	l4_src_port_cfg = deserialize_Access_list_ext_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(data.get('l4-src-port-cfg'))
	result = Access_list_ext_rules__l4_cfg__l4_src_cfg(any_src_tcp=any_src_tcp, host_src_tcp=host_src_tcp, subnet_src_tcp=subnet_src_tcp, mask_src_tcp=mask_src_tcp, l4_src_port_cfg=l4_src_port_cfg)
	return result

def deserialize_Access_list_ext_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(obj):
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
	result = Access_list_ext_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg(eq_dst=eq_dst, gt_dst=gt_dst, lt_dst=lt_dst, range_dst=range_dst, port_num_end_dst=port_num_end_dst)
	return result

def deserialize_Access_list_ext_rules__l4_cfg__l4_dst_cfg_json(obj):
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
	l4_dst_port_cfg = deserialize_Access_list_ext_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(data.get('l4-dst-port-cfg'))
	result = Access_list_ext_rules__l4_cfg__l4_dst_cfg(any_dst_tcp=any_dst_tcp, host_dst_tcp=host_dst_tcp, subnet_dst_tcp=subnet_dst_tcp, mask_dst_tcp=mask_dst_tcp, l4_dst_port_cfg=l4_dst_port_cfg)
	return result

def deserialize_Access_list_ext_rules__l4_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	l4_src_cfg = deserialize_Access_list_ext_rules__l4_cfg__l4_src_cfg_json(data.get('l4-src-cfg'))
	l4_dst_cfg = deserialize_Access_list_ext_rules__l4_cfg__l4_dst_cfg_json(data.get('l4-dst-cfg'))
	tcp_fragments = data.get('tcp-fragments')
	vlan = data.get('vlan')
	dscp = data.get('dscp')
	established = data.get('established')
	log = data.get('log')
	result = Access_list_ext_rules__l4_cfg(tcp=tcp, udp=udp, l4_src_cfg=l4_src_cfg, l4_dst_cfg=l4_dst_cfg, tcp_fragments=tcp_fragments, vlan=vlan, dscp=dscp, established=established, log=log)
	return result

def deserialize_Access_list_ext_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	seq_num = data.get('seq-num')
	remark_extd = data.get('remark-extd')
	action_extd = data.get('action-extd')
	icmp_cfg = deserialize_Access_list_ext_rules__icmp_cfg_json(data.get('icmp-cfg'))
	ip_cfg = deserialize_Access_list_ext_rules__ip_cfg_json(data.get('ip-cfg'))
	any_code_any_source_cfg = deserialize_Access_list_ext_rules__any_code_any_source_cfg_json(data.get('any-code-any-source-cfg'))
	dst_ip_cfg = deserialize_Access_list_ext_rules__dst_ip_cfg_json(data.get('dst-ip-cfg'))
	l4_cfg = deserialize_Access_list_ext_rules__l4_cfg_json(data.get('l4-cfg'))
	result = Access_list_ext_rules(seq_num=seq_num, remark_extd=remark_extd, action_extd=action_extd, icmp_cfg=icmp_cfg, ip_cfg=ip_cfg, any_code_any_source_cfg=any_code_any_source_cfg, dst_ip_cfg=dst_ip_cfg, l4_cfg=l4_cfg)
	return result

def deserialize_list_Access_list_ext_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Access_list_ext_rules_json(item))
	return list(container)

def deserialize_Access_list__extd_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	extd = data.get('extd')
	ext_rules = deserialize_list_Access_list_ext_rules_json(data.get('ext-rules'))
	result = Access_list__extd_cfg(extd=extd, ext_rules=ext_rules)
	return result

def deserialize_Access_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	std_cfg = deserialize_Access_list__std_cfg_json(data.get('std-cfg'))
	extd_cfg = deserialize_Access_list__extd_cfg_json(data.get('extd-cfg'))
	result = Access_list(std_cfg=std_cfg, extd_cfg=extd_cfg)
	return result

def serialize_Access_list_rules__std_action_cfg_json(obj):
	output = OrderedDict()
	if obj.action is not None:
		output['action'] = obj.action
	if obj.any is not None:
		output['any'] = obj.any
	if obj.host is not None:
		output['host'] = obj.host
	if obj.subnet is not None:
		output['subnet'] = obj.subnet
	if obj.rev_subnet_mask is not None:
		output['rev-subnet-mask'] = obj.rev_subnet_mask
	if obj.log is not None:
		output['log'] = obj.log
	return output

def serialize_Access_list_rules_json(obj):
	output = OrderedDict()
	if obj.seq_num is not None:
		output['seq-num'] = obj.seq_num
	if obj.remark_std is not None:
		output['remark-std'] = obj.remark_std
	if obj.std_action_cfg is not None:
		output['std-action-cfg'] = serialize_Access_list_rules__std_action_cfg_json(obj.std_action_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Access_list_rules_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Access_list_rules_json(item))
	return output

def serialize_Access_list__std_cfg_json(obj):
	output = OrderedDict()
	output['std'] = obj.std
	if obj.rules is not None:
		output['rules'] = serialize_list_Access_list_rules_json(obj.rules)
	return output

def serialize_Access_list_ext_rules__icmp_cfg__icmp_src_cfg_json(obj):
	output = OrderedDict()
	if obj.any_src_icmp is not None:
		output['any-src-icmp'] = obj.any_src_icmp
	if obj.host_src_icmp is not None:
		output['host-src-icmp'] = obj.host_src_icmp
	if obj.subnet_src_icmp is not None:
		output['subnet-src-icmp'] = obj.subnet_src_icmp
	if obj.mask_src_icmp is not None:
		output['mask-src-icmp'] = obj.mask_src_icmp
	return output

def serialize_Access_list_ext_rules__icmp_cfg__code_json(obj):
	output = OrderedDict()
	if obj.any_code is not None:
		output['any-code'] = obj.any_code
	if obj.icmp_code is not None:
		output['icmp-code'] = obj.icmp_code
	return output

def serialize_Access_list_ext_rules__icmp_cfg__type__type_code_json(obj):
	output = OrderedDict()
	if obj.type_any_code is not None:
		output['type-any-code'] = obj.type_any_code
	if obj.type_icmp_code is not None:
		output['type-icmp-code'] = obj.type_icmp_code
	if obj.type_any_src is not None:
		output['type-any-src'] = obj.type_any_src
	if obj.type_host_src is not None:
		output['type-host-src'] = obj.type_host_src
	if obj.type_subnet_src is not None:
		output['type-subnet-src'] = obj.type_subnet_src
	if obj.type_mask_src is not None:
		output['type-mask-src'] = obj.type_mask_src
	return output

def serialize_Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(obj):
	output = OrderedDict()
	if obj.dest_un_any_code is not None:
		output['dest-un-any-code'] = obj.dest_un_any_code
	if obj.dest_un_icmp_code is not None:
		output['dest-un-icmp-code'] = obj.dest_un_icmp_code
	if obj.frag_required is not None:
		output['frag-required'] = obj.frag_required
	if obj.host_unreachable is not None:
		output['host-unreachable'] = obj.host_unreachable
	if obj.network_unreachable is not None:
		output['network-unreachable'] = obj.network_unreachable
	if obj.port_unreachable is not None:
		output['port-unreachable'] = obj.port_unreachable
	if obj.proto_unreachable is not None:
		output['proto-unreachable'] = obj.proto_unreachable
	if obj.route_failed is not None:
		output['route-failed'] = obj.route_failed
	return output

def serialize_Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg_json(obj):
	output = OrderedDict()
	if obj.dest_unreachable is not None:
		output['dest-unreachable'] = obj.dest_unreachable
	if obj.dest_un_code is not None:
		output['dest-un-code'] = serialize_Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code_json(obj.dest_un_code)
	if obj.dest_un_any_src is not None:
		output['dest-un-any-src'] = obj.dest_un_any_src
	if obj.dest_un_host_src is not None:
		output['dest-un-host-src'] = obj.dest_un_host_src
	if obj.dest_un_subnet_src is not None:
		output['dest-un-subnet-src'] = obj.dest_un_subnet_src
	if obj.dest_un_mask_src is not None:
		output['dest-un-mask-src'] = obj.dest_un_mask_src
	return output

def serialize_Access_list_ext_rules__icmp_cfg__type_json(obj):
	output = OrderedDict()
	if obj.icmp_type is not None:
		output['icmp-type'] = obj.icmp_type
	if obj.any_type is not None:
		output['any-type'] = obj.any_type
	if obj.echo_reply is not None:
		output['echo-reply'] = obj.echo_reply
	if obj.echo_request is not None:
		output['echo-request'] = obj.echo_request
	if obj.info_reply is not None:
		output['info-reply'] = obj.info_reply
	if obj.info_request is not None:
		output['info-request'] = obj.info_request
	if obj.mask_reply is not None:
		output['mask-reply'] = obj.mask_reply
	if obj.mask_request is not None:
		output['mask-request'] = obj.mask_request
	if obj.parameter_problem is not None:
		output['parameter-problem'] = obj.parameter_problem
	if obj.redirect is not None:
		output['redirect'] = obj.redirect
	if obj.source_quench is not None:
		output['source-quench'] = obj.source_quench
	if obj.time_exceeded is not None:
		output['time-exceeded'] = obj.time_exceeded
	if obj.timestamp is not None:
		output['timestamp'] = obj.timestamp
	if obj.timestamp_reply is not None:
		output['timestamp-reply'] = obj.timestamp_reply
	if obj.type_code is not None:
		output['type-code'] = serialize_Access_list_ext_rules__icmp_cfg__type__type_code_json(obj.type_code)
	if obj.dest_unreach_cfg is not None:
		output['dest-unreach-cfg'] = serialize_Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg_json(obj.dest_unreach_cfg)
	return output

def serialize_Access_list_ext_rules__icmp_cfg_json(obj):
	output = OrderedDict()
	if obj.icmp is not None:
		output['icmp'] = obj.icmp
	if obj.icmp_src_cfg is not None:
		output['icmp-src-cfg'] = serialize_Access_list_ext_rules__icmp_cfg__icmp_src_cfg_json(obj.icmp_src_cfg)
	if obj.code is not None:
		output['code'] = serialize_Access_list_ext_rules__icmp_cfg__code_json(obj.code)
	if obj.type is not None:
		output['type'] = serialize_Access_list_ext_rules__icmp_cfg__type_json(obj.type)
	return output

def serialize_Access_list_ext_rules__ip_cfg_json(obj):
	output = OrderedDict()
	if obj.ip is not None:
		output['ip'] = obj.ip
	if obj.any_src_ip is not None:
		output['any-src-ip'] = obj.any_src_ip
	if obj.host_src_ip is not None:
		output['host-src-ip'] = obj.host_src_ip
	if obj.subnet_src_ip is not None:
		output['subnet-src-ip'] = obj.subnet_src_ip
	if obj.mask_src_ip is not None:
		output['mask-src-ip'] = obj.mask_src_ip
	return output

def serialize_Access_list_ext_rules__any_code_any_source_cfg_json(obj):
	output = OrderedDict()
	if obj.any_code_any_src is not None:
		output['any-code-any-src'] = obj.any_code_any_src
	if obj.any_code_host_src is not None:
		output['any-code-host-src'] = obj.any_code_host_src
	if obj.any_code_subnet_src is not None:
		output['any-code-subnet-src'] = obj.any_code_subnet_src
	if obj.any_code_mask_src is not None:
		output['any-code-mask-src'] = obj.any_code_mask_src
	return output

def serialize_Access_list_ext_rules__dst_ip_cfg_json(obj):
	output = OrderedDict()
	if obj.any_dst_ip is not None:
		output['any-dst-ip'] = obj.any_dst_ip
	if obj.host_dst_ip is not None:
		output['host-dst-ip'] = obj.host_dst_ip
	if obj.subnet_dst_ip is not None:
		output['subnet-dst-ip'] = obj.subnet_dst_ip
	if obj.mask_dst_ip is not None:
		output['mask-dst-ip'] = obj.mask_dst_ip
	if obj.fragments is not None:
		output['fragments'] = obj.fragments
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	if obj.dscp is not None:
		output['dscp'] = obj.dscp
	if obj.log is not None:
		output['log'] = obj.log
	return output

def serialize_Access_list_ext_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(obj):
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

def serialize_Access_list_ext_rules__l4_cfg__l4_src_cfg_json(obj):
	output = OrderedDict()
	if obj.any_src_tcp is not None:
		output['any-src-tcp'] = obj.any_src_tcp
	if obj.host_src_tcp is not None:
		output['host-src-tcp'] = obj.host_src_tcp
	if obj.subnet_src_tcp is not None:
		output['subnet-src-tcp'] = obj.subnet_src_tcp
	if obj.mask_src_tcp is not None:
		output['mask-src-tcp'] = obj.mask_src_tcp
	if obj.l4_src_port_cfg is not None:
		output['l4-src-port-cfg'] = serialize_Access_list_ext_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg_json(obj.l4_src_port_cfg)
	return output

def serialize_Access_list_ext_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(obj):
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

def serialize_Access_list_ext_rules__l4_cfg__l4_dst_cfg_json(obj):
	output = OrderedDict()
	if obj.any_dst_tcp is not None:
		output['any-dst-tcp'] = obj.any_dst_tcp
	if obj.host_dst_tcp is not None:
		output['host-dst-tcp'] = obj.host_dst_tcp
	if obj.subnet_dst_tcp is not None:
		output['subnet-dst-tcp'] = obj.subnet_dst_tcp
	if obj.mask_dst_tcp is not None:
		output['mask-dst-tcp'] = obj.mask_dst_tcp
	if obj.l4_dst_port_cfg is not None:
		output['l4-dst-port-cfg'] = serialize_Access_list_ext_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg_json(obj.l4_dst_port_cfg)
	return output

def serialize_Access_list_ext_rules__l4_cfg_json(obj):
	output = OrderedDict()
	if obj.tcp is not None:
		output['tcp'] = obj.tcp
	if obj.udp is not None:
		output['udp'] = obj.udp
	if obj.l4_src_cfg is not None:
		output['l4-src-cfg'] = serialize_Access_list_ext_rules__l4_cfg__l4_src_cfg_json(obj.l4_src_cfg)
	if obj.l4_dst_cfg is not None:
		output['l4-dst-cfg'] = serialize_Access_list_ext_rules__l4_cfg__l4_dst_cfg_json(obj.l4_dst_cfg)
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
	return output

def serialize_Access_list_ext_rules_json(obj):
	output = OrderedDict()
	if obj.seq_num is not None:
		output['seq-num'] = obj.seq_num
	if obj.remark_extd is not None:
		output['remark-extd'] = obj.remark_extd
	if obj.action_extd is not None:
		output['action-extd'] = obj.action_extd
	if obj.icmp_cfg is not None:
		output['icmp-cfg'] = serialize_Access_list_ext_rules__icmp_cfg_json(obj.icmp_cfg)
	if obj.ip_cfg is not None:
		output['ip-cfg'] = serialize_Access_list_ext_rules__ip_cfg_json(obj.ip_cfg)
	if obj.any_code_any_source_cfg is not None:
		output['any-code-any-source-cfg'] = serialize_Access_list_ext_rules__any_code_any_source_cfg_json(obj.any_code_any_source_cfg)
	if obj.dst_ip_cfg is not None:
		output['dst-ip-cfg'] = serialize_Access_list_ext_rules__dst_ip_cfg_json(obj.dst_ip_cfg)
	if obj.l4_cfg is not None:
		output['l4-cfg'] = serialize_Access_list_ext_rules__l4_cfg_json(obj.l4_cfg)
	return output

def serialize_list_Access_list_ext_rules_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Access_list_ext_rules_json(item))
	return output

def serialize_Access_list__extd_cfg_json(obj):
	output = OrderedDict()
	output['extd'] = obj.extd
	if obj.ext_rules is not None:
		output['ext-rules'] = serialize_list_Access_list_ext_rules_json(obj.ext_rules)
	return output

def serialize_Access_list_json(obj):
	output = OrderedDict()
	output['std-cfg'] = serialize_Access_list__std_cfg_json(obj.std_cfg)
	if obj.extd_cfg is not None:
		output['extd-cfg'] = serialize_Access_list__extd_cfg_json(obj.extd_cfg)
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

class Access_list__std_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	std=PosRangedInteger(1, 99)
	def __init__(self, std, rules=None):
		self.std = std
		self.rules = rules

	def __str__(self):
		return str(self.std)

class Access_list__extd_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	extd=PosRangedInteger(100, 199)
	def __init__(self, extd, ext_rules=None):
		self.extd = extd
		self.ext_rules = ext_rules

	def __str__(self):
		return str(self.extd)

class Access_list(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, std_cfg, extd_cfg=None):
		self.std_cfg = std_cfg
		self.extd_cfg = extd_cfg

	def __str__(self):
		return str(self.std_cfg)

class Access_list_rules__std_action_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	action = Enum(['deny', 'permit', 'l3-vlan-fwd-disable'])
	any=PosRangedInteger(0, 1)
	host = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	rev_subnet_mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	log=PosRangedInteger(0, 1)
	def __init__(self, action=None, any=None, host=None, subnet=None, rev_subnet_mask=None, log=None):
		self.action = action
		self.any = any
		self.host = host
		self.subnet = subnet
		self.rev_subnet_mask = rev_subnet_mask
		self.log = log

	def __str__(self):
		return ""

class Access_list_rules(AxapiObject):
	__metaclass__ = StructMeta 
	seq_num=PosRangedInteger(1, 8192)
	remark_std=SizedString(1, 63)
	def __init__(self, seq_num=None, remark_std=None, std_action_cfg=None):
		self.seq_num = seq_num
		self.remark_std = remark_std
		self.std_action_cfg = std_action_cfg

	def __str__(self):
		return ""

class Access_list_std_cfg__std_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	std=PosRangedInteger(1, 99)
	def __init__(self, std, rules=None):
		self.std = std
		self.rules = rules

	def __str__(self):
		return str(self.std)

class Access_list_std_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, std_cfg):
		self.std_cfg = std_cfg

	def __str__(self):
		return str(self.std_cfg)

class Access_list_ext_rules__icmp_cfg__icmp_src_cfg(AxapiObject):
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

class Access_list_ext_rules__icmp_cfg__code(AxapiObject):
	__metaclass__ = StructMeta 
	any_code=PosRangedInteger(0, 1)
	icmp_code=PosRangedInteger(0, 254)
	def __init__(self, any_code=None, icmp_code=None):
		self.any_code = any_code
		self.icmp_code = icmp_code

	def __str__(self):
		return ""

class Access_list_ext_rules__icmp_cfg__type__type_code(AxapiObject):
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

class Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg__dest_un_code(AxapiObject):
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

class Access_list_ext_rules__icmp_cfg__type__dest_unreach_cfg(AxapiObject):
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

class Access_list_ext_rules__icmp_cfg__type(AxapiObject):
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

class Access_list_ext_rules__icmp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	icmp=PosRangedInteger(0, 1)
	def __init__(self, icmp=None, icmp_src_cfg=None, code=None, type=None):
		self.icmp = icmp
		self.icmp_src_cfg = icmp_src_cfg
		self.code = code
		self.type = type

	def __str__(self):
		return ""

class Access_list_ext_rules__ip_cfg(AxapiObject):
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

class Access_list_ext_rules__any_code_any_source_cfg(AxapiObject):
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

class Access_list_ext_rules__dst_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	any_dst_ip=PosRangedInteger(0, 1)
	host_dst_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_dst_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	mask_dst_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	fragments=PosRangedInteger(0, 1)
	vlan=PosRangedInteger(1, 4094)
	dscp=PosRangedInteger(1, 63)
	log=PosInteger()
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

class Access_list_ext_rules__l4_cfg__l4_src_cfg__l4_src_port_cfg(AxapiObject):
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

class Access_list_ext_rules__l4_cfg__l4_src_cfg(AxapiObject):
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

class Access_list_ext_rules__l4_cfg__l4_dst_cfg__l4_dst_port_cfg(AxapiObject):
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

class Access_list_ext_rules__l4_cfg__l4_dst_cfg(AxapiObject):
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

class Access_list_ext_rules__l4_cfg(AxapiObject):
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

class Access_list_ext_rules(AxapiObject):
	__metaclass__ = StructMeta 
	seq_num=PosRangedInteger(1, 8192)
	remark_extd=SizedString(1, 63)
	action_extd = Enum(['deny', 'permit', 'l3-vlan-fwd-disable'])
	def __init__(self, seq_num=None, remark_extd=None, action_extd=None, icmp_cfg=None, ip_cfg=None, any_code_any_source_cfg=None, dst_ip_cfg=None, l4_cfg=None):
		self.seq_num = seq_num
		self.remark_extd = remark_extd
		self.action_extd = action_extd
		self.icmp_cfg = icmp_cfg
		self.ip_cfg = ip_cfg
		self.any_code_any_source_cfg = any_code_any_source_cfg
		self.dst_ip_cfg = dst_ip_cfg
		self.l4_cfg = l4_cfg

	def __str__(self):
		return ""

class AccesslistClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getAccesslist(self, access_list_std_cfg):
		"""
		Retrieve the access_list identified by the specified identifier
		
		Args:
			access_list_std_cfg Access_list_std_cfg
		
		Returns:
			An instance of the Access_list class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(access_list_std_cfg) .replace("/", "%2f") + query, headers=headers)
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

	def putAccesslist(self, access_list_std_cfg, access_list):
		"""
		Replace the object access_list
		
		Args:
			access_list_std_cfg Access_list_std_cfg
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
		conn.request('PUT', self.get_path() + '/' + str(access_list_std_cfg) .replace("/", "%2f") + query, payload, headers)
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

	def deleteAccesslist(self, access_list_std_cfg):
		"""
		Remove the access_list identified by the specified identifier from the system
		
		Args:
			access_list_std_cfg Access_list_std_cfg
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(access_list_std_cfg) .replace("/", "%2f") + query, headers=headers)
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

class AllAccesslistsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitAccesslist(self, access_list):
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

	def getAllAccesslists(self):
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

