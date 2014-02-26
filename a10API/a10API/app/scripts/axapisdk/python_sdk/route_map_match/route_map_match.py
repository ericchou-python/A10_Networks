########################################################################################################################
# File name: route_map_match.py
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
	'https://axapi.a10networks.com/axapi/v3/route-map/match',
]

def deserialize_Match__as_path_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	result = Match__as_path(name=name)
	return result

def deserialize_Match__community__l_std_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	l_std = data.get('l-std')
	exact_match = data.get('exact-match')
	result = Match__community__l_std_cfg(l_std=l_std, exact_match=exact_match)
	return result

def deserialize_Match__community__l_ext_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	l_ext = data.get('l-ext')
	exact_match = data.get('exact-match')
	result = Match__community__l_ext_cfg(l_ext=l_ext, exact_match=exact_match)
	return result

def deserialize_Match__community__name_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	exact_match = data.get('exact-match')
	result = Match__community__name_cfg(name=name, exact_match=exact_match)
	return result

def deserialize_Match__community_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	l_std_cfg = deserialize_Match__community__l_std_cfg_json(data.get('l-std-cfg'))
	l_ext_cfg = deserialize_Match__community__l_ext_cfg_json(data.get('l-ext-cfg'))
	name_cfg = deserialize_Match__community__name_cfg_json(data.get('name-cfg'))
	result = Match__community(l_std_cfg=l_std_cfg, l_ext_cfg=l_ext_cfg, name_cfg=name_cfg)
	return result

def deserialize_Match__extcommunity__extcommunity_l_std_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	l_std = data.get('l-std')
	exact_match = data.get('exact-match')
	result = Match__extcommunity__extcommunity_l_std_cfg(l_std=l_std, exact_match=exact_match)
	return result

def deserialize_Match__extcommunity__extcommunity_l_ext_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	l_ext = data.get('l-ext')
	exact_match = data.get('exact-match')
	result = Match__extcommunity__extcommunity_l_ext_cfg(l_ext=l_ext, exact_match=exact_match)
	return result

def deserialize_Match__extcommunity__extcommunity_l_name_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	exact_match = data.get('exact-match')
	result = Match__extcommunity__extcommunity_l_name(name=name, exact_match=exact_match)
	return result

def deserialize_Match__extcommunity_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	extcommunity_l_std_cfg = deserialize_Match__extcommunity__extcommunity_l_std_cfg_json(data.get('extcommunity-l-std-cfg'))
	extcommunity_l_ext_cfg = deserialize_Match__extcommunity__extcommunity_l_ext_cfg_json(data.get('extcommunity-l-ext-cfg'))
	extcommunity_l_name = deserialize_Match__extcommunity__extcommunity_l_name_json(data.get('extcommunity-l-name'))
	result = Match__extcommunity(extcommunity_l_std_cfg=extcommunity_l_std_cfg, extcommunity_l_ext_cfg=extcommunity_l_ext_cfg, extcommunity_l_name=extcommunity_l_name)
	return result

def deserialize_Match__interface_json(obj):
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
	result = Match__interface(ethernet=ethernet, loopback=loopback, trunk=trunk, ve=ve)
	return result

def deserialize_Match__origin_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	egp = data.get('egp')
	igp = data.get('igp')
	incomplete = data.get('incomplete')
	result = Match__origin(egp=egp, igp=igp, incomplete=incomplete)
	return result

def deserialize_Match__ip__address__prefix_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	result = Match__ip__address__prefix_list(name=name)
	return result

def deserialize_Match__ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl1 = data.get('acl1')
	acl2 = data.get('acl2')
	name = data.get('name')
	prefix_list = deserialize_Match__ip__address__prefix_list_json(data.get('prefix-list'))
	result = Match__ip__address(acl1=acl1, acl2=acl2, name=name, prefix_list=prefix_list)
	return result

def deserialize_Match__ip__next_hop__prefix_list_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	result = Match__ip__next_hop__prefix_list_1(name=name)
	return result

