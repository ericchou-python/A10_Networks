########################################################################################################################
# File name: vrrp_a.py
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
	'https://axapi.a10networks.com/axapi/v3/vrrp-a',
]

def deserialize_Vrrp_a__inline_mode_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	inline_mode = data.get('inline-mode')
	preferred_port = data.get('preferred-port')
	result = Vrrp_a__inline_mode_cfg(inline_mode=inline_mode, preferred_port=preferred_port)
	return result

def deserialize_Vrrp_a__ospf_inline_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	vlan = data.get('vlan')
	result = Vrrp_a__ospf_inline_cfg(vlan=vlan)
	return result

def deserialize_Vrrp_a__l2_inline_peer_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	l2_inline_peer_ip = data.get('l2-inline-peer-ip')
	ip_address = data.get('ip-address')
	result = Vrrp_a__l2_inline_peer_ip_cfg(l2_inline_peer_ip=l2_inline_peer_ip, ip_address=ip_address)
	return result

def deserialize_Vrrp_a__force_self_standby_cfg__vrid__value_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value = data.get('value')
	persistent = data.get('persistent')
	result = Vrrp_a__force_self_standby_cfg__vrid__value_cfg(value=value, persistent=persistent)
	return result

def deserialize_Vrrp_a__force_self_standby_cfg__vrid_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	value_cfg = deserialize_Vrrp_a__force_self_standby_cfg__vrid__value_cfg_json(data.get('value-cfg'))
	result = Vrrp_a__force_self_standby_cfg__vrid(value_cfg=value_cfg)
	return result

def deserialize_Vrrp_a__force_self_standby_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	force_self_standby = data.get('force-self-standby')
	persistent = data.get('persistent')
	vrid = deserialize_Vrrp_a__force_self_standby_cfg__vrid_json(data.get('vrid'))
	result = Vrrp_a__force_self_standby_cfg(force_self_standby=force_self_standby, persistent=persistent, vrid=vrid)
	return result

def deserialize_Vrrp_a_ip_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_address = data.get('ip-address')
	result = Vrrp_a_ip_address_cfg(ip_address=ip_address)
	return result

def deserialize_list_Vrrp_a_ip_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrrp_a_ip_address_cfg_json(item))
	return list(container)

def deserialize_Vrrp_a_ipv6_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_address = data.get('ipv6-address')
	result = Vrrp_a_ipv6_address_cfg(ipv6_address=ipv6_address)
	return result

def deserialize_list_Vrrp_a_ipv6_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrrp_a_ipv6_address_cfg_json(item))
	return list(container)

def deserialize_Vrrp_a_vrid__floating_ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_address_cfg = deserialize_list_Vrrp_a_ip_address_cfg_json(data.get('ip-address-cfg'))
	ipv6_address_cfg = deserialize_list_Vrrp_a_ipv6_address_cfg_json(data.get('ipv6-address-cfg'))
	result = Vrrp_a_vrid__floating_ip(ip_address_cfg=ip_address_cfg, ipv6_address_cfg=ipv6_address_cfg)
	return result

def deserialize_Vrrp_a_vrid__preempt_mode_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	threshhold = data.get('threshhold')
	disable = data.get('disable')
	result = Vrrp_a_vrid__preempt_mode(threshhold=threshhold, disable=disable)
	return result

def deserialize_Vrrp_a_interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet = data.get('ethernet')
	priority_cost = data.get('priority-cost')
	result = Vrrp_a_interface(ethernet=ethernet, priority_cost=priority_cost)
	return result

def deserialize_list_Vrrp_a_interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrrp_a_interface_json(item))
	return list(container)

def deserialize_Vrrp_a_vrid__tracking_options__trunk_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trunk = data.get('trunk')
	priority_cost = data.get('priority-cost')
	per_port_pri = data.get('per-port-pri')
	result = Vrrp_a_vrid__tracking_options__trunk_cfg(trunk=trunk, priority_cost=priority_cost, per_port_pri=per_port_pri)
	return result

