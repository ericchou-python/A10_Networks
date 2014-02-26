########################################################################################################################
# File name: object_group_service.py
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
	'https://axapi.a10networks.com/axapi/v3/object-group/service',
]

def deserialize_Service_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	svc_name = data.get('svc-name')
	icmp = data.get('icmp')
	icmpv6 = data.get('icmpv6')
	tcp_udp = data.get('tcp_udp')
	source = data.get('source')
	eq_src = data.get('eq-src')
	gt_src = data.get('gt-src')
	lt_src = data.get('lt-src')
	range_src = data.get('range-src')
	port_num_end_src = data.get('port-num-end-src')
	eq_dst = data.get('eq-dst')
	gt_dst = data.get('gt-dst')
	lt_dst = data.get('lt-dst')
	range_dst = data.get('range-dst')
	port_num_end_dst = data.get('port-num-end-dst')
	code = data.get('code')
	any_code = data.get('any-code')
	icmp_code = data.get('icmp-code')
	type = data.get('type')
	icmp_type = data.get('icmp-type')
	any_type = data.get('any-type')
	dest_unreachable = data.get('dest-unreachable')
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
	type_code = data.get('type-code')
	type_any_code = data.get('type-any-code')
	type_icmp_code = data.get('type-icmp-code')
	dest_un_code = data.get('dest-un-code')
	dest_un_any_code = data.get('dest-un-any-code')
	dest_un_icmp_code = data.get('dest-un-icmp-code')
	frag_required = data.get('frag-required')
	host_unreachable = data.get('host-unreachable')
	network_unreachable = data.get('network-unreachable')
	port_unreachable = data.get('port-unreachable')
	proto_unreachable = data.get('proto-unreachable')
	route_failed = data.get('route-failed')
	v6_code = data.get('v6-code')
	v6_any_code = data.get('v6-any-code')
	v6_icmp_code = data.get('v6-icmp-code')
	v6_type = data.get('v6-type')
	icmpv6_type = data.get('icmpv6-type')
	v6_any_type = data.get('v6-any-type')
	packet_too_big = data.get('packet-too-big')
	param_prob = data.get('param-prob')
	v6_type_code = data.get('v6-type-code')
	v6_type_any_code = data.get('v6-type-any-code')
	v6_type_icmp_code = data.get('v6-type-icmp-code')
	v6_dest_un_code = data.get('v6-dest-un-code')
	v6_dest_un_any_code = data.get('v6-dest-un-any-code')
	v6_dest_un_icmp_code = data.get('v6-dest-un-icmp-code')
	addr_unreachable = data.get('addr-unreachable')
	admin_prohibited = data.get('admin-prohibited')
	no_route = data.get('no-route')
	not_neighbour = data.get('not-neighbour')
	result = Service(svc_name=svc_name, icmp=icmp, icmpv6=icmpv6, tcp_udp=tcp_udp, source=source, eq_src=eq_src, gt_src=gt_src, lt_src=lt_src, range_src=range_src, port_num_end_src=port_num_end_src, eq_dst=eq_dst, gt_dst=gt_dst, lt_dst=lt_dst, range_dst=range_dst, port_num_end_dst=port_num_end_dst, code=code, any_code=any_code, icmp_code=icmp_code, type=type, icmp_type=icmp_type, any_type=any_type, dest_unreachable=dest_unreachable, echo_reply=echo_reply, echo_request=echo_request, info_reply=info_reply, info_request=info_request, mask_reply=mask_reply, mask_request=mask_request, parameter_problem=parameter_problem, redirect=redirect, source_quench=source_quench, time_exceeded=time_exceeded, timestamp=timestamp, timestamp_reply=timestamp_reply, type_code=type_code, type_any_code=type_any_code, type_icmp_code=type_icmp_code, dest_un_code=dest_un_code, dest_un_any_code=dest_un_any_code, dest_un_icmp_code=dest_un_icmp_code, frag_required=frag_required, host_unreachable=host_unreachable, network_unreachable=network_unreachable, port_unreachable=port_unreachable, proto_unreachable=proto_unreachable, route_failed=route_failed, v6_code=v6_code, v6_any_code=v6_any_code, v6_icmp_code=v6_icmp_code, v6_type=v6_type, icmpv6_type=icmpv6_type, v6_any_type=v6_any_type, packet_too_big=packet_too_big, param_prob=param_prob, v6_type_code=v6_type_code, v6_type_any_code=v6_type_any_code, v6_type_icmp_code=v6_type_icmp_code, v6_dest_un_code=v6_dest_un_code, v6_dest_un_any_code=v6_dest_un_any_code, v6_dest_un_icmp_code=v6_dest_un_icmp_code, addr_unreachable=addr_unreachable, admin_prohibited=admin_prohibited, no_route=no_route, not_neighbour=not_neighbour)
	return result