def deserialize_Match__ip__next_hop_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl1 = data.get('acl1')
	acl2 = data.get('acl2')
	name = data.get('name')
	prefix_list_1 = deserialize_Match__ip__next_hop__prefix_list_1_json(data.get('prefix-list-1'))
	result = Match__ip__next_hop(acl1=acl1, acl2=acl2, name=name, prefix_list_1=prefix_list_1)
	return result

def deserialize_Match__ip__peer_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl1 = data.get('acl1')
	acl2 = data.get('acl2')
	name = data.get('name')
	result = Match__ip__peer(acl1=acl1, acl2=acl2, name=name)
	return result

def deserialize_Match__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Match__ip__address_json(data.get('address'))
	next_hop = deserialize_Match__ip__next_hop_json(data.get('next-hop'))
	peer = deserialize_Match__ip__peer_json(data.get('peer'))
	result = Match__ip(address=address, next_hop=next_hop, peer=peer)
	return result

def deserialize_Match__ipv6__address_1__prefix_list_2_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	result = Match__ipv6__address_1__prefix_list_2(name=name)
	return result

def deserialize_Match__ipv6__address_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	prefix_list_2 = deserialize_Match__ipv6__address_1__prefix_list_2_json(data.get('prefix-list-2'))
	result = Match__ipv6__address_1(name=name, prefix_list_2=prefix_list_2)
	return result

def deserialize_Match__ipv6__next_hop_1__prefix_list_3_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	result = Match__ipv6__next_hop_1__prefix_list_3(name=name)
	return result

def deserialize_Match__ipv6__next_hop_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	v6_addr = data.get('v6-addr')
	prefix_list_3 = deserialize_Match__ipv6__next_hop_1__prefix_list_3_json(data.get('prefix-list-3'))
	result = Match__ipv6__next_hop_1(name=name, v6_addr=v6_addr, prefix_list_3=prefix_list_3)
	return result

def deserialize_Match__ipv6__peer_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	acl1 = data.get('acl1')
	acl2 = data.get('acl2')
	name = data.get('name')
	result = Match__ipv6__peer_1(acl1=acl1, acl2=acl2, name=name)
	return result

def deserialize_Match__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_1 = deserialize_Match__ipv6__address_1_json(data.get('address-1'))
	next_hop_1 = deserialize_Match__ipv6__next_hop_1_json(data.get('next-hop-1'))
	peer_1 = deserialize_Match__ipv6__peer_1_json(data.get('peer-1'))
	result = Match__ipv6(address_1=address_1, next_hop_1=next_hop_1, peer_1=peer_1)
	return result

def deserialize_Match__metric_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Match__metric(value=value)
	return result

def deserialize_Match__route_type__external_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Match__route_type__external(value=value)
	return result

def deserialize_Match__route_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	external = deserialize_Match__route_type__external_json(data.get('external'))
	result = Match__route_type(external=external)
	return result

def deserialize_Match__tag_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Match__tag(value=value)
	return result

def deserialize_Match_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	as_path = deserialize_Match__as_path_json(data.get('as-path'))
	community = deserialize_Match__community_json(data.get('community'))
	extcommunity = deserialize_Match__extcommunity_json(data.get('extcommunity'))
	interface = deserialize_Match__interface_json(data.get('interface'))
	origin = deserialize_Match__origin_json(data.get('origin'))
	ip = deserialize_Match__ip_json(data.get('ip'))
	ipv6 = deserialize_Match__ipv6_json(data.get('ipv6'))
	metric = deserialize_Match__metric_json(data.get('metric'))
	route_type = deserialize_Match__route_type_json(data.get('route-type'))
	tag = deserialize_Match__tag_json(data.get('tag'))
	result = Match(as_path=as_path, community=community, extcommunity=extcommunity, interface=interface, origin=origin, ip=ip, ipv6=ipv6, metric=metric, route_type=route_type, tag=tag)
	return result

