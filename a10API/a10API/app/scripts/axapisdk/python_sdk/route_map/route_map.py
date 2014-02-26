########################################################################################################################
# File name: route_map.py
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
	'https://axapi.a10networks.com/axapi/v3/route-map',
]

def deserialize_Route_map__tag_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tag = data.get('tag')
	action = data.get('action')
	sequence = data.get('sequence')
	result = Route_map__tag_cfg(tag=tag, action=action, sequence=sequence)
	return result

def deserialize_Route_map__match__as_path_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	result = Route_map__match__as_path(name=name)
	return result

def deserialize_Route_map__match__community__l_std_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	l_std = data.get('l-std')
	exact_match = data.get('exact-match')
	result = Route_map__match__community__l_std_cfg(l_std=l_std, exact_match=exact_match)
	return result

def deserialize_Route_map__match__community__l_ext_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	l_ext = data.get('l-ext')
	exact_match = data.get('exact-match')
	result = Route_map__match__community__l_ext_cfg(l_ext=l_ext, exact_match=exact_match)
	return result

def deserialize_Route_map__match__community__name_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	exact_match = data.get('exact-match')
	result = Route_map__match__community__name_cfg(name=name, exact_match=exact_match)
	return result

def deserialize_Route_map__match__community_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	l_std_cfg = deserialize_Route_map__match__community__l_std_cfg_json(data.get('l-std-cfg'))
	l_ext_cfg = deserialize_Route_map__match__community__l_ext_cfg_json(data.get('l-ext-cfg'))
	name_cfg = deserialize_Route_map__match__community__name_cfg_json(data.get('name-cfg'))
	result = Route_map__match__community(l_std_cfg=l_std_cfg, l_ext_cfg=l_ext_cfg, name_cfg=name_cfg)
	return result

def deserialize_Route_map__match__extcommunity__extcommunity_l_std_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	l_std = data.get('l-std')
	exact_match = data.get('exact-match')
	result = Route_map__match__extcommunity__extcommunity_l_std_cfg(l_std=l_std, exact_match=exact_match)
	return result

def deserialize_Route_map__match__extcommunity__extcommunity_l_ext_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	l_ext = data.get('l-ext')
	exact_match = data.get('exact-match')
	result = Route_map__match__extcommunity__extcommunity_l_ext_cfg(l_ext=l_ext, exact_match=exact_match)
	return result

def deserialize_Route_map__match__extcommunity__extcommunity_l_name_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	exact_match = data.get('exact-match')
	result = Route_map__match__extcommunity__extcommunity_l_name(name=name, exact_match=exact_match)
	return result

def deserialize_Route_map__match__extcommunity_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	extcommunity_l_std_cfg = deserialize_Route_map__match__extcommunity__extcommunity_l_std_cfg_json(data.get('extcommunity-l-std-cfg'))
	extcommunity_l_ext_cfg = deserialize_Route_map__match__extcommunity__extcommunity_l_ext_cfg_json(data.get('extcommunity-l-ext-cfg'))
	extcommunity_l_name = deserialize_Route_map__match__extcommunity__extcommunity_l_name_json(data.get('extcommunity-l-name'))
	result = Route_map__match__extcommunity(extcommunity_l_std_cfg=extcommunity_l_std_cfg, extcommunity_l_ext_cfg=extcommunity_l_ext_cfg, extcommunity_l_name=extcommunity_l_name)
	return result

def deserialize_Route_map__match__interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet = data.get('ethernet')
	loopback = data.get('loopback')
	trunk = data.get('trunk')
	ve = data.get('ve')
	result = Route_map__match__interface(ethernet=ethernet, loopback=loopback, trunk=trunk, ve=ve)
	return result

def deserialize_Route_map__match__origin_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	egp = data.get('egp')
	igp = data.get('igp')
	incomplete = data.get('incomplete')
	result = Route_map__match__origin(egp=egp, igp=igp, incomplete=incomplete)
	return result

def deserialize_Route_map__match__ip__address__prefix_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	result = Route_map__match__ip__address__prefix_list(name=name)
	return result

def deserialize_Route_map__match__ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl1 = data.get('acl1')
	acl2 = data.get('acl2')
	name = data.get('name')
	prefix_list = deserialize_Route_map__match__ip__address__prefix_list_json(data.get('prefix-list'))
	result = Route_map__match__ip__address(acl1=acl1, acl2=acl2, name=name, prefix_list=prefix_list)
	return result

def deserialize_Route_map__match__ip__next_hop__prefix_list_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	result = Route_map__match__ip__next_hop__prefix_list_1(name=name)
	return result

def deserialize_Route_map__match__ip__next_hop_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl1 = data.get('acl1')
	acl2 = data.get('acl2')
	name = data.get('name')
	prefix_list_1 = deserialize_Route_map__match__ip__next_hop__prefix_list_1_json(data.get('prefix-list-1'))
	result = Route_map__match__ip__next_hop(acl1=acl1, acl2=acl2, name=name, prefix_list_1=prefix_list_1)
	return result

def deserialize_Route_map__match__ip__peer_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl1 = data.get('acl1')
	acl2 = data.get('acl2')
	name = data.get('name')
	result = Route_map__match__ip__peer(acl1=acl1, acl2=acl2, name=name)
	return result

def deserialize_Route_map__match__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Route_map__match__ip__address_json(data.get('address'))
	next_hop = deserialize_Route_map__match__ip__next_hop_json(data.get('next-hop'))
	peer = deserialize_Route_map__match__ip__peer_json(data.get('peer'))
	result = Route_map__match__ip(address=address, next_hop=next_hop, peer=peer)
	return result

def deserialize_Route_map__match__ipv6__address_1__prefix_list_2_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	result = Route_map__match__ipv6__address_1__prefix_list_2(name=name)
	return result

def deserialize_Route_map__match__ipv6__address_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	prefix_list_2 = deserialize_Route_map__match__ipv6__address_1__prefix_list_2_json(data.get('prefix-list-2'))
	result = Route_map__match__ipv6__address_1(name=name, prefix_list_2=prefix_list_2)
	return result

