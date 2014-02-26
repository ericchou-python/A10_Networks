########################################################################################################################
# File name: router_bgp.py
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
	'https://axapi.a10networks.com/axapi/v3/router/bgp',
]

def deserialize_Router_bgp_aggregate_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	aggregate_address = data.get('aggregate-address')
	as_set = data.get('as-set')
	summary_only = data.get('summary-only')
	result = Router_bgp_aggregate_address_cfg(aggregate_address=aggregate_address, as_set=as_set, summary_only=summary_only)
	return result

def deserialize_list_Router_bgp_aggregate_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_aggregate_address_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_bestpath_cfg__as_path_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	as_path = data.get('as-path')
	ignore = data.get('ignore')
	result = Router_bgp_bestpath_cfg__as_path_cfg(as_path=as_path, ignore=ignore)
	return result

def deserialize_Router_bgp_bestpath_cfg__med_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	med = data.get('med')
	remove_recv_med = data.get('remove-recv-med')
	remove_send_med = data.get('remove-send-med')
	confed = data.get('confed')
	missing_as_worst = data.get('missing-as-worst')
	result = Router_bgp_bestpath_cfg__med_cfg(med=med, remove_recv_med=remove_recv_med, remove_send_med=remove_send_med, confed=confed, missing_as_worst=missing_as_worst)
	return result

def deserialize_Router_bgp_bestpath_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bestpath = data.get('bestpath')
	as_path_cfg = deserialize_Router_bgp_bestpath_cfg__as_path_cfg_json(data.get('as-path-cfg'))
	compare_routerid = data.get('compare-routerid')
	med_cfg = deserialize_Router_bgp_bestpath_cfg__med_cfg_json(data.get('med-cfg'))
	result = Router_bgp_bestpath_cfg(bestpath=bestpath, as_path_cfg=as_path_cfg, compare_routerid=compare_routerid, med_cfg=med_cfg)
	return result

def deserialize_list_Router_bgp_bestpath_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_bestpath_cfg_json(item))
	return list(container)

def deserialize_Bgp__bgp__dampening_cfg__dampening_half_time_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dampening_half_time = data.get('dampening-half-time')
	dampening_reuse = data.get('dampening-reuse')
	dampening_supress = data.get('dampening-supress')
	dampening_max_supress = data.get('dampening-max-supress')
	dampening_penalty = data.get('dampening-penalty')
	result = Bgp__bgp__dampening_cfg__dampening_half_time_cfg(dampening_half_time=dampening_half_time, dampening_reuse=dampening_reuse, dampening_supress=dampening_supress, dampening_max_supress=dampening_max_supress, dampening_penalty=dampening_penalty)
	return result

def deserialize_Bgp__bgp__dampening_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dampening = data.get('dampening')
	dampening_half_time_cfg = deserialize_Bgp__bgp__dampening_cfg__dampening_half_time_cfg_json(data.get('dampening-half-time-cfg'))
	route_map = data.get('route-map')
	result = Bgp__bgp__dampening_cfg(dampening=dampening, dampening_half_time_cfg=dampening_half_time_cfg, route_map=route_map)
	return result

def deserialize_Bgp__bgp__default__local_preference_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_preference_value = data.get('local-preference-value')
	result = Bgp__bgp__default__local_preference(local_preference_value=local_preference_value)
	return result

def deserialize_Bgp__bgp__default_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4_unicast = data.get('ipv4-unicast')
	local_preference = deserialize_Bgp__bgp__default__local_preference_json(data.get('local-preference'))
	result = Bgp__bgp__default(ipv4_unicast=ipv4_unicast, local_preference=local_preference)
	return result

def deserialize_Bgp__bgp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	always_compare_med = data.get('always-compare-med')
	bestpath_cfg = deserialize_list_Router_bgp_bestpath_cfg_json(data.get('bestpath-cfg'))
	dampening_cfg = deserialize_Bgp__bgp__dampening_cfg_json(data.get('dampening-cfg'))
	default = deserialize_Bgp__bgp__default_json(data.get('default'))
	deterministic_med = data.get('deterministic-med')
	enforce_first_as = data.get('enforce-first-as')
	fast_external_failover = data.get('fast-external-failover')
	log_neighbor_changes = data.get('log-neighbor-changes')
	nexthop_trigger_count = data.get('nexthop-trigger-count')
	router_id = data.get('router-id')
	scan_time = data.get('scan-time')
	result = Bgp__bgp(always_compare_med=always_compare_med, bestpath_cfg=bestpath_cfg, dampening_cfg=dampening_cfg, default=default, deterministic_med=deterministic_med, enforce_first_as=enforce_first_as, fast_external_failover=fast_external_failover, log_neighbor_changes=log_neighbor_changes, nexthop_trigger_count=nexthop_trigger_count, router_id=router_id, scan_time=scan_time)
	return result

def deserialize_Bgp__distance__admin_distance_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	admin_distance = data.get('admin-distance')
	src_prefix = data.get('src-prefix')
	acl_str = data.get('acl-str')
	result = Bgp__distance__admin_distance_cfg(admin_distance=admin_distance, src_prefix=src_prefix, acl_str=acl_str)
	return result

def deserialize_Bgp__distance__distance_bgp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bgp = data.get('bgp')
	ext_routes_dist = data.get('ext-routes-dist')
	int_routes_dist = data.get('int-routes-dist')
	local_routes_dist = data.get('local-routes-dist')
	result = Bgp__distance__distance_bgp_cfg(bgp=bgp, ext_routes_dist=ext_routes_dist, int_routes_dist=int_routes_dist, local_routes_dist=local_routes_dist)
	return result

def deserialize_Bgp__distance_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	admin_distance_cfg = deserialize_Bgp__distance__admin_distance_cfg_json(data.get('admin-distance-cfg'))
	distance_bgp_cfg = deserialize_Bgp__distance__distance_bgp_cfg_json(data.get('distance-bgp-cfg'))
	result = Bgp__distance(admin_distance_cfg=admin_distance_cfg, distance_bgp_cfg=distance_bgp_cfg)
	return result

def deserialize_Bgp__maximum_paths_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Bgp__maximum_paths(value=value)
	return result

def deserialize_Router_bgp_network_ipv4_cfg__backdoor_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	network_backdoor = data.get('network-backdoor')
	network_backdoor_desc = data.get('network-backdoor-desc')
	result = Router_bgp_network_ipv4_cfg__backdoor_cfg(network_backdoor=network_backdoor, network_backdoor_desc=network_backdoor_desc)
	return result

def deserialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_backdoor_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	network_mask_backdoor = data.get('network-mask-backdoor')
	network_mask_backdoor_desc = data.get('network-mask-backdoor-desc')
	result = Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_backdoor_cfg(network_mask_backdoor=network_mask_backdoor, network_mask_backdoor_desc=network_mask_backdoor_desc)
	return result

def deserialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg__network_mask_rmap_backdoor_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	network_mask_rmap_backdoor = data.get('network-mask-rmap-backdoor')
	network_mask_rmap_backdoor_desc = data.get('network-mask-rmap-backdoor-desc')
	result = Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg__network_mask_rmap_backdoor_cfg(network_mask_rmap_backdoor=network_mask_rmap_backdoor, network_mask_rmap_backdoor_desc=network_mask_rmap_backdoor_desc)
	return result

def deserialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	network_mask_rmap = data.get('network-mask-rmap')
	network_mask_rmap_backdoor_cfg = deserialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg__network_mask_rmap_backdoor_cfg_json(data.get('network-mask-rmap-backdoor-cfg'))
	network_mask_rmap_desc = data.get('network-mask-rmap-desc')
	result = Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg(network_mask_rmap=network_mask_rmap, network_mask_rmap_backdoor_cfg=network_mask_rmap_backdoor_cfg, network_mask_rmap_desc=network_mask_rmap_desc)
	return result

def deserialize_Router_bgp_network_ipv4_cfg__mask_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	network_mask = data.get('network-mask')
	network_mask_backdoor_cfg = deserialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_backdoor_cfg_json(data.get('network-mask-backdoor-cfg'))
	network_mask_desc = data.get('network-mask-desc')
	network_mask_route_map_cfg = deserialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg_json(data.get('network-mask-route-map-cfg'))
	result = Router_bgp_network_ipv4_cfg__mask_cfg(network_mask=network_mask, network_mask_backdoor_cfg=network_mask_backdoor_cfg, network_mask_desc=network_mask_desc, network_mask_route_map_cfg=network_mask_route_map_cfg)
	return result

def deserialize_Router_bgp_network_ipv4_cfg__network_route_map_cfg__network_rmap_backdoor_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	network_rmap_backdoor = data.get('network-rmap-backdoor')
	network_mask_rmap_backdoor_desc = data.get('network-mask-rmap-backdoor-desc')
	result = Router_bgp_network_ipv4_cfg__network_route_map_cfg__network_rmap_backdoor_cfg(network_rmap_backdoor=network_rmap_backdoor, network_mask_rmap_backdoor_desc=network_mask_rmap_backdoor_desc)
	return result

def deserialize_Router_bgp_network_ipv4_cfg__network_route_map_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	network_rmap = data.get('network-rmap')
	network_rmap_backdoor_cfg = deserialize_Router_bgp_network_ipv4_cfg__network_route_map_cfg__network_rmap_backdoor_cfg_json(data.get('network-rmap-backdoor-cfg'))
	network_rmap_desc = data.get('network-rmap-desc')
	result = Router_bgp_network_ipv4_cfg__network_route_map_cfg(network_rmap=network_rmap, network_rmap_backdoor_cfg=network_rmap_backdoor_cfg, network_rmap_desc=network_rmap_desc)
	return result

def deserialize_Router_bgp_network_ipv4_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	network_ipv4 = data.get('network-ipv4')
	backdoor_cfg = deserialize_Router_bgp_network_ipv4_cfg__backdoor_cfg_json(data.get('backdoor-cfg'))
	network_desc = data.get('network-desc')
	mask_cfg = deserialize_Router_bgp_network_ipv4_cfg__mask_cfg_json(data.get('mask-cfg'))
	network_route_map_cfg = deserialize_Router_bgp_network_ipv4_cfg__network_route_map_cfg_json(data.get('network-route-map-cfg'))
	result = Router_bgp_network_ipv4_cfg(network_ipv4=network_ipv4, backdoor_cfg=backdoor_cfg, network_desc=network_desc, mask_cfg=mask_cfg, network_route_map_cfg=network_route_map_cfg)
	return result

def deserialize_list_Router_bgp_network_ipv4_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_network_ipv4_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_backdoor_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	net_prefix_backdoor = data.get('net-prefix-backdoor')
	net_prefix_backdoor_desc = data.get('net-prefix-backdoor-desc')
	result = Router_bgp_network_ipv4_mask_cfg__net_prefix_backdoor_cfg(net_prefix_backdoor=net_prefix_backdoor, net_prefix_backdoor_desc=net_prefix_backdoor_desc)
	return result

def deserialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg__net_prefix_rmap_backdoor_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	net_prefix_rmap_backdoor = data.get('net-prefix-rmap-backdoor')
	net_prefix_rmap_backdoor_desc = data.get('net-prefix-rmap-backdoor-desc')
	result = Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg__net_prefix_rmap_backdoor_cfg(net_prefix_rmap_backdoor=net_prefix_rmap_backdoor, net_prefix_rmap_backdoor_desc=net_prefix_rmap_backdoor_desc)
	return result

def deserialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	net_prefix_rmap = data.get('net-prefix-rmap')
	net_prefix_rmap_backdoor_cfg = deserialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg__net_prefix_rmap_backdoor_cfg_json(data.get('net-prefix-rmap-backdoor-cfg'))
	net_prefix_rmap_desc = data.get('net-prefix-rmap-desc')
	result = Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg(net_prefix_rmap=net_prefix_rmap, net_prefix_rmap_backdoor_cfg=net_prefix_rmap_backdoor_cfg, net_prefix_rmap_desc=net_prefix_rmap_desc)
	return result

def deserialize_Router_bgp_network_ipv4_mask_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	net_prefix = data.get('net-prefix')
	net_prefix_backdoor_cfg = deserialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_backdoor_cfg_json(data.get('net-prefix-backdoor-cfg'))
	net_prefix_desc = data.get('net-prefix-desc')
	net_prefix_route_map_cfg = deserialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg_json(data.get('net-prefix-route-map-cfg'))
	result = Router_bgp_network_ipv4_mask_cfg(net_prefix=net_prefix, net_prefix_backdoor_cfg=net_prefix_backdoor_cfg, net_prefix_desc=net_prefix_desc, net_prefix_route_map_cfg=net_prefix_route_map_cfg)
	return result

def deserialize_list_Router_bgp_network_ipv4_mask_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_network_ipv4_mask_cfg_json(item))
	return list(container)