def deserialize_Vrrp_a_vrid__tracking_options_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	interface = deserialize_list_Vrrp_a_interface_json(data.get('interface'))
	trunk_cfg = deserialize_Vrrp_a_vrid__tracking_options__trunk_cfg_json(data.get('trunk-cfg'))
	vlan = data.get('vlan')
	timeout = data.get('timeout')
	priority_cost = data.get('priority-cost')
	result = Vrrp_a_vrid__tracking_options(interface=interface, trunk_cfg=trunk_cfg, vlan=vlan, timeout=timeout, priority_cost=priority_cost)
	return result

def deserialize_Vrrp_a_vrid_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	vrid_val = data.get('vrid-val')
	floating_ip = deserialize_Vrrp_a_vrid__floating_ip_json(data.get('floating-ip'))
	preempt_mode = deserialize_Vrrp_a_vrid__preempt_mode_json(data.get('preempt-mode'))
	priority = data.get('priority')
	tracking_options = deserialize_Vrrp_a_vrid__tracking_options_json(data.get('tracking-options'))
	result = Vrrp_a_vrid(vrid_val=vrid_val, floating_ip=floating_ip, preempt_mode=preempt_mode, priority=priority, tracking_options=tracking_options)
	return result

def deserialize_list_Vrrp_a_vrid_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrrp_a_vrid_json(item))
	return list(container)

def deserialize_Vrrp_a_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	flap_ethernet_start = data.get('flap-ethernet-start')
	flap_ethernet_end = data.get('flap-ethernet-end')
	result = Vrrp_a_eth_cfg(flap_ethernet_start=flap_ethernet_start, flap_ethernet_end=flap_ethernet_end)
	return result

def deserialize_list_Vrrp_a_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrrp_a_eth_cfg_json(item))
	return list(container)

def deserialize_Vrrp_a__restart_port_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	eth_cfg = deserialize_list_Vrrp_a_eth_cfg_json(data.get('eth-cfg'))
	result = Vrrp_a__restart_port_list(eth_cfg=eth_cfg)
	return result

def deserialize_Vrrp_a_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	device_id = data.get('device-id')
	set_id = data.get('set-id')
	enable = data.get('enable')
	hello_interval = data.get('hello-interval')
	preemption_delay = data.get('preemption-delay')
	dead_timer = data.get('dead-timer')
	arp_retry = data.get('arp-retry')
	track_event_delay = data.get('track-event-delay')
	inline_mode_cfg = deserialize_Vrrp_a__inline_mode_cfg_json(data.get('inline-mode-cfg'))
	ospf_inline_cfg = deserialize_Vrrp_a__ospf_inline_cfg_json(data.get('ospf-inline-cfg'))
	restart_time = data.get('restart-time')
	l2_inline_peer_ip_cfg = deserialize_Vrrp_a__l2_inline_peer_ip_cfg_json(data.get('l2-inline-peer-ip-cfg'))
	force_self_standby_cfg = deserialize_Vrrp_a__force_self_standby_cfg_json(data.get('force-self-standby-cfg'))
	vridlist = deserialize_list_Vrrp_a_vrid_json(data.get('vridList'))
	interfacelist = deserialize_list_Vrrp_a_interface_json(data.get('interfaceList'))
	restart_port_list = deserialize_Vrrp_a__restart_port_list_json(data.get('restart-port-list'))
	result = Vrrp_a(device_id=device_id, set_id=set_id, enable=enable, hello_interval=hello_interval, preemption_delay=preemption_delay, dead_timer=dead_timer, arp_retry=arp_retry, track_event_delay=track_event_delay, inline_mode_cfg=inline_mode_cfg, ospf_inline_cfg=ospf_inline_cfg, restart_time=restart_time, l2_inline_peer_ip_cfg=l2_inline_peer_ip_cfg, force_self_standby_cfg=force_self_standby_cfg, vridlist=vridlist, interfacelist=interfacelist, restart_port_list=restart_port_list)
	return result