def serialize_Service_json(obj):
	output = OrderedDict()
	output['svc-name'] = obj.svc_name
	if obj.icmp is not None:
		output['icmp'] = obj.icmp
	if obj.icmpv6 is not None:
		output['icmpv6'] = obj.icmpv6
	if obj.tcp_udp is not None:
		output['tcp_udp'] = obj.tcp_udp
	output['source'] = obj.source
	output['eq-src'] = obj.eq_src
	output['gt-src'] = obj.gt_src
	output['lt-src'] = obj.lt_src
	output['range-src'] = obj.range_src
	if obj.port_num_end_src is not None:
		output['port-num-end-src'] = obj.port_num_end_src
	output['eq-dst'] = obj.eq_dst
	output['gt-dst'] = obj.gt_dst
	output['lt-dst'] = obj.lt_dst
	output['range-dst'] = obj.range_dst
	if obj.port_num_end_dst is not None:
		output['port-num-end-dst'] = obj.port_num_end_dst
	output['code'] = obj.code
	output['any-code'] = obj.any_code
	output['icmp-code'] = obj.icmp_code
	output['type'] = obj.type
	output['icmp-type'] = obj.icmp_type
	output['any-type'] = obj.any_type
	output['dest-unreachable'] = obj.dest_unreachable
	output['echo-reply'] = obj.echo_reply
	output['echo-request'] = obj.echo_request
	output['info-reply'] = obj.info_reply
	output['info-request'] = obj.info_request
	output['mask-reply'] = obj.mask_reply
	output['mask-request'] = obj.mask_request
	output['parameter-problem'] = obj.parameter_problem
	output['redirect'] = obj.redirect
	output['source-quench'] = obj.source_quench
	output['time-exceeded'] = obj.time_exceeded
	output['timestamp'] = obj.timestamp
	output['timestamp-reply'] = obj.timestamp_reply
	output['type-code'] = obj.type_code
	output['type-any-code'] = obj.type_any_code
	output['type-icmp-code'] = obj.type_icmp_code
	output['dest-un-code'] = obj.dest_un_code
	output['dest-un-any-code'] = obj.dest_un_any_code
	output['dest-un-icmp-code'] = obj.dest_un_icmp_code
	output['frag-required'] = obj.frag_required
	output['host-unreachable'] = obj.host_unreachable
	output['network-unreachable'] = obj.network_unreachable
	output['port-unreachable'] = obj.port_unreachable
	output['proto-unreachable'] = obj.proto_unreachable
	output['route-failed'] = obj.route_failed
	output['v6-code'] = obj.v6_code
	output['v6-any-code'] = obj.v6_any_code
	output['v6-icmp-code'] = obj.v6_icmp_code
	output['v6-type'] = obj.v6_type
	output['icmpv6-type'] = obj.icmpv6_type
	output['v6-any-type'] = obj.v6_any_type
	output['packet-too-big'] = obj.packet_too_big
	output['param-prob'] = obj.param_prob
	output['v6-type-code'] = obj.v6_type_code
	output['v6-type-any-code'] = obj.v6_type_any_code
	output['v6-type-icmp-code'] = obj.v6_type_icmp_code
	output['v6-dest-un-code'] = obj.v6_dest_un_code
	output['v6-dest-un-any-code'] = obj.v6_dest_un_any_code
	output['v6-dest-un-icmp-code'] = obj.v6_dest_un_icmp_code
	output['addr-unreachable'] = obj.addr_unreachable
	output['admin-prohibited'] = obj.admin_prohibited
	output['no-route'] = obj.no_route
	output['not-neighbour'] = obj.not_neighbour
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Service_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Service_json(item))
	return list(container)

