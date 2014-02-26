########################################################################################################################
# File name: interface_trunk.py
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
	'https://axapi.a10networks.com/axapi/v3/interface/trunk',
]

def deserialize_Trunk__icmp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmp_rate_limit = data.get('icmp-rate-limit')
	normal_val = data.get('normal-val')
	lockup = data.get('lockup')
	lockup_period = data.get('lockup-period')
	result = Trunk__icmp_cfg(icmp_rate_limit=icmp_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
	return result

def deserialize_Trunk__icmpv6_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	icmpv6_rate_limit = data.get('icmpv6-rate-limit')
	normal_val = data.get('normal-val')
	lockup = data.get('lockup')
	lockup_period = data.get('lockup-period')
	result = Trunk__icmpv6_cfg(icmpv6_rate_limit=icmpv6_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
	return result

def deserialize_Interface_trunk_address_val_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val = data.get('address_val')
	netmask = data.get('netmask')
	result = Interface_trunk_address_val_cfg(address_val=address_val, netmask=netmask)
	return result

def deserialize_list_Interface_trunk_address_val_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_trunk_address_val_cfg_json(item))
	return list(container)

def deserialize_Trunk__ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val_cfg = deserialize_list_Interface_trunk_address_val_cfg_json(data.get('address_val-cfg'))
	dhcp = data.get('dhcp')
	result = Trunk__ip__address(address_val_cfg=address_val_cfg, dhcp=dhcp)
	return result

def deserialize_Trunk__ip__nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	inside = data.get('inside')
	outside = data.get('outside')
	result = Trunk__ip__nat(inside=inside, outside=outside)
	return result

def deserialize_Trunk__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Trunk__ip__address_json(data.get('address'))
	cache_spoofing_port = data.get('cache-spoofing-port')
	helper_address = data.get('helper-address')
	nat = deserialize_Trunk__ip__nat_json(data.get('nat'))
	generate_membership_query = data.get('generate-membership-query')
	generate_membership_query_val = data.get('generate-membership-query-val')
	max_resp_time = data.get('max-resp-time')
	result = Trunk__ip(address=address, cache_spoofing_port=cache_spoofing_port, helper_address=helper_address, nat=nat, generate_membership_query=generate_membership_query, generate_membership_query_val=generate_membership_query_val, max_resp_time=max_resp_time)
	return result

def deserialize_Interface_trunk_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	anycast = data.get('anycast')
	link_local = data.get('link-local')
	result = Interface_trunk_address_cfg(ipv6_addr=ipv6_addr, anycast=anycast, link_local=link_local)
	return result

def deserialize_list_Interface_trunk_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_trunk_address_cfg_json(item))
	return list(container)

def deserialize_Trunk__ipv6__nat_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	inside = data.get('inside')
	outside = data.get('outside')
	result = Trunk__ipv6__nat(inside=inside, outside=outside)
	return result

def deserialize_Trunk__ipv6__ndisc__router_adver__mtu_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_mtu = data.get('adver-mtu')
	adver_mtu_disable = data.get('adver-mtu-disable')
	result = Trunk__ipv6__ndisc__router_adver__mtu(adver_mtu=adver_mtu, adver_mtu_disable=adver_mtu_disable)
	return result

def deserialize_Interface_trunk_prefix_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	prefix = data.get('prefix')
	not_autonomous = data.get('not-autonomous')
	not_on_link = data.get('not-on-link')
	preferred_lifetime = data.get('preferred-lifetime')
	valid_lifetime = data.get('valid-lifetime')
	result = Interface_trunk_prefix_cfg(prefix=prefix, not_autonomous=not_autonomous, not_on_link=not_on_link, preferred_lifetime=preferred_lifetime, valid_lifetime=valid_lifetime)
	return result

def deserialize_list_Interface_trunk_prefix_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_trunk_prefix_cfg_json(item))
	return list(container)