def serialize_Vrrp_a__inline_mode_cfg_json(obj):
	output = OrderedDict()
	if obj.inline_mode is not None:
		output['inline-mode'] = obj.inline_mode
	if obj.preferred_port is not None:
		output['preferred-port'] = obj.preferred_port
	return output

def serialize_Vrrp_a__ospf_inline_cfg_json(obj):
	output = OrderedDict()
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	return output

def serialize_Vrrp_a__l2_inline_peer_ip_cfg_json(obj):
	output = OrderedDict()
	if obj.l2_inline_peer_ip is not None:
		output['l2-inline-peer-ip'] = obj.l2_inline_peer_ip
	if obj.ip_address is not None:
		output['ip-address'] = obj.ip_address
	return output

def serialize_Vrrp_a__force_self_standby_cfg__vrid__value_cfg_json(obj):
	output = OrderedDict()
	if obj.value is not None:
		output['value'] = obj.value
	if obj.persistent is not None:
		output['persistent'] = obj.persistent
	return output

def serialize_Vrrp_a__force_self_standby_cfg__vrid_json(obj):
	output = OrderedDict()
	if obj.value_cfg is not None:
		output['value-cfg'] = serialize_Vrrp_a__force_self_standby_cfg__vrid__value_cfg_json(obj.value_cfg)
	return output

def serialize_Vrrp_a__force_self_standby_cfg_json(obj):
	output = OrderedDict()
	if obj.force_self_standby is not None:
		output['force-self-standby'] = obj.force_self_standby
	if obj.persistent is not None:
		output['persistent'] = obj.persistent
	if obj.vrid is not None:
		output['vrid'] = serialize_Vrrp_a__force_self_standby_cfg__vrid_json(obj.vrid)
	return output

def serialize_Vrrp_a_ip_address_cfg_json(obj):
	output = OrderedDict()
	if obj.ip_address is not None:
		output['ip-address'] = obj.ip_address
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Vrrp_a_ip_address_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vrrp_a_ip_address_cfg_json(item))
	return output

def serialize_Vrrp_a_ipv6_address_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv6_address is not None:
		output['ipv6-address'] = obj.ipv6_address
	return output

def serialize_list_Vrrp_a_ipv6_address_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vrrp_a_ipv6_address_cfg_json(item))
	return output

def serialize_Vrrp_a_vrid__floating_ip_json(obj):
	output = OrderedDict()
	if obj.ip_address_cfg is not None:
		output['ip-address-cfg'] = serialize_list_Vrrp_a_ip_address_cfg_json(obj.ip_address_cfg)
	if obj.ipv6_address_cfg is not None:
		output['ipv6-address-cfg'] = serialize_list_Vrrp_a_ipv6_address_cfg_json(obj.ipv6_address_cfg)
	return output

def serialize_Vrrp_a_vrid__preempt_mode_json(obj):
	output = OrderedDict()
	if obj.threshhold is not None:
		output['threshhold'] = obj.threshhold
	if obj.disable is not None:
		output['disable'] = obj.disable
	return output

def serialize_Vrrp_a_interface_json(obj):
	output = OrderedDict()
	if obj.ethernet is not None:
		output['ethernet'] = obj.ethernet
	if obj.priority_cost is not None:
		output['priority-cost'] = obj.priority_cost
	return output

def serialize_list_Vrrp_a_interface_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vrrp_a_interface_json(item))
	return output

def serialize_Vrrp_a_vrid__tracking_options__trunk_cfg_json(obj):
	output = OrderedDict()
	if obj.trunk is not None:
		output['trunk'] = obj.trunk
	if obj.priority_cost is not None:
		output['priority-cost'] = obj.priority_cost
	if obj.per_port_pri is not None:
		output['per-port-pri'] = obj.per_port_pri
	return output

