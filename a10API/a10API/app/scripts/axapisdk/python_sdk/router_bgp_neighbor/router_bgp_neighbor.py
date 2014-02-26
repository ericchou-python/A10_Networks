########################################################################################################################
# File name: router_bgp_neighbor.py
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
	'https://axapi.a10networks.com/axapi/v3/router/bgp/neighbor',
]

def deserialize_Neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	allowas_in = data.get('allowas-in')
	allowas_in_count = data.get('allowas-in-count')
	result = Neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg(allowas_in=allowas_in, allowas_in_count=allowas_in_count)
	return result

def deserialize_Neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	orf = data.get('orf')
	prefix_list = data.get('prefix-list')
	both = data.get('both')
	receive = data.get('receive')
	send = data.get('send')
	result = Neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg(orf=orf, prefix_list=prefix_list, both=both, receive=receive, send=send)
	return result

def deserialize_Neighbor__neighbor_str_cfg__neighbor_capability_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dynamic = data.get('dynamic')
	neighbor_orf_cfg = deserialize_Neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg_json(data.get('neighbor-orf-cfg'))
	route_refresh = data.get('route-refresh')
	result = Neighbor__neighbor_str_cfg__neighbor_capability(dynamic=dynamic, neighbor_orf_cfg=neighbor_orf_cfg, route_refresh=route_refresh)
	return result

def deserialize_Neighbor__neighbor_str_cfg__neighbor_default_originate_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default_originate = data.get('default-originate')
	route_map = data.get('route-map')
	result = Neighbor__neighbor_str_cfg__neighbor_default_originate_cfg(default_originate=default_originate, route_map=route_map)
	return result