def deserialize_Trunk__ipv6__ndisc__router_adver__vrid_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_vrid = data.get('adver-vrid')
	adver_vrid_default = data.get('adver-vrid-default')
	use_floating_ip = data.get('use-floating-ip')
	floating_ip = data.get('floating-ip')
	result = Trunk__ipv6__ndisc__router_adver__vrid(adver_vrid=adver_vrid, adver_vrid_default=adver_vrid_default, use_floating_ip=use_floating_ip, floating_ip=floating_ip)
	return result

def deserialize_Trunk__ipv6__ndisc__router_adver__ha_group_id_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_ha_group_id = data.get('adver-ha-group-id')
	ha_use_floating_ip = data.get('ha-use-floating-ip')
	ha_floating_ip = data.get('ha-floating-ip')
	result = Trunk__ipv6__ndisc__router_adver__ha_group_id(adver_ha_group_id=adver_ha_group_id, ha_use_floating_ip=ha_use_floating_ip, ha_floating_ip=ha_floating_ip)
	return result

def deserialize_Trunk__ipv6__ndisc__router_adver_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	adver_enable = data.get('adver-enable')
	adver_disable = data.get('adver-disable')
	default_lifetime = data.get('default-lifetime')
	hop_limit = data.get('hop-limit')
	max_interval = data.get('max-interval')
	min_interval = data.get('min-interval')
	rate_limit = data.get('rate-limit')
	reachable_time = data.get('reachable-time')
	retransmit_timer = data.get('retransmit-timer')
	mtu = deserialize_Trunk__ipv6__ndisc__router_adver__mtu_json(data.get('mtu'))
	prefix_cfg = deserialize_list_Interface_trunk_prefix_cfg_json(data.get('prefix-cfg'))
	vrid = deserialize_Trunk__ipv6__ndisc__router_adver__vrid_json(data.get('vrid'))
	ha_group_id = deserialize_Trunk__ipv6__ndisc__router_adver__ha_group_id_json(data.get('ha-group-id'))
	result = Trunk__ipv6__ndisc__router_adver(adver_enable=adver_enable, adver_disable=adver_disable, default_lifetime=default_lifetime, hop_limit=hop_limit, max_interval=max_interval, min_interval=min_interval, rate_limit=rate_limit, reachable_time=reachable_time, retransmit_timer=retransmit_timer, mtu=mtu, prefix_cfg=prefix_cfg, vrid=vrid, ha_group_id=ha_group_id)
	return result

def deserialize_Trunk__ipv6__ndisc_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	router_adver = deserialize_Trunk__ipv6__ndisc__router_adver_json(data.get('router-adver'))
	result = Trunk__ipv6__ndisc(router_adver=router_adver)
	return result

def deserialize_Trunk__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_cfg = deserialize_list_Interface_trunk_address_cfg_json(data.get('address-cfg'))
	ipv6_enable = data.get('ipv6-enable')
	nat = deserialize_Trunk__ipv6__nat_json(data.get('nat'))
	ndisc = deserialize_Trunk__ipv6__ndisc_json(data.get('ndisc'))
	result = Trunk__ipv6(address_cfg=address_cfg, ipv6_enable=ipv6_enable, nat=nat, ndisc=ndisc)
	return result

def deserialize_Trunk__ddos_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	outside = data.get('outside')
	inside = data.get('inside')
	result = Trunk__ddos(outside=outside, inside=inside)
	return result

def deserialize_Trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ifnum = data.get('ifnum')
	name = data.get('name')
	l3_vlan_fwd_disable = data.get('l3-vlan-fwd-disable')
	mtu = data.get('mtu')
	action = data.get('action')
	icmp_cfg = deserialize_Trunk__icmp_cfg_json(data.get('icmp-cfg'))
	icmpv6_cfg = deserialize_Trunk__icmpv6_cfg_json(data.get('icmpv6-cfg'))
	ip = deserialize_Trunk__ip_json(data.get('ip'))
	ipv6 = deserialize_Trunk__ipv6_json(data.get('ipv6'))
	ddos = deserialize_Trunk__ddos_json(data.get('ddos'))
	result = Trunk(ifnum=ifnum, name=name, l3_vlan_fwd_disable=l3_vlan_fwd_disable, mtu=mtu, action=action, icmp_cfg=icmp_cfg, icmpv6_cfg=icmpv6_cfg, ip=ip, ipv6=ipv6, ddos=ddos)
	return result