def serialize_Vrrp_a_vrid__tracking_options_json(obj):
	output = OrderedDict()
	if obj.interface is not None:
		output['interface'] = serialize_list_Vrrp_a_interface_json(obj.interface)
	if obj.trunk_cfg is not None:
		output['trunk-cfg'] = serialize_Vrrp_a_vrid__tracking_options__trunk_cfg_json(obj.trunk_cfg)
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	if obj.timeout is not None:
		output['timeout'] = obj.timeout
	if obj.priority_cost is not None:
		output['priority-cost'] = obj.priority_cost
	return output

def serialize_Vrrp_a_vrid_json(obj):
	output = OrderedDict()
	output['vrid-val'] = obj.vrid_val
	if obj.floating_ip is not None:
		output['floating-ip'] = serialize_Vrrp_a_vrid__floating_ip_json(obj.floating_ip)
	if obj.preempt_mode is not None:
		output['preempt-mode'] = serialize_Vrrp_a_vrid__preempt_mode_json(obj.preempt_mode)
	if obj.priority is not None:
		output['priority'] = obj.priority
	if obj.tracking_options is not None:
		output['tracking-options'] = serialize_Vrrp_a_vrid__tracking_options_json(obj.tracking_options)
	return output

def serialize_list_Vrrp_a_vrid_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vrrp_a_vrid_json(item))
	return output

def serialize_Vrrp_a_eth_cfg_json(obj):
	output = OrderedDict()
	if obj.flap_ethernet_start is not None:
		output['flap-ethernet-start'] = obj.flap_ethernet_start
	if obj.flap_ethernet_end is not None:
		output['flap-ethernet-end'] = obj.flap_ethernet_end
	return output

def serialize_list_Vrrp_a_eth_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vrrp_a_eth_cfg_json(item))
	return output

def serialize_Vrrp_a__restart_port_list_json(obj):
	output = OrderedDict()
	if obj.eth_cfg is not None:
		output['eth-cfg'] = serialize_list_Vrrp_a_eth_cfg_json(obj.eth_cfg)
	return output

def serialize_Vrrp_a_json(obj):
	output = OrderedDict()
	if obj.device_id is not None:
		output['device-id'] = obj.device_id
	if obj.set_id is not None:
		output['set-id'] = obj.set_id
	if obj.enable is not None:
		output['enable'] = obj.enable
	if obj.hello_interval is not None:
		output['hello-interval'] = obj.hello_interval
	if obj.preemption_delay is not None:
		output['preemption-delay'] = obj.preemption_delay
	if obj.dead_timer is not None:
		output['dead-timer'] = obj.dead_timer
	if obj.arp_retry is not None:
		output['arp-retry'] = obj.arp_retry
	if obj.track_event_delay is not None:
		output['track-event-delay'] = obj.track_event_delay
	if obj.inline_mode_cfg is not None:
		output['inline-mode-cfg'] = serialize_Vrrp_a__inline_mode_cfg_json(obj.inline_mode_cfg)
	if obj.ospf_inline_cfg is not None:
		output['ospf-inline-cfg'] = serialize_Vrrp_a__ospf_inline_cfg_json(obj.ospf_inline_cfg)
	if obj.restart_time is not None:
		output['restart-time'] = obj.restart_time
	if obj.l2_inline_peer_ip_cfg is not None:
		output['l2-inline-peer-ip-cfg'] = serialize_Vrrp_a__l2_inline_peer_ip_cfg_json(obj.l2_inline_peer_ip_cfg)
	if obj.force_self_standby_cfg is not None:
		output['force-self-standby-cfg'] = serialize_Vrrp_a__force_self_standby_cfg_json(obj.force_self_standby_cfg)
	if obj.vridlist is not None:
		output['vridList'] = serialize_list_Vrrp_a_vrid_json(obj.vridlist)
	if obj.interfacelist is not None:
		output['interfaceList'] = serialize_list_Vrrp_a_interface_json(obj.interfacelist)
	if obj.restart_port_list is not None:
		output['restart-port-list'] = serialize_Vrrp_a__restart_port_list_json(obj.restart_port_list)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Vrrp_a_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrrp_a_json(item))
	return list(container)