def deserialize_Route_map__match__ipv6__next_hop_1__prefix_list_3_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	result = Route_map__match__ipv6__next_hop_1__prefix_list_3(name=name)
	return result

def deserialize_Route_map__match__ipv6__next_hop_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	v6_addr = data.get('v6-addr')
	prefix_list_3 = deserialize_Route_map__match__ipv6__next_hop_1__prefix_list_3_json(data.get('prefix-list-3'))
	result = Route_map__match__ipv6__next_hop_1(name=name, v6_addr=v6_addr, prefix_list_3=prefix_list_3)
	return result

def deserialize_Route_map__match__ipv6__peer_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl1 = data.get('acl1')
	acl2 = data.get('acl2')
	name = data.get('name')
	result = Route_map__match__ipv6__peer_1(acl1=acl1, acl2=acl2, name=name)
	return result

def deserialize_Route_map__match__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_1 = deserialize_Route_map__match__ipv6__address_1_json(data.get('address-1'))
	next_hop_1 = deserialize_Route_map__match__ipv6__next_hop_1_json(data.get('next-hop-1'))
	peer_1 = deserialize_Route_map__match__ipv6__peer_1_json(data.get('peer-1'))
	result = Route_map__match__ipv6(address_1=address_1, next_hop_1=next_hop_1, peer_1=peer_1)
	return result

def deserialize_Route_map__match__metric_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Route_map__match__metric(value=value)
	return result

def deserialize_Route_map__match__route_type__external_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Route_map__match__route_type__external(value=value)
	return result

def deserialize_Route_map__match__route_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	external = deserialize_Route_map__match__route_type__external_json(data.get('external'))
	result = Route_map__match__route_type(external=external)
	return result

def deserialize_Route_map__match__tag_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Route_map__match__tag(value=value)
	return result

def deserialize_Route_map__match_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	as_path = deserialize_Route_map__match__as_path_json(data.get('as-path'))
	community = deserialize_Route_map__match__community_json(data.get('community'))
	extcommunity = deserialize_Route_map__match__extcommunity_json(data.get('extcommunity'))
	interface = deserialize_Route_map__match__interface_json(data.get('interface'))
	origin = deserialize_Route_map__match__origin_json(data.get('origin'))
	ip = deserialize_Route_map__match__ip_json(data.get('ip'))
	ipv6 = deserialize_Route_map__match__ipv6_json(data.get('ipv6'))
	metric = deserialize_Route_map__match__metric_json(data.get('metric'))
	route_type = deserialize_Route_map__match__route_type_json(data.get('route-type'))
	tag = deserialize_Route_map__match__tag_json(data.get('tag'))
	result = Route_map__match(as_path=as_path, community=community, extcommunity=extcommunity, interface=interface, origin=origin, ip=ip, ipv6=ipv6, metric=metric, route_type=route_type, tag=tag)
	return result

def deserialize_Route_map__set__ip__next_hop_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = data.get('address')
	result = Route_map__set__ip__next_hop(address=address)
	return result

def deserialize_Route_map__set__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	next_hop = deserialize_Route_map__set__ip__next_hop_json(data.get('next-hop'))
	result = Route_map__set__ip(next_hop=next_hop)
	return result

def deserialize_Route_map__set__ipv6__next_hop_1__local_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = data.get('address')
	result = Route_map__set__ipv6__next_hop_1__local(address=address)
	return result

def deserialize_Route_map__set__ipv6__next_hop_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = data.get('address')
	local = deserialize_Route_map__set__ipv6__next_hop_1__local_json(data.get('local'))
	result = Route_map__set__ipv6__next_hop_1(address=address, local=local)
	return result

def deserialize_Route_map__set__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	next_hop_1 = deserialize_Route_map__set__ipv6__next_hop_1_json(data.get('next-hop-1'))
	result = Route_map__set__ipv6(next_hop_1=next_hop_1)
	return result

def deserialize_Route_map__set__level_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Route_map__set__level(value=value)
	return result

def deserialize_Route_map__set__metric_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Route_map__set__metric(value=value)
	return result

def deserialize_Route_map__set__metric_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Route_map__set__metric_type(value=value)
	return result

def deserialize_Route_map__set__tag_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Route_map__set__tag(value=value)
	return result

def deserialize_Route_map__set__aggregator__as_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	asn = data.get('asn')
	ip = data.get('ip')
	result = Route_map__set__aggregator__as(asn=asn, ip=ip)
	return result

def deserialize_Route_map__set__aggregator_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	py_kw_rsvd_as = deserialize_Route_map__set__aggregator__as_json(data.get('as'))
	result = Route_map__set__aggregator(py_kw_rsvd_as=py_kw_rsvd_as)
	return result

def deserialize_Route_map__set__as_path_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	prepend = data.get('prepend')
	num = data.get('num')
	num2 = data.get('num2')
	result = Route_map__set__as_path(prepend=prepend, num=num, num2=num2)
	return result

def deserialize_Route_map__set__comm_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	v_std = data.get('v-std')
	delete = data.get('delete')
	v_exp = data.get('v-exp')
	name = data.get('name')
	result = Route_map__set__comm_list(v_std=v_std, delete=delete, v_exp=v_exp, name=name)
	return result

def deserialize_Route_map__set__dampening_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dampening = data.get('dampening')
	dampening_half_time = data.get('dampening-half-time')
	dampening_reuse = data.get('dampening-reuse')
	dampening_supress = data.get('dampening-supress')
	dampening_max_supress = data.get('dampening-max-supress')
	dampening_penalty = data.get('dampening-penalty')
	result = Route_map__set__dampening_cfg(dampening=dampening, dampening_half_time=dampening_half_time, dampening_reuse=dampening_reuse, dampening_supress=dampening_supress, dampening_max_supress=dampening_max_supress, dampening_penalty=dampening_penalty)
	return result

def deserialize_Route_map__set__extcommunity__rt_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Route_map__set__extcommunity__rt(value=value)
	return result