class Service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable(AxapiObject):
	__metaclass__ = StructMeta 
	svc_name=SizedString(1, 63)
	source=PosRangedInteger(0, 1)
	eq_src=PosRangedInteger(1, 65535)
	gt_src=PosRangedInteger(1, 65535)
	lt_src=PosRangedInteger(1, 65535)
	range_src=PosRangedInteger(1, 65535)
	eq_dst=PosRangedInteger(1, 65535)
	gt_dst=PosRangedInteger(1, 65535)
	lt_dst=PosRangedInteger(1, 65535)
	range_dst=PosRangedInteger(1, 65535)
	code=PosRangedInteger(0, 1)
	any_code=PosRangedInteger(0, 1)
	icmp_code=PosRangedInteger(0, 254)
	type=PosRangedInteger(0, 1)
	icmp_type=PosRangedInteger(0, 254)
	any_type=PosRangedInteger(0, 1)
	dest_unreachable=PosRangedInteger(0, 1)
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
	type_code=PosRangedInteger(0, 1)
	type_any_code=PosRangedInteger(0, 1)
	type_icmp_code=PosRangedInteger(0, 254)
	dest_un_code=PosRangedInteger(0, 1)
	dest_un_any_code=PosRangedInteger(0, 1)
	dest_un_icmp_code=PosRangedInteger(0, 254)
	frag_required=PosRangedInteger(0, 1)
	host_unreachable=PosRangedInteger(0, 1)
	network_unreachable=PosRangedInteger(0, 1)
	port_unreachable=PosRangedInteger(0, 1)
	proto_unreachable=PosRangedInteger(0, 1)
	route_failed=PosRangedInteger(0, 1)
	v6_code=PosRangedInteger(0, 1)
	v6_any_code=PosRangedInteger(0, 1)
	v6_icmp_code=PosRangedInteger(0, 254)
	v6_type=PosRangedInteger(0, 1)
	icmpv6_type=PosRangedInteger(0, 254)
	v6_any_type=PosRangedInteger(0, 1)
	packet_too_big=PosRangedInteger(0, 1)
	param_prob=PosRangedInteger(0, 1)
	v6_type_code=PosRangedInteger(0, 1)
	v6_type_any_code=PosRangedInteger(0, 1)
	v6_type_icmp_code=PosRangedInteger(0, 254)
	v6_dest_un_code=PosRangedInteger(0, 1)
	v6_dest_un_any_code=PosRangedInteger(0, 1)
	v6_dest_un_icmp_code=PosRangedInteger(0, 254)
	addr_unreachable=PosRangedInteger(0, 1)
	admin_prohibited=PosRangedInteger(0, 1)
	no_route=PosRangedInteger(0, 1)
	not_neighbour=PosRangedInteger(0, 1)
	def __init__(self, svc_name, source, eq_src, gt_src, lt_src, range_src, eq_dst, gt_dst, lt_dst, range_dst, code, any_code, icmp_code, type, icmp_type, any_type, dest_unreachable, echo_reply, echo_request, info_reply, info_request, mask_reply, mask_request, parameter_problem, redirect, source_quench, time_exceeded, timestamp, timestamp_reply, type_code, type_any_code, type_icmp_code, dest_un_code, dest_un_any_code, dest_un_icmp_code, frag_required, host_unreachable, network_unreachable, port_unreachable, proto_unreachable, route_failed, v6_code, v6_any_code, v6_icmp_code, v6_type, icmpv6_type, v6_any_type, packet_too_big, param_prob, v6_type_code, v6_type_any_code, v6_type_icmp_code, v6_dest_un_code, v6_dest_un_any_code, v6_dest_un_icmp_code, addr_unreachable, admin_prohibited, no_route, not_neighbour):
		self.svc_name = svc_name
		self.source = source
		self.eq_src = eq_src
		self.gt_src = gt_src
		self.lt_src = lt_src
		self.range_src = range_src
		self.eq_dst = eq_dst
		self.gt_dst = gt_dst
		self.lt_dst = lt_dst
		self.range_dst = range_dst
		self.code = code
		self.any_code = any_code
		self.icmp_code = icmp_code
		self.type = type
		self.icmp_type = icmp_type
		self.any_type = any_type
		self.dest_unreachable = dest_unreachable
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
		self.type_any_code = type_any_code
		self.type_icmp_code = type_icmp_code
		self.dest_un_code = dest_un_code
		self.dest_un_any_code = dest_un_any_code
		self.dest_un_icmp_code = dest_un_icmp_code
		self.frag_required = frag_required
		self.host_unreachable = host_unreachable
		self.network_unreachable = network_unreachable
		self.port_unreachable = port_unreachable
		self.proto_unreachable = proto_unreachable
		self.route_failed = route_failed
		self.v6_code = v6_code
		self.v6_any_code = v6_any_code
		self.v6_icmp_code = v6_icmp_code
		self.v6_type = v6_type
		self.icmpv6_type = icmpv6_type
		self.v6_any_type = v6_any_type
		self.packet_too_big = packet_too_big
		self.param_prob = param_prob
		self.v6_type_code = v6_type_code
		self.v6_type_any_code = v6_type_any_code
		self.v6_type_icmp_code = v6_type_icmp_code
		self.v6_dest_un_code = v6_dest_un_code
		self.v6_dest_un_any_code = v6_dest_un_any_code
		self.v6_dest_un_icmp_code = v6_dest_un_icmp_code
		self.addr_unreachable = addr_unreachable
		self.admin_prohibited = admin_prohibited
		self.no_route = no_route
		self.not_neighbour = not_neighbour

	def __str__(self):
		return str(self.svc_name) + '+' + str(self.source) + '+' + str(self.eq_src) + '+' + str(self.gt_src) + '+' + str(self.lt_src) + '+' + str(self.range_src) + '+' + str(self.eq_dst) + '+' + str(self.gt_dst) + '+' + str(self.lt_dst) + '+' + str(self.range_dst) + '+' + str(self.code) + '+' + str(self.any_code) + '+' + str(self.icmp_code) + '+' + str(self.type) + '+' + str(self.icmp_type) + '+' + str(self.any_type) + '+' + str(self.dest_unreachable) + '+' + str(self.echo_reply) + '+' + str(self.echo_request) + '+' + str(self.info_reply) + '+' + str(self.info_request) + '+' + str(self.mask_reply) + '+' + str(self.mask_request) + '+' + str(self.parameter_problem) + '+' + str(self.redirect) + '+' + str(self.source_quench) + '+' + str(self.time_exceeded) + '+' + str(self.timestamp) + '+' + str(self.timestamp_reply) + '+' + str(self.type_code) + '+' + str(self.type_any_code) + '+' + str(self.type_icmp_code) + '+' + str(self.dest_un_code) + '+' + str(self.dest_un_any_code) + '+' + str(self.dest_un_icmp_code) + '+' + str(self.frag_required) + '+' + str(self.host_unreachable) + '+' + str(self.network_unreachable) + '+' + str(self.port_unreachable) + '+' + str(self.proto_unreachable) + '+' + str(self.route_failed) + '+' + str(self.v6_code) + '+' + str(self.v6_any_code) + '+' + str(self.v6_icmp_code) + '+' + str(self.v6_type) + '+' + str(self.icmpv6_type) + '+' + str(self.v6_any_type) + '+' + str(self.packet_too_big) + '+' + str(self.param_prob) + '+' + str(self.v6_type_code) + '+' + str(self.v6_type_any_code) + '+' + str(self.v6_type_icmp_code) + '+' + str(self.v6_dest_un_code) + '+' + str(self.v6_dest_un_any_code) + '+' + str(self.v6_dest_un_icmp_code) + '+' + str(self.addr_unreachable) + '+' + str(self.admin_prohibited) + '+' + str(self.no_route) + '+' + str(self.not_neighbour)