class Vrrp_a__inline_mode_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	inline_mode=PosRangedInteger(0, 1)
	preferred_port=PosRangedInteger(1, 2048)
	def __init__(self, inline_mode=None, preferred_port=None):
		self.inline_mode = inline_mode
		self.preferred_port = preferred_port

	def __str__(self):
		return ""

class Vrrp_a__ospf_inline_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	vlan=PosRangedInteger(1, 4094)
	def __init__(self, vlan=None):
		self.vlan = vlan

	def __str__(self):
		return ""

class Vrrp_a__l2_inline_peer_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	l2_inline_peer_ip=PosRangedInteger(0, 1)
	ip_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, l2_inline_peer_ip=None, ip_address=None):
		self.l2_inline_peer_ip = l2_inline_peer_ip
		self.ip_address = ip_address

	def __str__(self):
		return ""

class Vrrp_a__force_self_standby_cfg__vrid__value_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	value=PosRangedInteger(1, 1)
	persistent=PosInteger()
	def __init__(self, value=None, persistent=None):
		self.value = value
		self.persistent = persistent

	def __str__(self):
		return ""

class Vrrp_a__force_self_standby_cfg__vrid(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, value_cfg=None):
		self.value_cfg = value_cfg

	def __str__(self):
		return ""

class Vrrp_a__force_self_standby_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	force_self_standby=PosRangedInteger(0, 1)
	persistent=PosRangedInteger(0, 1)
	def __init__(self, force_self_standby=None, persistent=None, vrid=None):
		self.force_self_standby = force_self_standby
		self.persistent = persistent
		self.vrid = vrid

	def __str__(self):
		return ""

class Vrrp_a__restart_port_list(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, eth_cfg=None):
		self.eth_cfg = eth_cfg

	def __str__(self):
		return ""

class Vrrp_a(AxapiObject):
	__metaclass__ = StructMeta 
	device_id=PosRangedInteger(1, 8)
	set_id=PosRangedInteger(1, 15)
	enable=PosRangedInteger(0, 1)
	hello_interval=PosRangedInteger(1, 255)
	preemption_delay=PosRangedInteger(1, 255)
	dead_timer=PosRangedInteger(2, 255)
	arp_retry=PosRangedInteger(1, 255)
	track_event_delay=PosRangedInteger(1, 100)
	restart_time=PosRangedInteger(1, 100)
	def __init__(self, device_id=None, set_id=None, enable=None, hello_interval=None, preemption_delay=None, dead_timer=None, arp_retry=None, track_event_delay=None, inline_mode_cfg=None, ospf_inline_cfg=None, restart_time=None, l2_inline_peer_ip_cfg=None, force_self_standby_cfg=None, vridlist=None, interfacelist=None, restart_port_list=None):
		self.device_id = device_id
		self.set_id = set_id
		self.enable = enable
		self.hello_interval = hello_interval
		self.preemption_delay = preemption_delay
		self.dead_timer = dead_timer
		self.arp_retry = arp_retry
		self.track_event_delay = track_event_delay
		self.inline_mode_cfg = inline_mode_cfg
		self.ospf_inline_cfg = ospf_inline_cfg
		self.restart_time = restart_time
		self.l2_inline_peer_ip_cfg = l2_inline_peer_ip_cfg
		self.force_self_standby_cfg = force_self_standby_cfg
		self.vridlist = vridlist
		self.interfacelist = interfacelist
		self.restart_port_list = restart_port_list

	def __str__(self):
		return ""

class Vrrp_a_vrid__floating_ip(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ip_address_cfg=None, ipv6_address_cfg=None):
		self.ip_address_cfg = ip_address_cfg
		self.ipv6_address_cfg = ipv6_address_cfg

	def __str__(self):
		return ""