def deserialize_Route_map__set__extcommunity__soo_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Route_map__set__extcommunity__soo(value=value)
	return result

def deserialize_Route_map__set__extcommunity_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	rt = deserialize_Route_map__set__extcommunity__rt_json(data.get('rt'))
	soo = deserialize_Route_map__set__extcommunity__soo_json(data.get('soo'))
	result = Route_map__set__extcommunity(rt=rt, soo=soo)
	return result

def deserialize_Route_map__set__local_preference_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	val = data.get('val')
	result = Route_map__set__local_preference(val=val)
	return result

def deserialize_Route_map__set__originator_id_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	originator_ip = data.get('originator-ip')
	result = Route_map__set__originator_id(originator_ip=originator_ip)
	return result

def deserialize_Route_map__set__weight_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	weight_val = data.get('weight-val')
	result = Route_map__set__weight(weight_val=weight_val)
	return result

def deserialize_Route_map__set__origin_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	egp = data.get('egp')
	igp = data.get('igp')
	incomplete = data.get('incomplete')
	result = Route_map__set__origin(egp=egp, igp=igp, incomplete=incomplete)
	return result

def deserialize_Route_map__set_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip = deserialize_Route_map__set__ip_json(data.get('ip'))
	ipv6 = deserialize_Route_map__set__ipv6_json(data.get('ipv6'))
	level = deserialize_Route_map__set__level_json(data.get('level'))
	metric = deserialize_Route_map__set__metric_json(data.get('metric'))
	metric_type = deserialize_Route_map__set__metric_type_json(data.get('metric-type'))
	tag = deserialize_Route_map__set__tag_json(data.get('tag'))
	aggregator = deserialize_Route_map__set__aggregator_json(data.get('aggregator'))
	as_path = deserialize_Route_map__set__as_path_json(data.get('as-path'))
	atomic_aggregate = data.get('atomic-aggregate')
	comm_list = deserialize_Route_map__set__comm_list_json(data.get('comm-list'))
	community = data.get('community')
	community_num = data.get('community-num')
	community_num_aa_nn = data.get('community-num-aa-nn')
	internet = data.get('internet')
	local_as = data.get('local-AS')
	no_advertise = data.get('no-advertise')
	no_export = data.get('no-export')
	none = data.get('none')
	community_num2 = data.get('community-num2')
	community_num_aa_nn2 = data.get('community-num-aa-nn2')
	internet2 = data.get('internet2')
	local_as2 = data.get('local-AS2')
	no_advertise2 = data.get('no-advertise2')
	no_export2 = data.get('no-export2')
	additive = data.get('additive')
	dampening_cfg = deserialize_Route_map__set__dampening_cfg_json(data.get('dampening-cfg'))
	extcommunity = deserialize_Route_map__set__extcommunity_json(data.get('extcommunity'))
	local_preference = deserialize_Route_map__set__local_preference_json(data.get('local-preference'))
	originator_id = deserialize_Route_map__set__originator_id_json(data.get('originator-id'))
	weight = deserialize_Route_map__set__weight_json(data.get('weight'))
	origin = deserialize_Route_map__set__origin_json(data.get('origin'))
	result = Route_map__set(ip=ip, ipv6=ipv6, level=level, metric=metric, metric_type=metric_type, tag=tag, aggregator=aggregator, as_path=as_path, atomic_aggregate=atomic_aggregate, comm_list=comm_list, community=community, community_num=community_num, community_num_aa_nn=community_num_aa_nn, internet=internet, local_as=local_as, no_advertise=no_advertise, no_export=no_export, none=none, community_num2=community_num2, community_num_aa_nn2=community_num_aa_nn2, internet2=internet2, local_as2=local_as2, no_advertise2=no_advertise2, no_export2=no_export2, additive=additive, dampening_cfg=dampening_cfg, extcommunity=extcommunity, local_preference=local_preference, originator_id=originator_id, weight=weight, origin=origin)
	return result

def deserialize_Route_map_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tag_cfg = deserialize_Route_map__tag_cfg_json(data.get('tag-cfg'))
	match = deserialize_Route_map__match_json(data.get('match'))
	set = deserialize_Route_map__set_json(data.get('set'))
	result = Route_map(tag_cfg=tag_cfg, match=match, set=set)
	return result

def serialize_Route_map__tag_cfg_json(obj):
	output = OrderedDict()
	output['tag'] = obj.tag
	output['action'] = obj.action
	output['sequence'] = obj.sequence
	return output

def serialize_Route_map__match__as_path_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Route_map__match__community__l_std_cfg_json(obj):
	output = OrderedDict()
	if obj.l_std is not None:
		output['l-std'] = obj.l_std
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Route_map__match__community__l_ext_cfg_json(obj):
	output = OrderedDict()
	if obj.l_ext is not None:
		output['l-ext'] = obj.l_ext
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Route_map__match__community__name_cfg_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Route_map__match__community_json(obj):
	output = OrderedDict()
	if obj.l_std_cfg is not None:
		output['l-std-cfg'] = serialize_Route_map__match__community__l_std_cfg_json(obj.l_std_cfg)
	if obj.l_ext_cfg is not None:
		output['l-ext-cfg'] = serialize_Route_map__match__community__l_ext_cfg_json(obj.l_ext_cfg)
	if obj.name_cfg is not None:
		output['name-cfg'] = serialize_Route_map__match__community__name_cfg_json(obj.name_cfg)
	return output

def serialize_Route_map__match__extcommunity__extcommunity_l_std_cfg_json(obj):
	output = OrderedDict()
	if obj.l_std is not None:
		output['l-std'] = obj.l_std
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Route_map__match__extcommunity__extcommunity_l_ext_cfg_json(obj):
	output = OrderedDict()
	if obj.l_ext is not None:
		output['l-ext'] = obj.l_ext
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Route_map__match__extcommunity__extcommunity_l_name_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Route_map__match__extcommunity_json(obj):
	output = OrderedDict()
	if obj.extcommunity_l_std_cfg is not None:
		output['extcommunity-l-std-cfg'] = serialize_Route_map__match__extcommunity__extcommunity_l_std_cfg_json(obj.extcommunity_l_std_cfg)
	if obj.extcommunity_l_ext_cfg is not None:
		output['extcommunity-l-ext-cfg'] = serialize_Route_map__match__extcommunity__extcommunity_l_ext_cfg_json(obj.extcommunity_l_ext_cfg)
	if obj.extcommunity_l_name is not None:
		output['extcommunity-l-name'] = serialize_Route_map__match__extcommunity__extcommunity_l_name_json(obj.extcommunity_l_name)
	return output