def deserialize_Router_bgp_neighbor_neighbor_distribute_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	distribute_list = data.get('distribute-list')
	acl_val = data.get('acl-val')
	py_kw_rsvd_in = data.get('in')
	out = data.get('out')
	result = Router_bgp_neighbor_neighbor_distribute_list_cfg(distribute_list=distribute_list, acl_val=acl_val, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_neighbor_neighbor_distribute_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_neighbor_neighbor_distribute_list_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_neighbor_neighbor_ebgp_multihop_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ebgp_multihop = data.get('ebgp-multihop')
	ebgp_multihop_hop_count = data.get('ebgp-multihop-hop-count')
	result = Router_bgp_neighbor_neighbor_ebgp_multihop_cfg(ebgp_multihop=ebgp_multihop, ebgp_multihop_hop_count=ebgp_multihop_hop_count)
	return result

def deserialize_list_Router_bgp_neighbor_neighbor_ebgp_multihop_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_neighbor_neighbor_ebgp_multihop_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_neighbor_neighbor_filter_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	filter_list = data.get('filter-list')
	py_kw_rsvd_in = data.get('in')
	out = data.get('out')
	result = Router_bgp_neighbor_neighbor_filter_list_cfg(filter_list=filter_list, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_neighbor_neighbor_filter_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_neighbor_neighbor_filter_list_cfg_json(item))
	return list(container)

def deserialize_Neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	maximum_prefix = data.get('maximum-prefix')
	maximum_prefix_thres = data.get('maximum-prefix-thres')
	result = Neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg(maximum_prefix=maximum_prefix, maximum_prefix_thres=maximum_prefix_thres)
	return result

def deserialize_Neighbor__neighbor_str_cfg__nbr_str_pass_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	encrypted = data.get('encrypted')
	result = Neighbor__neighbor_str_cfg__nbr_str_pass(value=value, encrypted=encrypted)
	return result

def deserialize_Router_bgp_neighbor_neighbor_prefix_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	prefix_list = data.get('prefix-list')
	py_kw_rsvd_in = data.get('in')
	out = data.get('out')
	result = Router_bgp_neighbor_neighbor_prefix_list_cfg(prefix_list=prefix_list, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_neighbor_neighbor_prefix_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_neighbor_neighbor_prefix_list_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_neighbor_neighbor_route_map_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	route_map = data.get('route-map')
	py_kw_rsvd_in = data.get('in')
	out = data.get('out')
	result = Router_bgp_neighbor_neighbor_route_map_cfg(route_map=route_map, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_neighbor_neighbor_route_map_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_neighbor_neighbor_route_map_cfg_json(item))
	return list(container)

def deserialize_Neighbor__neighbor_str_cfg__neighbor_send_community_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	send_community = data.get('send-community')
	both = data.get('both')
	extended = data.get('extended')
	standard = data.get('standard')
	result = Neighbor__neighbor_str_cfg__neighbor_send_community_cfg(send_community=send_community, both=both, extended=extended, standard=standard)
	return result

def deserialize_Neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	soft_reconfiguration = data.get('soft-reconfiguration')
	inbound = data.get('inbound')
	result = Neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg(soft_reconfiguration=soft_reconfiguration, inbound=inbound)
	return result

def deserialize_Neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timers_keepalive = data.get('timers-keepalive')
	timers_holdtime = data.get('timers-holdtime')
	result = Neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg(timers_keepalive=timers_keepalive, timers_holdtime=timers_holdtime)
	return result

def deserialize_Neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	connect = data.get('connect')
	result = Neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg(connect=connect)
	return result

def deserialize_Neighbor__neighbor_str_cfg__timers_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	neighbor_timers_keepalive_cfg = deserialize_Neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg_json(data.get('neighbor-timers-keepalive-cfg'))
	timers_con_under_group_cfg = deserialize_Neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg_json(data.get('timers-con-under-group-cfg'))
	result = Neighbor__neighbor_str_cfg__timers(neighbor_timers_keepalive_cfg=neighbor_timers_keepalive_cfg, timers_con_under_group_cfg=timers_con_under_group_cfg)
	return result

def deserialize_Neighbor__neighbor_str_cfg__neighbor_update_source_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	update_source = data.get('update-source')
	update_source_ip = data.get('update-source-ip')
	update_source_ipv6 = data.get('update-source-ipv6')
	ethernet = data.get('ethernet')
	loopback = data.get('loopback')
	ve = data.get('ve')
	trunk = data.get('trunk')
	result = Neighbor__neighbor_str_cfg__neighbor_update_source_cfg(update_source=update_source, update_source_ip=update_source_ip, update_source_ipv6=update_source_ipv6, ethernet=ethernet, loopback=loopback, ve=ve, trunk=trunk)
	return result

def deserialize_Neighbor__neighbor_str_cfg__neighbor_version_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	version = data.get('version')
	param_4 = data.get('4')
	result = Neighbor__neighbor_str_cfg__neighbor_version_cfg(version=version, param_4=param_4)
	return result

def deserialize_Neighbor__neighbor_str_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	neighbor_str = data.get('neighbor-str')
	peer_group = data.get('peer-group')
	remote_as = data.get('remote-as')
	activate = data.get('activate')
	advertisement_interval = data.get('advertisement-interval')
	neighbor_allowas_in_cfg = deserialize_Neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg_json(data.get('neighbor-allowas-in-cfg'))
	as_origination_interval = data.get('as-origination-interval')
	neighbor_capability = deserialize_Neighbor__neighbor_str_cfg__neighbor_capability_json(data.get('neighbor-capability'))
	collide_established = data.get('collide-established')
	connection_retry_time = data.get('connection-retry-time')
	neighbor_default_originate_cfg = deserialize_Neighbor__neighbor_str_cfg__neighbor_default_originate_cfg_json(data.get('neighbor-default-originate-cfg'))
	disallow_infinite_holdtime = data.get('disallow-infinite-holdtime')
	neighbor_distribute_list_cfg = deserialize_list_Router_bgp_neighbor_neighbor_distribute_list_cfg_json(data.get('neighbor-distribute-list-cfg'))
	dont_capability_negotiate = data.get('dont-capability-negotiate')
	neighbor_ebgp_multihop_cfg = deserialize_list_Router_bgp_neighbor_neighbor_ebgp_multihop_cfg_json(data.get('neighbor-ebgp-multihop-cfg'))
	enforce_multihop = data.get('enforce-multihop')
	neighbor_filter_list_cfg = deserialize_list_Router_bgp_neighbor_neighbor_filter_list_cfg_json(data.get('neighbor-filter-list-cfg'))
	neighbor_maximum_prefix_cfg = deserialize_Neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg_json(data.get('neighbor-maximum-prefix-cfg'))
	next_hop_self = data.get('next-hop-self')
	override_capability = data.get('override-capability')
	nbr_str_pass = deserialize_Neighbor__neighbor_str_cfg__nbr_str_pass_json(data.get('nbr-str-pass'))
	passive = data.get('passive')
	neighbor_prefix_list_cfg = deserialize_list_Router_bgp_neighbor_neighbor_prefix_list_cfg_json(data.get('neighbor-prefix-list-cfg'))
	remove_private_as = data.get('remove-private-AS')
	neighbor_route_map_cfg = deserialize_list_Router_bgp_neighbor_neighbor_route_map_cfg_json(data.get('neighbor-route-map-cfg'))
	neighbor_send_community_cfg = deserialize_Neighbor__neighbor_str_cfg__neighbor_send_community_cfg_json(data.get('neighbor-send-community-cfg'))
	neighbor_soft_reconfiguration_cfg = deserialize_Neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg_json(data.get('neighbor-soft-reconfiguration-cfg'))
	shutdown = data.get('shutdown')
	strict_capability_match = data.get('strict-capability-match')
	timers = deserialize_Neighbor__neighbor_str_cfg__timers_json(data.get('timers'))
	unsuppress_map = data.get('unsuppress-map')
	neighbor_update_source_cfg = deserialize_Neighbor__neighbor_str_cfg__neighbor_update_source_cfg_json(data.get('neighbor-update-source-cfg'))
	neighbor_version_cfg = deserialize_Neighbor__neighbor_str_cfg__neighbor_version_cfg_json(data.get('neighbor-version-cfg'))
	weight = data.get('weight')
	result = Neighbor__neighbor_str_cfg(neighbor_str=neighbor_str, peer_group=peer_group, remote_as=remote_as, activate=activate, advertisement_interval=advertisement_interval, neighbor_allowas_in_cfg=neighbor_allowas_in_cfg, as_origination_interval=as_origination_interval, neighbor_capability=neighbor_capability, collide_established=collide_established, connection_retry_time=connection_retry_time, neighbor_default_originate_cfg=neighbor_default_originate_cfg, disallow_infinite_holdtime=disallow_infinite_holdtime, neighbor_distribute_list_cfg=neighbor_distribute_list_cfg, dont_capability_negotiate=dont_capability_negotiate, neighbor_ebgp_multihop_cfg=neighbor_ebgp_multihop_cfg, enforce_multihop=enforce_multihop, neighbor_filter_list_cfg=neighbor_filter_list_cfg, neighbor_maximum_prefix_cfg=neighbor_maximum_prefix_cfg, next_hop_self=next_hop_self, override_capability=override_capability, nbr_str_pass=nbr_str_pass, passive=passive, neighbor_prefix_list_cfg=neighbor_prefix_list_cfg, remove_private_as=remove_private_as, neighbor_route_map_cfg=neighbor_route_map_cfg, neighbor_send_community_cfg=neighbor_send_community_cfg, neighbor_soft_reconfiguration_cfg=neighbor_soft_reconfiguration_cfg, shutdown=shutdown, strict_capability_match=strict_capability_match, timers=timers, unsuppress_map=unsuppress_map, neighbor_update_source_cfg=neighbor_update_source_cfg, neighbor_version_cfg=neighbor_version_cfg, weight=weight)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__allowas_in_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	allowas_in = data.get('allowas-in')
	allowas_in_count = data.get('allowas-in-count')
	result = Neighbor__neighbor_ipv4_cfg__allowas_in_cfg(allowas_in=allowas_in, allowas_in_count=allowas_in_count)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	orf = data.get('orf')
	prefix_list = data.get('prefix-list')
	both = data.get('both')
	receive = data.get('receive')
	send = data.get('send')
	result = Neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg(orf=orf, prefix_list=prefix_list, both=both, receive=receive, send=send)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__capability_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dynamic = data.get('dynamic')
	orf_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg_json(data.get('orf-cfg'))
	route_refresh = data.get('route-refresh')
	result = Neighbor__neighbor_ipv4_cfg__capability_1(dynamic=dynamic, orf_cfg=orf_cfg, route_refresh=route_refresh)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__default_originate_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default_originate = data.get('default-originate')
	route_map = data.get('route-map')
	result = Neighbor__neighbor_ipv4_cfg__default_originate_cfg(default_originate=default_originate, route_map=route_map)
	return result

def deserialize_Router_bgp_neighbor_distribute_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	distribute_list = data.get('distribute-list')
	acl_val = data.get('acl-val')
	py_kw_rsvd_in = data.get('in')
	out = data.get('out')
	result = Router_bgp_neighbor_distribute_list_cfg(distribute_list=distribute_list, acl_val=acl_val, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_neighbor_distribute_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_neighbor_distribute_list_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_neighbor_ebgp_multihop_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ebgp_multihop = data.get('ebgp-multihop')
	ebgp_multihop_hop_count = data.get('ebgp-multihop-hop-count')
	result = Router_bgp_neighbor_ebgp_multihop_cfg(ebgp_multihop=ebgp_multihop, ebgp_multihop_hop_count=ebgp_multihop_hop_count)
	return result

def deserialize_list_Router_bgp_neighbor_ebgp_multihop_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_neighbor_ebgp_multihop_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_neighbor_filter_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	filter_list = data.get('filter-list')
	py_kw_rsvd_in = data.get('in')
	out = data.get('out')
	result = Router_bgp_neighbor_filter_list_cfg(filter_list=filter_list, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_neighbor_filter_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_neighbor_filter_list_cfg_json(item))
	return list(container)

def deserialize_Neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	maximum_prefix = data.get('maximum-prefix')
	maximum_prefix_thres = data.get('maximum-prefix-thres')
	result = Neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg(maximum_prefix=maximum_prefix, maximum_prefix_thres=maximum_prefix_thres)
	return result

def deserialize_Router_bgp_neighbor_prefix_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	prefix_list = data.get('prefix-list')
	py_kw_rsvd_in = data.get('in')
	out = data.get('out')
	result = Router_bgp_neighbor_prefix_list_cfg(prefix_list=prefix_list, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_neighbor_prefix_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_neighbor_prefix_list_cfg_json(item))
	return list(container)

def deserialize_Neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	nbr_ipv4_pass_value = data.get('nbr-ipv4-pass-value')
	nbr_ipv4_pass_encrypted = data.get('nbr-ipv4-pass-encrypted')
	result = Neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass(nbr_ipv4_pass_value=nbr_ipv4_pass_value, nbr_ipv4_pass_encrypted=nbr_ipv4_pass_encrypted)
	return result

def deserialize_Router_bgp_neighbor_route_map_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	route_map = data.get('route-map')
	py_kw_rsvd_in = data.get('in')
	out = data.get('out')
	result = Router_bgp_neighbor_route_map_cfg(route_map=route_map, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_neighbor_route_map_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_neighbor_route_map_cfg_json(item))
	return list(container)

def deserialize_Neighbor__neighbor_ipv4_cfg__send_community_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	send_community = data.get('send-community')
	both = data.get('both')
	extended = data.get('extended')
	standard = data.get('standard')
	result = Neighbor__neighbor_ipv4_cfg__send_community_cfg(send_community=send_community, both=both, extended=extended, standard=standard)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	soft_reconfiguration = data.get('soft-reconfiguration')
	inbound = data.get('inbound')
	result = Neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg(soft_reconfiguration=soft_reconfiguration, inbound=inbound)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	md5_value = data.get('md5-value')
	md5_encrypted = data.get('md5-encrypted')
	result = Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5(md5_value=md5_value, md5_encrypted=md5_encrypted)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	meticulous_md5_value = data.get('meticulous-md5-value')
	meticulous_md5_encrypted = data.get('meticulous-md5-encrypted')
	result = Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5(meticulous_md5_value=meticulous_md5_value, meticulous_md5_encrypted=meticulous_md5_encrypted)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	meticulous_sha1_value = data.get('meticulous-sha1-value')
	meticulous_sha1_encrypted = data.get('meticulous-sha1-encrypted')
	result = Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1(meticulous_sha1_value=meticulous_sha1_value, meticulous_sha1_encrypted=meticulous_sha1_encrypted)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sha1_value = data.get('sha1-value')
	sha1_encrypted = data.get('sha1-encrypted')
	result = Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1(sha1_value=sha1_value, sha1_encrypted=sha1_encrypted)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	simple_value = data.get('simple-value')
	simple_encrypted = data.get('simple-encrypted')
	result = Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple(simple_value=simple_value, simple_encrypted=simple_encrypted)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key_id = data.get('key-id')
	md5 = deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5_json(data.get('md5'))
	meticulous_md5 = deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5_json(data.get('meticulous-md5'))
	meticulous_sha1 = deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1_json(data.get('meticulous-sha1'))
	sha1 = deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1_json(data.get('sha1'))
	simple = deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple_json(data.get('simple'))
	result = Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg(key_id=key_id, md5=md5, meticulous_md5=meticulous_md5, meticulous_sha1=meticulous_sha1, sha1=sha1, simple=simple)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key_id_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg_json(data.get('key-id-cfg'))
	result = Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication(key_id_cfg=key_id_cfg)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bfd = data.get('bfd')
	authentication = deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication_json(data.get('authentication'))
	multihop = data.get('multihop')
	result = Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg(bfd=bfd, authentication=authentication, multihop=multihop)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	fall_over = data.get('fall-over')
	bfd_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg_json(data.get('bfd-cfg'))
	result = Neighbor__neighbor_ipv4_cfg__fall_over_cfg(fall_over=fall_over, bfd_cfg=bfd_cfg)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	neighbor_ipv4_timers_keepalive = data.get('neighbor-ipv4-timers-keepalive')
	timers_holdtime = data.get('timers-holdtime')
	result = Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg(neighbor_ipv4_timers_keepalive=neighbor_ipv4_timers_keepalive, timers_holdtime=timers_holdtime)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	connect = data.get('connect')
	result = Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg(connect=connect)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timers_keepalive_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg_json(data.get('timers-keepalive-cfg'))
	timers_con_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg_json(data.get('timers-con-cfg'))
	result = Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers(timers_keepalive_cfg=timers_keepalive_cfg, timers_con_cfg=timers_con_cfg)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__update_source_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	update_source = data.get('update-source')
	update_source_ip = data.get('update-source-ip')
	update_source_ipv6 = data.get('update-source-ipv6')
	ethernet = data.get('ethernet')
	loopback = data.get('loopback')
	ve = data.get('ve')
	trunk = data.get('trunk')
	result = Neighbor__neighbor_ipv4_cfg__update_source_cfg(update_source=update_source, update_source_ip=update_source_ip, update_source_ipv6=update_source_ipv6, ethernet=ethernet, loopback=loopback, ve=ve, trunk=trunk)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg__version_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	version = data.get('version')
	param_4 = data.get('4')
	result = Neighbor__neighbor_ipv4_cfg__version_cfg(version=version, param_4=param_4)
	return result

def deserialize_Neighbor__neighbor_ipv4_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	neighbor_ipv4 = data.get('neighbor-ipv4')
	neighbor_ipv6 = data.get('neighbor-ipv6')
	remote_as = data.get('remote-as')
	peer_group = data.get('peer-group')
	activate = data.get('activate')
	advertisement_interval = data.get('advertisement-interval')
	allowas_in_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__allowas_in_cfg_json(data.get('allowas-in-cfg'))
	as_origination_interval = data.get('as-origination-interval')
	capability_1 = deserialize_Neighbor__neighbor_ipv4_cfg__capability_1_json(data.get('capability-1'))
	collide_established = data.get('collide-established')
	connection_retry_time = data.get('connection-retry-time')
	default_originate_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__default_originate_cfg_json(data.get('default-originate-cfg'))
	disallow_infinite_holdtime = data.get('disallow-infinite-holdtime')
	distribute_list_cfg = deserialize_list_Router_bgp_neighbor_distribute_list_cfg_json(data.get('distribute-list-cfg'))
	dont_capability_negotiate = data.get('dont-capability-negotiate')
	ebgp_multihop_cfg = deserialize_list_Router_bgp_neighbor_ebgp_multihop_cfg_json(data.get('ebgp-multihop-cfg'))
	enforce_multihop = data.get('enforce-multihop')
	filter_list_cfg = deserialize_list_Router_bgp_neighbor_filter_list_cfg_json(data.get('filter-list-cfg'))
	maximum_prefix_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg_json(data.get('maximum-prefix-cfg'))
	next_hop_self = data.get('next-hop-self')
	override_capability = data.get('override-capability')
	passive = data.get('passive')
	prefix_list_cfg = deserialize_list_Router_bgp_neighbor_prefix_list_cfg_json(data.get('prefix-list-cfg'))
	remove_private_as = data.get('remove-private-AS')
	nbr_ipv4_pass = deserialize_Neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass_json(data.get('nbr-ipv4-pass'))
	route_map_cfg = deserialize_list_Router_bgp_neighbor_route_map_cfg_json(data.get('route-map-cfg'))
	send_community_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__send_community_cfg_json(data.get('send-community-cfg'))
	soft_reconfiguration_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg_json(data.get('soft-reconfiguration-cfg'))
	shutdown = data.get('shutdown')
	fall_over_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg_json(data.get('fall-over-cfg'))
	strict_capability_match = data.get('strict-capability-match')
	neighbor_ipv4_timers = deserialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers_json(data.get('neighbor-ipv4-timers'))
	unsuppress_map = data.get('unsuppress-map')
	update_source_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__update_source_cfg_json(data.get('update-source-cfg'))
	version_cfg = deserialize_Neighbor__neighbor_ipv4_cfg__version_cfg_json(data.get('version-cfg'))
	weight = data.get('weight')
	result = Neighbor__neighbor_ipv4_cfg(neighbor_ipv4=neighbor_ipv4, neighbor_ipv6=neighbor_ipv6, remote_as=remote_as, peer_group=peer_group, activate=activate, advertisement_interval=advertisement_interval, allowas_in_cfg=allowas_in_cfg, as_origination_interval=as_origination_interval, capability_1=capability_1, collide_established=collide_established, connection_retry_time=connection_retry_time, default_originate_cfg=default_originate_cfg, disallow_infinite_holdtime=disallow_infinite_holdtime, distribute_list_cfg=distribute_list_cfg, dont_capability_negotiate=dont_capability_negotiate, ebgp_multihop_cfg=ebgp_multihop_cfg, enforce_multihop=enforce_multihop, filter_list_cfg=filter_list_cfg, maximum_prefix_cfg=maximum_prefix_cfg, next_hop_self=next_hop_self, override_capability=override_capability, passive=passive, prefix_list_cfg=prefix_list_cfg, remove_private_as=remove_private_as, nbr_ipv4_pass=nbr_ipv4_pass, route_map_cfg=route_map_cfg, send_community_cfg=send_community_cfg, soft_reconfiguration_cfg=soft_reconfiguration_cfg, shutdown=shutdown, fall_over_cfg=fall_over_cfg, strict_capability_match=strict_capability_match, neighbor_ipv4_timers=neighbor_ipv4_timers, unsuppress_map=unsuppress_map, update_source_cfg=update_source_cfg, version_cfg=version_cfg, weight=weight)
	return result

def deserialize_Neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	neighbor_str_cfg = deserialize_Neighbor__neighbor_str_cfg_json(data.get('neighbor-str-cfg'))
	neighbor_ipv4_cfg = deserialize_Neighbor__neighbor_ipv4_cfg_json(data.get('neighbor-ipv4-cfg'))
	result = Neighbor(neighbor_str_cfg=neighbor_str_cfg, neighbor_ipv4_cfg=neighbor_ipv4_cfg)
	return result

def serialize_Neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg_json(obj):
	output = OrderedDict()
	output['allowas-in'] = obj.allowas_in
	if obj.allowas_in_count is not None:
		output['allowas-in-count'] = obj.allowas_in_count
	return output

def serialize_Neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg_json(obj):
	output = OrderedDict()
	output['orf'] = obj.orf
	output['prefix-list'] = obj.prefix_list
	if obj.both is not None:
		output['both'] = obj.both
	output['receive'] = obj.receive
	output['send'] = obj.send
	return output

def serialize_Neighbor__neighbor_str_cfg__neighbor_capability_json(obj):
	output = OrderedDict()
	output['dynamic'] = obj.dynamic
	if obj.neighbor_orf_cfg is not None:
		output['neighbor-orf-cfg'] = serialize_Neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg_json(obj.neighbor_orf_cfg)
	output['route-refresh'] = obj.route_refresh
	return output

def serialize_Neighbor__neighbor_str_cfg__neighbor_default_originate_cfg_json(obj):
	output = OrderedDict()
	output['default-originate'] = obj.default_originate
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Router_bgp_neighbor_neighbor_distribute_list_cfg_json(obj):
	output = OrderedDict()
	if obj.distribute_list is not None:
		output['distribute-list'] = obj.distribute_list
	if obj.acl_val is not None:
		output['acl-val'] = obj.acl_val
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.out is not None:
		output['out'] = obj.out
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Router_bgp_neighbor_neighbor_distribute_list_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_neighbor_neighbor_distribute_list_cfg_json(item))
	return output

def serialize_Router_bgp_neighbor_neighbor_ebgp_multihop_cfg_json(obj):
	output = OrderedDict()
	if obj.ebgp_multihop is not None:
		output['ebgp-multihop'] = obj.ebgp_multihop
	if obj.ebgp_multihop_hop_count is not None:
		output['ebgp-multihop-hop-count'] = obj.ebgp_multihop_hop_count
	return output

def serialize_list_Router_bgp_neighbor_neighbor_ebgp_multihop_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_neighbor_neighbor_ebgp_multihop_cfg_json(item))
	return output

def serialize_Router_bgp_neighbor_neighbor_filter_list_cfg_json(obj):
	output = OrderedDict()
	if obj.filter_list is not None:
		output['filter-list'] = obj.filter_list
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.out is not None:
		output['out'] = obj.out
	return output

def serialize_list_Router_bgp_neighbor_neighbor_filter_list_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_neighbor_neighbor_filter_list_cfg_json(item))
	return output

