########################################################################################################################
# File name: route_map_set.py
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
	'https://axapi.a10networks.com/axapi/v3/route-map/set',
]

def deserialize_Set__ip__next_hop_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = data.get('address')
	result = Set__ip__next_hop(address=address)
	return result

def deserialize_Set__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	next_hop = deserialize_Set__ip__next_hop_json(data.get('next-hop'))
	result = Set__ip(next_hop=next_hop)
	return result

def deserialize_Set__ipv6__next_hop_1__local_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = data.get('address')
	result = Set__ipv6__next_hop_1__local(address=address)
	return result

def deserialize_Set__ipv6__next_hop_1_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = data.get('address')
	local = deserialize_Set__ipv6__next_hop_1__local_json(data.get('local'))
	result = Set__ipv6__next_hop_1(address=address, local=local)
	return result

def deserialize_Set__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	next_hop_1 = deserialize_Set__ipv6__next_hop_1_json(data.get('next-hop-1'))
	result = Set__ipv6(next_hop_1=next_hop_1)
	return result

def deserialize_Set__level_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Set__level(value=value)
	return result

def deserialize_Set__metric_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Set__metric(value=value)
	return result

def deserialize_Set__metric_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Set__metric_type(value=value)
	return result

def deserialize_Set__tag_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Set__tag(value=value)
	return result

def deserialize_Set__aggregator__as_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	asn = data.get('asn')
	ip = data.get('ip')
	result = Set__aggregator__as(asn=asn, ip=ip)
	return result

def deserialize_Set__aggregator_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	py_kw_rsvd_as = deserialize_Set__aggregator__as_json(data.get('as'))
	result = Set__aggregator(py_kw_rsvd_as=py_kw_rsvd_as)
	return result

def deserialize_Set__as_path_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	prepend = data.get('prepend')
	num = data.get('num')
	num2 = data.get('num2')
	result = Set__as_path(prepend=prepend, num=num, num2=num2)
	return result

def deserialize_Set__comm_list_json(obj):
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
	result = Set__comm_list(v_std=v_std, delete=delete, v_exp=v_exp, name=name)
	return result

def deserialize_Set__dampening_cfg_json(obj):
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
	result = Set__dampening_cfg(dampening=dampening, dampening_half_time=dampening_half_time, dampening_reuse=dampening_reuse, dampening_supress=dampening_supress, dampening_max_supress=dampening_max_supress, dampening_penalty=dampening_penalty)
	return result

def deserialize_Set__extcommunity__rt_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Set__extcommunity__rt(value=value)
	return result

def deserialize_Set__extcommunity__soo_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	result = Set__extcommunity__soo(value=value)
	return result

def deserialize_Set__extcommunity_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	rt = deserialize_Set__extcommunity__rt_json(data.get('rt'))
	soo = deserialize_Set__extcommunity__soo_json(data.get('soo'))
	result = Set__extcommunity(rt=rt, soo=soo)
	return result

def deserialize_Set__local_preference_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	val = data.get('val')
	result = Set__local_preference(val=val)
	return result

def deserialize_Set__originator_id_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	originator_ip = data.get('originator-ip')
	result = Set__originator_id(originator_ip=originator_ip)
	return result

def deserialize_Set__weight_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	weight_val = data.get('weight-val')
	result = Set__weight(weight_val=weight_val)
	return result

def deserialize_Set__origin_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	egp = data.get('egp')
	igp = data.get('igp')
	incomplete = data.get('incomplete')
	result = Set__origin(egp=egp, igp=igp, incomplete=incomplete)
	return result

def deserialize_Set_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip = deserialize_Set__ip_json(data.get('ip'))
	ipv6 = deserialize_Set__ipv6_json(data.get('ipv6'))
	level = deserialize_Set__level_json(data.get('level'))
	metric = deserialize_Set__metric_json(data.get('metric'))
	metric_type = deserialize_Set__metric_type_json(data.get('metric-type'))
	tag = deserialize_Set__tag_json(data.get('tag'))
	aggregator = deserialize_Set__aggregator_json(data.get('aggregator'))
	as_path = deserialize_Set__as_path_json(data.get('as-path'))
	atomic_aggregate = data.get('atomic-aggregate')
	comm_list = deserialize_Set__comm_list_json(data.get('comm-list'))
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
	dampening_cfg = deserialize_Set__dampening_cfg_json(data.get('dampening-cfg'))
	extcommunity = deserialize_Set__extcommunity_json(data.get('extcommunity'))
	local_preference = deserialize_Set__local_preference_json(data.get('local-preference'))
	originator_id = deserialize_Set__originator_id_json(data.get('originator-id'))
	weight = deserialize_Set__weight_json(data.get('weight'))
	origin = deserialize_Set__origin_json(data.get('origin'))
	result = Set(ip=ip, ipv6=ipv6, level=level, metric=metric, metric_type=metric_type, tag=tag, aggregator=aggregator, as_path=as_path, atomic_aggregate=atomic_aggregate, comm_list=comm_list, community=community, community_num=community_num, community_num_aa_nn=community_num_aa_nn, internet=internet, local_as=local_as, no_advertise=no_advertise, no_export=no_export, none=none, community_num2=community_num2, community_num_aa_nn2=community_num_aa_nn2, internet2=internet2, local_as2=local_as2, no_advertise2=no_advertise2, no_export2=no_export2, additive=additive, dampening_cfg=dampening_cfg, extcommunity=extcommunity, local_preference=local_preference, originator_id=originator_id, weight=weight, origin=origin)
	return result