def serialize_Trunk__icmp_cfg_json(obj):
	output = OrderedDict()
	if obj.icmp_rate_limit is not None:
		output['icmp-rate-limit'] = obj.icmp_rate_limit
	if obj.normal_val is not None:
		output['normal-val'] = obj.normal_val
	if obj.lockup is not None:
		output['lockup'] = obj.lockup
	if obj.lockup_period is not None:
		output['lockup-period'] = obj.lockup_period
	return output

def serialize_Trunk__icmpv6_cfg_json(obj):
	output = OrderedDict()
	if obj.icmpv6_rate_limit is not None:
		output['icmpv6-rate-limit'] = obj.icmpv6_rate_limit
	if obj.normal_val is not None:
		output['normal-val'] = obj.normal_val
	if obj.lockup is not None:
		output['lockup'] = obj.lockup
	if obj.lockup_period is not None:
		output['lockup-period'] = obj.lockup_period
	return output

def serialize_Interface_trunk_address_val_cfg_json(obj):
	output = OrderedDict()
	if obj.address_val is not None:
		output['address_val'] = obj.address_val
	if obj.netmask is not None:
		output['netmask'] = obj.netmask
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Interface_trunk_address_val_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_trunk_address_val_cfg_json(item))
	return output

def serialize_Trunk__ip__address_json(obj):
	output = OrderedDict()
	if obj.address_val_cfg is not None:
		output['address_val-cfg'] = serialize_list_Interface_trunk_address_val_cfg_json(obj.address_val_cfg)
	if obj.dhcp is not None:
		output['dhcp'] = obj.dhcp
	return output

def serialize_Trunk__ip__nat_json(obj):
	output = OrderedDict()
	if obj.inside is not None:
		output['inside'] = obj.inside
	if obj.outside is not None:
		output['outside'] = obj.outside
	return output

def serialize_Trunk__ip_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = serialize_Trunk__ip__address_json(obj.address)
	if obj.cache_spoofing_port is not None:
		output['cache-spoofing-port'] = obj.cache_spoofing_port
	if obj.helper_address is not None:
		output['helper-address'] = obj.helper_address
	if obj.nat is not None:
		output['nat'] = serialize_Trunk__ip__nat_json(obj.nat)
	if obj.generate_membership_query is not None:
		output['generate-membership-query'] = obj.generate_membership_query
	if obj.generate_membership_query_val is not None:
		output['generate-membership-query-val'] = obj.generate_membership_query_val
	if obj.max_resp_time is not None:
		output['max-resp-time'] = obj.max_resp_time
	return output

def serialize_Interface_trunk_address_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv6_addr is not None:
		output['ipv6-addr'] = obj.ipv6_addr
	if obj.anycast is not None:
		output['anycast'] = obj.anycast
	if obj.link_local is not None:
		output['link-local'] = obj.link_local
	return output

def serialize_list_Interface_trunk_address_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_trunk_address_cfg_json(item))
	return output

def serialize_Trunk__ipv6__nat_json(obj):
	output = OrderedDict()
	if obj.inside is not None:
		output['inside'] = obj.inside
	if obj.outside is not None:
		output['outside'] = obj.outside
	return output

def serialize_Trunk__ipv6__ndisc__router_adver__mtu_json(obj):
	output = OrderedDict()
	if obj.adver_mtu is not None:
		output['adver-mtu'] = obj.adver_mtu
	if obj.adver_mtu_disable is not None:
		output['adver-mtu-disable'] = obj.adver_mtu_disable
	return output