class Service(AxapiObject):
	__metaclass__ = StructMeta 
	svc_name=SizedString(1, 63)
	icmp=PosRangedInteger(0, 1)
	icmpv6=PosRangedInteger(0, 1)
	tcp_udp = Enum(['tcp', 'udp'])
	source=PosRangedInteger(0, 1)
	eq_src=PosRangedInteger(1, 65535)
	gt_src=PosRangedInteger(1, 65535)
	lt_src=PosRangedInteger(1, 65535)
	range_src=PosRangedInteger(1, 65535)
	port_num_end_src=PosRangedInteger(1, 65535)
	eq_dst=PosRangedInteger(1, 65535)
	gt_dst=PosRangedInteger(1, 65535)
	lt_dst=PosRangedInteger(1, 65535)
	range_dst=PosRangedInteger(1, 65535)
	port_num_end_dst=PosRangedInteger(1, 65535)
	code=PosRangedInteger(0, 1)
	any_code=PosRangedInteger(0, 1)
	icmp_code=PosRangedInteger(0, 254)
	type=PosRangedInteger(0, 1)
	icmp_type=PosRangedInteger(0, 254)
	any_type=PosRangedInteger(0, 1)
	dest_unreachable=PosRangedInteger(0, 1)
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
	type_code=PosRangedInteger(0, 1)
	type_any_code=PosRangedInteger(0, 1)
	type_icmp_code=PosRangedInteger(0, 254)
	dest_un_code=PosRangedInteger(0, 1)
	dest_un_any_code=PosRangedInteger(0, 1)
	dest_un_icmp_code=PosRangedInteger(0, 254)
	frag_required=PosRangedInteger(0, 1)
	host_unreachable=PosRangedInteger(0, 1)
	network_unreachable=PosRangedInteger(0, 1)
	port_unreachable=PosRangedInteger(0, 1)
	proto_unreachable=PosRangedInteger(0, 1)
	route_failed=PosRangedInteger(0, 1)
	v6_code=PosRangedInteger(0, 1)
	v6_any_code=PosRangedInteger(0, 1)
	v6_icmp_code=PosRangedInteger(0, 254)
	v6_type=PosRangedInteger(0, 1)
	icmpv6_type=PosRangedInteger(0, 254)
	v6_any_type=PosRangedInteger(0, 1)
	packet_too_big=PosRangedInteger(0, 1)
	param_prob=PosRangedInteger(0, 1)
	v6_type_code=PosRangedInteger(0, 1)
	v6_type_any_code=PosRangedInteger(0, 1)
	v6_type_icmp_code=PosRangedInteger(0, 254)
	v6_dest_un_code=PosRangedInteger(0, 1)
	v6_dest_un_any_code=PosRangedInteger(0, 1)
	v6_dest_un_icmp_code=PosRangedInteger(0, 254)
	addr_unreachable=PosRangedInteger(0, 1)
	admin_prohibited=PosRangedInteger(0, 1)
	no_route=PosRangedInteger(0, 1)
	not_neighbour=PosRangedInteger(0, 1)
	def __init__(self, svc_name, source, eq_src, gt_src, lt_src, range_src, eq_dst, gt_dst, lt_dst, range_dst, code, any_code, icmp_code, type, icmp_type, any_type, dest_unreachable, echo_reply, echo_request, info_reply, info_request, mask_reply, mask_request, parameter_problem, redirect, source_quench, time_exceeded, timestamp, timestamp_reply, type_code, type_any_code, type_icmp_code, dest_un_code, dest_un_any_code, dest_un_icmp_code, frag_required, host_unreachable, network_unreachable, port_unreachable, proto_unreachable, route_failed, v6_code, v6_any_code, v6_icmp_code, v6_type, icmpv6_type, v6_any_type, packet_too_big, param_prob, v6_type_code, v6_type_any_code, v6_type_icmp_code, v6_dest_un_code, v6_dest_un_any_code, v6_dest_un_icmp_code, addr_unreachable, admin_prohibited, no_route, not_neighbour, icmp=None, icmpv6=None, tcp_udp=None, port_num_end_src=None, port_num_end_dst=None):
		self.svc_name = svc_name
		self.icmp = icmp
		self.icmpv6 = icmpv6
		self.tcp_udp = tcp_udp
		self.source = source
		self.eq_src = eq_src
		self.gt_src = gt_src
		self.lt_src = lt_src
		self.range_src = range_src
		self.port_num_end_src = port_num_end_src
		self.eq_dst = eq_dst
		self.gt_dst = gt_dst
		self.lt_dst = lt_dst
		self.range_dst = range_dst
		self.port_num_end_dst = port_num_end_dst
		self.code = code
		self.any_code = any_code
		self.icmp_code = icmp_code
		self.type = type
		self.icmp_type = icmp_type
		self.any_type = any_type
		self.dest_unreachable = dest_unreachable
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
		self.type_any_code = type_any_code
		self.type_icmp_code = type_icmp_code
		self.dest_un_code = dest_un_code
		self.dest_un_any_code = dest_un_any_code
		self.dest_un_icmp_code = dest_un_icmp_code
		self.frag_required = frag_required
		self.host_unreachable = host_unreachable
		self.network_unreachable = network_unreachable
		self.port_unreachable = port_unreachable
		self.proto_unreachable = proto_unreachable
		self.route_failed = route_failed
		self.v6_code = v6_code
		self.v6_any_code = v6_any_code
		self.v6_icmp_code = v6_icmp_code
		self.v6_type = v6_type
		self.icmpv6_type = icmpv6_type
		self.v6_any_type = v6_any_type
		self.packet_too_big = packet_too_big
		self.param_prob = param_prob
		self.v6_type_code = v6_type_code
		self.v6_type_any_code = v6_type_any_code
		self.v6_type_icmp_code = v6_type_icmp_code
		self.v6_dest_un_code = v6_dest_un_code
		self.v6_dest_un_any_code = v6_dest_un_any_code
		self.v6_dest_un_icmp_code = v6_dest_un_icmp_code
		self.addr_unreachable = addr_unreachable
		self.admin_prohibited = admin_prohibited
		self.no_route = no_route
		self.not_neighbour = not_neighbour

	def __str__(self):
		return str(self.svc_name) + '+' + str(self.source) + '+' + str(self.eq_src) + '+' + str(self.gt_src) + '+' + str(self.lt_src) + '+' + str(self.range_src) + '+' + str(self.eq_dst) + '+' + str(self.gt_dst) + '+' + str(self.lt_dst) + '+' + str(self.range_dst) + '+' + str(self.code) + '+' + str(self.any_code) + '+' + str(self.icmp_code) + '+' + str(self.type) + '+' + str(self.icmp_type) + '+' + str(self.any_type) + '+' + str(self.dest_unreachable) + '+' + str(self.echo_reply) + '+' + str(self.echo_request) + '+' + str(self.info_reply) + '+' + str(self.info_request) + '+' + str(self.mask_reply) + '+' + str(self.mask_request) + '+' + str(self.parameter_problem) + '+' + str(self.redirect) + '+' + str(self.source_quench) + '+' + str(self.time_exceeded) + '+' + str(self.timestamp) + '+' + str(self.timestamp_reply) + '+' + str(self.type_code) + '+' + str(self.type_any_code) + '+' + str(self.type_icmp_code) + '+' + str(self.dest_un_code) + '+' + str(self.dest_un_any_code) + '+' + str(self.dest_un_icmp_code) + '+' + str(self.frag_required) + '+' + str(self.host_unreachable) + '+' + str(self.network_unreachable) + '+' + str(self.port_unreachable) + '+' + str(self.proto_unreachable) + '+' + str(self.route_failed) + '+' + str(self.v6_code) + '+' + str(self.v6_any_code) + '+' + str(self.v6_icmp_code) + '+' + str(self.v6_type) + '+' + str(self.icmpv6_type) + '+' + str(self.v6_any_type) + '+' + str(self.packet_too_big) + '+' + str(self.param_prob) + '+' + str(self.v6_type_code) + '+' + str(self.v6_type_any_code) + '+' + str(self.v6_type_icmp_code) + '+' + str(self.v6_dest_un_code) + '+' + str(self.v6_dest_un_any_code) + '+' + str(self.v6_dest_un_icmp_code) + '+' + str(self.addr_unreachable) + '+' + str(self.admin_prohibited) + '+' + str(self.no_route) + '+' + str(self.not_neighbour)

class ObjectgroupServiceClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getObjectgroupService(self, service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable):
		"""
		Retrieve the service identified by the specified identifier
		
		Args:
			service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable Service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable
		
		Returns:
			An instance of the Service class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified service does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('service')
		return deserialize_Service_json(payload)

	def putObjectgroupService(self, service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable, service):
		"""
		Replace the object service
		
		Args:
			service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable Service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable
			service An instance of the Service class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['service']=serialize_Service_json(service)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable) .replace("/", "%2f") + query, payload, headers)
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

	def deleteObjectgroupService(self, service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable):
		"""
		Remove the service identified by the specified identifier from the system
		
		Args:
			service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable Service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(service_svc_name_source_eq_src_gt_src_lt_src_range_src_eq_dst_gt_dst_lt_dst_range_dst_code_any_code_icmp_code_type_icmp_type_any_type_dest_unreachable_echo_reply_echo_request_info_reply_info_request_mask_reply_mask_request_parameter_problem_redirect_source_quench_time_exceeded_timestamp_timestamp_reply_type_code_type_any_code_type_icmp_code_dest_un_code_dest_un_any_code_dest_un_icmp_code_frag_required_host_unreachable_network_unreachable_port_unreachable_proto_unreachable_route_failed_v6_code_v6_any_code_v6_icmp_code_v6_type_icmpv6_type_v6_any_type_dest_unreachable_echo_reply_echo_request_packet_too_big_param_prob_time_exceeded_v6_type_code_v6_type_any_code_v6_type_icmp_code_v6_dest_un_code_v6_dest_un_any_code_v6_dest_un_icmp_code_addr_unreachable_admin_prohibited_no_route_not_neighbour_port_unreachable) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified service does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllObjectgroupServicesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitObjectgroupService(self, service):
		"""
		Create the object service
		
		Args:
			service An instance of the Service class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['service']=serialize_Service_json(service)
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

	def getAllObjectgroupServices(self):
		"""
		Retrieve all service objects currently pending in the system
		
		Returns:
			A list of Service objects
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
			payload= data.get('serviceList')
		return deserialize_list_Service_json(payload)