def serialize_Route_map__match__interface_json(obj):
	output = OrderedDict()
	if obj.ethernet is not None:
		output['ethernet'] = obj.ethernet
	if obj.loopback is not None:
		output['loopback'] = obj.loopback
	if obj.trunk is not None:
		output['trunk'] = obj.trunk
	if obj.ve is not None:
		output['ve'] = obj.ve
	return output

def serialize_Route_map__match__origin_json(obj):
	output = OrderedDict()
	if obj.egp is not None:
		output['egp'] = obj.egp
	if obj.igp is not None:
		output['igp'] = obj.igp
	if obj.incomplete is not None:
		output['incomplete'] = obj.incomplete
	return output

def serialize_Route_map__match__ip__address__prefix_list_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Route_map__match__ip__address_json(obj):
	output = OrderedDict()
	if obj.acl1 is not None:
		output['acl1'] = obj.acl1
	if obj.acl2 is not None:
		output['acl2'] = obj.acl2
	if obj.name is not None:
		output['name'] = obj.name
	if obj.prefix_list is not None:
		output['prefix-list'] = serialize_Route_map__match__ip__address__prefix_list_json(obj.prefix_list)
	return output

def serialize_Route_map__match__ip__next_hop__prefix_list_1_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Route_map__match__ip__next_hop_json(obj):
	output = OrderedDict()
	if obj.acl1 is not None:
		output['acl1'] = obj.acl1
	if obj.acl2 is not None:
		output['acl2'] = obj.acl2
	if obj.name is not None:
		output['name'] = obj.name
	if obj.prefix_list_1 is not None:
		output['prefix-list-1'] = serialize_Route_map__match__ip__next_hop__prefix_list_1_json(obj.prefix_list_1)
	return output

def serialize_Route_map__match__ip__peer_json(obj):
	output = OrderedDict()
	if obj.acl1 is not None:
		output['acl1'] = obj.acl1
	if obj.acl2 is not None:
		output['acl2'] = obj.acl2
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Route_map__match__ip_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = serialize_Route_map__match__ip__address_json(obj.address)
	if obj.next_hop is not None:
		output['next-hop'] = serialize_Route_map__match__ip__next_hop_json(obj.next_hop)
	if obj.peer is not None:
		output['peer'] = serialize_Route_map__match__ip__peer_json(obj.peer)
	return output

def serialize_Route_map__match__ipv6__address_1__prefix_list_2_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Route_map__match__ipv6__address_1_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	if obj.prefix_list_2 is not None:
		output['prefix-list-2'] = serialize_Route_map__match__ipv6__address_1__prefix_list_2_json(obj.prefix_list_2)
	return output

def serialize_Route_map__match__ipv6__next_hop_1__prefix_list_3_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Route_map__match__ipv6__next_hop_1_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	if obj.v6_addr is not None:
		output['v6-addr'] = obj.v6_addr
	if obj.prefix_list_3 is not None:
		output['prefix-list-3'] = serialize_Route_map__match__ipv6__next_hop_1__prefix_list_3_json(obj.prefix_list_3)
	return output

def serialize_Route_map__match__ipv6__peer_1_json(obj):
	output = OrderedDict()
	if obj.acl1 is not None:
		output['acl1'] = obj.acl1
	if obj.acl2 is not None:
		output['acl2'] = obj.acl2
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Route_map__match__ipv6_json(obj):
	output = OrderedDict()
	if obj.address_1 is not None:
		output['address-1'] = serialize_Route_map__match__ipv6__address_1_json(obj.address_1)
	if obj.next_hop_1 is not None:
		output['next-hop-1'] = serialize_Route_map__match__ipv6__next_hop_1_json(obj.next_hop_1)
	if obj.peer_1 is not None:
		output['peer-1'] = serialize_Route_map__match__ipv6__peer_1_json(obj.peer_1)
	return output

def serialize_Route_map__match__metric_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Route_map__match__route_type__external_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Route_map__match__route_type_json(obj):
	output = OrderedDict()
	if obj.external is not None:
		output['external'] = serialize_Route_map__match__route_type__external_json(obj.external)
	return output

def serialize_Route_map__match__tag_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Route_map__match_json(obj):
	output = OrderedDict()
	if obj.as_path is not None:
		output['as-path'] = serialize_Route_map__match__as_path_json(obj.as_path)
	if obj.community is not None:
		output['community'] = serialize_Route_map__match__community_json(obj.community)
	if obj.extcommunity is not None:
		output['extcommunity'] = serialize_Route_map__match__extcommunity_json(obj.extcommunity)
	if obj.interface is not None:
		output['interface'] = serialize_Route_map__match__interface_json(obj.interface)
	if obj.origin is not None:
		output['origin'] = serialize_Route_map__match__origin_json(obj.origin)
	if obj.ip is not None:
		output['ip'] = serialize_Route_map__match__ip_json(obj.ip)
	if obj.ipv6 is not None:
		output['ipv6'] = serialize_Route_map__match__ipv6_json(obj.ipv6)
	if obj.metric is not None:
		output['metric'] = serialize_Route_map__match__metric_json(obj.metric)
	if obj.route_type is not None:
		output['route-type'] = serialize_Route_map__match__route_type_json(obj.route_type)
	if obj.tag is not None:
		output['tag'] = serialize_Route_map__match__tag_json(obj.tag)
	return output

def serialize_Route_map__set__ip__next_hop_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = obj.address
	return output

def serialize_Route_map__set__ip_json(obj):
	output = OrderedDict()
	if obj.next_hop is not None:
		output['next-hop'] = serialize_Route_map__set__ip__next_hop_json(obj.next_hop)
	return output