def serialize_Interface_trunk_prefix_cfg_json(obj):
	output = OrderedDict()
	if obj.prefix is not None:
		output['prefix'] = obj.prefix
	if obj.not_autonomous is not None:
		output['not-autonomous'] = obj.not_autonomous
	if obj.not_on_link is not None:
		output['not-on-link'] = obj.not_on_link
	if obj.preferred_lifetime is not None:
		output['preferred-lifetime'] = obj.preferred_lifetime
	if obj.valid_lifetime is not None:
		output['valid-lifetime'] = obj.valid_lifetime
	return output

def serialize_list_Interface_trunk_prefix_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_trunk_prefix_cfg_json(item))
	return output

def serialize_Trunk__ipv6__ndisc__router_adver__vrid_json(obj):
	output = OrderedDict()
	if obj.adver_vrid is not None:
		output['adver-vrid'] = obj.adver_vrid
	if obj.adver_vrid_default is not None:
		output['adver-vrid-default'] = obj.adver_vrid_default
	if obj.use_floating_ip is not None:
		output['use-floating-ip'] = obj.use_floating_ip
	if obj.floating_ip is not None:
		output['floating-ip'] = obj.floating_ip
	return output

def serialize_Trunk__ipv6__ndisc__router_adver__ha_group_id_json(obj):
	output = OrderedDict()
	if obj.adver_ha_group_id is not None:
		output['adver-ha-group-id'] = obj.adver_ha_group_id
	if obj.ha_use_floating_ip is not None:
		output['ha-use-floating-ip'] = obj.ha_use_floating_ip
	if obj.ha_floating_ip is not None:
		output['ha-floating-ip'] = obj.ha_floating_ip
	return output

def serialize_Trunk__ipv6__ndisc__router_adver_json(obj):
	output = OrderedDict()
	if obj.adver_enable is not None:
		output['adver-enable'] = obj.adver_enable
	if obj.adver_disable is not None:
		output['adver-disable'] = obj.adver_disable
	if obj.default_lifetime is not None:
		output['default-lifetime'] = obj.default_lifetime
	if obj.hop_limit is not None:
		output['hop-limit'] = obj.hop_limit
	if obj.max_interval is not None:
		output['max-interval'] = obj.max_interval
	if obj.min_interval is not None:
		output['min-interval'] = obj.min_interval
	if obj.rate_limit is not None:
		output['rate-limit'] = obj.rate_limit
	if obj.reachable_time is not None:
		output['reachable-time'] = obj.reachable_time
	if obj.retransmit_timer is not None:
		output['retransmit-timer'] = obj.retransmit_timer
	if obj.mtu is not None:
		output['mtu'] = serialize_Trunk__ipv6__ndisc__router_adver__mtu_json(obj.mtu)
	if obj.prefix_cfg is not None:
		output['prefix-cfg'] = serialize_list_Interface_trunk_prefix_cfg_json(obj.prefix_cfg)
	if obj.vrid is not None:
		output['vrid'] = serialize_Trunk__ipv6__ndisc__router_adver__vrid_json(obj.vrid)
	if obj.ha_group_id is not None:
		output['ha-group-id'] = serialize_Trunk__ipv6__ndisc__router_adver__ha_group_id_json(obj.ha_group_id)
	return output

def serialize_Trunk__ipv6__ndisc_json(obj):
	output = OrderedDict()
	if obj.router_adver is not None:
		output['router-adver'] = serialize_Trunk__ipv6__ndisc__router_adver_json(obj.router_adver)
	return output

def serialize_Trunk__ipv6_json(obj):
	output = OrderedDict()
	if obj.address_cfg is not None:
		output['address-cfg'] = serialize_list_Interface_trunk_address_cfg_json(obj.address_cfg)
	if obj.ipv6_enable is not None:
		output['ipv6-enable'] = obj.ipv6_enable
	if obj.nat is not None:
		output['nat'] = serialize_Trunk__ipv6__nat_json(obj.nat)
	if obj.ndisc is not None:
		output['ndisc'] = serialize_Trunk__ipv6__ndisc_json(obj.ndisc)
	return output

def serialize_Trunk__ddos_json(obj):
	output = OrderedDict()
	if obj.outside is not None:
		output['outside'] = obj.outside
	if obj.inside is not None:
		output['inside'] = obj.inside
	return output