def deserialize_Bgp__network_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	network_ipv4_cfg = deserialize_list_Router_bgp_network_ipv4_cfg_json(data.get('network-ipv4-cfg'))
	network_ipv4_mask_cfg = deserialize_list_Router_bgp_network_ipv4_mask_cfg_json(data.get('network-ipv4-mask-cfg'))
	synchronization = data.get('synchronization')
	result = Bgp__network(network_ipv4_cfg=network_ipv4_cfg, network_ipv4_mask_cfg=network_ipv4_mask_cfg, synchronization=synchronization)
	return result

def deserialize_Bgp__timers__bgp_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bgp_keepalive = data.get('bgp-keepalive')
	bgp_holdtime = data.get('bgp-holdtime')
	result = Bgp__timers__bgp_1(bgp_keepalive=bgp_keepalive, bgp_holdtime=bgp_holdtime)
	return result

def deserialize_Bgp__timers_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bgp_1 = deserialize_Bgp__timers__bgp_1_json(data.get('bgp-1'))
	result = Bgp__timers(bgp_1=bgp_1)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	allowas_in = data.get('allowas-in')
	allowas_in_count = data.get('allowas-in-count')
	result = Router_bgp_neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg(allowas_in=allowas_in, allowas_in_count=allowas_in_count)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg_json(obj):
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
	result = Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg(orf=orf, prefix_list=prefix_list, both=both, receive=receive, send=send)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dynamic = data.get('dynamic')
	neighbor_orf_cfg = deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg_json(data.get('neighbor-orf-cfg'))
	route_refresh = data.get('route-refresh')
	result = Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability(dynamic=dynamic, neighbor_orf_cfg=neighbor_orf_cfg, route_refresh=route_refresh)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_default_originate_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default_originate = data.get('default-originate')
	route_map = data.get('route-map')
	result = Router_bgp_neighbor__neighbor_str_cfg__neighbor_default_originate_cfg(default_originate=default_originate, route_map=route_map)
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

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	maximum_prefix = data.get('maximum-prefix')
	maximum_prefix_thres = data.get('maximum-prefix-thres')
	result = Router_bgp_neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg(maximum_prefix=maximum_prefix, maximum_prefix_thres=maximum_prefix_thres)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__nbr_str_pass_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	encrypted = data.get('encrypted')
	result = Router_bgp_neighbor__neighbor_str_cfg__nbr_str_pass(value=value, encrypted=encrypted)
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

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_send_community_cfg_json(obj):
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
	result = Router_bgp_neighbor__neighbor_str_cfg__neighbor_send_community_cfg(send_community=send_community, both=both, extended=extended, standard=standard)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	soft_reconfiguration = data.get('soft-reconfiguration')
	inbound = data.get('inbound')
	result = Router_bgp_neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg(soft_reconfiguration=soft_reconfiguration, inbound=inbound)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timers_keepalive = data.get('timers-keepalive')
	timers_holdtime = data.get('timers-holdtime')
	result = Router_bgp_neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg(timers_keepalive=timers_keepalive, timers_holdtime=timers_holdtime)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	connect = data.get('connect')
	result = Router_bgp_neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg(connect=connect)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__timers_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	neighbor_timers_keepalive_cfg = deserialize_Router_bgp_neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg_json(data.get('neighbor-timers-keepalive-cfg'))
	timers_con_under_group_cfg = deserialize_Router_bgp_neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg_json(data.get('timers-con-under-group-cfg'))
	result = Router_bgp_neighbor__neighbor_str_cfg__timers(neighbor_timers_keepalive_cfg=neighbor_timers_keepalive_cfg, timers_con_under_group_cfg=timers_con_under_group_cfg)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_update_source_cfg_json(obj):
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
	result = Router_bgp_neighbor__neighbor_str_cfg__neighbor_update_source_cfg(update_source=update_source, update_source_ip=update_source_ip, update_source_ipv6=update_source_ipv6, ethernet=ethernet, loopback=loopback, ve=ve, trunk=trunk)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_version_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	version = data.get('version')
	param_4 = data.get('4')
	result = Router_bgp_neighbor__neighbor_str_cfg__neighbor_version_cfg(version=version, param_4=param_4)
	return result

def deserialize_Router_bgp_neighbor__neighbor_str_cfg_json(obj):
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
	neighbor_allowas_in_cfg = deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg_json(data.get('neighbor-allowas-in-cfg'))
	as_origination_interval = data.get('as-origination-interval')
	neighbor_capability = deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability_json(data.get('neighbor-capability'))
	collide_established = data.get('collide-established')
	connection_retry_time = data.get('connection-retry-time')
	neighbor_default_originate_cfg = deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_default_originate_cfg_json(data.get('neighbor-default-originate-cfg'))
	disallow_infinite_holdtime = data.get('disallow-infinite-holdtime')
	neighbor_distribute_list_cfg = deserialize_list_Router_bgp_neighbor_distribute_list_cfg_json(data.get('neighbor-distribute-list-cfg'))
	dont_capability_negotiate = data.get('dont-capability-negotiate')
	neighbor_ebgp_multihop_cfg = deserialize_list_Router_bgp_neighbor_ebgp_multihop_cfg_json(data.get('neighbor-ebgp-multihop-cfg'))
	enforce_multihop = data.get('enforce-multihop')
	neighbor_filter_list_cfg = deserialize_list_Router_bgp_neighbor_filter_list_cfg_json(data.get('neighbor-filter-list-cfg'))
	neighbor_maximum_prefix_cfg = deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg_json(data.get('neighbor-maximum-prefix-cfg'))
	next_hop_self = data.get('next-hop-self')
	override_capability = data.get('override-capability')
	nbr_str_pass = deserialize_Router_bgp_neighbor__neighbor_str_cfg__nbr_str_pass_json(data.get('nbr-str-pass'))
	passive = data.get('passive')
	neighbor_prefix_list_cfg = deserialize_list_Router_bgp_neighbor_prefix_list_cfg_json(data.get('neighbor-prefix-list-cfg'))
	remove_private_as = data.get('remove-private-AS')
	neighbor_route_map_cfg = deserialize_list_Router_bgp_neighbor_route_map_cfg_json(data.get('neighbor-route-map-cfg'))
	neighbor_send_community_cfg = deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_send_community_cfg_json(data.get('neighbor-send-community-cfg'))
	neighbor_soft_reconfiguration_cfg = deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg_json(data.get('neighbor-soft-reconfiguration-cfg'))
	shutdown = data.get('shutdown')
	strict_capability_match = data.get('strict-capability-match')
	timers = deserialize_Router_bgp_neighbor__neighbor_str_cfg__timers_json(data.get('timers'))
	unsuppress_map = data.get('unsuppress-map')
	neighbor_update_source_cfg = deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_update_source_cfg_json(data.get('neighbor-update-source-cfg'))
	neighbor_version_cfg = deserialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_version_cfg_json(data.get('neighbor-version-cfg'))
	weight = data.get('weight')
	result = Router_bgp_neighbor__neighbor_str_cfg(neighbor_str=neighbor_str, peer_group=peer_group, remote_as=remote_as, activate=activate, advertisement_interval=advertisement_interval, neighbor_allowas_in_cfg=neighbor_allowas_in_cfg, as_origination_interval=as_origination_interval, neighbor_capability=neighbor_capability, collide_established=collide_established, connection_retry_time=connection_retry_time, neighbor_default_originate_cfg=neighbor_default_originate_cfg, disallow_infinite_holdtime=disallow_infinite_holdtime, neighbor_distribute_list_cfg=neighbor_distribute_list_cfg, dont_capability_negotiate=dont_capability_negotiate, neighbor_ebgp_multihop_cfg=neighbor_ebgp_multihop_cfg, enforce_multihop=enforce_multihop, neighbor_filter_list_cfg=neighbor_filter_list_cfg, neighbor_maximum_prefix_cfg=neighbor_maximum_prefix_cfg, next_hop_self=next_hop_self, override_capability=override_capability, nbr_str_pass=nbr_str_pass, passive=passive, neighbor_prefix_list_cfg=neighbor_prefix_list_cfg, remove_private_as=remove_private_as, neighbor_route_map_cfg=neighbor_route_map_cfg, neighbor_send_community_cfg=neighbor_send_community_cfg, neighbor_soft_reconfiguration_cfg=neighbor_soft_reconfiguration_cfg, shutdown=shutdown, strict_capability_match=strict_capability_match, timers=timers, unsuppress_map=unsuppress_map, neighbor_update_source_cfg=neighbor_update_source_cfg, neighbor_version_cfg=neighbor_version_cfg, weight=weight)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__allowas_in_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	allowas_in = data.get('allowas-in')
	allowas_in_count = data.get('allowas-in-count')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__allowas_in_cfg(allowas_in=allowas_in, allowas_in_count=allowas_in_count)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg_json(obj):
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
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg(orf=orf, prefix_list=prefix_list, both=both, receive=receive, send=send)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dynamic = data.get('dynamic')
	orf_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg_json(data.get('orf-cfg'))
	route_refresh = data.get('route-refresh')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1(dynamic=dynamic, orf_cfg=orf_cfg, route_refresh=route_refresh)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__default_originate_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default_originate = data.get('default-originate')
	route_map = data.get('route-map')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__default_originate_cfg(default_originate=default_originate, route_map=route_map)
	return result