def serialize_Match__as_path_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Match__community__l_std_cfg_json(obj):
	output = OrderedDict()
	if obj.l_std is not None:
		output['l-std'] = obj.l_std
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Match__community__l_ext_cfg_json(obj):
	output = OrderedDict()
	if obj.l_ext is not None:
		output['l-ext'] = obj.l_ext
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Match__community__name_cfg_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Match__community_json(obj):
	output = OrderedDict()
	if obj.l_std_cfg is not None:
		output['l-std-cfg'] = serialize_Match__community__l_std_cfg_json(obj.l_std_cfg)
	if obj.l_ext_cfg is not None:
		output['l-ext-cfg'] = serialize_Match__community__l_ext_cfg_json(obj.l_ext_cfg)
	if obj.name_cfg is not None:
		output['name-cfg'] = serialize_Match__community__name_cfg_json(obj.name_cfg)
	return output

def serialize_Match__extcommunity__extcommunity_l_std_cfg_json(obj):
	output = OrderedDict()
	if obj.l_std is not None:
		output['l-std'] = obj.l_std
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Match__extcommunity__extcommunity_l_ext_cfg_json(obj):
	output = OrderedDict()
	if obj.l_ext is not None:
		output['l-ext'] = obj.l_ext
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Match__extcommunity__extcommunity_l_name_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	if obj.exact_match is not None:
		output['exact-match'] = obj.exact_match
	return output

def serialize_Match__extcommunity_json(obj):
	output = OrderedDict()
	if obj.extcommunity_l_std_cfg is not None:
		output['extcommunity-l-std-cfg'] = serialize_Match__extcommunity__extcommunity_l_std_cfg_json(obj.extcommunity_l_std_cfg)
	if obj.extcommunity_l_ext_cfg is not None:
		output['extcommunity-l-ext-cfg'] = serialize_Match__extcommunity__extcommunity_l_ext_cfg_json(obj.extcommunity_l_ext_cfg)
	if obj.extcommunity_l_name is not None:
		output['extcommunity-l-name'] = serialize_Match__extcommunity__extcommunity_l_name_json(obj.extcommunity_l_name)
	return output

def serialize_Match__interface_json(obj):
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

def serialize_Match__origin_json(obj):
	output = OrderedDict()
	if obj.egp is not None:
		output['egp'] = obj.egp
	if obj.igp is not None:
		output['igp'] = obj.igp
	if obj.incomplete is not None:
		output['incomplete'] = obj.incomplete
	return output

def serialize_Match__ip__address__prefix_list_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Match__ip__address_json(obj):
	output = OrderedDict()
	if obj.acl1 is not None:
		output['acl1'] = obj.acl1
	if obj.acl2 is not None:
		output['acl2'] = obj.acl2
	if obj.name is not None:
		output['name'] = obj.name
	if obj.prefix_list is not None:
		output['prefix-list'] = serialize_Match__ip__address__prefix_list_json(obj.prefix_list)
	return output

def serialize_Match__ip__next_hop__prefix_list_1_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Match__ip__next_hop_json(obj):
	output = OrderedDict()
	if obj.acl1 is not None:
		output['acl1'] = obj.acl1
	if obj.acl2 is not None:
		output['acl2'] = obj.acl2
	if obj.name is not None:
		output['name'] = obj.name
	if obj.prefix_list_1 is not None:
		output['prefix-list-1'] = serialize_Match__ip__next_hop__prefix_list_1_json(obj.prefix_list_1)
	return output

def serialize_Match__ip__peer_json(obj):
	output = OrderedDict()
	if obj.acl1 is not None:
		output['acl1'] = obj.acl1
	if obj.acl2 is not None:
		output['acl2'] = obj.acl2
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Match__ip_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = serialize_Match__ip__address_json(obj.address)
	if obj.next_hop is not None:
		output['next-hop'] = serialize_Match__ip__next_hop_json(obj.next_hop)
	if obj.peer is not None:
		output['peer'] = serialize_Match__ip__peer_json(obj.peer)
	return output