class Vrrp_a_vrid__preempt_mode(AxapiObject):
	__metaclass__ = StructMeta 
	threshhold=PosRangedInteger(1, 255)
	disable=PosRangedInteger(0, 1)
	def __init__(self, threshhold=None, disable=None):
		self.threshhold = threshhold
		self.disable = disable

	def __str__(self):
		return ""

class Vrrp_a_vrid__tracking_options__trunk_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	trunk=PosRangedInteger(1, 16)
	priority_cost=PosRangedInteger(1, 255)
	per_port_pri=PosRangedInteger(1, 255)
	def __init__(self, trunk=None, priority_cost=None, per_port_pri=None):
		self.trunk = trunk
		self.priority_cost = priority_cost
		self.per_port_pri = per_port_pri

	def __str__(self):
		return ""

class Vrrp_a_vrid__tracking_options(AxapiObject):
	__metaclass__ = StructMeta 
	vlan=PosRangedInteger(2, 4094)
	timeout=PosRangedInteger(2, 600)
	priority_cost=PosRangedInteger(1, 255)
	def __init__(self, interface=None, trunk_cfg=None, vlan=None, timeout=None, priority_cost=None):
		self.interface = interface
		self.trunk_cfg = trunk_cfg
		self.vlan = vlan
		self.timeout = timeout
		self.priority_cost = priority_cost

	def __str__(self):
		return ""

class Vrrp_a_vrid(AxapiObject):
	__metaclass__ = StructMeta 
	vrid_val=PosRangedInteger(1, 1)
	priority=PosRangedInteger(1, 255)
	def __init__(self, vrid_val, floating_ip=None, preempt_mode=None, priority=None, tracking_options=None):
		self.vrid_val = vrid_val
		self.floating_ip = floating_ip
		self.preempt_mode = preempt_mode
		self.priority = priority
		self.tracking_options = tracking_options

	def __str__(self):
		return str(self.vrid_val)

class Vrrp_a_ip_address_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip_address = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ip_address=None):
		self.ip_address = ip_address

	def __str__(self):
		return ""

class Vrrp_a_ipv6_address_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_address=SizedString(1, 255)
	def __init__(self, ipv6_address=None):
		self.ipv6_address = ipv6_address

	def __str__(self):
		return ""

class Vrrp_a_interface(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet=PosRangedInteger(1, 2048)
	priority_cost=PosRangedInteger(1, 255)
	def __init__(self, ethernet=None, priority_cost=None):
		self.ethernet = ethernet
		self.priority_cost = priority_cost

	def __str__(self):
		return ""

class Vrrp_a_eth_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	flap_ethernet_start=PosRangedInteger(1, 2048)
	flap_ethernet_end=PosRangedInteger(1, 2048)
	def __init__(self, flap_ethernet_start=None, flap_ethernet_end=None):
		self.flap_ethernet_start = flap_ethernet_start
		self.flap_ethernet_end = flap_ethernet_end

	def __str__(self):
		return ""

class VrrpaClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getVrrpa(self):
		"""
		Retrieve the vrrp_a identified by the specified identifier
		
		Returns:
			An instance of the Vrrp_a class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified vrrp_a does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('vrrp-a')
		return deserialize_Vrrp_a_json(payload)

	def putVrrpa(self, vrrp_a):
		"""
		Replace the object vrrp_a
		
		Args:
			vrrp_a An instance of the Vrrp_a class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['vrrp-a']=serialize_Vrrp_a_json(vrrp_a)
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

	def deleteVrrpa(self):
		"""
		Remove the vrrp_a identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified vrrp_a does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllVrrpasClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitVrrpa(self, vrrp_a):
		"""
		Create the object vrrp_a
		
		Args:
			vrrp_a An instance of the Vrrp_a class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['vrrp-a']=serialize_Vrrp_a_json(vrrp_a)
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

	def getAllVrrpas(self):
		"""
		Retrieve all vrrp_a objects currently pending in the system
		
		Returns:
			A list of Vrrp_a objects
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
			payload= data.get('vrrp-aList')
		return deserialize_list_Vrrp_a_json(payload)