def serialize_Route_map__set__ipv6__next_hop_1__local_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = obj.address
	return output

def serialize_Route_map__set__ipv6__next_hop_1_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = obj.address
	if obj.local is not None:
		output['local'] = serialize_Route_map__set__ipv6__next_hop_1__local_json(obj.local)
	return output

def serialize_Route_map__set__ipv6_json(obj):
	output = OrderedDict()
	if obj.next_hop_1 is not None:
		output['next-hop-1'] = serialize_Route_map__set__ipv6__next_hop_1_json(obj.next_hop_1)
	return output

def serialize_Route_map__set__level_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Route_map__set__metric_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Route_map__set__metric_type_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Route_map__set__tag_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Route_map__set__aggregator__as_json(obj):
	output = OrderedDict()
	if obj.asn is not None:
		output['asn'] = obj.asn
	if obj.ip is not None:
		output['ip'] = obj.ip
	return output

def serialize_Route_map__set__aggregator_json(obj):
	output = OrderedDict()
	if obj.py_kw_rsvd_as is not None:
		output['as'] = serialize_Route_map__set__aggregator__as_json(obj.py_kw_rsvd_as)
	return output

def serialize_Route_map__set__as_path_json(obj):
	output = OrderedDict()
	if obj.prepend is not None:
		output['prepend'] = obj.prepend
	if obj.num is not None:
		output['num'] = obj.num
	if obj.num2 is not None:
		output['num2'] = obj.num2
	return output

def serialize_Route_map__set__comm_list_json(obj):
	output = OrderedDict()
	if obj.v_std is not None:
		output['v-std'] = obj.v_std
	if obj.delete is not None:
		output['delete'] = obj.delete
	if obj.v_exp is not None:
		output['v-exp'] = obj.v_exp
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Route_map__set__dampening_cfg_json(obj):
	output = OrderedDict()
	if obj.dampening is not None:
		output['dampening'] = obj.dampening
	if obj.dampening_half_time is not None:
		output['dampening-half-time'] = obj.dampening_half_time
	if obj.dampening_reuse is not None:
		output['dampening-reuse'] = obj.dampening_reuse
	if obj.dampening_supress is not None:
		output['dampening-supress'] = obj.dampening_supress
	if obj.dampening_max_supress is not None:
		output['dampening-max-supress'] = obj.dampening_max_supress
	if obj.dampening_penalty is not None:
		output['dampening-penalty'] = obj.dampening_penalty
	return output

def serialize_Route_map__set__extcommunity__rt_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Route_map__set__extcommunity__soo_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Route_map__set__extcommunity_json(obj):
	output = OrderedDict()
	if obj.rt is not None:
		output['rt'] = serialize_Route_map__set__extcommunity__rt_json(obj.rt)
	if obj.soo is not None:
		output['soo'] = serialize_Route_map__set__extcommunity__soo_json(obj.soo)
	return output

def serialize_Route_map__set__local_preference_json(obj):
	output = OrderedDict()
	if obj.val is not None:
		output['val'] = obj.val
	return output

def serialize_Route_map__set__originator_id_json(obj):
	output = OrderedDict()
	if obj.originator_ip is not None:
		output['originator-ip'] = obj.originator_ip
	return output

def serialize_Route_map__set__weight_json(obj):
	output = OrderedDict()
	if obj.weight_val is not None:
		output['weight-val'] = obj.weight_val
	return output

def serialize_Route_map__set__origin_json(obj):
	output = OrderedDict()
	if obj.egp is not None:
		output['egp'] = obj.egp
	if obj.igp is not None:
		output['igp'] = obj.igp
	if obj.incomplete is not None:
		output['incomplete'] = obj.incomplete
	return output

def serialize_Route_map__set_json(obj):
	output = OrderedDict()
	if obj.ip is not None:
		output['ip'] = serialize_Route_map__set__ip_json(obj.ip)
	if obj.ipv6 is not None:
		output['ipv6'] = serialize_Route_map__set__ipv6_json(obj.ipv6)
	if obj.level is not None:
		output['level'] = serialize_Route_map__set__level_json(obj.level)
	if obj.metric is not None:
		output['metric'] = serialize_Route_map__set__metric_json(obj.metric)
	if obj.metric_type is not None:
		output['metric-type'] = serialize_Route_map__set__metric_type_json(obj.metric_type)
	if obj.tag is not None:
		output['tag'] = serialize_Route_map__set__tag_json(obj.tag)
	if obj.aggregator is not None:
		output['aggregator'] = serialize_Route_map__set__aggregator_json(obj.aggregator)
	if obj.as_path is not None:
		output['as-path'] = serialize_Route_map__set__as_path_json(obj.as_path)
	if obj.atomic_aggregate is not None:
		output['atomic-aggregate'] = obj.atomic_aggregate
	if obj.comm_list is not None:
		output['comm-list'] = serialize_Route_map__set__comm_list_json(obj.comm_list)
	if obj.community is not None:
		output['community'] = obj.community
	if obj.community_num is not None:
		output['community-num'] = obj.community_num
	if obj.community_num_aa_nn is not None:
		output['community-num-aa-nn'] = obj.community_num_aa_nn
	if obj.internet is not None:
		output['internet'] = obj.internet
	if obj.local_as is not None:
		output['local-AS'] = obj.local_as
	if obj.no_advertise is not None:
		output['no-advertise'] = obj.no_advertise
	if obj.no_export is not None:
		output['no-export'] = obj.no_export
	if obj.none is not None:
		output['none'] = obj.none
	if obj.community_num2 is not None:
		output['community-num2'] = obj.community_num2
	if obj.community_num_aa_nn2 is not None:
		output['community-num-aa-nn2'] = obj.community_num_aa_nn2
	if obj.internet2 is not None:
		output['internet2'] = obj.internet2
	if obj.local_as2 is not None:
		output['local-AS2'] = obj.local_as2
	if obj.no_advertise2 is not None:
		output['no-advertise2'] = obj.no_advertise2
	if obj.no_export2 is not None:
		output['no-export2'] = obj.no_export2
	if obj.additive is not None:
		output['additive'] = obj.additive
	if obj.dampening_cfg is not None:
		output['dampening-cfg'] = serialize_Route_map__set__dampening_cfg_json(obj.dampening_cfg)
	if obj.extcommunity is not None:
		output['extcommunity'] = serialize_Route_map__set__extcommunity_json(obj.extcommunity)
	if obj.local_preference is not None:
		output['local-preference'] = serialize_Route_map__set__local_preference_json(obj.local_preference)
	if obj.originator_id is not None:
		output['originator-id'] = serialize_Route_map__set__originator_id_json(obj.originator_id)
	if obj.weight is not None:
		output['weight'] = serialize_Route_map__set__weight_json(obj.weight)
	if obj.origin is not None:
		output['origin'] = serialize_Route_map__set__origin_json(obj.origin)
	return output