def deserialize_Router_bgp_distribute_list_cfg_json(obj):
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
	result = Router_bgp_distribute_list_cfg(distribute_list=distribute_list, acl_val=acl_val, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_distribute_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_distribute_list_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_ebgp_multihop_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ebgp_multihop = data.get('ebgp-multihop')
	ebgp_multihop_hop_count = data.get('ebgp-multihop-hop-count')
	result = Router_bgp_ebgp_multihop_cfg(ebgp_multihop=ebgp_multihop, ebgp_multihop_hop_count=ebgp_multihop_hop_count)
	return result

def deserialize_list_Router_bgp_ebgp_multihop_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_ebgp_multihop_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_filter_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	filter_list = data.get('filter-list')
	py_kw_rsvd_in = data.get('in')
	out = data.get('out')
	result = Router_bgp_filter_list_cfg(filter_list=filter_list, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_filter_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_filter_list_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	maximum_prefix = data.get('maximum-prefix')
	maximum_prefix_thres = data.get('maximum-prefix-thres')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg(maximum_prefix=maximum_prefix, maximum_prefix_thres=maximum_prefix_thres)
	return result

def deserialize_Router_bgp_prefix_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	prefix_list = data.get('prefix-list')
	py_kw_rsvd_in = data.get('in')
	out = data.get('out')
	result = Router_bgp_prefix_list_cfg(prefix_list=prefix_list, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_prefix_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_prefix_list_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	nbr_ipv4_pass_value = data.get('nbr-ipv4-pass-value')
	nbr_ipv4_pass_encrypted = data.get('nbr-ipv4-pass-encrypted')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass(nbr_ipv4_pass_value=nbr_ipv4_pass_value, nbr_ipv4_pass_encrypted=nbr_ipv4_pass_encrypted)
	return result

def deserialize_Router_bgp_route_map_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	route_map = data.get('route-map')
	py_kw_rsvd_in = data.get('in')
	out = data.get('out')
	result = Router_bgp_route_map_cfg(route_map=route_map, py_kw_rsvd_in=py_kw_rsvd_in, out=out)
	return result

def deserialize_list_Router_bgp_route_map_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_route_map_cfg_json(item))
	return list(container)

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__send_community_cfg_json(obj):
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
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__send_community_cfg(send_community=send_community, both=both, extended=extended, standard=standard)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	soft_reconfiguration = data.get('soft-reconfiguration')
	inbound = data.get('inbound')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg(soft_reconfiguration=soft_reconfiguration, inbound=inbound)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	md5_value = data.get('md5-value')
	md5_encrypted = data.get('md5-encrypted')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5(md5_value=md5_value, md5_encrypted=md5_encrypted)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	meticulous_md5_value = data.get('meticulous-md5-value')
	meticulous_md5_encrypted = data.get('meticulous-md5-encrypted')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5(meticulous_md5_value=meticulous_md5_value, meticulous_md5_encrypted=meticulous_md5_encrypted)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	meticulous_sha1_value = data.get('meticulous-sha1-value')
	meticulous_sha1_encrypted = data.get('meticulous-sha1-encrypted')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1(meticulous_sha1_value=meticulous_sha1_value, meticulous_sha1_encrypted=meticulous_sha1_encrypted)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sha1_value = data.get('sha1-value')
	sha1_encrypted = data.get('sha1-encrypted')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1(sha1_value=sha1_value, sha1_encrypted=sha1_encrypted)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	simple_value = data.get('simple-value')
	simple_encrypted = data.get('simple-encrypted')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple(simple_value=simple_value, simple_encrypted=simple_encrypted)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key_id = data.get('key-id')
	md5 = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5_json(data.get('md5'))
	meticulous_md5 = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5_json(data.get('meticulous-md5'))
	meticulous_sha1 = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1_json(data.get('meticulous-sha1'))
	sha1 = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1_json(data.get('sha1'))
	simple = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple_json(data.get('simple'))
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg(key_id=key_id, md5=md5, meticulous_md5=meticulous_md5, meticulous_sha1=meticulous_sha1, sha1=sha1, simple=simple)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key_id_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg_json(data.get('key-id-cfg'))
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication(key_id_cfg=key_id_cfg)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bfd = data.get('bfd')
	authentication = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication_json(data.get('authentication'))
	multihop = data.get('multihop')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg(bfd=bfd, authentication=authentication, multihop=multihop)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	fall_over = data.get('fall-over')
	bfd_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg_json(data.get('bfd-cfg'))
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg(fall_over=fall_over, bfd_cfg=bfd_cfg)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	neighbor_ipv4_timers_keepalive = data.get('neighbor-ipv4-timers-keepalive')
	timers_holdtime = data.get('timers-holdtime')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg(neighbor_ipv4_timers_keepalive=neighbor_ipv4_timers_keepalive, timers_holdtime=timers_holdtime)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	connect = data.get('connect')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg(connect=connect)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timers_keepalive_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg_json(data.get('timers-keepalive-cfg'))
	timers_con_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg_json(data.get('timers-con-cfg'))
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers(timers_keepalive_cfg=timers_keepalive_cfg, timers_con_cfg=timers_con_cfg)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__update_source_cfg_json(obj):
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
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__update_source_cfg(update_source=update_source, update_source_ip=update_source_ip, update_source_ipv6=update_source_ipv6, ethernet=ethernet, loopback=loopback, ve=ve, trunk=trunk)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__version_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	version = data.get('version')
	param_4 = data.get('4')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg__version_cfg(version=version, param_4=param_4)
	return result

def deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg_json(obj):
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
	allowas_in_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__allowas_in_cfg_json(data.get('allowas-in-cfg'))
	as_origination_interval = data.get('as-origination-interval')
	capability_1 = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1_json(data.get('capability-1'))
	collide_established = data.get('collide-established')
	connection_retry_time = data.get('connection-retry-time')
	default_originate_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__default_originate_cfg_json(data.get('default-originate-cfg'))
	disallow_infinite_holdtime = data.get('disallow-infinite-holdtime')
	distribute_list_cfg = deserialize_list_Router_bgp_distribute_list_cfg_json(data.get('distribute-list-cfg'))
	dont_capability_negotiate = data.get('dont-capability-negotiate')
	ebgp_multihop_cfg = deserialize_list_Router_bgp_ebgp_multihop_cfg_json(data.get('ebgp-multihop-cfg'))
	enforce_multihop = data.get('enforce-multihop')
	filter_list_cfg = deserialize_list_Router_bgp_filter_list_cfg_json(data.get('filter-list-cfg'))
	maximum_prefix_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg_json(data.get('maximum-prefix-cfg'))
	next_hop_self = data.get('next-hop-self')
	override_capability = data.get('override-capability')
	passive = data.get('passive')
	prefix_list_cfg = deserialize_list_Router_bgp_prefix_list_cfg_json(data.get('prefix-list-cfg'))
	remove_private_as = data.get('remove-private-AS')
	nbr_ipv4_pass = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass_json(data.get('nbr-ipv4-pass'))
	route_map_cfg = deserialize_list_Router_bgp_route_map_cfg_json(data.get('route-map-cfg'))
	send_community_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__send_community_cfg_json(data.get('send-community-cfg'))
	soft_reconfiguration_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg_json(data.get('soft-reconfiguration-cfg'))
	shutdown = data.get('shutdown')
	fall_over_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg_json(data.get('fall-over-cfg'))
	strict_capability_match = data.get('strict-capability-match')
	neighbor_ipv4_timers = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers_json(data.get('neighbor-ipv4-timers'))
	unsuppress_map = data.get('unsuppress-map')
	update_source_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__update_source_cfg_json(data.get('update-source-cfg'))
	version_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg__version_cfg_json(data.get('version-cfg'))
	weight = data.get('weight')
	result = Router_bgp_neighbor__neighbor_ipv4_cfg(neighbor_ipv4=neighbor_ipv4, neighbor_ipv6=neighbor_ipv6, remote_as=remote_as, peer_group=peer_group, activate=activate, advertisement_interval=advertisement_interval, allowas_in_cfg=allowas_in_cfg, as_origination_interval=as_origination_interval, capability_1=capability_1, collide_established=collide_established, connection_retry_time=connection_retry_time, default_originate_cfg=default_originate_cfg, disallow_infinite_holdtime=disallow_infinite_holdtime, distribute_list_cfg=distribute_list_cfg, dont_capability_negotiate=dont_capability_negotiate, ebgp_multihop_cfg=ebgp_multihop_cfg, enforce_multihop=enforce_multihop, filter_list_cfg=filter_list_cfg, maximum_prefix_cfg=maximum_prefix_cfg, next_hop_self=next_hop_self, override_capability=override_capability, passive=passive, prefix_list_cfg=prefix_list_cfg, remove_private_as=remove_private_as, nbr_ipv4_pass=nbr_ipv4_pass, route_map_cfg=route_map_cfg, send_community_cfg=send_community_cfg, soft_reconfiguration_cfg=soft_reconfiguration_cfg, shutdown=shutdown, fall_over_cfg=fall_over_cfg, strict_capability_match=strict_capability_match, neighbor_ipv4_timers=neighbor_ipv4_timers, unsuppress_map=unsuppress_map, update_source_cfg=update_source_cfg, version_cfg=version_cfg, weight=weight)
	return result

def deserialize_Router_bgp_neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	neighbor_str_cfg = deserialize_Router_bgp_neighbor__neighbor_str_cfg_json(data.get('neighbor-str-cfg'))
	neighbor_ipv4_cfg = deserialize_Router_bgp_neighbor__neighbor_ipv4_cfg_json(data.get('neighbor-ipv4-cfg'))
	result = Router_bgp_neighbor(neighbor_str_cfg=neighbor_str_cfg, neighbor_ipv4_cfg=neighbor_ipv4_cfg)
	return result

def deserialize_list_Router_bgp_neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_neighbor_json(item))
	return list(container)

def deserialize_Bgp__redistribute__connected_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	connected = data.get('connected')
	route_map = data.get('route-map')
	result = Bgp__redistribute__connected_cfg(connected=connected, route_map=route_map)
	return result

def deserialize_Bgp__redistribute__floating_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	route_map = data.get('route-map')
	result = Bgp__redistribute__floating_ip_cfg(route_map=route_map)
	return result

def deserialize_Bgp__redistribute__ip_nat_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_nat = data.get('ip-nat')
	route_map = data.get('route-map')
	result = Bgp__redistribute__ip_nat_cfg(ip_nat=ip_nat, route_map=route_map)
	return result

def deserialize_Bgp__redistribute__ip_nat_list_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_nat_list = data.get('ip-nat-list')
	route_map = data.get('route-map')
	result = Bgp__redistribute__ip_nat_list_cfg(ip_nat_list=ip_nat_list, route_map=route_map)
	return result

def deserialize_Bgp__redistribute__isis_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	route_map = data.get('route-map')
	result = Bgp__redistribute__isis_cfg(route_map=route_map)
	return result

def deserialize_Bgp__redistribute__kernel_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	kernel = data.get('kernel')
	route_map = data.get('route-map')
	result = Bgp__redistribute__kernel_cfg(kernel=kernel, route_map=route_map)
	return result

def deserialize_Bgp__redistribute__ospf_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ospf = data.get('ospf')
	route_map = data.get('route-map')
	result = Bgp__redistribute__ospf_cfg(ospf=ospf, route_map=route_map)
	return result

def deserialize_Bgp__redistribute__rip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	route_map = data.get('route-map')
	result = Bgp__redistribute__rip_cfg(route_map=route_map)
	return result

def deserialize_Bgp__redistribute__static_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	static = data.get('static')
	route_map = data.get('route-map')
	result = Bgp__redistribute__static_cfg(static=static, route_map=route_map)
	return result

def deserialize_Bgp__redistribute_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	connected_cfg = deserialize_Bgp__redistribute__connected_cfg_json(data.get('connected-cfg'))
	floating_ip_cfg = deserialize_Bgp__redistribute__floating_ip_cfg_json(data.get('floating-ip-cfg'))
	ip_nat_cfg = deserialize_Bgp__redistribute__ip_nat_cfg_json(data.get('ip-nat-cfg'))
	ip_nat_list_cfg = deserialize_Bgp__redistribute__ip_nat_list_cfg_json(data.get('ip-nat-list-cfg'))
	isis_cfg = deserialize_Bgp__redistribute__isis_cfg_json(data.get('isis-cfg'))
	kernel_cfg = deserialize_Bgp__redistribute__kernel_cfg_json(data.get('kernel-cfg'))
	ospf_cfg = deserialize_Bgp__redistribute__ospf_cfg_json(data.get('ospf-cfg'))
	rip_cfg = deserialize_Bgp__redistribute__rip_cfg_json(data.get('rip-cfg'))
	static_cfg = deserialize_Bgp__redistribute__static_cfg_json(data.get('static-cfg'))
	result = Bgp__redistribute(connected_cfg=connected_cfg, floating_ip_cfg=floating_ip_cfg, ip_nat_cfg=ip_nat_cfg, ip_nat_list_cfg=ip_nat_list_cfg, isis_cfg=isis_cfg, kernel_cfg=kernel_cfg, ospf_cfg=ospf_cfg, rip_cfg=rip_cfg, static_cfg=static_cfg)
	return result

def deserialize_Router_bgp_address_family_ipv6_neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	result = Router_bgp_address_family_ipv6_neighbor()
	return result

def deserialize_list_Router_bgp_address_family_ipv6_neighbor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Router_bgp_address_family_ipv6_neighbor_json(item))
	return list(container)

def deserialize_Bgp__address_family__ipv6__redistribute_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	result = Bgp__address_family__ipv6__redistribute()
	return result

def deserialize_Bgp__address_family__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	neighborlist = deserialize_list_Router_bgp_address_family_ipv6_neighbor_json(data.get('neighborList'))
	redistribute = deserialize_Bgp__address_family__ipv6__redistribute_json(data.get('redistribute'))
	result = Bgp__address_family__ipv6(neighborlist=neighborlist, redistribute=redistribute)
	return result

def deserialize_Bgp__address_family_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6 = deserialize_Bgp__address_family__ipv6_json(data.get('ipv6'))
	result = Bgp__address_family(ipv6=ipv6)
	return result

def deserialize_Bgp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	process_id = data.get('process-id')
	aggregate_address_cfg = deserialize_list_Router_bgp_aggregate_address_cfg_json(data.get('aggregate-address-cfg'))
	bgp = deserialize_Bgp__bgp_json(data.get('bgp'))
	distance = deserialize_Bgp__distance_json(data.get('distance'))
	maximum_paths = deserialize_Bgp__maximum_paths_json(data.get('maximum-paths'))
	network = deserialize_Bgp__network_json(data.get('network'))
	timers = deserialize_Bgp__timers_json(data.get('timers'))
	synchronization = data.get('synchronization')
	auto_summary = data.get('auto-summary')
	neighborlist = deserialize_list_Router_bgp_neighbor_json(data.get('neighborList'))
	redistribute = deserialize_Bgp__redistribute_json(data.get('redistribute'))
	address_family = deserialize_Bgp__address_family_json(data.get('address-family'))
	result = Bgp(process_id=process_id, aggregate_address_cfg=aggregate_address_cfg, bgp=bgp, distance=distance, maximum_paths=maximum_paths, network=network, timers=timers, synchronization=synchronization, auto_summary=auto_summary, neighborlist=neighborlist, redistribute=redistribute, address_family=address_family)
	return result

def serialize_Router_bgp_aggregate_address_cfg_json(obj):
	output = OrderedDict()
	if obj.aggregate_address is not None:
		output['aggregate-address'] = obj.aggregate_address
	if obj.as_set is not None:
		output['as-set'] = obj.as_set
	if obj.summary_only is not None:
		output['summary-only'] = obj.summary_only
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Router_bgp_aggregate_address_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_aggregate_address_cfg_json(item))
	return output

def serialize_Router_bgp_bestpath_cfg__as_path_cfg_json(obj):
	output = OrderedDict()
	if obj.as_path is not None:
		output['as-path'] = obj.as_path
	if obj.ignore is not None:
		output['ignore'] = obj.ignore
	return output

def serialize_Router_bgp_bestpath_cfg__med_cfg_json(obj):
	output = OrderedDict()
	if obj.med is not None:
		output['med'] = obj.med
	if obj.remove_recv_med is not None:
		output['remove-recv-med'] = obj.remove_recv_med
	if obj.remove_send_med is not None:
		output['remove-send-med'] = obj.remove_send_med
	if obj.confed is not None:
		output['confed'] = obj.confed
	if obj.missing_as_worst is not None:
		output['missing-as-worst'] = obj.missing_as_worst
	return output