def serialize_Neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg_json(obj):
	output = OrderedDict()
	output['maximum-prefix'] = obj.maximum_prefix
	if obj.maximum_prefix_thres is not None:
		output['maximum-prefix-thres'] = obj.maximum_prefix_thres
	return output

def serialize_Neighbor__neighbor_str_cfg__nbr_str_pass_json(obj):
	output = OrderedDict()
	output['value'] = obj.value
	output['encrypted'] = obj.encrypted
	return output

def serialize_Router_bgp_neighbor_neighbor_prefix_list_cfg_json(obj):
	output = OrderedDict()
	output['prefix-list'] = obj.prefix_list
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.out is not None:
		output['out'] = obj.out
	return output

def serialize_list_Router_bgp_neighbor_neighbor_prefix_list_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_neighbor_neighbor_prefix_list_cfg_json(item))
	return output

def serialize_Router_bgp_neighbor_neighbor_route_map_cfg_json(obj):
	output = OrderedDict()
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.out is not None:
		output['out'] = obj.out
	return output

def serialize_list_Router_bgp_neighbor_neighbor_route_map_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_neighbor_neighbor_route_map_cfg_json(item))
	return output

def serialize_Neighbor__neighbor_str_cfg__neighbor_send_community_cfg_json(obj):
	output = OrderedDict()
	output['send-community'] = obj.send_community
	if obj.both is not None:
		output['both'] = obj.both
	if obj.extended is not None:
		output['extended'] = obj.extended
	if obj.standard is not None:
		output['standard'] = obj.standard
	return output

def serialize_Neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg_json(obj):
	output = OrderedDict()
	output['soft-reconfiguration'] = obj.soft_reconfiguration
	output['inbound'] = obj.inbound
	return output

def serialize_Neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg_json(obj):
	output = OrderedDict()
	output['timers-keepalive'] = obj.timers_keepalive
	output['timers-holdtime'] = obj.timers_holdtime
	return output

def serialize_Neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg_json(obj):
	output = OrderedDict()
	output['connect'] = obj.connect
	return output

def serialize_Neighbor__neighbor_str_cfg__timers_json(obj):
	output = OrderedDict()
	if obj.neighbor_timers_keepalive_cfg is not None:
		output['neighbor-timers-keepalive-cfg'] = serialize_Neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg_json(obj.neighbor_timers_keepalive_cfg)
	if obj.timers_con_under_group_cfg is not None:
		output['timers-con-under-group-cfg'] = serialize_Neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg_json(obj.timers_con_under_group_cfg)
	return output

def serialize_Neighbor__neighbor_str_cfg__neighbor_update_source_cfg_json(obj):
	output = OrderedDict()
	output['update-source'] = obj.update_source
	output['update-source-ip'] = obj.update_source_ip
	output['update-source-ipv6'] = obj.update_source_ipv6
	output['ethernet'] = obj.ethernet
	output['loopback'] = obj.loopback
	output['ve'] = obj.ve
	output['trunk'] = obj.trunk
	return output

def serialize_Neighbor__neighbor_str_cfg__neighbor_version_cfg_json(obj):
	output = OrderedDict()
	output['version'] = obj.version
	output['4'] = obj.param_4
	return output