def serialize_Route_map_json(obj):
	output = OrderedDict()
	output['tag-cfg'] = serialize_Route_map__tag_cfg_json(obj.tag_cfg)
	if obj.match is not None:
		output['match'] = serialize_Route_map__match_json(obj.match)
	if obj.set is not None:
		output['set'] = serialize_Route_map__set_json(obj.set)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Route_map_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Route_map_json(item))
	return list(container)

class Route_map_tag_cfg_action_sequence__tag_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tag=SizedString(1, 255)
	action = Enum(['permit', 'deny'])
	sequence=PosRangedInteger(1, 65535)
	def __init__(self, tag, action, sequence):
		self.tag = tag
		self.action = action
		self.sequence = sequence

	def __str__(self):
		return str(self.tag) + '+' + str(self.action) + '+' + str(self.sequence)

class Route_map_tag_cfg_action_sequence(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, tag_cfg):
		self.tag_cfg = tag_cfg

	def __str__(self):
		return str(self.tag_cfg)

class Route_map__tag_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tag=SizedString(1, 255)
	action = Enum(['permit', 'deny'])
	sequence=PosRangedInteger(1, 65535)
	def __init__(self, tag, action, sequence):
		self.tag = tag
		self.action = action
		self.sequence = sequence

	def __str__(self):
		return str(self.tag) + '+' + str(self.action) + '+' + str(self.sequence)

class Route_map__match__as_path(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None):
		self.name = name

	def __str__(self):
		return ""

class Route_map__match__community__l_std_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	l_std=PosRangedInteger(1, 99)
	exact_match=PosRangedInteger(0, 1)
	def __init__(self, l_std=None, exact_match=None):
		self.l_std = l_std
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Route_map__match__community__l_ext_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	l_ext=PosRangedInteger(100, 199)
	exact_match=PosInteger()
	def __init__(self, l_ext=None, exact_match=None):
		self.l_ext = l_ext
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Route_map__match__community__name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	exact_match=PosInteger()
	def __init__(self, name=None, exact_match=None):
		self.name = name
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Route_map__match__community(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, l_std_cfg=None, l_ext_cfg=None, name_cfg=None):
		self.l_std_cfg = l_std_cfg
		self.l_ext_cfg = l_ext_cfg
		self.name_cfg = name_cfg

	def __str__(self):
		return ""

class Route_map__match__extcommunity__extcommunity_l_std_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	l_std=PosRangedInteger(1, 99)
	exact_match=PosInteger()
	def __init__(self, l_std=None, exact_match=None):
		self.l_std = l_std
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Route_map__match__extcommunity__extcommunity_l_ext_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	l_ext=PosRangedInteger(100, 199)
	exact_match=PosInteger()
	def __init__(self, l_ext=None, exact_match=None):
		self.l_ext = l_ext
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Route_map__match__extcommunity__extcommunity_l_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	exact_match=PosInteger()
	def __init__(self, name=None, exact_match=None):
		self.name = name
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Route_map__match__extcommunity(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, extcommunity_l_std_cfg=None, extcommunity_l_ext_cfg=None, extcommunity_l_name=None):
		self.extcommunity_l_std_cfg = extcommunity_l_std_cfg
		self.extcommunity_l_ext_cfg = extcommunity_l_ext_cfg
		self.extcommunity_l_name = extcommunity_l_name

	def __str__(self):
		return ""