def serialize_Trunk_json(obj):
	output = OrderedDict()
	output['ifnum'] = obj.ifnum
	if obj.name is not None:
		output['name'] = obj.name
	if obj.l3_vlan_fwd_disable is not None:
		output['l3-vlan-fwd-disable'] = obj.l3_vlan_fwd_disable
	if obj.mtu is not None:
		output['mtu'] = obj.mtu
	if obj.action is not None:
		output['action'] = obj.action
	if obj.icmp_cfg is not None:
		output['icmp-cfg'] = serialize_Trunk__icmp_cfg_json(obj.icmp_cfg)
	if obj.icmpv6_cfg is not None:
		output['icmpv6-cfg'] = serialize_Trunk__icmpv6_cfg_json(obj.icmpv6_cfg)
	if obj.ip is not None:
		output['ip'] = serialize_Trunk__ip_json(obj.ip)
	if obj.ipv6 is not None:
		output['ipv6'] = serialize_Trunk__ipv6_json(obj.ipv6)
	if obj.ddos is not None:
		output['ddos'] = serialize_Trunk__ddos_json(obj.ddos)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Trunk_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Trunk_json(item))
	return list(container)

class Trunk__icmp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	icmp_rate_limit=PosRangedInteger(0, 1)
	normal_val=PosRangedInteger(1, 65535)
	lockup=PosRangedInteger(1, 65535)
	lockup_period=PosRangedInteger(1, 16383)
	def __init__(self, icmp_rate_limit=None, normal_val=None, lockup=None, lockup_period=None):
		self.icmp_rate_limit = icmp_rate_limit
		self.normal_val = normal_val
		self.lockup = lockup
		self.lockup_period = lockup_period

	def __str__(self):
		return ""

class Trunk__icmpv6_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	icmpv6_rate_limit=PosRangedInteger(0, 1)
	normal_val=PosRangedInteger(1, 65535)
	lockup=PosRangedInteger(1, 65535)
	lockup_period=PosRangedInteger(1, 16383)
	def __init__(self, icmpv6_rate_limit=None, normal_val=None, lockup=None, lockup_period=None):
		self.icmpv6_rate_limit = icmpv6_rate_limit
		self.normal_val = normal_val
		self.lockup = lockup
		self.lockup_period = lockup_period

	def __str__(self):
		return ""

class Trunk__ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	dhcp=PosRangedInteger(0, 1)
	def __init__(self, address_val_cfg=None, dhcp=None):
		self.address_val_cfg = address_val_cfg
		self.dhcp = dhcp

	def __str__(self):
		return ""

class Trunk__ip__nat(AxapiObject):
	__metaclass__ = StructMeta 
	inside=PosRangedInteger(0, 1)
	outside=PosRangedInteger(0, 1)
	def __init__(self, inside=None, outside=None):
		self.inside = inside
		self.outside = outside

	def __str__(self):
		return ""

class Trunk__ip(AxapiObject):
	__metaclass__ = StructMeta 
	cache_spoofing_port=PosRangedInteger(0, 1)
	helper_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	generate_membership_query=PosRangedInteger(0, 1)
	generate_membership_query_val=PosRangedInteger(1, 255)
	max_resp_time=PosRangedInteger(1, 255)
	def __init__(self, address=None, cache_spoofing_port=None, helper_address=None, nat=None, generate_membership_query=None, generate_membership_query_val=None, max_resp_time=None):
		self.address = address
		self.cache_spoofing_port = cache_spoofing_port
		self.helper_address = helper_address
		self.nat = nat
		self.generate_membership_query = generate_membership_query
		self.generate_membership_query_val = generate_membership_query_val
		self.max_resp_time = max_resp_time

	def __str__(self):
		return ""

class Trunk__ipv6__nat(AxapiObject):
	__metaclass__ = StructMeta 
	inside=PosRangedInteger(0, 1)
	outside=PosRangedInteger(0, 1)
	def __init__(self, inside=None, outside=None):
		self.inside = inside
		self.outside = outside

	def __str__(self):
		return ""