def serialize_Set__ip__next_hop_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = obj.address
	return output

def serialize_Set__ip_json(obj):
	output = OrderedDict()
	if obj.next_hop is not None:
		output['next-hop'] = serialize_Set__ip__next_hop_json(obj.next_hop)
	return output

def serialize_Set__ipv6__next_hop_1__local_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = obj.address
	return output

def serialize_Set__ipv6__next_hop_1_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = obj.address
	if obj.local is not None:
		output['local'] = serialize_Set__ipv6__next_hop_1__local_json(obj.local)
	return output

def serialize_Set__ipv6_json(obj):
	output = OrderedDict()
	if obj.next_hop_1 is not None:
		output['next-hop-1'] = serialize_Set__ipv6__next_hop_1_json(obj.next_hop_1)
	return output

def serialize_Set__level_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Set__metric_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Set__metric_type_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Set__tag_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Set__aggregator__as_json(obj):
	output = OrderedDict()
	if obj.asn is not None:
		output['asn'] = obj.asn
	if obj.ip is not None:
		output['ip'] = obj.ip
	return output

def serialize_Set__aggregator_json(obj):
	output = OrderedDict()
	if obj.py_kw_rsvd_as is not None:
		output['as'] = serialize_Set__aggregator__as_json(obj.py_kw_rsvd_as)
	return output

def serialize_Set__as_path_json(obj):
	output = OrderedDict()
	if obj.prepend is not None:
		output['prepend'] = obj.prepend
	if obj.num is not None:
		output['num'] = obj.num
	if obj.num2 is not None:
		output['num2'] = obj.num2
	return output

def serialize_Set__comm_list_json(obj):
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

def serialize_Set__dampening_cfg_json(obj):
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

def serialize_Set__extcommunity__rt_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Set__extcommunity__soo_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Set__extcommunity_json(obj):
	output = OrderedDict()
	if obj.rt is not None:
		output['rt'] = serialize_Set__extcommunity__rt_json(obj.rt)
	if obj.soo is not None:
		output['soo'] = serialize_Set__extcommunity__soo_json(obj.soo)
	return output

def serialize_Set__local_preference_json(obj):
	output = OrderedDict()
	if obj.val is not None:
		output['val'] = obj.val
	return output

def serialize_Set__originator_id_json(obj):
	output = OrderedDict()
	if obj.originator_ip is not None:
		output['originator-ip'] = obj.originator_ip
	return output

def serialize_Set__weight_json(obj):
	output = OrderedDict()
	if obj.weight_val is not None:
		output['weight-val'] = obj.weight_val
	return output

def serialize_Set__origin_json(obj):
	output = OrderedDict()
	if obj.egp is not None:
		output['egp'] = obj.egp
	if obj.igp is not None:
		output['igp'] = obj.igp
	if obj.incomplete is not None:
		output['incomplete'] = obj.incomplete
	return output