def serialize_Match__ipv6__address_1__prefix_list_2_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Match__ipv6__address_1_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	if obj.prefix_list_2 is not None:
		output['prefix-list-2'] = serialize_Match__ipv6__address_1__prefix_list_2_json(obj.prefix_list_2)
	return output

def serialize_Match__ipv6__next_hop_1__prefix_list_3_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Match__ipv6__next_hop_1_json(obj):
	output = OrderedDict()
	if obj.name is not None:
		output['name'] = obj.name
	if obj.v6_addr is not None:
		output['v6-addr'] = obj.v6_addr
	if obj.prefix_list_3 is not None:
		output['prefix-list-3'] = serialize_Match__ipv6__next_hop_1__prefix_list_3_json(obj.prefix_list_3)
	return output

def serialize_Match__ipv6__peer_1_json(obj):
	output = OrderedDict()
	if obj.acl1 is not None:
		output['acl1'] = obj.acl1
	if obj.acl2 is not None:
		output['acl2'] = obj.acl2
	if obj.name is not None:
		output['name'] = obj.name
	return output

def serialize_Match__ipv6_json(obj):
	output = OrderedDict()
	if obj.address_1 is not None:
		output['address-1'] = serialize_Match__ipv6__address_1_json(obj.address_1)
	if obj.next_hop_1 is not None:
		output['next-hop-1'] = serialize_Match__ipv6__next_hop_1_json(obj.next_hop_1)
	if obj.peer_1 is not None:
		output['peer-1'] = serialize_Match__ipv6__peer_1_json(obj.peer_1)
	return output

def serialize_Match__metric_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Match__route_type__external_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Match__route_type_json(obj):
	output = OrderedDict()
	if obj.external is not None:
		output['external'] = serialize_Match__route_type__external_json(obj.external)
	return output

def serialize_Match__tag_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Match_json(obj):
	output = OrderedDict()
	if obj.as_path is not None:
		output['as-path'] = serialize_Match__as_path_json(obj.as_path)
	if obj.community is not None:
		output['community'] = serialize_Match__community_json(obj.community)
	if obj.extcommunity is not None:
		output['extcommunity'] = serialize_Match__extcommunity_json(obj.extcommunity)
	if obj.interface is not None:
		output['interface'] = serialize_Match__interface_json(obj.interface)
	if obj.origin is not None:
		output['origin'] = serialize_Match__origin_json(obj.origin)
	if obj.ip is not None:
		output['ip'] = serialize_Match__ip_json(obj.ip)
	if obj.ipv6 is not None:
		output['ipv6'] = serialize_Match__ipv6_json(obj.ipv6)
	if obj.metric is not None:
		output['metric'] = serialize_Match__metric_json(obj.metric)
	if obj.route_type is not None:
		output['route-type'] = serialize_Match__route_type_json(obj.route_type)
	if obj.tag is not None:
		output['tag'] = serialize_Match__tag_json(obj.tag)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Match_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Match_json(item))
	return list(container)

class Match__as_path(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None):
		self.name = name

	def __str__(self):
		return ""

class Match__community__l_std_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	l_std=PosRangedInteger(1, 99)
	exact_match=PosRangedInteger(0, 1)
	def __init__(self, l_std=None, exact_match=None):
		self.l_std = l_std
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Match__community__l_ext_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	l_ext=PosRangedInteger(100, 199)
	exact_match=PosInteger()
	def __init__(self, l_ext=None, exact_match=None):
		self.l_ext = l_ext
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Match__community__name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	exact_match=PosInteger()
	def __init__(self, name=None, exact_match=None):
		self.name = name
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Match__community(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, l_std_cfg=None, l_ext_cfg=None, name_cfg=None):
		self.l_std_cfg = l_std_cfg
		self.l_ext_cfg = l_ext_cfg
		self.name_cfg = name_cfg

	def __str__(self):
		return ""