class Trunk__ipv6__ndisc__router_adver__mtu(AxapiObject):
	__metaclass__ = StructMeta 
	adver_mtu=PosRangedInteger(1200, 1500)
	adver_mtu_disable=PosRangedInteger(0, 1)
	def __init__(self, adver_mtu=None, adver_mtu_disable=None):
		self.adver_mtu = adver_mtu
		self.adver_mtu_disable = adver_mtu_disable

	def __str__(self):
		return ""

class Trunk__ipv6__ndisc__router_adver__vrid(AxapiObject):
	__metaclass__ = StructMeta 
	adver_vrid=PosRangedInteger(1, 31)
	adver_vrid_default=PosRangedInteger(0, 1)
	use_floating_ip=PosRangedInteger(0, 1)
	floating_ip=SizedString(1, 255)
	def __init__(self, adver_vrid=None, adver_vrid_default=None, use_floating_ip=None, floating_ip=None):
		self.adver_vrid = adver_vrid
		self.adver_vrid_default = adver_vrid_default
		self.use_floating_ip = use_floating_ip
		self.floating_ip = floating_ip

	def __str__(self):
		return ""

class Trunk__ipv6__ndisc__router_adver__ha_group_id(AxapiObject):
	__metaclass__ = StructMeta 
	adver_ha_group_id=PosRangedInteger(1, 31)
	ha_use_floating_ip=PosRangedInteger(0, 1)
	ha_floating_ip=SizedString(1, 255)
	def __init__(self, adver_ha_group_id=None, ha_use_floating_ip=None, ha_floating_ip=None):
		self.adver_ha_group_id = adver_ha_group_id
		self.ha_use_floating_ip = ha_use_floating_ip
		self.ha_floating_ip = ha_floating_ip

	def __str__(self):
		return ""

class Trunk__ipv6__ndisc__router_adver(AxapiObject):
	__metaclass__ = StructMeta 
	adver_enable=PosRangedInteger(0, 1)
	adver_disable=PosRangedInteger(0, 1)
	default_lifetime=PosRangedInteger(0, 9000)
	hop_limit=PosRangedInteger(1, 255)
	max_interval=PosRangedInteger(4, 1800)
	min_interval=PosRangedInteger(3, 1350)
	rate_limit=PosRangedInteger(1, 100000)
	reachable_time=PosRangedInteger(0, 3600000)
	retransmit_timer=PosRangedInteger(0, 4294967295)
	def __init__(self, adver_enable=None, adver_disable=None, default_lifetime=None, hop_limit=None, max_interval=None, min_interval=None, rate_limit=None, reachable_time=None, retransmit_timer=None, mtu=None, prefix_cfg=None, vrid=None, ha_group_id=None):
		self.adver_enable = adver_enable
		self.adver_disable = adver_disable
		self.default_lifetime = default_lifetime
		self.hop_limit = hop_limit
		self.max_interval = max_interval
		self.min_interval = min_interval
		self.rate_limit = rate_limit
		self.reachable_time = reachable_time
		self.retransmit_timer = retransmit_timer
		self.mtu = mtu
		self.prefix_cfg = prefix_cfg
		self.vrid = vrid
		self.ha_group_id = ha_group_id

	def __str__(self):
		return ""

class Trunk__ipv6__ndisc(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, router_adver=None):
		self.router_adver = router_adver

	def __str__(self):
		return ""

class Trunk__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_enable=PosRangedInteger(0, 1)
	def __init__(self, address_cfg=None, ipv6_enable=None, nat=None, ndisc=None):
		self.address_cfg = address_cfg
		self.ipv6_enable = ipv6_enable
		self.nat = nat
		self.ndisc = ndisc

	def __str__(self):
		return ""

class Trunk__ddos(AxapiObject):
	__metaclass__ = StructMeta 
	outside=PosRangedInteger(0, 1)
	inside=PosRangedInteger(0, 1)
	def __init__(self, outside=None, inside=None):
		self.outside = outside
		self.inside = inside

	def __str__(self):
		return ""