class Route_map__match__interface(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet=PosRangedInteger(1, 2048)
	loopback=PosRangedInteger(1, 10)
	trunk=PosRangedInteger(1, 16)
	ve=PosRangedInteger(2, 4094)
	def __init__(self, ethernet=None, loopback=None, trunk=None, ve=None):
		self.ethernet = ethernet
		self.loopback = loopback
		self.trunk = trunk
		self.ve = ve

	def __str__(self):
		return ""

class Route_map__match__origin(AxapiObject):
	__metaclass__ = StructMeta 
	egp=PosRangedInteger(0, 1)
	igp=PosRangedInteger(0, 1)
	incomplete=PosRangedInteger(0, 1)
	def __init__(self, egp=None, igp=None, incomplete=None):
		self.egp = egp
		self.igp = igp
		self.incomplete = incomplete

	def __str__(self):
		return ""

class Route_map__match__ip__address__prefix_list(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None):
		self.name = name

	def __str__(self):
		return ""

class Route_map__match__ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	acl1=PosRangedInteger(1, 199)
	acl2=PosRangedInteger(1300, 2699)
	name=SizedString(1, 255)
	def __init__(self, acl1=None, acl2=None, name=None, prefix_list=None):
		self.acl1 = acl1
		self.acl2 = acl2
		self.name = name
		self.prefix_list = prefix_list

	def __str__(self):
		return ""

class Route_map__match__ip__next_hop__prefix_list_1(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None):
		self.name = name

	def __str__(self):
		return ""

class Route_map__match__ip__next_hop(AxapiObject):
	__metaclass__ = StructMeta 
	acl1=PosRangedInteger(1, 199)
	acl2=PosRangedInteger(1300, 2699)
	name=SizedString(1, 255)
	def __init__(self, acl1=None, acl2=None, name=None, prefix_list_1=None):
		self.acl1 = acl1
		self.acl2 = acl2
		self.name = name
		self.prefix_list_1 = prefix_list_1

	def __str__(self):
		return ""

class Route_map__match__ip__peer(AxapiObject):
	__metaclass__ = StructMeta 
	acl1=PosRangedInteger(1, 199)
	acl2=PosRangedInteger(1300, 2699)
	name=SizedString(1, 255)
	def __init__(self, acl1=None, acl2=None, name=None):
		self.acl1 = acl1
		self.acl2 = acl2
		self.name = name

	def __str__(self):
		return ""

class Route_map__match__ip(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address=None, next_hop=None, peer=None):
		self.address = address
		self.next_hop = next_hop
		self.peer = peer

	def __str__(self):
		return ""

class Route_map__match__ipv6__address_1__prefix_list_2(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None):
		self.name = name

	def __str__(self):
		return ""

class Route_map__match__ipv6__address_1(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None, prefix_list_2=None):
		self.name = name
		self.prefix_list_2 = prefix_list_2

	def __str__(self):
		return ""

class Route_map__match__ipv6__next_hop_1__prefix_list_3(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None):
		self.name = name

	def __str__(self):
		return ""

class Route_map__match__ipv6__next_hop_1(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	v6_addr=SizedString(1, 255)
	def __init__(self, name=None, v6_addr=None, prefix_list_3=None):
		self.name = name
		self.v6_addr = v6_addr
		self.prefix_list_3 = prefix_list_3

	def __str__(self):
		return ""

class Route_map__match__ipv6__peer_1(AxapiObject):
	__metaclass__ = StructMeta 
	acl1=PosRangedInteger(1, 199)
	acl2=PosRangedInteger(1300, 2699)
	name=SizedString(1, 255)
	def __init__(self, acl1=None, acl2=None, name=None):
		self.acl1 = acl1
		self.acl2 = acl2
		self.name = name

	def __str__(self):
		return ""

class Route_map__match__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address_1=None, next_hop_1=None, peer_1=None):
		self.address_1 = address_1
		self.next_hop_1 = next_hop_1
		self.peer_1 = peer_1

	def __str__(self):
		return ""

class Route_map__match__metric(AxapiObject):
	__metaclass__ = StructMeta 
	value=PosRangedInteger(0, 4294967295)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Route_map__match__route_type__external(AxapiObject):
	__metaclass__ = StructMeta 
	value=PosRangedInteger(0, 4294967295)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Route_map__match__route_type(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, external=None):
		self.external = external

	def __str__(self):
		return ""

class Route_map__match__tag(AxapiObject):
	__metaclass__ = StructMeta 
	value=PosRangedInteger(0, 4294967295)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Route_map__match(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, as_path=None, community=None, extcommunity=None, interface=None, origin=None, ip=None, ipv6=None, metric=None, route_type=None, tag=None):
		self.as_path = as_path
		self.community = community
		self.extcommunity = extcommunity
		self.interface = interface
		self.origin = origin
		self.ip = ip
		self.ipv6 = ipv6
		self.metric = metric
		self.route_type = route_type
		self.tag = tag

	def __str__(self):
		return ""

class Route_map__set__ip__next_hop(AxapiObject):
	__metaclass__ = StructMeta 
	address=SizedString(1, 255)
	def __init__(self, address=None):
		self.address = address

	def __str__(self):
		return ""

class Route_map__set__ip(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, next_hop=None):
		self.next_hop = next_hop

	def __str__(self):
		return ""

class Route_map__set__ipv6__next_hop_1__local(AxapiObject):
	__metaclass__ = StructMeta 
	address=SizedString(1, 255)
	def __init__(self, address=None):
		self.address = address

	def __str__(self):
		return ""

class Route_map__set__ipv6__next_hop_1(AxapiObject):
	__metaclass__ = StructMeta 
	address=SizedString(1, 255)
	def __init__(self, address=None, local=None):
		self.address = address
		self.local = local

	def __str__(self):
		return ""

class Route_map__set__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, next_hop_1=None):
		self.next_hop_1 = next_hop_1

	def __str__(self):
		return ""