class Match__extcommunity__extcommunity_l_std_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	l_std=PosRangedInteger(1, 99)
	exact_match=PosInteger()
	def __init__(self, l_std=None, exact_match=None):
		self.l_std = l_std
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Match__extcommunity__extcommunity_l_ext_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	l_ext=PosRangedInteger(100, 199)
	exact_match=PosInteger()
	def __init__(self, l_ext=None, exact_match=None):
		self.l_ext = l_ext
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Match__extcommunity__extcommunity_l_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	exact_match=PosInteger()
	def __init__(self, name=None, exact_match=None):
		self.name = name
		self.exact_match = exact_match

	def __str__(self):
		return ""

class Match__extcommunity(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, extcommunity_l_std_cfg=None, extcommunity_l_ext_cfg=None, extcommunity_l_name=None):
		self.extcommunity_l_std_cfg = extcommunity_l_std_cfg
		self.extcommunity_l_ext_cfg = extcommunity_l_ext_cfg
		self.extcommunity_l_name = extcommunity_l_name

	def __str__(self):
		return ""

class Match__interface(AxapiObject):
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

class Match__origin(AxapiObject):
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

class Match__ip__address__prefix_list(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None):
		self.name = name

	def __str__(self):
		return ""

class Match__ip__address(AxapiObject):
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

class Match__ip__next_hop__prefix_list_1(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None):
		self.name = name

	def __str__(self):
		return ""

class Match__ip__next_hop(AxapiObject):
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

class Match__ip__peer(AxapiObject):
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

class Match__ip(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address=None, next_hop=None, peer=None):
		self.address = address
		self.next_hop = next_hop
		self.peer = peer

	def __str__(self):
		return ""

class Match__ipv6__address_1__prefix_list_2(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None):
		self.name = name

	def __str__(self):
		return ""

class Match__ipv6__address_1(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None, prefix_list_2=None):
		self.name = name
		self.prefix_list_2 = prefix_list_2

	def __str__(self):
		return ""

class Match__ipv6__next_hop_1__prefix_list_3(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name=None):
		self.name = name

	def __str__(self):
		return ""

class Match__ipv6__next_hop_1(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	v6_addr=SizedString(1, 255)
	def __init__(self, name=None, v6_addr=None, prefix_list_3=None):
		self.name = name
		self.v6_addr = v6_addr
		self.prefix_list_3 = prefix_list_3

	def __str__(self):
		return ""

class Match__ipv6__peer_1(AxapiObject):
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

class Match__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address_1=None, next_hop_1=None, peer_1=None):
		self.address_1 = address_1
		self.next_hop_1 = next_hop_1
		self.peer_1 = peer_1

	def __str__(self):
		return ""

class Match__metric(AxapiObject):
	__metaclass__ = StructMeta 
	value=PosRangedInteger(0, 4294967295)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Match__route_type__external(AxapiObject):
	__metaclass__ = StructMeta 
	value=PosRangedInteger(0, 4294967295)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Match__route_type(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, external=None):
		self.external = external

	def __str__(self):
		return ""

class Match__tag(AxapiObject):
	__metaclass__ = StructMeta 
	value=PosRangedInteger(0, 4294967295)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Match(AxapiObject):
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

class RoutemapMatchClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRoutemapMatch(self):
		"""
		Retrieve the match identified by the specified identifier
		
		Returns:
			An instance of the Match class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified match does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('match')
		return deserialize_Match_json(payload)

	def putRoutemapMatch(self, match):
		"""
		Replace the object match
		
		Args:
			match An instance of the Match class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['match']=serialize_Match_json(match)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + query, payload, headers)
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

	def deleteRoutemapMatch(self):
		"""
		Remove the match identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified match does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllRoutemapMatchsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitRoutemapMatch(self, match):
		"""
		Create the object match
		
		Args:
			match An instance of the Match class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['match']=serialize_Match_json(match)
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

	def getAllRoutemapMatchs(self):
		"""
		Retrieve all match objects currently pending in the system
		
		Returns:
			A list of Match objects
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
			payload= data.get('matchList')
		return deserialize_list_Match_json(payload)