def serialize_Router_bgp_bestpath_cfg_json(obj):
	output = OrderedDict()
	if obj.bestpath is not None:
		output['bestpath'] = obj.bestpath
	if obj.as_path_cfg is not None:
		output['as-path-cfg'] = serialize_Router_bgp_bestpath_cfg__as_path_cfg_json(obj.as_path_cfg)
	if obj.compare_routerid is not None:
		output['compare-routerid'] = obj.compare_routerid
	if obj.med_cfg is not None:
		output['med-cfg'] = serialize_Router_bgp_bestpath_cfg__med_cfg_json(obj.med_cfg)
	return output

def serialize_list_Router_bgp_bestpath_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_bestpath_cfg_json(item))
	return output

def serialize_Bgp__bgp__dampening_cfg__dampening_half_time_cfg_json(obj):
	output = OrderedDict()
	if obj.dampening_half_time is not None:
		output['dampening-half-time'] = obj.dampening_half_time
	if obj.dampening_reuse is not None:
		output['dampening-reuse'] = obj.dampening_reuse
	output['dampening-supress'] = obj.dampening_supress
	output['dampening-max-supress'] = obj.dampening_max_supress
	if obj.dampening_penalty is not None:
		output['dampening-penalty'] = obj.dampening_penalty
	return output

def serialize_Bgp__bgp__dampening_cfg_json(obj):
	output = OrderedDict()
	output['dampening'] = obj.dampening
	if obj.dampening_half_time_cfg is not None:
		output['dampening-half-time-cfg'] = serialize_Bgp__bgp__dampening_cfg__dampening_half_time_cfg_json(obj.dampening_half_time_cfg)
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Bgp__bgp__default__local_preference_json(obj):
	output = OrderedDict()
	output['local-preference-value'] = obj.local_preference_value
	return output

def serialize_Bgp__bgp__default_json(obj):
	output = OrderedDict()
	output['ipv4-unicast'] = obj.ipv4_unicast
	output['local-preference'] = serialize_Bgp__bgp__default__local_preference_json(obj.local_preference)
	return output

def serialize_Bgp__bgp_json(obj):
	output = OrderedDict()
	output['always-compare-med'] = obj.always_compare_med
	if obj.bestpath_cfg is not None:
		output['bestpath-cfg'] = serialize_list_Router_bgp_bestpath_cfg_json(obj.bestpath_cfg)
	if obj.dampening_cfg is not None:
		output['dampening-cfg'] = serialize_Bgp__bgp__dampening_cfg_json(obj.dampening_cfg)
	output['default'] = serialize_Bgp__bgp__default_json(obj.default)
	output['deterministic-med'] = obj.deterministic_med
	output['enforce-first-as'] = obj.enforce_first_as
	output['fast-external-failover'] = obj.fast_external_failover
	output['log-neighbor-changes'] = obj.log_neighbor_changes
	output['nexthop-trigger-count'] = obj.nexthop_trigger_count
	output['router-id'] = obj.router_id
	output['scan-time'] = obj.scan_time
	return output

def serialize_Bgp__distance__admin_distance_cfg_json(obj):
	output = OrderedDict()
	output['admin-distance'] = obj.admin_distance
	output['src-prefix'] = obj.src_prefix
	if obj.acl_str is not None:
		output['acl-str'] = obj.acl_str
	return output

def serialize_Bgp__distance__distance_bgp_cfg_json(obj):
	output = OrderedDict()
	output['bgp'] = obj.bgp
	output['ext-routes-dist'] = obj.ext_routes_dist
	output['int-routes-dist'] = obj.int_routes_dist
	output['local-routes-dist'] = obj.local_routes_dist
	return output

def serialize_Bgp__distance_json(obj):
	output = OrderedDict()
	if obj.admin_distance_cfg is not None:
		output['admin-distance-cfg'] = serialize_Bgp__distance__admin_distance_cfg_json(obj.admin_distance_cfg)
	if obj.distance_bgp_cfg is not None:
		output['distance-bgp-cfg'] = serialize_Bgp__distance__distance_bgp_cfg_json(obj.distance_bgp_cfg)
	return output

def serialize_Bgp__maximum_paths_json(obj):
	output = OrderedDict()
	output['value'] = obj.value
	return output

def serialize_Router_bgp_network_ipv4_cfg__backdoor_cfg_json(obj):
	output = OrderedDict()
	if obj.network_backdoor is not None:
		output['network-backdoor'] = obj.network_backdoor
	if obj.network_backdoor_desc is not None:
		output['network-backdoor-desc'] = obj.network_backdoor_desc
	return output

def serialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_backdoor_cfg_json(obj):
	output = OrderedDict()
	if obj.network_mask_backdoor is not None:
		output['network-mask-backdoor'] = obj.network_mask_backdoor
	if obj.network_mask_backdoor_desc is not None:
		output['network-mask-backdoor-desc'] = obj.network_mask_backdoor_desc
	return output

def serialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg__network_mask_rmap_backdoor_cfg_json(obj):
	output = OrderedDict()
	if obj.network_mask_rmap_backdoor is not None:
		output['network-mask-rmap-backdoor'] = obj.network_mask_rmap_backdoor
	if obj.network_mask_rmap_backdoor_desc is not None:
		output['network-mask-rmap-backdoor-desc'] = obj.network_mask_rmap_backdoor_desc
	return output

def serialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg_json(obj):
	output = OrderedDict()
	if obj.network_mask_rmap is not None:
		output['network-mask-rmap'] = obj.network_mask_rmap
	if obj.network_mask_rmap_backdoor_cfg is not None:
		output['network-mask-rmap-backdoor-cfg'] = serialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg__network_mask_rmap_backdoor_cfg_json(obj.network_mask_rmap_backdoor_cfg)
	if obj.network_mask_rmap_desc is not None:
		output['network-mask-rmap-desc'] = obj.network_mask_rmap_desc
	return output

def serialize_Router_bgp_network_ipv4_cfg__mask_cfg_json(obj):
	output = OrderedDict()
	if obj.network_mask is not None:
		output['network-mask'] = obj.network_mask
	if obj.network_mask_backdoor_cfg is not None:
		output['network-mask-backdoor-cfg'] = serialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_backdoor_cfg_json(obj.network_mask_backdoor_cfg)
	if obj.network_mask_desc is not None:
		output['network-mask-desc'] = obj.network_mask_desc
	if obj.network_mask_route_map_cfg is not None:
		output['network-mask-route-map-cfg'] = serialize_Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg_json(obj.network_mask_route_map_cfg)
	return output

def serialize_Router_bgp_network_ipv4_cfg__network_route_map_cfg__network_rmap_backdoor_cfg_json(obj):
	output = OrderedDict()
	if obj.network_rmap_backdoor is not None:
		output['network-rmap-backdoor'] = obj.network_rmap_backdoor
	if obj.network_mask_rmap_backdoor_desc is not None:
		output['network-mask-rmap-backdoor-desc'] = obj.network_mask_rmap_backdoor_desc
	return output

def serialize_Router_bgp_network_ipv4_cfg__network_route_map_cfg_json(obj):
	output = OrderedDict()
	if obj.network_rmap is not None:
		output['network-rmap'] = obj.network_rmap
	if obj.network_rmap_backdoor_cfg is not None:
		output['network-rmap-backdoor-cfg'] = serialize_Router_bgp_network_ipv4_cfg__network_route_map_cfg__network_rmap_backdoor_cfg_json(obj.network_rmap_backdoor_cfg)
	if obj.network_rmap_desc is not None:
		output['network-rmap-desc'] = obj.network_rmap_desc
	return output

def serialize_Router_bgp_network_ipv4_cfg_json(obj):
	output = OrderedDict()
	if obj.network_ipv4 is not None:
		output['network-ipv4'] = obj.network_ipv4
	if obj.backdoor_cfg is not None:
		output['backdoor-cfg'] = serialize_Router_bgp_network_ipv4_cfg__backdoor_cfg_json(obj.backdoor_cfg)
	if obj.network_desc is not None:
		output['network-desc'] = obj.network_desc
	if obj.mask_cfg is not None:
		output['mask-cfg'] = serialize_Router_bgp_network_ipv4_cfg__mask_cfg_json(obj.mask_cfg)
	if obj.network_route_map_cfg is not None:
		output['network-route-map-cfg'] = serialize_Router_bgp_network_ipv4_cfg__network_route_map_cfg_json(obj.network_route_map_cfg)
	return output

def serialize_list_Router_bgp_network_ipv4_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_network_ipv4_cfg_json(item))
	return output

def serialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_backdoor_cfg_json(obj):
	output = OrderedDict()
	if obj.net_prefix_backdoor is not None:
		output['net-prefix-backdoor'] = obj.net_prefix_backdoor
	if obj.net_prefix_backdoor_desc is not None:
		output['net-prefix-backdoor-desc'] = obj.net_prefix_backdoor_desc
	return output

def serialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg__net_prefix_rmap_backdoor_cfg_json(obj):
	output = OrderedDict()
	if obj.net_prefix_rmap_backdoor is not None:
		output['net-prefix-rmap-backdoor'] = obj.net_prefix_rmap_backdoor
	if obj.net_prefix_rmap_backdoor_desc is not None:
		output['net-prefix-rmap-backdoor-desc'] = obj.net_prefix_rmap_backdoor_desc
	return output

def serialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg_json(obj):
	output = OrderedDict()
	if obj.net_prefix_rmap is not None:
		output['net-prefix-rmap'] = obj.net_prefix_rmap
	if obj.net_prefix_rmap_backdoor_cfg is not None:
		output['net-prefix-rmap-backdoor-cfg'] = serialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg__net_prefix_rmap_backdoor_cfg_json(obj.net_prefix_rmap_backdoor_cfg)
	if obj.net_prefix_rmap_desc is not None:
		output['net-prefix-rmap-desc'] = obj.net_prefix_rmap_desc
	return output

def serialize_Router_bgp_network_ipv4_mask_cfg_json(obj):
	output = OrderedDict()
	if obj.net_prefix is not None:
		output['net-prefix'] = obj.net_prefix
	if obj.net_prefix_backdoor_cfg is not None:
		output['net-prefix-backdoor-cfg'] = serialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_backdoor_cfg_json(obj.net_prefix_backdoor_cfg)
	if obj.net_prefix_desc is not None:
		output['net-prefix-desc'] = obj.net_prefix_desc
	if obj.net_prefix_route_map_cfg is not None:
		output['net-prefix-route-map-cfg'] = serialize_Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg_json(obj.net_prefix_route_map_cfg)
	return output

def serialize_list_Router_bgp_network_ipv4_mask_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_network_ipv4_mask_cfg_json(item))
	return output

def serialize_Bgp__network_json(obj):
	output = OrderedDict()
	if obj.network_ipv4_cfg is not None:
		output['network-ipv4-cfg'] = serialize_list_Router_bgp_network_ipv4_cfg_json(obj.network_ipv4_cfg)
	if obj.network_ipv4_mask_cfg is not None:
		output['network-ipv4-mask-cfg'] = serialize_list_Router_bgp_network_ipv4_mask_cfg_json(obj.network_ipv4_mask_cfg)
	output['synchronization'] = obj.synchronization
	return output

def serialize_Bgp__timers__bgp_1_json(obj):
	output = OrderedDict()
	output['bgp-keepalive'] = obj.bgp_keepalive
	output['bgp-holdtime'] = obj.bgp_holdtime
	return output