class Trunk(AxapiObject):
	__metaclass__ = StructMeta 
	ifnum=PosInteger()
	name=SizedString(1, 32)
	l3_vlan_fwd_disable=PosRangedInteger(0, 1)
	mtu=PosRangedInteger(1200, 12000)
	action = Enum(['enable', 'disable'])
	def __init__(self, ifnum, name=None, l3_vlan_fwd_disable=None, mtu=None, action=None, icmp_cfg=None, icmpv6_cfg=None, ip=None, ipv6=None, ddos=None):
		self.ifnum = ifnum
		self.name = name
		self.l3_vlan_fwd_disable = l3_vlan_fwd_disable
		self.mtu = mtu
		self.action = action
		self.icmp_cfg = icmp_cfg
		self.icmpv6_cfg = icmpv6_cfg
		self.ip = ip
		self.ipv6 = ipv6
		self.ddos = ddos

	def __str__(self):
		return str(self.ifnum)

class Interface_trunk_address_val_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	address_val = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, address_val=None, netmask=None):
		self.address_val = address_val
		self.netmask = netmask

	def __str__(self):
		return ""

class Interface_trunk_address_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	anycast=PosRangedInteger(0, 1)
	link_local=PosRangedInteger(0, 1)
	def __init__(self, ipv6_addr=None, anycast=None, link_local=None):
		self.ipv6_addr = ipv6_addr
		self.anycast = anycast
		self.link_local = link_local

	def __str__(self):
		return ""

class Trunk_ifnum(AxapiObject):
	__metaclass__ = StructMeta 
	ifnum=PosInteger()
	def __init__(self, ifnum):
		self.ifnum = ifnum

	def __str__(self):
		return str(self.ifnum)

class Interface_trunk_prefix_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	prefix=SizedString(1, 255)
	not_autonomous=PosRangedInteger(0, 1)
	not_on_link=PosRangedInteger(0, 1)
	preferred_lifetime=PosRangedInteger(0, 4294967295)
	valid_lifetime=PosRangedInteger(0, 4294967295)
	def __init__(self, prefix=None, not_autonomous=None, not_on_link=None, preferred_lifetime=None, valid_lifetime=None):
		self.prefix = prefix
		self.not_autonomous = not_autonomous
		self.not_on_link = not_on_link
		self.preferred_lifetime = preferred_lifetime
		self.valid_lifetime = valid_lifetime

	def __str__(self):
		return ""

class InterfaceTrunkClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getInterfaceTrunk(self, trunk_ifnum):
		"""
		Retrieve the trunk identified by the specified identifier
		
		Args:
			trunk_ifnum Trunk_ifnum
		
		Returns:
			An instance of the Trunk class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(trunk_ifnum) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified trunk does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('trunk')
		return deserialize_Trunk_json(payload)

	def putInterfaceTrunk(self, trunk_ifnum, trunk):
		"""
		Replace the object trunk
		
		Args:
			trunk_ifnum Trunk_ifnum
			trunk An instance of the Trunk class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['trunk']=serialize_Trunk_json(trunk)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(trunk_ifnum) .replace("/", "%2f") + query, payload, headers)
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

	def deleteInterfaceTrunk(self, trunk_ifnum):
		"""
		Remove the trunk identified by the specified identifier from the system
		
		Args:
			trunk_ifnum Trunk_ifnum
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(trunk_ifnum) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified trunk does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllInterfaceTrunksClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitInterfaceTrunk(self, trunk):
		"""
		Create the object trunk
		
		Args:
			trunk An instance of the Trunk class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['trunk']=serialize_Trunk_json(trunk)
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

	def getAllInterfaceTrunks(self):
		"""
		Retrieve all trunk objects currently pending in the system
		
		Returns:
			A list of Trunk objects
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
			payload= data.get('trunkList')
		return deserialize_list_Trunk_json(payload)