class Route_map__set__level(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(0, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Route_map__set__metric(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Route_map__set__metric_type(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Route_map__set__tag(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Route_map__set__aggregator__as(AxapiObject):
	__metaclass__ = StructMeta 
	asn=PosRangedInteger(1, 4294967295)
	ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, asn=None, ip=None):
		self.asn = asn
		self.ip = ip

	def __str__(self):
		return ""

class Route_map__set__aggregator(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, py_kw_rsvd_as=None):
		self.py_kw_rsvd_as = py_kw_rsvd_as

	def __str__(self):
		return ""

class Route_map__set__as_path(AxapiObject):
	__metaclass__ = StructMeta 
	prepend=SizedString(1, 255)
	num=PosRangedInteger(1, 4294967295)
	num2=PosRangedInteger(1, 4294967295)
	def __init__(self, prepend=None, num=None, num2=None):
		self.prepend = prepend
		self.num = num
		self.num2 = num2

	def __str__(self):
		return ""

class Route_map__set__comm_list(AxapiObject):
	__metaclass__ = StructMeta 
	v_std=PosRangedInteger(1, 99)
	delete=PosRangedInteger(0, 1)
	v_exp=PosRangedInteger(100, 199)
	name=SizedString(1, 255)
	def __init__(self, v_std=None, delete=None, v_exp=None, name=None):
		self.v_std = v_std
		self.delete = delete
		self.v_exp = v_exp
		self.name = name

	def __str__(self):
		return ""

class Route_map__set__dampening_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dampening=PosRangedInteger(0, 1)
	dampening_half_time=PosRangedInteger(1, 45)
	dampening_reuse=PosRangedInteger(1, 20000)
	dampening_supress=PosRangedInteger(1, 20000)
	dampening_max_supress=PosRangedInteger(1, 255)
	dampening_penalty=PosRangedInteger(1, 45)
	def __init__(self, dampening=None, dampening_half_time=None, dampening_reuse=None, dampening_supress=None, dampening_max_supress=None, dampening_penalty=None):
		self.dampening = dampening
		self.dampening_half_time = dampening_half_time
		self.dampening_reuse = dampening_reuse
		self.dampening_supress = dampening_supress
		self.dampening_max_supress = dampening_max_supress
		self.dampening_penalty = dampening_penalty

	def __str__(self):
		return ""

class Route_map__set__extcommunity__rt(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Route_map__set__extcommunity__soo(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Route_map__set__extcommunity(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, rt=None, soo=None):
		self.rt = rt
		self.soo = soo

	def __str__(self):
		return ""

class Route_map__set__local_preference(AxapiObject):
	__metaclass__ = StructMeta 
	val=PosRangedInteger(0, 4294967295)
	def __init__(self, val=None):
		self.val = val

	def __str__(self):
		return ""

class Route_map__set__originator_id(AxapiObject):
	__metaclass__ = StructMeta 
	originator_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, originator_ip=None):
		self.originator_ip = originator_ip

	def __str__(self):
		return ""

class Route_map__set__weight(AxapiObject):
	__metaclass__ = StructMeta 
	weight_val=PosRangedInteger(0, 4294967295)
	def __init__(self, weight_val=None):
		self.weight_val = weight_val

	def __str__(self):
		return ""

class Route_map__set__origin(AxapiObject):
	__metaclass__ = StructMeta 
	egp=PosRangedInteger(0, 1)
	igp=PosRangedInteger(0, 1)
	incomplete=PosRangedInteger(0, 1)
	def __init__(self, egp=None, igp=None, incomplete=None):
		self.egp = egp
		self.igp = igp
		self.incomplete = incomplete

	def __str__(self):
		return ""

class Route_map__set(AxapiObject):
	__metaclass__ = StructMeta 
	atomic_aggregate=PosRangedInteger(0, 1)
	community=SizedString(1, 255)
	community_num=PosRangedInteger(1, 4294967295)
	community_num_aa_nn=SizedString(1, 255)
	internet=PosRangedInteger(0, 1)
	local_as=PosRangedInteger(0, 1)
	no_advertise=PosRangedInteger(0, 1)
	no_export=PosRangedInteger(0, 1)
	none=PosRangedInteger(0, 1)
	community_num2=PosRangedInteger(1, 4294967295)
	community_num_aa_nn2=SizedString(1, 255)
	internet2=PosRangedInteger(0, 1)
	local_as2=PosRangedInteger(0, 1)
	no_advertise2=PosRangedInteger(0, 1)
	no_export2=PosRangedInteger(0, 1)
	additive=PosRangedInteger(0, 1)
	def __init__(self, ip=None, ipv6=None, level=None, metric=None, metric_type=None, tag=None, aggregator=None, as_path=None, atomic_aggregate=None, comm_list=None, community=None, community_num=None, community_num_aa_nn=None, internet=None, local_as=None, no_advertise=None, no_export=None, none=None, community_num2=None, community_num_aa_nn2=None, internet2=None, local_as2=None, no_advertise2=None, no_export2=None, additive=None, dampening_cfg=None, extcommunity=None, local_preference=None, originator_id=None, weight=None, origin=None):
		self.ip = ip
		self.ipv6 = ipv6
		self.level = level
		self.metric = metric
		self.metric_type = metric_type
		self.tag = tag
		self.aggregator = aggregator
		self.as_path = as_path
		self.atomic_aggregate = atomic_aggregate
		self.comm_list = comm_list
		self.community = community
		self.community_num = community_num
		self.community_num_aa_nn = community_num_aa_nn
		self.internet = internet
		self.local_as = local_as
		self.no_advertise = no_advertise
		self.no_export = no_export
		self.none = none
		self.community_num2 = community_num2
		self.community_num_aa_nn2 = community_num_aa_nn2
		self.internet2 = internet2
		self.local_as2 = local_as2
		self.no_advertise2 = no_advertise2
		self.no_export2 = no_export2
		self.additive = additive
		self.dampening_cfg = dampening_cfg
		self.extcommunity = extcommunity
		self.local_preference = local_preference
		self.originator_id = originator_id
		self.weight = weight
		self.origin = origin

	def __str__(self):
		return ""

class Route_map(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, tag_cfg, match=None, set=None):
		self.tag_cfg = tag_cfg
		self.match = match
		self.set = set

	def __str__(self):
		return str(self.tag_cfg)

class RoutemapClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRoutemap(self, route_map_tag_cfg_action_sequence):
		"""
		Retrieve the route_map identified by the specified identifier
		
		Args:
			route_map_tag_cfg_action_sequence Route_map_tag_cfg_action_sequence
		
		Returns:
			An instance of the Route_map class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(route_map_tag_cfg_action_sequence) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified route_map does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('route-map')
		return deserialize_Route_map_json(payload)

	def putRoutemap(self, route_map_tag_cfg_action_sequence, route_map):
		"""
		Replace the object route_map
		
		Args:
			route_map_tag_cfg_action_sequence Route_map_tag_cfg_action_sequence
			route_map An instance of the Route_map class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['route-map']=serialize_Route_map_json(route_map)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(route_map_tag_cfg_action_sequence) .replace("/", "%2f") + query, payload, headers)
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

	def deleteRoutemap(self, route_map_tag_cfg_action_sequence):
		"""
		Remove the route_map identified by the specified identifier from the system
		
		Args:
			route_map_tag_cfg_action_sequence Route_map_tag_cfg_action_sequence
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(route_map_tag_cfg_action_sequence) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified route_map does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllRoutemapsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitRoutemap(self, route_map):
		"""
		Create the object route_map
		
		Args:
			route_map An instance of the Route_map class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['route-map']=serialize_Route_map_json(route_map)
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

	def getAllRoutemaps(self):
		"""
		Retrieve all route_map objects currently pending in the system
		
		Returns:
			A list of Route_map objects
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
			payload= data.get('route-mapList')
		return deserialize_list_Route_map_json(payload)