def serialize_Neighbor__neighbor_str_cfg_json(obj):
	output = OrderedDict()
	output['neighbor-str'] = obj.neighbor_str
	output['peer-group'] = obj.peer_group
	output['remote-as'] = obj.remote_as
	output['activate'] = obj.activate
	output['advertisement-interval'] = obj.advertisement_interval
	if obj.neighbor_allowas_in_cfg is not None:
		output['neighbor-allowas-in-cfg'] = serialize_Neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg_json(obj.neighbor_allowas_in_cfg)
	output['as-origination-interval'] = obj.as_origination_interval
	output['neighbor-capability'] = serialize_Neighbor__neighbor_str_cfg__neighbor_capability_json(obj.neighbor_capability)
	output['collide-established'] = obj.collide_established
	output['connection-retry-time'] = obj.connection_retry_time
	if obj.neighbor_default_originate_cfg is not None:
		output['neighbor-default-originate-cfg'] = serialize_Neighbor__neighbor_str_cfg__neighbor_default_originate_cfg_json(obj.neighbor_default_originate_cfg)
	output['disallow-infinite-holdtime'] = obj.disallow_infinite_holdtime
	if obj.neighbor_distribute_list_cfg is not None:
		output['neighbor-distribute-list-cfg'] = serialize_list_Router_bgp_neighbor_neighbor_distribute_list_cfg_json(obj.neighbor_distribute_list_cfg)
	output['dont-capability-negotiate'] = obj.dont_capability_negotiate
	if obj.neighbor_ebgp_multihop_cfg is not None:
		output['neighbor-ebgp-multihop-cfg'] = serialize_list_Router_bgp_neighbor_neighbor_ebgp_multihop_cfg_json(obj.neighbor_ebgp_multihop_cfg)
	output['enforce-multihop'] = obj.enforce_multihop
	if obj.neighbor_filter_list_cfg is not None:
		output['neighbor-filter-list-cfg'] = serialize_list_Router_bgp_neighbor_neighbor_filter_list_cfg_json(obj.neighbor_filter_list_cfg)
	if obj.neighbor_maximum_prefix_cfg is not None:
		output['neighbor-maximum-prefix-cfg'] = serialize_Neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg_json(obj.neighbor_maximum_prefix_cfg)
	output['next-hop-self'] = obj.next_hop_self
	output['override-capability'] = obj.override_capability
	output['nbr-str-pass'] = serialize_Neighbor__neighbor_str_cfg__nbr_str_pass_json(obj.nbr_str_pass)
	output['passive'] = obj.passive
	if obj.neighbor_prefix_list_cfg is not None:
		output['neighbor-prefix-list-cfg'] = serialize_list_Router_bgp_neighbor_neighbor_prefix_list_cfg_json(obj.neighbor_prefix_list_cfg)
	output['remove-private-AS'] = obj.remove_private_as
	if obj.neighbor_route_map_cfg is not None:
		output['neighbor-route-map-cfg'] = serialize_list_Router_bgp_neighbor_neighbor_route_map_cfg_json(obj.neighbor_route_map_cfg)
	if obj.neighbor_send_community_cfg is not None:
		output['neighbor-send-community-cfg'] = serialize_Neighbor__neighbor_str_cfg__neighbor_send_community_cfg_json(obj.neighbor_send_community_cfg)
	if obj.neighbor_soft_reconfiguration_cfg is not None:
		output['neighbor-soft-reconfiguration-cfg'] = serialize_Neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg_json(obj.neighbor_soft_reconfiguration_cfg)
	output['shutdown'] = obj.shutdown
	output['strict-capability-match'] = obj.strict_capability_match
	output['timers'] = serialize_Neighbor__neighbor_str_cfg__timers_json(obj.timers)
	output['unsuppress-map'] = obj.unsuppress_map
	if obj.neighbor_update_source_cfg is not None:
		output['neighbor-update-source-cfg'] = serialize_Neighbor__neighbor_str_cfg__neighbor_update_source_cfg_json(obj.neighbor_update_source_cfg)
	if obj.neighbor_version_cfg is not None:
		output['neighbor-version-cfg'] = serialize_Neighbor__neighbor_str_cfg__neighbor_version_cfg_json(obj.neighbor_version_cfg)
	output['weight'] = obj.weight
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__allowas_in_cfg_json(obj):
	output = OrderedDict()
	output['allowas-in'] = obj.allowas_in
	if obj.allowas_in_count is not None:
		output['allowas-in-count'] = obj.allowas_in_count
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg_json(obj):
	output = OrderedDict()
	output['orf'] = obj.orf
	output['prefix-list'] = obj.prefix_list
	if obj.both is not None:
		output['both'] = obj.both
	output['receive'] = obj.receive
	output['send'] = obj.send
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__capability_1_json(obj):
	output = OrderedDict()
	output['dynamic'] = obj.dynamic
	if obj.orf_cfg is not None:
		output['orf-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg_json(obj.orf_cfg)
	output['route-refresh'] = obj.route_refresh
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__default_originate_cfg_json(obj):
	output = OrderedDict()
	output['default-originate'] = obj.default_originate
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Router_bgp_neighbor_distribute_list_cfg_json(obj):
	output = OrderedDict()
	if obj.distribute_list is not None:
		output['distribute-list'] = obj.distribute_list
	if obj.acl_val is not None:
		output['acl-val'] = obj.acl_val
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.out is not None:
		output['out'] = obj.out
	return output

def serialize_list_Router_bgp_neighbor_distribute_list_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_neighbor_distribute_list_cfg_json(item))
	return output

def serialize_Router_bgp_neighbor_ebgp_multihop_cfg_json(obj):
	output = OrderedDict()
	if obj.ebgp_multihop is not None:
		output['ebgp-multihop'] = obj.ebgp_multihop
	if obj.ebgp_multihop_hop_count is not None:
		output['ebgp-multihop-hop-count'] = obj.ebgp_multihop_hop_count
	return output

def serialize_list_Router_bgp_neighbor_ebgp_multihop_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_neighbor_ebgp_multihop_cfg_json(item))
	return output

def serialize_Router_bgp_neighbor_filter_list_cfg_json(obj):
	output = OrderedDict()
	if obj.filter_list is not None:
		output['filter-list'] = obj.filter_list
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.out is not None:
		output['out'] = obj.out
	return output

def serialize_list_Router_bgp_neighbor_filter_list_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_neighbor_filter_list_cfg_json(item))
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg_json(obj):
	output = OrderedDict()
	output['maximum-prefix'] = obj.maximum_prefix
	if obj.maximum_prefix_thres is not None:
		output['maximum-prefix-thres'] = obj.maximum_prefix_thres
	return output

def serialize_Router_bgp_neighbor_prefix_list_cfg_json(obj):
	output = OrderedDict()
	output['prefix-list'] = obj.prefix_list
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.out is not None:
		output['out'] = obj.out
	return output

def serialize_list_Router_bgp_neighbor_prefix_list_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_neighbor_prefix_list_cfg_json(item))
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass_json(obj):
	output = OrderedDict()
	output['nbr-ipv4-pass-value'] = obj.nbr_ipv4_pass_value
	output['nbr-ipv4-pass-encrypted'] = obj.nbr_ipv4_pass_encrypted
	return output

def serialize_Router_bgp_neighbor_route_map_cfg_json(obj):
	output = OrderedDict()
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.out is not None:
		output['out'] = obj.out
	return output