def serialize_Set_json(obj):
	output = OrderedDict()
	if obj.ip is not None:
		output['ip'] = serialize_Set__ip_json(obj.ip)
	if obj.ipv6 is not None:
		output['ipv6'] = serialize_Set__ipv6_json(obj.ipv6)
	if obj.level is not None:
		output['level'] = serialize_Set__level_json(obj.level)
	if obj.metric is not None:
		output['metric'] = serialize_Set__metric_json(obj.metric)
	if obj.metric_type is not None:
		output['metric-type'] = serialize_Set__metric_type_json(obj.metric_type)
	if obj.tag is not None:
		output['tag'] = serialize_Set__tag_json(obj.tag)
	if obj.aggregator is not None:
		output['aggregator'] = serialize_Set__aggregator_json(obj.aggregator)
	if obj.as_path is not None:
		output['as-path'] = serialize_Set__as_path_json(obj.as_path)
	if obj.atomic_aggregate is not None:
		output['atomic-aggregate'] = obj.atomic_aggregate
	if obj.comm_list is not None:
		output['comm-list'] = serialize_Set__comm_list_json(obj.comm_list)
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
		output['dampening-cfg'] = serialize_Set__dampening_cfg_json(obj.dampening_cfg)
	if obj.extcommunity is not None:
		output['extcommunity'] = serialize_Set__extcommunity_json(obj.extcommunity)
	if obj.local_preference is not None:
		output['local-preference'] = serialize_Set__local_preference_json(obj.local_preference)
	if obj.originator_id is not None:
		output['originator-id'] = serialize_Set__originator_id_json(obj.originator_id)
	if obj.weight is not None:
		output['weight'] = serialize_Set__weight_json(obj.weight)
	if obj.origin is not None:
		output['origin'] = serialize_Set__origin_json(obj.origin)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Set_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Set_json(item))
	return list(container)

class Set__ip__next_hop(AxapiObject):
	__metaclass__ = StructMeta 
	address=SizedString(1, 255)
	def __init__(self, address=None):
		self.address = address

	def __str__(self):
		return ""

class Set__ip(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, next_hop=None):
		self.next_hop = next_hop

	def __str__(self):
		return ""

class Set__ipv6__next_hop_1__local(AxapiObject):
	__metaclass__ = StructMeta 
	address=SizedString(1, 255)
	def __init__(self, address=None):
		self.address = address

	def __str__(self):
		return ""

class Set__ipv6__next_hop_1(AxapiObject):
	__metaclass__ = StructMeta 
	address=SizedString(1, 255)
	def __init__(self, address=None, local=None):
		self.address = address
		self.local = local

	def __str__(self):
		return ""

class Set__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, next_hop_1=None):
		self.next_hop_1 = next_hop_1

	def __str__(self):
		return ""

class Set__level(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(0, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Set__metric(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Set__metric_type(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Set__tag(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Set__aggregator__as(AxapiObject):
	__metaclass__ = StructMeta 
	asn=PosRangedInteger(1, 4294967295)
	ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, asn=None, ip=None):
		self.asn = asn
		self.ip = ip

	def __str__(self):
		return ""

class Set__aggregator(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, py_kw_rsvd_as=None):
		self.py_kw_rsvd_as = py_kw_rsvd_as

	def __str__(self):
		return ""

class Set__as_path(AxapiObject):
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

class Set__comm_list(AxapiObject):
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

class Set__dampening_cfg(AxapiObject):
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

class Set__extcommunity__rt(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Set__extcommunity__soo(AxapiObject):
	__metaclass__ = StructMeta 
	value=SizedString(1, 255)
	def __init__(self, value=None):
		self.value = value

	def __str__(self):
		return ""

class Set__extcommunity(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, rt=None, soo=None):
		self.rt = rt
		self.soo = soo

	def __str__(self):
		return ""

class Set__local_preference(AxapiObject):
	__metaclass__ = StructMeta 
	val=PosRangedInteger(0, 4294967295)
	def __init__(self, val=None):
		self.val = val

	def __str__(self):
		return ""

class Set__originator_id(AxapiObject):
	__metaclass__ = StructMeta 
	originator_ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, originator_ip=None):
		self.originator_ip = originator_ip

	def __str__(self):
		return ""

class Set__weight(AxapiObject):
	__metaclass__ = StructMeta 
	weight_val=PosRangedInteger(0, 4294967295)
	def __init__(self, weight_val=None):
		self.weight_val = weight_val

	def __str__(self):
		return ""

class Set__origin(AxapiObject):
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

class Set(AxapiObject):
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

class RoutemapSetClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getRoutemapSet(self):
		"""
		Retrieve the set identified by the specified identifier
		
		Returns:
			An instance of the Set class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified set does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('set')
		return deserialize_Set_json(payload)

	def putRoutemapSet(self, set):
		"""
		Replace the object set
		
		Args:
			set An instance of the Set class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['set']=serialize_Set_json(set)
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

	def deleteRoutemapSet(self):
		"""
		Remove the set identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified set does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllRoutemapSetsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitRoutemapSet(self, set):
		"""
		Create the object set
		
		Args:
			set An instance of the Set class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['set']=serialize_Set_json(set)
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

	def getAllRoutemapSets(self):
		"""
		Retrieve all set objects currently pending in the system
		
		Returns:
			A list of Set objects
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
			payload= data.get('setList')
		return deserialize_list_Set_json(payload)