def serialize_Bgp__timers_json(obj):
	output = OrderedDict()
	output['bgp-1'] = serialize_Bgp__timers__bgp_1_json(obj.bgp_1)
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg_json(obj):
	output = OrderedDict()
	output['allowas-in'] = obj.allowas_in
	if obj.allowas_in_count is not None:
		output['allowas-in-count'] = obj.allowas_in_count
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg_json(obj):
	output = OrderedDict()
	output['orf'] = obj.orf
	output['prefix-list'] = obj.prefix_list
	if obj.both is not None:
		output['both'] = obj.both
	output['receive'] = obj.receive
	output['send'] = obj.send
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability_json(obj):
	output = OrderedDict()
	output['dynamic'] = obj.dynamic
	if obj.neighbor_orf_cfg is not None:
		output['neighbor-orf-cfg'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg_json(obj.neighbor_orf_cfg)
	output['route-refresh'] = obj.route_refresh
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_default_originate_cfg_json(obj):
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

def serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg_json(obj):
	output = OrderedDict()
	output['maximum-prefix'] = obj.maximum_prefix
	if obj.maximum_prefix_thres is not None:
		output['maximum-prefix-thres'] = obj.maximum_prefix_thres
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg__nbr_str_pass_json(obj):
	output = OrderedDict()
	output['value'] = obj.value
	output['encrypted'] = obj.encrypted
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

def serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_send_community_cfg_json(obj):
	output = OrderedDict()
	output['send-community'] = obj.send_community
	if obj.both is not None:
		output['both'] = obj.both
	if obj.extended is not None:
		output['extended'] = obj.extended
	if obj.standard is not None:
		output['standard'] = obj.standard
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg_json(obj):
	output = OrderedDict()
	output['soft-reconfiguration'] = obj.soft_reconfiguration
	output['inbound'] = obj.inbound
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg_json(obj):
	output = OrderedDict()
	output['timers-keepalive'] = obj.timers_keepalive
	output['timers-holdtime'] = obj.timers_holdtime
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg_json(obj):
	output = OrderedDict()
	output['connect'] = obj.connect
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg__timers_json(obj):
	output = OrderedDict()
	if obj.neighbor_timers_keepalive_cfg is not None:
		output['neighbor-timers-keepalive-cfg'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg_json(obj.neighbor_timers_keepalive_cfg)
	if obj.timers_con_under_group_cfg is not None:
		output['timers-con-under-group-cfg'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg_json(obj.timers_con_under_group_cfg)
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_update_source_cfg_json(obj):
	output = OrderedDict()
	output['update-source'] = obj.update_source
	output['update-source-ip'] = obj.update_source_ip
	output['update-source-ipv6'] = obj.update_source_ipv6
	output['ethernet'] = obj.ethernet
	output['loopback'] = obj.loopback
	output['ve'] = obj.ve
	output['trunk'] = obj.trunk
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_version_cfg_json(obj):
	output = OrderedDict()
	output['version'] = obj.version
	output['4'] = obj.param_4
	return output

def serialize_Router_bgp_neighbor__neighbor_str_cfg_json(obj):
	output = OrderedDict()
	output['neighbor-str'] = obj.neighbor_str
	output['peer-group'] = obj.peer_group
	output['remote-as'] = obj.remote_as
	output['activate'] = obj.activate
	output['advertisement-interval'] = obj.advertisement_interval
	if obj.neighbor_allowas_in_cfg is not None:
		output['neighbor-allowas-in-cfg'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg_json(obj.neighbor_allowas_in_cfg)
	output['as-origination-interval'] = obj.as_origination_interval
	output['neighbor-capability'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability_json(obj.neighbor_capability)
	output['collide-established'] = obj.collide_established
	output['connection-retry-time'] = obj.connection_retry_time
	if obj.neighbor_default_originate_cfg is not None:
		output['neighbor-default-originate-cfg'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_default_originate_cfg_json(obj.neighbor_default_originate_cfg)
	output['disallow-infinite-holdtime'] = obj.disallow_infinite_holdtime
	if obj.neighbor_distribute_list_cfg is not None:
		output['neighbor-distribute-list-cfg'] = serialize_list_Router_bgp_neighbor_distribute_list_cfg_json(obj.neighbor_distribute_list_cfg)
	output['dont-capability-negotiate'] = obj.dont_capability_negotiate
	if obj.neighbor_ebgp_multihop_cfg is not None:
		output['neighbor-ebgp-multihop-cfg'] = serialize_list_Router_bgp_neighbor_ebgp_multihop_cfg_json(obj.neighbor_ebgp_multihop_cfg)
	output['enforce-multihop'] = obj.enforce_multihop
	if obj.neighbor_filter_list_cfg is not None:
		output['neighbor-filter-list-cfg'] = serialize_list_Router_bgp_neighbor_filter_list_cfg_json(obj.neighbor_filter_list_cfg)
	if obj.neighbor_maximum_prefix_cfg is not None:
		output['neighbor-maximum-prefix-cfg'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg_json(obj.neighbor_maximum_prefix_cfg)
	output['next-hop-self'] = obj.next_hop_self
	output['override-capability'] = obj.override_capability
	output['nbr-str-pass'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__nbr_str_pass_json(obj.nbr_str_pass)
	output['passive'] = obj.passive
	if obj.neighbor_prefix_list_cfg is not None:
		output['neighbor-prefix-list-cfg'] = serialize_list_Router_bgp_neighbor_prefix_list_cfg_json(obj.neighbor_prefix_list_cfg)
	output['remove-private-AS'] = obj.remove_private_as
	if obj.neighbor_route_map_cfg is not None:
		output['neighbor-route-map-cfg'] = serialize_list_Router_bgp_neighbor_route_map_cfg_json(obj.neighbor_route_map_cfg)
	if obj.neighbor_send_community_cfg is not None:
		output['neighbor-send-community-cfg'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_send_community_cfg_json(obj.neighbor_send_community_cfg)
	if obj.neighbor_soft_reconfiguration_cfg is not None:
		output['neighbor-soft-reconfiguration-cfg'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg_json(obj.neighbor_soft_reconfiguration_cfg)
	output['shutdown'] = obj.shutdown
	output['strict-capability-match'] = obj.strict_capability_match
	output['timers'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__timers_json(obj.timers)
	output['unsuppress-map'] = obj.unsuppress_map
	if obj.neighbor_update_source_cfg is not None:
		output['neighbor-update-source-cfg'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_update_source_cfg_json(obj.neighbor_update_source_cfg)
	if obj.neighbor_version_cfg is not None:
		output['neighbor-version-cfg'] = serialize_Router_bgp_neighbor__neighbor_str_cfg__neighbor_version_cfg_json(obj.neighbor_version_cfg)
	output['weight'] = obj.weight
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__allowas_in_cfg_json(obj):
	output = OrderedDict()
	output['allowas-in'] = obj.allowas_in
	if obj.allowas_in_count is not None:
		output['allowas-in-count'] = obj.allowas_in_count
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg_json(obj):
	output = OrderedDict()
	output['orf'] = obj.orf
	output['prefix-list'] = obj.prefix_list
	if obj.both is not None:
		output['both'] = obj.both
	output['receive'] = obj.receive
	output['send'] = obj.send
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1_json(obj):
	output = OrderedDict()
	output['dynamic'] = obj.dynamic
	if obj.orf_cfg is not None:
		output['orf-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg_json(obj.orf_cfg)
	output['route-refresh'] = obj.route_refresh
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__default_originate_cfg_json(obj):
	output = OrderedDict()
	output['default-originate'] = obj.default_originate
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Router_bgp_distribute_list_cfg_json(obj):
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

def serialize_list_Router_bgp_distribute_list_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_distribute_list_cfg_json(item))
	return output

def serialize_Router_bgp_ebgp_multihop_cfg_json(obj):
	output = OrderedDict()
	if obj.ebgp_multihop is not None:
		output['ebgp-multihop'] = obj.ebgp_multihop
	if obj.ebgp_multihop_hop_count is not None:
		output['ebgp-multihop-hop-count'] = obj.ebgp_multihop_hop_count
	return output

def serialize_list_Router_bgp_ebgp_multihop_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_ebgp_multihop_cfg_json(item))
	return output

def serialize_Router_bgp_filter_list_cfg_json(obj):
	output = OrderedDict()
	if obj.filter_list is not None:
		output['filter-list'] = obj.filter_list
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.out is not None:
		output['out'] = obj.out
	return output

def serialize_list_Router_bgp_filter_list_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_filter_list_cfg_json(item))
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg_json(obj):
	output = OrderedDict()
	output['maximum-prefix'] = obj.maximum_prefix
	if obj.maximum_prefix_thres is not None:
		output['maximum-prefix-thres'] = obj.maximum_prefix_thres
	return output

def serialize_Router_bgp_prefix_list_cfg_json(obj):
	output = OrderedDict()
	output['prefix-list'] = obj.prefix_list
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.out is not None:
		output['out'] = obj.out
	return output

def serialize_list_Router_bgp_prefix_list_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_prefix_list_cfg_json(item))
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass_json(obj):
	output = OrderedDict()
	output['nbr-ipv4-pass-value'] = obj.nbr_ipv4_pass_value
	output['nbr-ipv4-pass-encrypted'] = obj.nbr_ipv4_pass_encrypted
	return output

def serialize_Router_bgp_route_map_cfg_json(obj):
	output = OrderedDict()
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	if obj.py_kw_rsvd_in is not None:
		output['in'] = obj.py_kw_rsvd_in
	if obj.out is not None:
		output['out'] = obj.out
	return output

def serialize_list_Router_bgp_route_map_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_route_map_cfg_json(item))
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__send_community_cfg_json(obj):
	output = OrderedDict()
	output['send-community'] = obj.send_community
	if obj.both is not None:
		output['both'] = obj.both
	if obj.extended is not None:
		output['extended'] = obj.extended
	if obj.standard is not None:
		output['standard'] = obj.standard
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg_json(obj):
	output = OrderedDict()
	output['soft-reconfiguration'] = obj.soft_reconfiguration
	output['inbound'] = obj.inbound
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5_json(obj):
	output = OrderedDict()
	output['md5-value'] = obj.md5_value
	output['md5-encrypted'] = obj.md5_encrypted
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5_json(obj):
	output = OrderedDict()
	output['meticulous-md5-value'] = obj.meticulous_md5_value
	output['meticulous-md5-encrypted'] = obj.meticulous_md5_encrypted
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1_json(obj):
	output = OrderedDict()
	output['meticulous-sha1-value'] = obj.meticulous_sha1_value
	output['meticulous-sha1-encrypted'] = obj.meticulous_sha1_encrypted
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1_json(obj):
	output = OrderedDict()
	output['sha1-value'] = obj.sha1_value
	output['sha1-encrypted'] = obj.sha1_encrypted
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple_json(obj):
	output = OrderedDict()
	output['simple-value'] = obj.simple_value
	output['simple-encrypted'] = obj.simple_encrypted
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg_json(obj):
	output = OrderedDict()
	output['key-id'] = obj.key_id
	output['md5'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5_json(obj.md5)
	output['meticulous-md5'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5_json(obj.meticulous_md5)
	output['meticulous-sha1'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1_json(obj.meticulous_sha1)
	output['sha1'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1_json(obj.sha1)
	output['simple'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple_json(obj.simple)
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication_json(obj):
	output = OrderedDict()
	if obj.key_id_cfg is not None:
		output['key-id-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg_json(obj.key_id_cfg)
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg_json(obj):
	output = OrderedDict()
	output['bfd'] = obj.bfd
	if obj.authentication is not None:
		output['authentication'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication_json(obj.authentication)
	if obj.multihop is not None:
		output['multihop'] = obj.multihop
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg_json(obj):
	output = OrderedDict()
	output['fall-over'] = obj.fall_over
	if obj.bfd_cfg is not None:
		output['bfd-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg_json(obj.bfd_cfg)
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg_json(obj):
	output = OrderedDict()
	output['neighbor-ipv4-timers-keepalive'] = obj.neighbor_ipv4_timers_keepalive
	output['timers-holdtime'] = obj.timers_holdtime
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg_json(obj):
	output = OrderedDict()
	output['connect'] = obj.connect
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers_json(obj):
	output = OrderedDict()
	if obj.timers_keepalive_cfg is not None:
		output['timers-keepalive-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg_json(obj.timers_keepalive_cfg)
	if obj.timers_con_cfg is not None:
		output['timers-con-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg_json(obj.timers_con_cfg)
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__update_source_cfg_json(obj):
	output = OrderedDict()
	output['update-source'] = obj.update_source
	output['update-source-ip'] = obj.update_source_ip
	output['update-source-ipv6'] = obj.update_source_ipv6
	output['ethernet'] = obj.ethernet
	output['loopback'] = obj.loopback
	output['ve'] = obj.ve
	output['trunk'] = obj.trunk
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__version_cfg_json(obj):
	output = OrderedDict()
	output['version'] = obj.version
	output['4'] = obj.param_4
	return output

def serialize_Router_bgp_neighbor__neighbor_ipv4_cfg_json(obj):
	output = OrderedDict()
	output['neighbor-ipv4'] = obj.neighbor_ipv4
	output['neighbor-ipv6'] = obj.neighbor_ipv6
	output['remote-as'] = obj.remote_as
	output['peer-group'] = obj.peer_group
	output['activate'] = obj.activate
	output['advertisement-interval'] = obj.advertisement_interval
	if obj.allowas_in_cfg is not None:
		output['allowas-in-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__allowas_in_cfg_json(obj.allowas_in_cfg)
	output['as-origination-interval'] = obj.as_origination_interval
	output['capability-1'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1_json(obj.capability_1)
	output['collide-established'] = obj.collide_established
	output['connection-retry-time'] = obj.connection_retry_time
	if obj.default_originate_cfg is not None:
		output['default-originate-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__default_originate_cfg_json(obj.default_originate_cfg)
	output['disallow-infinite-holdtime'] = obj.disallow_infinite_holdtime
	if obj.distribute_list_cfg is not None:
		output['distribute-list-cfg'] = serialize_list_Router_bgp_distribute_list_cfg_json(obj.distribute_list_cfg)
	output['dont-capability-negotiate'] = obj.dont_capability_negotiate
	if obj.ebgp_multihop_cfg is not None:
		output['ebgp-multihop-cfg'] = serialize_list_Router_bgp_ebgp_multihop_cfg_json(obj.ebgp_multihop_cfg)
	output['enforce-multihop'] = obj.enforce_multihop
	if obj.filter_list_cfg is not None:
		output['filter-list-cfg'] = serialize_list_Router_bgp_filter_list_cfg_json(obj.filter_list_cfg)
	if obj.maximum_prefix_cfg is not None:
		output['maximum-prefix-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg_json(obj.maximum_prefix_cfg)
	output['next-hop-self'] = obj.next_hop_self
	output['override-capability'] = obj.override_capability
	output['passive'] = obj.passive
	if obj.prefix_list_cfg is not None:
		output['prefix-list-cfg'] = serialize_list_Router_bgp_prefix_list_cfg_json(obj.prefix_list_cfg)
	output['remove-private-AS'] = obj.remove_private_as
	output['nbr-ipv4-pass'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass_json(obj.nbr_ipv4_pass)
	if obj.route_map_cfg is not None:
		output['route-map-cfg'] = serialize_list_Router_bgp_route_map_cfg_json(obj.route_map_cfg)
	if obj.send_community_cfg is not None:
		output['send-community-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__send_community_cfg_json(obj.send_community_cfg)
	if obj.soft_reconfiguration_cfg is not None:
		output['soft-reconfiguration-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg_json(obj.soft_reconfiguration_cfg)
	output['shutdown'] = obj.shutdown
	if obj.fall_over_cfg is not None:
		output['fall-over-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg_json(obj.fall_over_cfg)
	output['strict-capability-match'] = obj.strict_capability_match
	output['neighbor-ipv4-timers'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers_json(obj.neighbor_ipv4_timers)
	output['unsuppress-map'] = obj.unsuppress_map
	if obj.update_source_cfg is not None:
		output['update-source-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__update_source_cfg_json(obj.update_source_cfg)
	if obj.version_cfg is not None:
		output['version-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg__version_cfg_json(obj.version_cfg)
	output['weight'] = obj.weight
	return output

def serialize_Router_bgp_neighbor_json(obj):
	output = OrderedDict()
	output['neighbor-str-cfg'] = serialize_Router_bgp_neighbor__neighbor_str_cfg_json(obj.neighbor_str_cfg)
	if obj.neighbor_ipv4_cfg is not None:
		output['neighbor-ipv4-cfg'] = serialize_Router_bgp_neighbor__neighbor_ipv4_cfg_json(obj.neighbor_ipv4_cfg)
	return output

def serialize_list_Router_bgp_neighbor_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_neighbor_json(item))
	return output

def serialize_Bgp__redistribute__connected_cfg_json(obj):
	output = OrderedDict()
	if obj.connected is not None:
		output['connected'] = obj.connected
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Bgp__redistribute__floating_ip_cfg_json(obj):
	output = OrderedDict()
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Bgp__redistribute__ip_nat_cfg_json(obj):
	output = OrderedDict()
	if obj.ip_nat is not None:
		output['ip-nat'] = obj.ip_nat
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Bgp__redistribute__ip_nat_list_cfg_json(obj):
	output = OrderedDict()
	if obj.ip_nat_list is not None:
		output['ip-nat-list'] = obj.ip_nat_list
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Bgp__redistribute__isis_cfg_json(obj):
	output = OrderedDict()
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Bgp__redistribute__kernel_cfg_json(obj):
	output = OrderedDict()
	if obj.kernel is not None:
		output['kernel'] = obj.kernel
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Bgp__redistribute__ospf_cfg_json(obj):
	output = OrderedDict()
	if obj.ospf is not None:
		output['ospf'] = obj.ospf
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Bgp__redistribute__rip_cfg_json(obj):
	output = OrderedDict()
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Bgp__redistribute__static_cfg_json(obj):
	output = OrderedDict()
	if obj.static is not None:
		output['static'] = obj.static
	if obj.route_map is not None:
		output['route-map'] = obj.route_map
	return output

def serialize_Bgp__redistribute_json(obj):
	output = OrderedDict()
	if obj.connected_cfg is not None:
		output['connected-cfg'] = serialize_Bgp__redistribute__connected_cfg_json(obj.connected_cfg)
	if obj.floating_ip_cfg is not None:
		output['floating-ip-cfg'] = serialize_Bgp__redistribute__floating_ip_cfg_json(obj.floating_ip_cfg)
	if obj.ip_nat_cfg is not None:
		output['ip-nat-cfg'] = serialize_Bgp__redistribute__ip_nat_cfg_json(obj.ip_nat_cfg)
	if obj.ip_nat_list_cfg is not None:
		output['ip-nat-list-cfg'] = serialize_Bgp__redistribute__ip_nat_list_cfg_json(obj.ip_nat_list_cfg)
	if obj.isis_cfg is not None:
		output['isis-cfg'] = serialize_Bgp__redistribute__isis_cfg_json(obj.isis_cfg)
	if obj.kernel_cfg is not None:
		output['kernel-cfg'] = serialize_Bgp__redistribute__kernel_cfg_json(obj.kernel_cfg)
	if obj.ospf_cfg is not None:
		output['ospf-cfg'] = serialize_Bgp__redistribute__ospf_cfg_json(obj.ospf_cfg)
	if obj.rip_cfg is not None:
		output['rip-cfg'] = serialize_Bgp__redistribute__rip_cfg_json(obj.rip_cfg)
	if obj.static_cfg is not None:
		output['static-cfg'] = serialize_Bgp__redistribute__static_cfg_json(obj.static_cfg)
	return output

def serialize_Router_bgp_address_family_ipv6_neighbor_json(obj):
	output = OrderedDict()
	return output

def serialize_list_Router_bgp_address_family_ipv6_neighbor_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Router_bgp_address_family_ipv6_neighbor_json(item))
	return output

def serialize_Bgp__address_family__ipv6__redistribute_json(obj):
	output = OrderedDict()
	return output

def serialize_Bgp__address_family__ipv6_json(obj):
	output = OrderedDict()
	if obj.neighborlist is not None:
		output['neighborList'] = serialize_list_Router_bgp_address_family_ipv6_neighbor_json(obj.neighborlist)
	if obj.redistribute is not None:
		output['redistribute'] = serialize_Bgp__address_family__ipv6__redistribute_json(obj.redistribute)
	return output

def serialize_Bgp__address_family_json(obj):
	output = OrderedDict()
	if obj.ipv6 is not None:
		output['ipv6'] = serialize_Bgp__address_family__ipv6_json(obj.ipv6)
	return output

def serialize_Bgp_json(obj):
	output = OrderedDict()
	output['process-id'] = obj.process_id
	if obj.aggregate_address_cfg is not None:
		output['aggregate-address-cfg'] = serialize_list_Router_bgp_aggregate_address_cfg_json(obj.aggregate_address_cfg)
	output['bgp'] = serialize_Bgp__bgp_json(obj.bgp)
	output['distance'] = serialize_Bgp__distance_json(obj.distance)
	output['maximum-paths'] = serialize_Bgp__maximum_paths_json(obj.maximum_paths)
	output['network'] = serialize_Bgp__network_json(obj.network)
	output['timers'] = serialize_Bgp__timers_json(obj.timers)
	output['synchronization'] = obj.synchronization
	output['auto-summary'] = obj.auto_summary
	if obj.neighborlist is not None:
		output['neighborList'] = serialize_list_Router_bgp_neighbor_json(obj.neighborlist)
	if obj.redistribute is not None:
		output['redistribute'] = serialize_Bgp__redistribute_json(obj.redistribute)
	if obj.address_family is not None:
		output['address-family'] = serialize_Bgp__address_family_json(obj.address_family)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Bgp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Bgp_json(item))
	return list(container)

class Bgp__bgp__dampening_cfg__dampening_half_time_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dampening_half_time=PosRangedInteger(1, 45)
	dampening_reuse=PosRangedInteger(1, 20000)
	dampening_supress=PosRangedInteger(1, 20000)
	dampening_max_supress=PosRangedInteger(1, 255)
	dampening_penalty=PosRangedInteger(1, 45)
	def __init__(self, dampening_supress, dampening_max_supress, dampening_half_time=None, dampening_reuse=None, dampening_penalty=None):
		self.dampening_half_time = dampening_half_time
		self.dampening_reuse = dampening_reuse
		self.dampening_supress = dampening_supress
		self.dampening_max_supress = dampening_max_supress
		self.dampening_penalty = dampening_penalty

	def __str__(self):
		return str(self.dampening_supress) + '+' + str(self.dampening_max_supress)

class Bgp__bgp__dampening_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dampening=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, dampening, dampening_half_time_cfg=None, route_map=None):
		self.dampening = dampening
		self.dampening_half_time_cfg = dampening_half_time_cfg
		self.route_map = route_map

	def __str__(self):
		return str(self.dampening)

class Bgp__bgp__default__local_preference(AxapiObject):
	__metaclass__ = StructMeta 
	local_preference_value=PosRangedInteger(0, 4294967295)
	def __init__(self, local_preference_value):
		self.local_preference_value = local_preference_value

	def __str__(self):
		return str(self.local_preference_value)

class Bgp__bgp__default(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4_unicast=PosRangedInteger(0, 1)
	def __init__(self, ipv4_unicast, local_preference):
		self.ipv4_unicast = ipv4_unicast
		self.local_preference = local_preference

	def __str__(self):
		return str(self.ipv4_unicast) + '+' + str(self.local_preference)

class Bgp__bgp(AxapiObject):
	__metaclass__ = StructMeta 
	always_compare_med=PosRangedInteger(0, 1)
	deterministic_med=PosRangedInteger(0, 1)
	enforce_first_as=PosRangedInteger(0, 1)
	fast_external_failover=PosRangedInteger(0, 1)
	log_neighbor_changes=PosRangedInteger(0, 1)
	nexthop_trigger_count=PosRangedInteger(0, 127)
	router_id = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	scan_time=PosRangedInteger(0, 60)
	def __init__(self, always_compare_med, default, deterministic_med, enforce_first_as, fast_external_failover, log_neighbor_changes, nexthop_trigger_count, router_id, scan_time, bestpath_cfg=None, dampening_cfg=None):
		self.always_compare_med = always_compare_med
		self.bestpath_cfg = bestpath_cfg
		self.dampening_cfg = dampening_cfg
		self.default = default
		self.deterministic_med = deterministic_med
		self.enforce_first_as = enforce_first_as
		self.fast_external_failover = fast_external_failover
		self.log_neighbor_changes = log_neighbor_changes
		self.nexthop_trigger_count = nexthop_trigger_count
		self.router_id = router_id
		self.scan_time = scan_time

	def __str__(self):
		return str(self.always_compare_med) + '+' + str(self.default) + '+' + str(self.deterministic_med) + '+' + str(self.enforce_first_as) + '+' + str(self.fast_external_failover) + '+' + str(self.log_neighbor_changes) + '+' + str(self.nexthop_trigger_count) + '+' + str(self.router_id) + '+' + str(self.scan_time)

class Bgp__distance__admin_distance_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	admin_distance=PosRangedInteger(1, 255)
	src_prefix = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	acl_str=SizedString(1, 255)
	def __init__(self, admin_distance, src_prefix, acl_str=None):
		self.admin_distance = admin_distance
		self.src_prefix = src_prefix
		self.acl_str = acl_str

	def __str__(self):
		return str(self.admin_distance) + '+' + str(self.src_prefix)

class Bgp__distance__distance_bgp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	bgp=PosRangedInteger(0, 1)
	ext_routes_dist=PosRangedInteger(1, 255)
	int_routes_dist=PosRangedInteger(1, 255)
	local_routes_dist=PosRangedInteger(1, 255)
	def __init__(self, bgp, ext_routes_dist, int_routes_dist, local_routes_dist):
		self.bgp = bgp
		self.ext_routes_dist = ext_routes_dist
		self.int_routes_dist = int_routes_dist
		self.local_routes_dist = local_routes_dist

	def __str__(self):
		return str(self.bgp) + '+' + str(self.ext_routes_dist) + '+' + str(self.int_routes_dist) + '+' + str(self.local_routes_dist)

class Bgp__distance(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, admin_distance_cfg=None, distance_bgp_cfg=None):
		self.admin_distance_cfg = admin_distance_cfg
		self.distance_bgp_cfg = distance_bgp_cfg

	def __str__(self):
		return ""

class Bgp__maximum_paths(AxapiObject):
	__metaclass__ = StructMeta 
	value=PosRangedInteger(1, 10)
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return str(self.value)

class Bgp__network(AxapiObject):
	__metaclass__ = StructMeta 
	synchronization=PosRangedInteger(0, 1)
	def __init__(self, synchronization, network_ipv4_cfg=None, network_ipv4_mask_cfg=None):
		self.network_ipv4_cfg = network_ipv4_cfg
		self.network_ipv4_mask_cfg = network_ipv4_mask_cfg
		self.synchronization = synchronization

	def __str__(self):
		return str(self.synchronization)

class Bgp__timers__bgp_1(AxapiObject):
	__metaclass__ = StructMeta 
	bgp_keepalive=PosRangedInteger(0, 65535)
	bgp_holdtime=PosRangedInteger(0, 65535)
	def __init__(self, bgp_keepalive, bgp_holdtime):
		self.bgp_keepalive = bgp_keepalive
		self.bgp_holdtime = bgp_holdtime

	def __str__(self):
		return str(self.bgp_keepalive) + '+' + str(self.bgp_holdtime)

class Bgp__timers(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, bgp_1):
		self.bgp_1 = bgp_1

	def __str__(self):
		return str(self.bgp_1)

class Bgp__redistribute__connected_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	connected=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, connected=None, route_map=None):
		self.connected = connected
		self.route_map = route_map

	def __str__(self):
		return ""

class Bgp__redistribute__floating_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	route_map=SizedString(1, 255)
	def __init__(self, route_map=None):
		self.route_map = route_map

	def __str__(self):
		return ""

class Bgp__redistribute__ip_nat_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip_nat=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, ip_nat=None, route_map=None):
		self.ip_nat = ip_nat
		self.route_map = route_map

	def __str__(self):
		return ""

class Bgp__redistribute__ip_nat_list_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip_nat_list=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, ip_nat_list=None, route_map=None):
		self.ip_nat_list = ip_nat_list
		self.route_map = route_map

	def __str__(self):
		return ""

class Bgp__redistribute__isis_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	route_map=SizedString(1, 255)
	def __init__(self, route_map=None):
		self.route_map = route_map

	def __str__(self):
		return ""

class Bgp__redistribute__kernel_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	kernel=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, kernel=None, route_map=None):
		self.kernel = kernel
		self.route_map = route_map

	def __str__(self):
		return ""

class Bgp__redistribute__ospf_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ospf=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, ospf=None, route_map=None):
		self.ospf = ospf
		self.route_map = route_map

	def __str__(self):
		return ""

class Bgp__redistribute__rip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	route_map=SizedString(1, 255)
	def __init__(self, route_map=None):
		self.route_map = route_map

	def __str__(self):
		return ""

class Bgp__redistribute__static_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	static=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, static=None, route_map=None):
		self.static = static
		self.route_map = route_map

	def __str__(self):
		return ""

class Bgp__redistribute(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, connected_cfg=None, floating_ip_cfg=None, ip_nat_cfg=None, ip_nat_list_cfg=None, isis_cfg=None, kernel_cfg=None, ospf_cfg=None, rip_cfg=None, static_cfg=None):
		self.connected_cfg = connected_cfg
		self.floating_ip_cfg = floating_ip_cfg
		self.ip_nat_cfg = ip_nat_cfg
		self.ip_nat_list_cfg = ip_nat_list_cfg
		self.isis_cfg = isis_cfg
		self.kernel_cfg = kernel_cfg
		self.ospf_cfg = ospf_cfg
		self.rip_cfg = rip_cfg
		self.static_cfg = static_cfg

	def __str__(self):
		return ""

class Bgp__address_family__ipv6__redistribute(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class Bgp__address_family__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, neighborlist=None, redistribute=None):
		self.neighborlist = neighborlist
		self.redistribute = redistribute

	def __str__(self):
		return ""

class Bgp__address_family(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ipv6=None):
		self.ipv6 = ipv6

	def __str__(self):
		return ""

class Bgp(AxapiObject):
	__metaclass__ = StructMeta 
	process_id=PosRangedInteger(1, 4294967295)
	synchronization=PosInteger()
	auto_summary=PosRangedInteger(0, 1)
	def __init__(self, process_id, bgp, distance, maximum_paths, network, timers, synchronization, auto_summary, aggregate_address_cfg=None, neighborlist=None, redistribute=None, address_family=None):
		self.process_id = process_id
		self.aggregate_address_cfg = aggregate_address_cfg
		self.bgp = bgp
		self.distance = distance
		self.maximum_paths = maximum_paths
		self.network = network
		self.timers = timers
		self.synchronization = synchronization
		self.auto_summary = auto_summary
		self.neighborlist = neighborlist
		self.redistribute = redistribute
		self.address_family = address_family

	def __str__(self):
		return str(self.process_id) + '+' + str(self.bgp) + '+' + str(self.distance) + '+' + str(self.maximum_paths) + '+' + str(self.network) + '+' + str(self.timers) + '+' + str(self.synchronization) + '+' + str(self.auto_summary)

class Router_bgp_aggregate_address_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	aggregate_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	as_set=PosRangedInteger(0, 1)
	summary_only=PosRangedInteger(0, 1)
	def __init__(self, aggregate_address=None, as_set=None, summary_only=None):
		self.aggregate_address = aggregate_address
		self.as_set = as_set
		self.summary_only = summary_only

	def __str__(self):
		return ""

class Router_bgp_bestpath_cfg__as_path_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	as_path=PosRangedInteger(0, 1)
	ignore=PosRangedInteger(0, 1)
	def __init__(self, as_path=None, ignore=None):
		self.as_path = as_path
		self.ignore = ignore

	def __str__(self):
		return ""

class Router_bgp_bestpath_cfg__med_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	med=PosRangedInteger(0, 1)
	remove_recv_med=PosRangedInteger(0, 1)
	remove_send_med=PosRangedInteger(0, 1)
	confed=PosRangedInteger(0, 1)
	missing_as_worst=PosRangedInteger(0, 1)
	def __init__(self, med=None, remove_recv_med=None, remove_send_med=None, confed=None, missing_as_worst=None):
		self.med = med
		self.remove_recv_med = remove_recv_med
		self.remove_send_med = remove_send_med
		self.confed = confed
		self.missing_as_worst = missing_as_worst

	def __str__(self):
		return ""

class Router_bgp_bestpath_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	bestpath=PosRangedInteger(0, 1)
	compare_routerid=PosRangedInteger(0, 1)
	def __init__(self, bestpath=None, as_path_cfg=None, compare_routerid=None, med_cfg=None):
		self.bestpath = bestpath
		self.as_path_cfg = as_path_cfg
		self.compare_routerid = compare_routerid
		self.med_cfg = med_cfg

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_cfg__backdoor_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	network_backdoor=PosRangedInteger(0, 1)
	network_backdoor_desc=SizedString(1, 255)
	def __init__(self, network_backdoor=None, network_backdoor_desc=None):
		self.network_backdoor = network_backdoor
		self.network_backdoor_desc = network_backdoor_desc

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_backdoor_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	network_mask_backdoor=PosRangedInteger(0, 1)
	network_mask_backdoor_desc=SizedString(1, 255)
	def __init__(self, network_mask_backdoor=None, network_mask_backdoor_desc=None):
		self.network_mask_backdoor = network_mask_backdoor
		self.network_mask_backdoor_desc = network_mask_backdoor_desc

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg__network_mask_rmap_backdoor_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	network_mask_rmap_backdoor=PosRangedInteger(0, 1)
	network_mask_rmap_backdoor_desc=SizedString(1, 255)
	def __init__(self, network_mask_rmap_backdoor=None, network_mask_rmap_backdoor_desc=None):
		self.network_mask_rmap_backdoor = network_mask_rmap_backdoor
		self.network_mask_rmap_backdoor_desc = network_mask_rmap_backdoor_desc

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_cfg__mask_cfg__network_mask_route_map_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	network_mask_rmap=SizedString(1, 255)
	network_mask_rmap_desc=SizedString(1, 255)
	def __init__(self, network_mask_rmap=None, network_mask_rmap_backdoor_cfg=None, network_mask_rmap_desc=None):
		self.network_mask_rmap = network_mask_rmap
		self.network_mask_rmap_backdoor_cfg = network_mask_rmap_backdoor_cfg
		self.network_mask_rmap_desc = network_mask_rmap_desc

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_cfg__mask_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	network_mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	network_mask_desc=SizedString(1, 255)
	def __init__(self, network_mask=None, network_mask_backdoor_cfg=None, network_mask_desc=None, network_mask_route_map_cfg=None):
		self.network_mask = network_mask
		self.network_mask_backdoor_cfg = network_mask_backdoor_cfg
		self.network_mask_desc = network_mask_desc
		self.network_mask_route_map_cfg = network_mask_route_map_cfg

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_cfg__network_route_map_cfg__network_rmap_backdoor_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	network_rmap_backdoor=PosRangedInteger(0, 1)
	network_mask_rmap_backdoor_desc=SizedString(1, 255)
	def __init__(self, network_rmap_backdoor=None, network_mask_rmap_backdoor_desc=None):
		self.network_rmap_backdoor = network_rmap_backdoor
		self.network_mask_rmap_backdoor_desc = network_mask_rmap_backdoor_desc

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_cfg__network_route_map_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	network_rmap=SizedString(1, 255)
	network_rmap_desc=SizedString(1, 255)
	def __init__(self, network_rmap=None, network_rmap_backdoor_cfg=None, network_rmap_desc=None):
		self.network_rmap = network_rmap
		self.network_rmap_backdoor_cfg = network_rmap_backdoor_cfg
		self.network_rmap_desc = network_rmap_desc

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	network_ipv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	network_desc=SizedString(1, 255)
	def __init__(self, network_ipv4=None, backdoor_cfg=None, network_desc=None, mask_cfg=None, network_route_map_cfg=None):
		self.network_ipv4 = network_ipv4
		self.backdoor_cfg = backdoor_cfg
		self.network_desc = network_desc
		self.mask_cfg = mask_cfg
		self.network_route_map_cfg = network_route_map_cfg

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_mask_cfg__net_prefix_backdoor_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	net_prefix_backdoor=PosRangedInteger(0, 1)
	net_prefix_backdoor_desc=SizedString(1, 255)
	def __init__(self, net_prefix_backdoor=None, net_prefix_backdoor_desc=None):
		self.net_prefix_backdoor = net_prefix_backdoor
		self.net_prefix_backdoor_desc = net_prefix_backdoor_desc

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg__net_prefix_rmap_backdoor_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	net_prefix_rmap_backdoor=PosRangedInteger(0, 1)
	net_prefix_rmap_backdoor_desc=SizedString(1, 255)
	def __init__(self, net_prefix_rmap_backdoor=None, net_prefix_rmap_backdoor_desc=None):
		self.net_prefix_rmap_backdoor = net_prefix_rmap_backdoor
		self.net_prefix_rmap_backdoor_desc = net_prefix_rmap_backdoor_desc

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_mask_cfg__net_prefix_route_map_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	net_prefix_rmap=SizedString(1, 255)
	net_prefix_rmap_desc=SizedString(1, 255)
	def __init__(self, net_prefix_rmap=None, net_prefix_rmap_backdoor_cfg=None, net_prefix_rmap_desc=None):
		self.net_prefix_rmap = net_prefix_rmap
		self.net_prefix_rmap_backdoor_cfg = net_prefix_rmap_backdoor_cfg
		self.net_prefix_rmap_desc = net_prefix_rmap_desc

	def __str__(self):
		return ""

class Router_bgp_network_ipv4_mask_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	net_prefix = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	net_prefix_desc=SizedString(1, 255)
	def __init__(self, net_prefix=None, net_prefix_backdoor_cfg=None, net_prefix_desc=None, net_prefix_route_map_cfg=None):
		self.net_prefix = net_prefix
		self.net_prefix_backdoor_cfg = net_prefix_backdoor_cfg
		self.net_prefix_desc = net_prefix_desc
		self.net_prefix_route_map_cfg = net_prefix_route_map_cfg

	def __str__(self):
		return ""

class Router_bgp_neighbor__neighbor_str_cfg__neighbor_allowas_in_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	allowas_in=PosRangedInteger(0, 1)
	allowas_in_count=PosRangedInteger(1, 10)
	def __init__(self, allowas_in, allowas_in_count=None):
		self.allowas_in = allowas_in
		self.allowas_in_count = allowas_in_count

	def __str__(self):
		return str(self.allowas_in)

class Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability__neighbor_orf_cfg(AxapiObject):
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

class Router_bgp_neighbor__neighbor_str_cfg__neighbor_capability(AxapiObject):
	__metaclass__ = StructMeta 
	dynamic=PosRangedInteger(0, 1)
	route_refresh=PosRangedInteger(0, 1)
	def __init__(self, dynamic, route_refresh, neighbor_orf_cfg=None):
		self.dynamic = dynamic
		self.neighbor_orf_cfg = neighbor_orf_cfg
		self.route_refresh = route_refresh

	def __str__(self):
		return str(self.dynamic) + '+' + str(self.route_refresh)

class Router_bgp_neighbor__neighbor_str_cfg__neighbor_default_originate_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	default_originate=PosRangedInteger(0, 1)
	route_map=SizedString(1, 255)
	def __init__(self, default_originate, route_map=None):
		self.default_originate = default_originate
		self.route_map = route_map

	def __str__(self):
		return str(self.default_originate)

class Router_bgp_neighbor__neighbor_str_cfg__neighbor_maximum_prefix_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	maximum_prefix=PosRangedInteger(1, 65536)
	maximum_prefix_thres=PosRangedInteger(1, 100)
	def __init__(self, maximum_prefix, maximum_prefix_thres=None):
		self.maximum_prefix = maximum_prefix
		self.maximum_prefix_thres = maximum_prefix_thres

	def __str__(self):
		return str(self.maximum_prefix)

class Router_bgp_neighbor__neighbor_str_cfg__nbr_str_pass(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 80)
	encrypted=SizedString(1, 255)
	def __init__(self, value, encrypted):
		self.value = value
		self.encrypted = encrypted

	def __str__(self):
		return str(self.value) + '+' + str(self.encrypted)

class Router_bgp_neighbor__neighbor_str_cfg__neighbor_send_community_cfg(AxapiObject):
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

class Router_bgp_neighbor__neighbor_str_cfg__neighbor_soft_reconfiguration_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	soft_reconfiguration=PosRangedInteger(0, 1)
	inbound=PosRangedInteger(0, 1)
	def __init__(self, soft_reconfiguration, inbound):
		self.soft_reconfiguration = soft_reconfiguration
		self.inbound = inbound

	def __str__(self):
		return str(self.soft_reconfiguration) + '+' + str(self.inbound)

class Router_bgp_neighbor__neighbor_str_cfg__timers__neighbor_timers_keepalive_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	timers_keepalive=PosRangedInteger(0, 65535)
	timers_holdtime=PosRangedInteger(0, 65535)
	def __init__(self, timers_keepalive, timers_holdtime):
		self.timers_keepalive = timers_keepalive
		self.timers_holdtime = timers_holdtime

	def __str__(self):
		return str(self.timers_keepalive) + '+' + str(self.timers_holdtime)

class Router_bgp_neighbor__neighbor_str_cfg__timers__timers_con_under_group_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	connect=PosRangedInteger(1, 65535)
	def __init__(self, connect):
		self.connect = connect

	def __str__(self):
		return str(self.connect)

class Router_bgp_neighbor__neighbor_str_cfg__timers(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, neighbor_timers_keepalive_cfg=None, timers_con_under_group_cfg=None):
		self.neighbor_timers_keepalive_cfg = neighbor_timers_keepalive_cfg
		self.timers_con_under_group_cfg = timers_con_under_group_cfg

	def __str__(self):
		return ""

class Router_bgp_neighbor__neighbor_str_cfg__neighbor_update_source_cfg(AxapiObject):
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

class Router_bgp_neighbor__neighbor_str_cfg__neighbor_version_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	version=PosRangedInteger(0, 1)
	param_4=PosRangedInteger(0, 1)
	def __init__(self, version, param_4):
		self.version = version
		self.param_4 = param_4

	def __str__(self):
		return str(self.version) + '+' + str(self.param_4)

class Router_bgp_neighbor__neighbor_str_cfg(AxapiObject):
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

class Router_bgp_neighbor__neighbor_ipv4_cfg__allowas_in_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	allowas_in=PosInteger()
	allowas_in_count=PosRangedInteger(1, 10)
	def __init__(self, allowas_in, allowas_in_count=None):
		self.allowas_in = allowas_in
		self.allowas_in_count = allowas_in_count

	def __str__(self):
		return str(self.allowas_in)

class Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1__orf_cfg(AxapiObject):
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

class Router_bgp_neighbor__neighbor_ipv4_cfg__capability_1(AxapiObject):
	__metaclass__ = StructMeta 
	dynamic=PosInteger()
	route_refresh=PosInteger()
	def __init__(self, dynamic, route_refresh, orf_cfg=None):
		self.dynamic = dynamic
		self.orf_cfg = orf_cfg
		self.route_refresh = route_refresh

	def __str__(self):
		return str(self.dynamic) + '+' + str(self.route_refresh)

class Router_bgp_neighbor__neighbor_ipv4_cfg__default_originate_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	default_originate=PosInteger()
	route_map=SizedString(1, 255)
	def __init__(self, default_originate, route_map=None):
		self.default_originate = default_originate
		self.route_map = route_map

	def __str__(self):
		return str(self.default_originate)

class Router_bgp_neighbor__neighbor_ipv4_cfg__maximum_prefix_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	maximum_prefix=PosRangedInteger(1, 65536)
	maximum_prefix_thres=PosRangedInteger(1, 100)
	def __init__(self, maximum_prefix, maximum_prefix_thres=None):
		self.maximum_prefix = maximum_prefix
		self.maximum_prefix_thres = maximum_prefix_thres

	def __str__(self):
		return str(self.maximum_prefix)

class Router_bgp_neighbor__neighbor_ipv4_cfg__nbr_ipv4_pass(AxapiObject):
	__metaclass__ = StructMeta 
	nbr_ipv4_pass_value=SizedString(1, 80)
	nbr_ipv4_pass_encrypted=SizedString(1, 255)
	def __init__(self, nbr_ipv4_pass_value, nbr_ipv4_pass_encrypted):
		self.nbr_ipv4_pass_value = nbr_ipv4_pass_value
		self.nbr_ipv4_pass_encrypted = nbr_ipv4_pass_encrypted

	def __str__(self):
		return str(self.nbr_ipv4_pass_value) + '+' + str(self.nbr_ipv4_pass_encrypted)

class Router_bgp_neighbor__neighbor_ipv4_cfg__send_community_cfg(AxapiObject):
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

class Router_bgp_neighbor__neighbor_ipv4_cfg__soft_reconfiguration_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	soft_reconfiguration=PosInteger()
	inbound=PosInteger()
	def __init__(self, soft_reconfiguration, inbound):
		self.soft_reconfiguration = soft_reconfiguration
		self.inbound = inbound

	def __str__(self):
		return str(self.soft_reconfiguration) + '+' + str(self.inbound)

class Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__md5(AxapiObject):
	__metaclass__ = StructMeta 
	md5_value=SizedString(1, 255)
	md5_encrypted=SizedString(1, 255)
	def __init__(self, md5_value, md5_encrypted):
		self.md5_value = md5_value
		self.md5_encrypted = md5_encrypted

	def __str__(self):
		return str(self.md5_value) + '+' + str(self.md5_encrypted)

class Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_md5(AxapiObject):
	__metaclass__ = StructMeta 
	meticulous_md5_value=SizedString(1, 255)
	meticulous_md5_encrypted=SizedString(1, 255)
	def __init__(self, meticulous_md5_value, meticulous_md5_encrypted):
		self.meticulous_md5_value = meticulous_md5_value
		self.meticulous_md5_encrypted = meticulous_md5_encrypted

	def __str__(self):
		return str(self.meticulous_md5_value) + '+' + str(self.meticulous_md5_encrypted)

class Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__meticulous_sha1(AxapiObject):
	__metaclass__ = StructMeta 
	meticulous_sha1_value=SizedString(1, 255)
	meticulous_sha1_encrypted=SizedString(1, 255)
	def __init__(self, meticulous_sha1_value, meticulous_sha1_encrypted):
		self.meticulous_sha1_value = meticulous_sha1_value
		self.meticulous_sha1_encrypted = meticulous_sha1_encrypted

	def __str__(self):
		return str(self.meticulous_sha1_value) + '+' + str(self.meticulous_sha1_encrypted)

class Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__sha1(AxapiObject):
	__metaclass__ = StructMeta 
	sha1_value=SizedString(1, 255)
	sha1_encrypted=SizedString(1, 255)
	def __init__(self, sha1_value, sha1_encrypted):
		self.sha1_value = sha1_value
		self.sha1_encrypted = sha1_encrypted

	def __str__(self):
		return str(self.sha1_value) + '+' + str(self.sha1_encrypted)

class Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg__simple(AxapiObject):
	__metaclass__ = StructMeta 
	simple_value=SizedString(1, 255)
	simple_encrypted=SizedString(1, 255)
	def __init__(self, simple_value, simple_encrypted):
		self.simple_value = simple_value
		self.simple_encrypted = simple_encrypted

	def __str__(self):
		return str(self.simple_value) + '+' + str(self.simple_encrypted)

class Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication__key_id_cfg(AxapiObject):
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

class Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg__authentication(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, key_id_cfg=None):
		self.key_id_cfg = key_id_cfg

	def __str__(self):
		return ""

class Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg__bfd_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	bfd=PosRangedInteger(0, 1)
	multihop=PosRangedInteger(0, 1)
	def __init__(self, bfd, authentication=None, multihop=None):
		self.bfd = bfd
		self.authentication = authentication
		self.multihop = multihop

	def __str__(self):
		return str(self.bfd)

class Router_bgp_neighbor__neighbor_ipv4_cfg__fall_over_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	fall_over=PosRangedInteger(0, 1)
	def __init__(self, fall_over, bfd_cfg=None):
		self.fall_over = fall_over
		self.bfd_cfg = bfd_cfg

	def __str__(self):
		return str(self.fall_over)

class Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_keepalive_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	neighbor_ipv4_timers_keepalive=PosRangedInteger(0, 65535)
	timers_holdtime=PosRangedInteger(0, 65535)
	def __init__(self, neighbor_ipv4_timers_keepalive, timers_holdtime):
		self.neighbor_ipv4_timers_keepalive = neighbor_ipv4_timers_keepalive
		self.timers_holdtime = timers_holdtime

	def __str__(self):
		return str(self.neighbor_ipv4_timers_keepalive) + '+' + str(self.timers_holdtime)

class Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers__timers_con_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	connect=PosRangedInteger(1, 65535)
	def __init__(self, connect):
		self.connect = connect

	def __str__(self):
		return str(self.connect)

class Router_bgp_neighbor__neighbor_ipv4_cfg__neighbor_ipv4_timers(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, timers_keepalive_cfg=None, timers_con_cfg=None):
		self.timers_keepalive_cfg = timers_keepalive_cfg
		self.timers_con_cfg = timers_con_cfg

	def __str__(self):
		return ""

class Router_bgp_neighbor__neighbor_ipv4_cfg__update_source_cfg(AxapiObject):
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

class Router_bgp_neighbor__neighbor_ipv4_cfg__version_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	version=PosInteger()
	param_4=PosInteger()
	def __init__(self, version, param_4):
		self.version = version
		self.param_4 = param_4

	def __str__(self):
		return str(self.version) + '+' + str(self.param_4)

class Router_bgp_neighbor__neighbor_ipv4_cfg(AxapiObject):
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

class Router_bgp_neighbor(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, neighbor_str_cfg, neighbor_ipv4_cfg=None):
		self.neighbor_str_cfg = neighbor_str_cfg
		self.neighbor_ipv4_cfg = neighbor_ipv4_cfg

	def __str__(self):
		return str(self.neighbor_str_cfg)

class Router_bgp_neighbor_distribute_list_cfg(AxapiObject):
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

class Router_bgp_neighbor_ebgp_multihop_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ebgp_multihop=PosRangedInteger(0, 1)
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

class Router_bgp_distribute_list_cfg(AxapiObject):
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

class Router_bgp_ebgp_multihop_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ebgp_multihop=PosInteger()
	ebgp_multihop_hop_count=PosRangedInteger(1, 255)
	def __init__(self, ebgp_multihop=None, ebgp_multihop_hop_count=None):
		self.ebgp_multihop = ebgp_multihop
		self.ebgp_multihop_hop_count = ebgp_multihop_hop_count

	def __str__(self):
		return ""

class Router_bgp_filter_list_cfg(AxapiObject):
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

class Router_bgp_prefix_list_cfg(AxapiObject):
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

class Router_bgp_route_map_cfg(AxapiObject):
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

class Bgp_process_id(AxapiObject):
	__metaclass__ = StructMeta 
	process_id=PosRangedInteger(1, 4294967295)
	def __init__(self, process_id):
		self.process_id = process_id

	def __str__(self):
		return str(self.process_id)

class Router_bgp_address_family_ipv6_neighbor(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self):
		pass

	def __str__(self):
		return ""

class RouterBgpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRouterBgp(self, bgp_process_id):
		"""
		Retrieve the bgp identified by the specified identifier
		
		Args:
			bgp_process_id Bgp_process_id
		
		Returns:
			An instance of the Bgp class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(bgp_process_id) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bgp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('bgp')
		return deserialize_Bgp_json(payload)

	def putRouterBgp(self, bgp_process_id, bgp):
		"""
		Replace the object bgp
		
		Args:
			bgp_process_id Bgp_process_id
			bgp An instance of the Bgp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bgp']=serialize_Bgp_json(bgp)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(bgp_process_id) .replace("/", "%2f") + query, payload, headers)
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

	def deleteRouterBgp(self, bgp_process_id):
		"""
		Remove the bgp identified by the specified identifier from the system
		
		Args:
			bgp_process_id Bgp_process_id
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(bgp_process_id) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bgp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllRouterBgpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitRouterBgp(self, bgp):
		"""
		Create the object bgp
		
		Args:
			bgp An instance of the Bgp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bgp']=serialize_Bgp_json(bgp)
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

	def getAllRouterBgps(self):
		"""
		Retrieve all bgp objects currently pending in the system
		
		Returns:
			A list of Bgp objects
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
			payload= data.get('bgpList')
		return deserialize_list_Bgp_json(payload)