def serialize_list_Router_bgp_neighbor_route_map_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_neighbor_route_map_cfg_json(item))
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__send_community_cfg_json(obj):
	output = OrderedDict()
	output['send-community'] = obj.send_community
	if obj.both is not None:
		output['both'] = obj.both
	if obj.extended is not None:
		output['extended'] = obj.extended
	if obj.standard is not None:
		output['standard'] = obj.standard
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg_json(obj):
	output = OrderedDict()
	output['soft-reconfiguration'] = obj.soft_reconfiguration
	output['inbound'] = obj.inbound
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5_json(obj):
	output = OrderedDict()
	output['md5-value'] = obj.md5_value
	output['md5-encrypted'] = obj.md5_encrypted
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5_json(obj):
	output = OrderedDict()
	output['meticulous-md5-value'] = obj.meticulous_md5_value
	output['meticulous-md5-encrypted'] = obj.meticulous_md5_encrypted
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1_json(obj):
	output = OrderedDict()
	output['meticulous-sha1-value'] = obj.meticulous_sha1_value
	output['meticulous-sha1-encrypted'] = obj.meticulous_sha1_encrypted
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1_json(obj):
	output = OrderedDict()
	output['sha1-value'] = obj.sha1_value
	output['sha1-encrypted'] = obj.sha1_encrypted
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple_json(obj):
	output = OrderedDict()
	output['simple-value'] = obj.simple_value
	output['simple-encrypted'] = obj.simple_encrypted
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg_json(obj):
	output = OrderedDict()
	output['key-id'] = obj.key_id
	output['md5'] = serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5_json(obj.md5)
	output['meticulous-md5'] = serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5_json(obj.meticulous_md5)
	output['meticulous-sha1'] = serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1_json(obj.meticulous_sha1)
	output['sha1'] = serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1_json(obj.sha1)
	output['simple'] = serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple_json(obj.simple)
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication_json(obj):
	output = OrderedDict()
	if obj.key_id_cfg is not None:
		output['key-id-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg_json(obj.key_id_cfg)
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg_json(obj):
	output = OrderedDict()
	output['bfd'] = obj.bfd
	if obj.authentication is not None:
		output['authentication'] = serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication_json(obj.authentication)
	if obj.multihop is not None:
		output['multihop'] = obj.multihop
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg_json(obj):
	output = OrderedDict()
	output['fall-over'] = obj.fall_over
	if obj.bfd_cfg is not None:
		output['bfd-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg_json(obj.bfd_cfg)
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg_json(obj):
	output = OrderedDict()
	output['neighbor-ipv4-timers-keepalive'] = obj.neighbor_ipv4_timers_keepalive
	output['timers-holdtime'] = obj.timers_holdtime
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg_json(obj):
	output = OrderedDict()
	output['connect'] = obj.connect
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers_json(obj):
	output = OrderedDict()
	if obj.timers_keepalive_cfg is not None:
		output['timers-keepalive-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg_json(obj.timers_keepalive_cfg)
	if obj.timers_con_cfg is not None:
		output['timers-con-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg_json(obj.timers_con_cfg)
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__update_source_cfg_json(obj):
	output = OrderedDict()
	output['update-source'] = obj.update_source
	output['update-source-ip'] = obj.update_source_ip
	output['update-source-ipv6'] = obj.update_source_ipv6
	output['ethernet'] = obj.ethernet
	output['loopback'] = obj.loopback
	output['ve'] = obj.ve
	output['trunk'] = obj.trunk
	return output

def serialize_Neighbor__neighbor_ipv4_cfg__version_cfg_json(obj):
	output = OrderedDict()
	output['version'] = obj.version
	output['4'] = obj.param_4
	return output

def serialize_Neighbor__neighbor_ipv4_cfg_json(obj):
	output = OrderedDict()
	output['neighbor-ipv4'] = obj.neighbor_ipv4
	output['neighbor-ipv6'] = obj.neighbor_ipv6
	output['remote-as'] = obj.remote_as
	output['peer-group'] = obj.peer_group
	output['activate'] = obj.activate
	output['advertisement-interval'] = obj.advertisement_interval
	if obj.allowas_in_cfg is not None:
		output['allowas-in-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__allowas_in_cfg_json(obj.allowas_in_cfg)
	output['as-origination-interval'] = obj.as_origination_interval
	output['capability-1'] = serialize_Neighbor__neighbor_ipv4_cfg__capability_1_json(obj.capability_1)
	output['collide-established'] = obj.collide_established
	output['connection-retry-time'] = obj.connection_retry_time
	if obj.default_originate_cfg is not None:
		output['default-originate-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__default_originate_cfg_json(obj.default_originate_cfg)
	output['disallow-infinite-holdtime'] = obj.disallow_infinite_holdtime
	if obj.distribute_list_cfg is not None:
		output['distribute-list-cfg'] = serialize_list_Router_bgp_neighbor_distribute_list_cfg_json(obj.distribute_list_cfg)
	output['dont-capability-negotiate'] = obj.dont_capability_negotiate
	if obj.ebgp_multihop_cfg is not None:
		output['ebgp-multihop-cfg'] = serialize_list_Router_bgp_neighbor_ebgp_multihop_cfg_json(obj.ebgp_multihop_cfg)
	output['enforce-multihop'] = obj.enforce_multihop
	if obj.filter_list_cfg is not None:
		output['filter-list-cfg'] = serialize_list_Router_bgp_neighbor_filter_list_cfg_json(obj.filter_list_cfg)
	if obj.maximum_prefix_cfg is not None:
		output['maximum-prefix-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg_json(obj.maximum_prefix_cfg)
	output['next-hop-self'] = obj.next_hop_self
	output['override-capability'] = obj.override_capability
	output['passive'] = obj.passive
	if obj.prefix_list_cfg is not None:
		output['prefix-list-cfg'] = serialize_list_Router_bgp_neighbor_prefix_list_cfg_json(obj.prefix_list_cfg)
	output['remove-private-AS'] = obj.remove_private_as
	output['nbr-ipv4-pass'] = serialize_Neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass_json(obj.nbr_ipv4_pass)
	if obj.route_map_cfg is not None:
		output['route-map-cfg'] = serialize_list_Router_bgp_neighbor_route_map_cfg_json(obj.route_map_cfg)
	if obj.send_community_cfg is not None:
		output['send-community-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__send_community_cfg_json(obj.send_community_cfg)
	if obj.soft_reconfiguration_cfg is not None:
		output['soft-reconfiguration-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg_json(obj.soft_reconfiguration_cfg)
	output['shutdown'] = obj.shutdown
	if obj.fall_over_cfg is not None:
		output['fall-over-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__fall_over_cfg_json(obj.fall_over_cfg)
	output['strict-capability-match'] = obj.strict_capability_match
	output['neighbor-ipv4-timers'] = serialize_Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers_json(obj.neighbor_ipv4_timers)
	output['unsuppress-map'] = obj.unsuppress_map
	if obj.update_source_cfg is not None:
		output['update-source-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__update_source_cfg_json(obj.update_source_cfg)
	if obj.version_cfg is not None:
		output['version-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg__version_cfg_json(obj.version_cfg)
	output['weight'] = obj.weight
	return output

def serialize_Neighbor_json(obj):
	output = OrderedDict()
	output['neighbor-str-cfg'] = serialize_Neighbor__neighbor_str_cfg_json(obj.neighbor_str_cfg)
	if obj.neighbor_ipv4_cfg is not None:
		output['neighbor-ipv4-cfg'] = serialize_Neighbor__neighbor_ipv4_cfg_json(obj.neighbor_ipv4_cfg)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Neighbor_json(item))
	return list(container)

class Neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	allowas_in=PosRangedInteger(0, 1)
	allowas_in_count=PosRangedInteger(1, 10)
	def __init__(self, allowas_in, allowas_in_count=None):
		self.allowas_in = allowas_in
		self.allowas_in_count = allowas_in_count

	def __str__(self):
		return str(self.allowas_in)

class Neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	orf=PosRangedInteger(0, 1)
	prefix_list=PosRangedInteger(0, 1)
	both=PosRangedInteger(0, 1)
	receive=PosRangedInteger(0, 1)
	send=PosRangedInteger(0, 1)
	def __init__(self, orf, prefix_list, receive, send, both=None):
		self.orf = orf
		self.prefix_list = prefix_list
		self.both = both
		self.receive = receive
		self.send = send

	def __str__(self):
		return str(self.orf) + '+' + str(self.prefix_list) + '+' + str(self.receive) + '+' + str(self.send)

class Neighbor__neighbor_str_cfg__neighbor_capability(AxapiObject):
	__metaclass__ = StructMeta 
	dynamic=PosRangedInteger(0, 1)
	route_refresh=PosRangedInteger(0, 1)
	def __init__(self, dynamic, route_refresh, neighbor_orf_cfg=None):
		self.dynamic = dynamic
		self.neighbor_orf_cfg = neighbor_orf_cfg
		self.route_refresh = route_refresh

	def __str__(self):
		return str(self.dynamic) + '+' + str(self.route_refresh)

class Neighbor__neighbor_str_cfg__neighbor_default_originate_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	default_originate=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, default_originate, route_map=None):
		self.default_originate = default_originate
		self.route_map = route_map

	def __str__(self):
		return str(self.default_originate)

class Neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	maximum_prefix=PosRangedInteger(1, 65536)
	maximum_prefix_thres=PosRangedInteger(1, 100)
	def __init__(self, maximum_prefix, maximum_prefix_thres=None):
		self.maximum_prefix = maximum_prefix
		self.maximum_prefix_thres = maximum_prefix_thres

	def __str__(self):
		return str(self.maximum_prefix)

class Neighbor__neighbor_str_cfg__nbr_str_pass(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 80)
	encrypted=SizedString(1, 255)
	def __init__(self, value, encrypted):
		self.value = value
		self.encrypted = encrypted

	def __str__(self):
		return str(self.value) + '+' + str(self.encrypted)

class Neighbor__neighbor_str_cfg__neighbor_send_community_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	send_community=PosRangedInteger(0, 1)
	both=PosInteger()
	extended=PosRangedInteger(0, 1)
	standard=PosRangedInteger(0, 1)
	def __init__(self, send_community, both=None, extended=None, standard=None):
		self.send_community = send_community
		self.both = both
		self.extended = extended
		self.standard = standard

	def __str__(self):
		return str(self.send_community)

class Neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	soft_reconfiguration=PosRangedInteger(0, 1)
	inbound=PosRangedInteger(0, 1)
	def __init__(self, soft_reconfiguration, inbound):
		self.soft_reconfiguration = soft_reconfiguration
		self.inbound = inbound

	def __str__(self):
		return str(self.soft_reconfiguration) + '+' + str(self.inbound)

class Neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	timers_keepalive=PosRangedInteger(0, 65535)
	timers_holdtime=PosRangedInteger(0, 65535)
	def __init__(self, timers_keepalive, timers_holdtime):
		self.timers_keepalive = timers_keepalive
		self.timers_holdtime = timers_holdtime

	def __str__(self):
		return str(self.timers_keepalive) + '+' + str(self.timers_holdtime)

class Neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	connect=PosRangedInteger(1, 65535)
	def __init__(self, connect):
		self.connect = connect

	def __str__(self):
		return str(self.connect)

class Neighbor__neighbor_str_cfg__timers(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, neighbor_timers_keepalive_cfg=None, timers_con_under_group_cfg=None):
		self.neighbor_timers_keepalive_cfg = neighbor_timers_keepalive_cfg
		self.timers_con_under_group_cfg = timers_con_under_group_cfg

	def __str__(self):
		return ""

class Neighbor__neighbor_str_cfg__neighbor_update_source_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	update_source=PosRangedInteger(0, 1)
	update_source_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	update_source_ipv6=SizedString(1, 255)
	ethernet=PosRangedInteger(1, 2048)
	loopback=PosRangedInteger(1, 2048)
	ve=PosRangedInteger(1, 2048)
	trunk=PosRangedInteger(1, 2048)
	def __init__(self, update_source, update_source_ip, update_source_ipv6, ethernet, loopback, ve, trunk):
		self.update_source = update_source
		self.update_source_ip = update_source_ip
		self.update_source_ipv6 = update_source_ipv6
		self.ethernet = ethernet
		self.loopback = loopback
		self.ve = ve
		self.trunk = trunk

	def __str__(self):
		return str(self.update_source) + '+' + str(self.update_source_ip) + '+' + str(self.update_source_ipv6) + '+' + str(self.ethernet) + '+' + str(self.loopback) + '+' + str(self.ve) + '+' + str(self.trunk)

class Neighbor__neighbor_str_cfg__neighbor_version_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	version=PosRangedInteger(0, 1)
	param_4=PosRangedInteger(0, 1)
	def __init__(self, version, param_4):
		self.version = version
		self.param_4 = param_4

	def __str__(self):
		return str(self.version) + '+' + str(self.param_4)

class Neighbor__neighbor_str_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	neighbor_str=SizedString(1, 255)
	peer_group=SizedString(1, 255)
	remote_as=PosRangedInteger(1, 4294967295)
	activate=PosRangedInteger(0, 1)
	advertisement_interval=PosRangedInteger(1, 600)
	as_origination_interval=PosRangedInteger(1, 600)
	collide_established=PosRangedInteger(0, 1)
	connection_retry_time=PosRangedInteger(1, 65535)
	disallow_infinite_holdtime=PosRangedInteger(0, 1)
	dont_capability_negotiate=PosRangedInteger(0, 1)
	enforce_multihop=PosRangedInteger(0, 1)
	next_hop_self=PosRangedInteger(0, 1)
	override_capability=PosRangedInteger(0, 1)
	passive=PosRangedInteger(0, 1)
	remove_private_as=PosRangedInteger(0, 1)
	shutdown=PosRangedInteger(0, 1)
	strict_capability_match=PosRangedInteger(0, 1)
	unsuppress_map=SizedString(1, 255)
	weight=PosRangedInteger(0, 65535)
	def __init__(self, neighbor_str, peer_group, remote_as, activate, advertisement_interval, as_origination_interval, neighbor_capability, collide_established, connection_retry_time, disallow_infinite_holdtime, dont_capability_negotiate, enforce_multihop, next_hop_self, override_capability, nbr_str_pass, passive, remove_private_as, shutdown, strict_capability_match, timers, unsuppress_map, weight, neighbor_allowas_in_cfg=None, neighbor_default_originate_cfg=None, neighbor_distribute_list_cfg=None, neighbor_ebgp_multihop_cfg=None, neighbor_filter_list_cfg=None, neighbor_maximum_prefix_cfg=None, neighbor_prefix_list_cfg=None, neighbor_route_map_cfg=None, neighbor_send_community_cfg=None, neighbor_soft_reconfiguration_cfg=None, neighbor_update_source_cfg=None, neighbor_version_cfg=None):
		self.neighbor_str = neighbor_str
		self.peer_group = peer_group
		self.remote_as = remote_as
		self.activate = activate
		self.advertisement_interval = advertisement_interval
		self.neighbor_allowas_in_cfg = neighbor_allowas_in_cfg
		self.as_origination_interval = as_origination_interval
		self.neighbor_capability = neighbor_capability
		self.collide_established = collide_established
		self.connection_retry_time = connection_retry_time
		self.neighbor_default_originate_cfg = neighbor_default_originate_cfg
		self.disallow_infinite_holdtime = disallow_infinite_holdtime
		self.neighbor_distribute_list_cfg = neighbor_distribute_list_cfg
		self.dont_capability_negotiate = dont_capability_negotiate
		self.neighbor_ebgp_multihop_cfg = neighbor_ebgp_multihop_cfg
		self.enforce_multihop = enforce_multihop
		self.neighbor_filter_list_cfg = neighbor_filter_list_cfg
		self.neighbor_maximum_prefix_cfg = neighbor_maximum_prefix_cfg
		self.next_hop_self = next_hop_self
		self.override_capability = override_capability
		self.nbr_str_pass = nbr_str_pass
		self.passive = passive
		self.neighbor_prefix_list_cfg = neighbor_prefix_list_cfg
		self.remove_private_as = remove_private_as
		self.neighbor_route_map_cfg = neighbor_route_map_cfg
		self.neighbor_send_community_cfg = neighbor_send_community_cfg
		self.neighbor_soft_reconfiguration_cfg = neighbor_soft_reconfiguration_cfg
		self.shutdown = shutdown
		self.strict_capability_match = strict_capability_match
		self.timers = timers
		self.unsuppress_map = unsuppress_map
		self.neighbor_update_source_cfg = neighbor_update_source_cfg
		self.neighbor_version_cfg = neighbor_version_cfg
		self.weight = weight

	def __str__(self):
		return str(self.neighbor_str) + '+' + str(self.peer_group) + '+' + str(self.remote_as) + '+' + str(self.activate) + '+' + str(self.advertisement_interval) + '+' + str(self.as_origination_interval) + '+' + str(self.neighbor_capability) + '+' + str(self.collide_established) + '+' + str(self.connection_retry_time) + '+' + str(self.disallow_infinite_holdtime) + '+' + str(self.dont_capability_negotiate) + '+' + str(self.enforce_multihop) + '+' + str(self.next_hop_self) + '+' + str(self.override_capability) + '+' + str(self.nbr_str_pass) + '+' + str(self.passive) + '+' + str(self.remove_private_as) + '+' + str(self.shutdown) + '+' + str(self.strict_capability_match) + '+' + str(self.timers) + '+' + str(self.unsuppress_map) + '+' + str(self.weight)

class Neighbor__neighbor_ipv4_cfg__allowas_in_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	allowas_in=PosInteger()
	allowas_in_count=PosRangedInteger(1, 10)
	def __init__(self, allowas_in, allowas_in_count=None):
		self.allowas_in = allowas_in
		self.allowas_in_count = allowas_in_count

	def __str__(self):
		return str(self.allowas_in)

class Neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	orf=PosInteger()
	prefix_list=PosInteger()
	both=PosInteger()
	receive=PosInteger()
	send=PosInteger()
	def __init__(self, orf, prefix_list, receive, send, both=None):
		self.orf = orf
		self.prefix_list = prefix_list
		self.both = both
		self.receive = receive
		self.send = send

	def __str__(self):
		return str(self.orf) + '+' + str(self.prefix_list) + '+' + str(self.receive) + '+' + str(self.send)

class Neighbor__neighbor_ipv4_cfg__capability_1(AxapiObject):
	__metaclass__ = StructMeta 
	dynamic=PosInteger()
	route_refresh=PosInteger()
	def __init__(self, dynamic, route_refresh, orf_cfg=None):
		self.dynamic = dynamic
		self.orf_cfg = orf_cfg
		self.route_refresh = route_refresh

	def __str__(self):
		return str(self.dynamic) + '+' + str(self.route_refresh)

class Neighbor__neighbor_ipv4_cfg__default_originate_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	default_originate=PosInteger()
	route_map=SizedString(1, 255)
	def __init__(self, default_originate, route_map=None):
		self.default_originate = default_originate
		self.route_map = route_map

	def __str__(self):
		return str(self.default_originate)

class Neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	maximum_prefix=PosRangedInteger(1, 65536)
	maximum_prefix_thres=PosRangedInteger(1, 100)
	def __init__(self, maximum_prefix, maximum_prefix_thres=None):
		self.maximum_prefix = maximum_prefix
		self.maximum_prefix_thres = maximum_prefix_thres

	def __str__(self):
		return str(self.maximum_prefix)

class Neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass(AxapiObject):
	__metaclass__ = StructMeta 
	nbr_ipv4_pass_value=SizedString(1, 80)
	nbr_ipv4_pass_encrypted=SizedString(1, 255)
	def __init__(self, nbr_ipv4_pass_value, nbr_ipv4_pass_encrypted):
		self.nbr_ipv4_pass_value = nbr_ipv4_pass_value
		self.nbr_ipv4_pass_encrypted = nbr_ipv4_pass_encrypted

	def __str__(self):
		return str(self.nbr_ipv4_pass_value) + '+' + str(self.nbr_ipv4_pass_encrypted)

class Neighbor__neighbor_ipv4_cfg__send_community_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	send_community=PosInteger()
	both=PosInteger()
	extended=PosInteger()
	standard=PosInteger()
	def __init__(self, send_community, both=None, extended=None, standard=None):
		self.send_community = send_community
		self.both = both
		self.extended = extended
		self.standard = standard

	def __str__(self):
		return str(self.send_community)

class Neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	soft_reconfiguration=PosInteger()
	inbound=PosInteger()
	def __init__(self, soft_reconfiguration, inbound):
		self.soft_reconfiguration = soft_reconfiguration
		self.inbound = inbound

	def __str__(self):
		return str(self.soft_reconfiguration) + '+' + str(self.inbound)

class Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5(AxapiObject):
	__metaclass__ = StructMeta 
	md5_value=SizedString(1, 255)
	md5_encrypted=SizedString(1, 255)
	def __init__(self, md5_value, md5_encrypted):
		self.md5_value = md5_value
		self.md5_encrypted = md5_encrypted

	def __str__(self):
		return str(self.md5_value) + '+' + str(self.md5_encrypted)

class Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5(AxapiObject):
	__metaclass__ = StructMeta 
	meticulous_md5_value=SizedString(1, 255)
	meticulous_md5_encrypted=SizedString(1, 255)
	def __init__(self, meticulous_md5_value, meticulous_md5_encrypted):
		self.meticulous_md5_value = meticulous_md5_value
		self.meticulous_md5_encrypted = meticulous_md5_encrypted

	def __str__(self):
		return str(self.meticulous_md5_value) + '+' + str(self.meticulous_md5_encrypted)

class Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1(AxapiObject):
	__metaclass__ = StructMeta 
	meticulous_sha1_value=SizedString(1, 255)
	meticulous_sha1_encrypted=SizedString(1, 255)
	def __init__(self, meticulous_sha1_value, meticulous_sha1_encrypted):
		self.meticulous_sha1_value = meticulous_sha1_value
		self.meticulous_sha1_encrypted = meticulous_sha1_encrypted

	def __str__(self):
		return str(self.meticulous_sha1_value) + '+' + str(self.meticulous_sha1_encrypted)

class Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1(AxapiObject):
	__metaclass__ = StructMeta 
	sha1_value=SizedString(1, 255)
	sha1_encrypted=SizedString(1, 255)
	def __init__(self, sha1_value, sha1_encrypted):
		self.sha1_value = sha1_value
		self.sha1_encrypted = sha1_encrypted

	def __str__(self):
		return str(self.sha1_value) + '+' + str(self.sha1_encrypted)

class Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple(AxapiObject):
	__metaclass__ = StructMeta 
	simple_value=SizedString(1, 255)
	simple_encrypted=SizedString(1, 255)
	def __init__(self, simple_value, simple_encrypted):
		self.simple_value = simple_value
		self.simple_encrypted = simple_encrypted

	def __str__(self):
		return str(self.simple_value) + '+' + str(self.simple_encrypted)

class Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	key_id=PosRangedInteger(0, 255)
	def __init__(self, key_id, md5, meticulous_md5, meticulous_sha1, sha1, simple):
		self.key_id = key_id
		self.md5 = md5
		self.meticulous_md5 = meticulous_md5
		self.meticulous_sha1 = meticulous_sha1
		self.sha1 = sha1
		self.simple = simple

	def __str__(self):
		return str(self.key_id) + '+' + str(self.md5) + '+' + str(self.meticulous_md5) + '+' + str(self.meticulous_sha1) + '+' + str(self.sha1) + '+' + str(self.simple)

class Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, key_id_cfg=None):
		self.key_id_cfg = key_id_cfg

	def __str__(self):
		return ""

class Neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	bfd=PosRangedInteger(0, 1)
	multihop=PosRangedInteger(0, 1)
	def __init__(self, bfd, authentication=None, multihop=None):
		self.bfd = bfd
		self.authentication = authentication
		self.multihop = multihop

	def __str__(self):
		return str(self.bfd)

class Neighbor__neighbor_ipv4_cfg__fall_over_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	fall_over=PosRangedInteger(0, 1)
	def __init__(self, fall_over, bfd_cfg=None):
		self.fall_over = fall_over
		self.bfd_cfg = bfd_cfg

	def __str__(self):
		return str(self.fall_over)

class Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	neighbor_ipv4_timers_keepalive=PosRangedInteger(0, 65535)
	timers_holdtime=PosRangedInteger(0, 65535)
	def __init__(self, neighbor_ipv4_timers_keepalive, timers_holdtime):
		self.neighbor_ipv4_timers_keepalive = neighbor_ipv4_timers_keepalive
		self.timers_holdtime = timers_holdtime

	def __str__(self):
		return str(self.neighbor_ipv4_timers_keepalive) + '+' + str(self.timers_holdtime)

class Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	connect=PosRangedInteger(1, 65535)
	def __init__(self, connect):
		self.connect = connect

	def __str__(self):
		return str(self.connect)

class Neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, timers_keepalive_cfg=None, timers_con_cfg=None):
		self.timers_keepalive_cfg = timers_keepalive_cfg
		self.timers_con_cfg = timers_con_cfg

	def __str__(self):
		return ""

class Neighbor__neighbor_ipv4_cfg__update_source_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	update_source=PosInteger()
	update_source_ip=SizedString(1, 255)
	update_source_ipv6=SizedString(1, 255)
	ethernet=PosInteger()
	loopback=PosInteger()
	ve=PosInteger()
	trunk=PosInteger()
	def __init__(self, update_source, update_source_ip, update_source_ipv6, ethernet, loopback, ve, trunk):
		self.update_source = update_source
		self.update_source_ip = update_source_ip
		self.update_source_ipv6 = update_source_ipv6
		self.ethernet = ethernet
		self.loopback = loopback
		self.ve = ve
		self.trunk = trunk

	def __str__(self):
		return str(self.update_source) + '+' + str(self.update_source_ip) + '+' + str(self.update_source_ipv6) + '+' + str(self.ethernet) + '+' + str(self.loopback) + '+' + str(self.ve) + '+' + str(self.trunk)

class Neighbor__neighbor_ipv4_cfg__version_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	version=PosInteger()
	param_4=PosInteger()
	def __init__(self, version, param_4):
		self.version = version
		self.param_4 = param_4

	def __str__(self):
		return str(self.version) + '+' + str(self.param_4)

class Neighbor__neighbor_ipv4_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	neighbor_ipv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	neighbor_ipv6=SizedString(1, 255)
	remote_as=PosRangedInteger(1, 4294967295)
	peer_group=SizedString(1, 255)
	activate=PosInteger()
	advertisement_interval=PosRangedInteger(1, 600)
	as_origination_interval=PosRangedInteger(1, 600)
	collide_established=PosInteger()
	connection_retry_time=PosRangedInteger(1, 65535)
	disallow_infinite_holdtime=PosInteger()
	dont_capability_negotiate=PosInteger()
	enforce_multihop=PosInteger()
	next_hop_self=PosInteger()
	override_capability=PosInteger()
	passive=PosInteger()
	remove_private_as=PosInteger()
	shutdown=PosInteger()
	strict_capability_match=PosInteger()
	unsuppress_map=SizedString(1, 255)
	weight=PosRangedInteger(0, 65535)
	def __init__(self, neighbor_ipv4, neighbor_ipv6, remote_as, peer_group, activate, advertisement_interval, as_origination_interval, capability_1, collide_established, connection_retry_time, disallow_infinite_holdtime, dont_capability_negotiate, enforce_multihop, next_hop_self, override_capability, passive, remove_private_as, nbr_ipv4_pass, shutdown, strict_capability_match, neighbor_ipv4_timers, unsuppress_map, weight, allowas_in_cfg=None, default_originate_cfg=None, distribute_list_cfg=None, ebgp_multihop_cfg=None, filter_list_cfg=None, maximum_prefix_cfg=None, prefix_list_cfg=None, route_map_cfg=None, send_community_cfg=None, soft_reconfiguration_cfg=None, fall_over_cfg=None, update_source_cfg=None, version_cfg=None):
		self.neighbor_ipv4 = neighbor_ipv4
		self.neighbor_ipv6 = neighbor_ipv6
		self.remote_as = remote_as
		self.peer_group = peer_group
		self.activate = activate
		self.advertisement_interval = advertisement_interval
		self.allowas_in_cfg = allowas_in_cfg
		self.as_origination_interval = as_origination_interval
		self.capability_1 = capability_1
		self.collide_established = collide_established
		self.connection_retry_time = connection_retry_time
		self.default_originate_cfg = default_originate_cfg
		self.disallow_infinite_holdtime = disallow_infinite_holdtime
		self.distribute_list_cfg = distribute_list_cfg
		self.dont_capability_negotiate = dont_capability_negotiate
		self.ebgp_multihop_cfg = ebgp_multihop_cfg
		self.enforce_multihop = enforce_multihop
		self.filter_list_cfg = filter_list_cfg
		self.maximum_prefix_cfg = maximum_prefix_cfg
		self.next_hop_self = next_hop_self
		self.override_capability = override_capability
		self.passive = passive
		self.prefix_list_cfg = prefix_list_cfg
		self.remove_private_as = remove_private_as
		self.nbr_ipv4_pass = nbr_ipv4_pass
		self.route_map_cfg = route_map_cfg
		self.send_community_cfg = send_community_cfg
		self.soft_reconfiguration_cfg = soft_reconfiguration_cfg
		self.shutdown = shutdown
		self.fall_over_cfg = fall_over_cfg
		self.strict_capability_match = strict_capability_match
		self.neighbor_ipv4_timers = neighbor_ipv4_timers
		self.unsuppress_map = unsuppress_map
		self.update_source_cfg = update_source_cfg
		self.version_cfg = version_cfg
		self.weight = weight

	def __str__(self):
		return str(self.neighbor_ipv4) + '+' + str(self.neighbor_ipv6) + '+' + str(self.remote_as) + '+' + str(self.peer_group) + '+' + str(self.activate) + '+' + str(self.advertisement_interval) + '+' + str(self.as_origination_interval) + '+' + str(self.capability_1) + '+' + str(self.collide_established) + '+' + str(self.connection_retry_time) + '+' + str(self.disallow_infinite_holdtime) + '+' + str(self.dont_capability_negotiate) + '+' + str(self.enforce_multihop) + '+' + str(self.next_hop_self) + '+' + str(self.override_capability) + '+' + str(self.passive) + '+' + str(self.remove_private_as) + '+' + str(self.nbr_ipv4_pass) + '+' + str(self.shutdown) + '+' + str(self.strict_capability_match) + '+' + str(self.neighbor_ipv4_timers) + '+' + str(self.unsuppress_map) + '+' + str(self.weight)

class Neighbor(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, neighbor_str_cfg, neighbor_ipv4_cfg=None):
		self.neighbor_str_cfg = neighbor_str_cfg
		self.neighbor_ipv4_cfg = neighbor_ipv4_cfg

	def __str__(self):
		return str(self.neighbor_str_cfg)

class Router_bgp_neighbor_neighbor_distribute_list_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	distribute_list=PosRangedInteger(0, 1)
	acl_val=SizedString(1, 255)
	py_kw_rsvd_in=PosRangedInteger(0, 1)
	out=PosRangedInteger(0, 1)
	def __init__(self, distribute_list=None, acl_val=None, py_kw_rsvd_in=None, out=None):
		self.distribute_list = distribute_list
		self.acl_val = acl_val
		self.py_kw_rsvd_in = py_kw_rsvd_in
		self.out = out

	def __str__(self):
		return ""

class Router_bgp_neighbor_neighbor_ebgp_multihop_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ebgp_multihop=PosRangedInteger(0, 1)
	ebgp_multihop_hop_count=PosRangedInteger(1, 255)
	def __init__(self, ebgp_multihop=None, ebgp_multihop_hop_count=None):
		self.ebgp_multihop = ebgp_multihop
		self.ebgp_multihop_hop_count = ebgp_multihop_hop_count

	def __str__(self):
		return ""

class Router_bgp_neighbor_neighbor_filter_list_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	filter_list=SizedString(1, 255)
	py_kw_rsvd_in=PosInteger()
	out=PosInteger()
	def __init__(self, filter_list=None, py_kw_rsvd_in=None, out=None):
		self.filter_list = filter_list
		self.py_kw_rsvd_in = py_kw_rsvd_in
		self.out = out

	def __str__(self):
		return ""

class Router_bgp_neighbor_neighbor_prefix_list_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	prefix_list=PosInteger()
	py_kw_rsvd_in=PosInteger()
	out=PosInteger()
	def __init__(self, prefix_list, py_kw_rsvd_in=None, out=None):
		self.prefix_list = prefix_list
		self.py_kw_rsvd_in = py_kw_rsvd_in
		self.out = out

	def __str__(self):
		return str(self.prefix_list)

class Router_bgp_neighbor_neighbor_route_map_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	route_map=SizedString(1, 255)
	py_kw_rsvd_in=PosInteger()
	out=PosInteger()
	def __init__(self, route_map=None, py_kw_rsvd_in=None, out=None):
		self.route_map = route_map
		self.py_kw_rsvd_in = py_kw_rsvd_in
		self.out = out

	def __str__(self):
		return ""

class Router_bgp_neighbor_distribute_list_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	distribute_list=PosInteger()
	acl_val=SizedString(1, 255)
	py_kw_rsvd_in=PosInteger()
	out=PosInteger()
	def __init__(self, distribute_list=None, acl_val=None, py_kw_rsvd_in=None, out=None):
		self.distribute_list = distribute_list
		self.acl_val = acl_val
		self.py_kw_rsvd_in = py_kw_rsvd_in
		self.out = out

	def __str__(self):
		return ""

class Router_bgp_neighbor_ebgp_multihop_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ebgp_multihop=PosInteger()
	ebgp_multihop_hop_count=PosRangedInteger(1, 255)
	def __init__(self, ebgp_multihop=None, ebgp_multihop_hop_count=None):
		self.ebgp_multihop = ebgp_multihop
		self.ebgp_multihop_hop_count = ebgp_multihop_hop_count

	def __str__(self):
		return ""

class Router_bgp_neighbor_filter_list_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	filter_list=SizedString(1, 255)
	py_kw_rsvd_in=PosInteger()
	out=PosInteger()
	def __init__(self, filter_list=None, py_kw_rsvd_in=None, out=None):
		self.filter_list = filter_list
		self.py_kw_rsvd_in = py_kw_rsvd_in
		self.out = out

	def __str__(self):
		return ""

class Router_bgp_neighbor_prefix_list_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	prefix_list=PosInteger()
	py_kw_rsvd_in=PosInteger()
	out=PosInteger()
	def __init__(self, prefix_list, py_kw_rsvd_in=None, out=None):
		self.prefix_list = prefix_list
		self.py_kw_rsvd_in = py_kw_rsvd_in
		self.out = out

	def __str__(self):
		return str(self.prefix_list)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__neighbor_allowas_in_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	allowas_in=PosRangedInteger(0, 1)
	allowas_in_count=PosRangedInteger(1, 10)
	def __init__(self, allowas_in, allowas_in_count=None):
		self.allowas_in = allowas_in
		self.allowas_in_count = allowas_in_count

	def __str__(self):
		return str(self.allowas_in)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	orf=PosRangedInteger(0, 1)
	prefix_list=PosRangedInteger(0, 1)
	both=PosRangedInteger(0, 1)
	receive=PosRangedInteger(0, 1)
	send=PosRangedInteger(0, 1)
	def __init__(self, orf, prefix_list, receive, send, both=None):
		self.orf = orf
		self.prefix_list = prefix_list
		self.both = both
		self.receive = receive
		self.send = send

	def __str__(self):
		return str(self.orf) + '+' + str(self.prefix_list) + '+' + str(self.receive) + '+' + str(self.send)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__neighbor_capability(AxapiObject):
	__metaclass__ = StructMeta 
	dynamic=PosRangedInteger(0, 1)
	route_refresh=PosRangedInteger(0, 1)
	def __init__(self, dynamic, route_refresh, neighbor_orf_cfg=None):
		self.dynamic = dynamic
		self.neighbor_orf_cfg = neighbor_orf_cfg
		self.route_refresh = route_refresh

	def __str__(self):
		return str(self.dynamic) + '+' + str(self.route_refresh)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__neighbor_default_originate_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	default_originate=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, default_originate, route_map=None):
		self.default_originate = default_originate
		self.route_map = route_map

	def __str__(self):
		return str(self.default_originate)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__neighbor_maximum_prefix_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	maximum_prefix=PosRangedInteger(1, 65536)
	maximum_prefix_thres=PosRangedInteger(1, 100)
	def __init__(self, maximum_prefix, maximum_prefix_thres=None):
		self.maximum_prefix = maximum_prefix
		self.maximum_prefix_thres = maximum_prefix_thres

	def __str__(self):
		return str(self.maximum_prefix)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__nbr_str_pass(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 80)
	encrypted=SizedString(1, 255)
	def __init__(self, value, encrypted):
		self.value = value
		self.encrypted = encrypted

	def __str__(self):
		return str(self.value) + '+' + str(self.encrypted)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__neighbor_send_community_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	send_community=PosRangedInteger(0, 1)
	both=PosInteger()
	extended=PosRangedInteger(0, 1)
	standard=PosRangedInteger(0, 1)
	def __init__(self, send_community, both=None, extended=None, standard=None):
		self.send_community = send_community
		self.both = both
		self.extended = extended
		self.standard = standard

	def __str__(self):
		return str(self.send_community)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	soft_reconfiguration=PosRangedInteger(0, 1)
	inbound=PosRangedInteger(0, 1)
	def __init__(self, soft_reconfiguration, inbound):
		self.soft_reconfiguration = soft_reconfiguration
		self.inbound = inbound

	def __str__(self):
		return str(self.soft_reconfiguration) + '+' + str(self.inbound)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	timers_keepalive=PosRangedInteger(0, 65535)
	timers_holdtime=PosRangedInteger(0, 65535)
	def __init__(self, timers_keepalive, timers_holdtime):
		self.timers_keepalive = timers_keepalive
		self.timers_holdtime = timers_holdtime

	def __str__(self):
		return str(self.timers_keepalive) + '+' + str(self.timers_holdtime)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__timers__timers_con_under_group_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	connect=PosRangedInteger(1, 65535)
	def __init__(self, connect):
		self.connect = connect

	def __str__(self):
		return str(self.connect)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__timers(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, neighbor_timers_keepalive_cfg=None, timers_con_under_group_cfg=None):
		self.neighbor_timers_keepalive_cfg = neighbor_timers_keepalive_cfg
		self.timers_con_under_group_cfg = timers_con_under_group_cfg

	def __str__(self):
		return ""

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__neighbor_update_source_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	update_source=PosRangedInteger(0, 1)
	update_source_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	update_source_ipv6=SizedString(1, 255)
	ethernet=PosRangedInteger(1, 2048)
	loopback=PosRangedInteger(1, 2048)
	ve=PosRangedInteger(1, 2048)
	trunk=PosRangedInteger(1, 2048)
	def __init__(self, update_source, update_source_ip, update_source_ipv6, ethernet, loopback, ve, trunk):
		self.update_source = update_source
		self.update_source_ip = update_source_ip
		self.update_source_ipv6 = update_source_ipv6
		self.ethernet = ethernet
		self.loopback = loopback
		self.ve = ve
		self.trunk = trunk

	def __str__(self):
		return str(self.update_source) + '+' + str(self.update_source_ip) + '+' + str(self.update_source_ipv6) + '+' + str(self.ethernet) + '+' + str(self.loopback) + '+' + str(self.ve) + '+' + str(self.trunk)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg__neighbor_version_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	version=PosRangedInteger(0, 1)
	param_4=PosRangedInteger(0, 1)
	def __init__(self, version, param_4):
		self.version = version
		self.param_4 = param_4

	def __str__(self):
		return str(self.version) + '+' + str(self.param_4)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6__neighbor_str_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	neighbor_str=SizedString(1, 255)
	peer_group=SizedString(1, 255)
	remote_as=PosRangedInteger(1, 4294967295)
	activate=PosRangedInteger(0, 1)
	advertisement_interval=PosRangedInteger(1, 600)
	as_origination_interval=PosRangedInteger(1, 600)
	collide_established=PosRangedInteger(0, 1)
	connection_retry_time=PosRangedInteger(1, 65535)
	disallow_infinite_holdtime=PosRangedInteger(0, 1)
	dont_capability_negotiate=PosRangedInteger(0, 1)
	enforce_multihop=PosRangedInteger(0, 1)
	next_hop_self=PosRangedInteger(0, 1)
	override_capability=PosRangedInteger(0, 1)
	passive=PosRangedInteger(0, 1)
	remove_private_as=PosRangedInteger(0, 1)
	shutdown=PosRangedInteger(0, 1)
	strict_capability_match=PosRangedInteger(0, 1)
	unsuppress_map=SizedString(1, 255)
	weight=PosRangedInteger(0, 65535)
	def __init__(self, neighbor_str, peer_group, remote_as, activate, advertisement_interval, as_origination_interval, neighbor_capability, collide_established, connection_retry_time, disallow_infinite_holdtime, dont_capability_negotiate, enforce_multihop, next_hop_self, override_capability, nbr_str_pass, passive, remove_private_as, shutdown, strict_capability_match, timers, unsuppress_map, weight, neighbor_allowas_in_cfg=None, neighbor_default_originate_cfg=None, neighbor_distribute_list_cfg=None, neighbor_ebgp_multihop_cfg=None, neighbor_filter_list_cfg=None, neighbor_maximum_prefix_cfg=None, neighbor_prefix_list_cfg=None, neighbor_route_map_cfg=None, neighbor_send_community_cfg=None, neighbor_soft_reconfiguration_cfg=None, neighbor_update_source_cfg=None, neighbor_version_cfg=None):
		self.neighbor_str = neighbor_str
		self.peer_group = peer_group
		self.remote_as = remote_as
		self.activate = activate
		self.advertisement_interval = advertisement_interval
		self.neighbor_allowas_in_cfg = neighbor_allowas_in_cfg
		self.as_origination_interval = as_origination_interval
		self.neighbor_capability = neighbor_capability
		self.collide_established = collide_established
		self.connection_retry_time = connection_retry_time
		self.neighbor_default_originate_cfg = neighbor_default_originate_cfg
		self.disallow_infinite_holdtime = disallow_infinite_holdtime
		self.neighbor_distribute_list_cfg = neighbor_distribute_list_cfg
		self.dont_capability_negotiate = dont_capability_negotiate
		self.neighbor_ebgp_multihop_cfg = neighbor_ebgp_multihop_cfg
		self.enforce_multihop = enforce_multihop
		self.neighbor_filter_list_cfg = neighbor_filter_list_cfg
		self.neighbor_maximum_prefix_cfg = neighbor_maximum_prefix_cfg
		self.next_hop_self = next_hop_self
		self.override_capability = override_capability
		self.nbr_str_pass = nbr_str_pass
		self.passive = passive
		self.neighbor_prefix_list_cfg = neighbor_prefix_list_cfg
		self.remove_private_as = remove_private_as
		self.neighbor_route_map_cfg = neighbor_route_map_cfg
		self.neighbor_send_community_cfg = neighbor_send_community_cfg
		self.neighbor_soft_reconfiguration_cfg = neighbor_soft_reconfiguration_cfg
		self.shutdown = shutdown
		self.strict_capability_match = strict_capability_match
		self.timers = timers
		self.unsuppress_map = unsuppress_map
		self.neighbor_update_source_cfg = neighbor_update_source_cfg
		self.neighbor_version_cfg = neighbor_version_cfg
		self.weight = weight

	def __str__(self):
		return str(self.neighbor_str) + '+' + str(self.peer_group) + '+' + str(self.remote_as) + '+' + str(self.activate) + '+' + str(self.advertisement_interval) + '+' + str(self.as_origination_interval) + '+' + str(self.neighbor_capability) + '+' + str(self.collide_established) + '+' + str(self.connection_retry_time) + '+' + str(self.disallow_infinite_holdtime) + '+' + str(self.dont_capability_negotiate) + '+' + str(self.enforce_multihop) + '+' + str(self.next_hop_self) + '+' + str(self.override_capability) + '+' + str(self.nbr_str_pass) + '+' + str(self.passive) + '+' + str(self.remove_private_as) + '+' + str(self.shutdown) + '+' + str(self.strict_capability_match) + '+' + str(self.timers) + '+' + str(self.unsuppress_map) + '+' + str(self.weight)

class Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, neighbor_str_cfg):
		self.neighbor_str_cfg = neighbor_str_cfg

	def __str__(self):
		return str(self.neighbor_str_cfg)

class Router_bgp_neighbor_route_map_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	route_map=SizedString(1, 255)
	py_kw_rsvd_in=PosInteger()
	out=PosInteger()
	def __init__(self, route_map=None, py_kw_rsvd_in=None, out=None):
		self.route_map = route_map
		self.py_kw_rsvd_in = py_kw_rsvd_in
		self.out = out

	def __str__(self):
		return ""

class RouterBgpNeighborClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRouterBgpNeighbor(self, neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6):
		"""
		Retrieve the neighbor identified by the specified identifier
		
		Args:
			neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6 Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6
		
		Returns:
			An instance of the Neighbor class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified neighbor does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('neighbor')
		return deserialize_Neighbor_json(payload)

	def putRouterBgpNeighbor(self, neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6, neighbor):
		"""
		Replace the object neighbor
		
		Args:
			neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6 Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6
			neighbor An instance of the Neighbor class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['neighbor']=serialize_Neighbor_json(neighbor)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6) .replace("/", "%2f") + query, payload, headers)
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

	def deleteRouterBgpNeighbor(self, neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6):
		"""
		Remove the neighbor identified by the specified identifier from the system
		
		Args:
			neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6 Neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(neighbor_neighbor_str_cfg_neighbor_str_neighbor_ipv4_neighbor_ipv6) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified neighbor does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllRouterBgpNeighborsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitRouterBgpNeighbor(self, neighbor):
		"""
		Create the object neighbor
		
		Args:
			neighbor An instance of the Neighbor class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['neighbor']=serialize_Neighbor_json(neighbor)
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

	def getAllRouterBgpNeighbors(self):
		"""
		Retrieve all neighbor objects currently pending in the system
		
		Returns:
			A list of Neighbor objects
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
			payload= data.get('neighborList')
		return deserialize_list_Neighbor_json(payload)

