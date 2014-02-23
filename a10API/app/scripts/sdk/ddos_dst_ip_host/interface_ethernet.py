import sys
from urlparse import urlparse
from collections import OrderedDict
import httplib
import json
import urllib

BASE_URL = [
  'https://axapi.a10networks.com/axapi/v3/interface/ethernet',
]

def deserialize_Ethernet_snmp_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  snmp_server = data.get('snmp-server')
  trap_source = data.get('trap-source')
  result = Ethernet_snmp_cfg(snmp_server=snmp_server, trap_source=trap_source)
  return result

def deserialize_Ethernet_icmp_cfg_json(obj):
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
  result = Ethernet_icmp_cfg(icmp_rate_limit=icmp_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
  return result

def deserialize_Ethernet_icmpv6_cfg_json(obj):
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
  result = Ethernet_icmpv6_cfg(icmpv6_rate_limit=icmpv6_rate_limit, normal_val=normal_val, lockup=lockup, lockup_period=lockup_period)
  return result

def deserialize_monitor_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  monitor = data.get('monitor')
  mirror_index = data.get('mirror-index')
  monitor_vlan = data.get('monitor-vlan')
  result = Monitor_cfg(monitor=monitor, mirror_index=mirror_index, monitor_vlan=monitor_vlan)
  return result

def deserialize_list_monitor_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_monitor_cfg_json(item))
  return list(container)

def deserialize_Ethernet_lldp_rt_enable_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  rx = data.get('rx')
  tx = data.get('tx')
  result = Ethernet_lldp_rt_enable(rx=rx, tx=tx)
  return result

def deserialize_Ethernet_lldp_notification_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  notif_enable = data.get('notif-enable')
  result = Ethernet_lldp_notification(notif_enable=notif_enable)
  return result

def deserialize_Ethernet_lldp_tx_dot1_tlvs_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  link_aggregation = data.get('link-aggregation')
  vlan = data.get('vlan')
  result = Ethernet_lldp_tx_dot1_tlvs(link_aggregation=link_aggregation, vlan=vlan)
  return result

def deserialize_Ethernet_lldp_tx_tlvs_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  management_address = data.get('management-address')
  port_description = data.get('port-description')
  system_capabilities = data.get('system-capabilities')
  system_description = data.get('system-description')
  system_name = data.get('system-name')
  result = Ethernet_lldp_tx_tlvs(management_address=management_address, port_description=port_description, system_capabilities=system_capabilities, system_description=system_description, system_name=system_name)
  return result

def deserialize_Ethernet_lldp_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  rt_enable = deserialize_Ethernet_lldp_rt_enable_json(data.get('rt-enable'))
  notification = deserialize_Ethernet_lldp_notification_json(data.get('notification'))
  tx_dot1_tlvs = deserialize_Ethernet_lldp_tx_dot1_tlvs_json(data.get('tx-dot1-tlvs'))
  tx_tlvs = deserialize_Ethernet_lldp_tx_tlvs_json(data.get('tx-tlvs'))
  result = Ethernet_lldp(rt_enable=rt_enable, notification=notification, tx_dot1_tlvs=tx_dot1_tlvs, tx_tlvs=tx_tlvs)
  return result

def deserialize_Ethernet_access_list_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  acl_id = data.get('acl-id')
  acl_name = data.get('acl-name')
  inbound = data.get('inbound')
  result = Ethernet_access_list(acl_id=acl_id, acl_name=acl_name, inbound=inbound)
  return result

def deserialize_Ethernet_lacp_trunk_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  trunk = data.get('trunk')
  mode = data.get('mode')
  admin_key = data.get('admin-key')
  unidirectional_detection = data.get('unidirectional-detection')
  result = Ethernet_lacp_trunk_cfg(trunk=trunk, mode=mode, admin_key=admin_key, unidirectional_detection=unidirectional_detection)
  return result

def deserialize_Ethernet_lacp_udld_timeout_cfg_fast_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  udld_fast_timeout = data.get('udld-fast-timeout')
  result = Ethernet_lacp_udld_timeout_cfg_fast(udld_fast_timeout=udld_fast_timeout)
  return result

def deserialize_Ethernet_lacp_udld_timeout_cfg_slow_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  udld_slow_timeout = data.get('udld-slow-timeout')
  result = Ethernet_lacp_udld_timeout_cfg_slow(udld_slow_timeout=udld_slow_timeout)
  return result

def deserialize_Ethernet_lacp_udld_timeout_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  udld_timeout = data.get('udld-timeout')
  fast = deserialize_Ethernet_lacp_udld_timeout_cfg_fast_json(data.get('fast'))
  slow = deserialize_Ethernet_lacp_udld_timeout_cfg_slow_json(data.get('slow'))
  result = Ethernet_lacp_udld_timeout_cfg(udld_timeout=udld_timeout, fast=fast, slow=slow)
  return result

def deserialize_Ethernet_lacp_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  trunk_cfg = deserialize_Ethernet_lacp_trunk_cfg_json(data.get('trunk-cfg'))
  port_priority = data.get('port-priority')
  timeout = data.get('timeout')
  udld_timeout_cfg = deserialize_Ethernet_lacp_udld_timeout_cfg_json(data.get('udld-timeout-cfg'))
  result = Ethernet_lacp(trunk_cfg=trunk_cfg, port_priority=port_priority, timeout=timeout, udld_timeout_cfg=udld_timeout_cfg)
  return result

def deserialize_Ethernet_ddos_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  outside = data.get('outside')
  inside = data.get('inside')
  result = Ethernet_ddos(outside=outside, inside=inside)
  return result

def deserialize_ip_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  ipv4_address = data.get('ipv4-address')
  ipv4_netmask = data.get('ipv4-netmask')
  result = Ip_cfg(ipv4_address=ipv4_address, ipv4_netmask=ipv4_netmask)
  return result

def deserialize_list_ip_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_ip_cfg_json(item))
  return list(container)

def deserialize_Ethernet_ip_address_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  ip_cfg = deserialize_list_ip_cfg_json(data.get('ip-cfg'))
  dhcp = data.get('dhcp')
  result = Ethernet_ip_address(ip_cfg=ip_cfg, dhcp=dhcp)
  return result

def deserialize_Ethernet_ip_nat_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  inside = data.get('inside')
  outside = data.get('outside')
  result = Ethernet_ip_nat(inside=inside, outside=outside)
  return result

def deserialize_Ethernet_ip_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  address = deserialize_Ethernet_ip_address_json(data.get('address'))
  allow_promiscuous_vip = data.get('allow-promiscuous-vip')
  cache_spoofing_port = data.get('cache-spoofing-port')
  helper_address = data.get('helper-address')
  nat = deserialize_Ethernet_ip_nat_json(data.get('nat'))
  slb_partition_redirect = data.get('slb-partition-redirect')
  igmp = data.get('igmp')
  generate_membership_query = data.get('generate-membership-query')
  generate_membership_query_val = data.get('generate-membership-query-val')
  max_resp_time = data.get('max-resp-time')
  result = Ethernet_ip(address=address, allow_promiscuous_vip=allow_promiscuous_vip, cache_spoofing_port=cache_spoofing_port, helper_address=helper_address, nat=nat, slb_partition_redirect=slb_partition_redirect, igmp=igmp, generate_membership_query=generate_membership_query, generate_membership_query_val=generate_membership_query_val, max_resp_time=max_resp_time)
  return result

def deserialize_address_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  ipv6_addr = data.get('ipv6-addr')
  anycast = data.get('anycast')
  link_local = data.get('link-local')
  result = Address_cfg(ipv6_addr=ipv6_addr, anycast=anycast, link_local=link_local)
  return result

def deserialize_list_address_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_address_cfg_json(item))
  return list(container)

def deserialize_Ethernet_ipv6_access_list_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  v6_acl_name = data.get('v6-acl-name')
  inbound = data.get('inbound')
  result = Ethernet_ipv6_access_list_cfg(v6_acl_name=v6_acl_name, inbound=inbound)
  return result

def deserialize_Ethernet_ipv6_ndisc_router_adver_mtu_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  adver_mtu = data.get('adver-mtu')
  adver_mtu_disable = data.get('adver-mtu-disable')
  result = Ethernet_ipv6_ndisc_router_adver_mtu(adver_mtu=adver_mtu, adver_mtu_disable=adver_mtu_disable)
  return result

def deserialize_prefix_cfg_json(obj):
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
  result = Prefix_cfg(prefix=prefix, not_autonomous=not_autonomous, not_on_link=not_on_link, preferred_lifetime=preferred_lifetime, valid_lifetime=valid_lifetime)
  return result

def deserialize_list_prefix_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_prefix_cfg_json(item))
  return list(container)

def deserialize_Ethernet_ipv6_ndisc_router_adver_vrid_json(obj):
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
  result = Ethernet_ipv6_ndisc_router_adver_vrid(adver_vrid=adver_vrid, adver_vrid_default=adver_vrid_default, use_floating_ip=use_floating_ip, floating_ip=floating_ip)
  return result

def deserialize_Ethernet_ipv6_ndisc_router_adver_ha_group_id_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  adver_ha_group_id = data.get('adver-ha-group-id')
  ha_use_floating_ip = data.get('ha-use-floating-ip')
  ha_floating_ip = data.get('ha-floating-ip')
  result = Ethernet_ipv6_ndisc_router_adver_ha_group_id(adver_ha_group_id=adver_ha_group_id, ha_use_floating_ip=ha_use_floating_ip, ha_floating_ip=ha_floating_ip)
  return result

def deserialize_Ethernet_ipv6_ndisc_router_adver_json(obj):
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
  mtu = deserialize_Ethernet_ipv6_ndisc_router_adver_mtu_json(data.get('mtu'))
  prefix_cfg = deserialize_list_prefix_cfg_json(data.get('prefix-cfg'))
  vrid = deserialize_Ethernet_ipv6_ndisc_router_adver_vrid_json(data.get('vrid'))
  ha_group_id = deserialize_Ethernet_ipv6_ndisc_router_adver_ha_group_id_json(data.get('ha-group-id'))
  result = Ethernet_ipv6_ndisc_router_adver(adver_enable=adver_enable, adver_disable=adver_disable, default_lifetime=default_lifetime, hop_limit=hop_limit, max_interval=max_interval, min_interval=min_interval, rate_limit=rate_limit, reachable_time=reachable_time, retransmit_timer=retransmit_timer, mtu=mtu, prefix_cfg=prefix_cfg, vrid=vrid, ha_group_id=ha_group_id)
  return result

def deserialize_Ethernet_ipv6_ndisc_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  router_adver = deserialize_Ethernet_ipv6_ndisc_router_adver_json(data.get('router-adver'))
  result = Ethernet_ipv6_ndisc(router_adver=router_adver)
  return result

def deserialize_Ethernet_ipv6_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  address_cfg = deserialize_list_address_cfg_json(data.get('address-cfg'))
  ipv6_enable = data.get('ipv6-enable')
  access_list_cfg = deserialize_Ethernet_ipv6_access_list_cfg_json(data.get('access-list-cfg'))
  ndisc = deserialize_Ethernet_ipv6_ndisc_json(data.get('ndisc'))
  result = Ethernet_ipv6(address_cfg=address_cfg, ipv6_enable=ipv6_enable, access_list_cfg=access_list_cfg, ndisc=ndisc)
  return result

def deserialize_Ethernet_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  ifnum = data.get('ifnum')
  name = data.get('name')
  l3_vlan_fwd_disable = data.get('l3-vlan-fwd-disable')
  load_interval = data.get('load-interval')
  mtu = data.get('mtu')
  snmp_cfg = deserialize_Ethernet_snmp_cfg_json(data.get('snmp-cfg'))
  duplexity = data.get('duplexity')
  speed = data.get('speed')
  flow_control = data.get('flow-control')
  enable = data.get('enable')
  disable = data.get('disable')
  icmp_cfg = deserialize_Ethernet_icmp_cfg_json(data.get('icmp-cfg'))
  icmpv6_cfg = deserialize_Ethernet_icmpv6_cfg_json(data.get('icmpv6-cfg'))
  monitor_cfg = deserialize_list_monitor_cfg_json(data.get('monitor-cfg'))
  cpu_process = data.get('cpu-process')
  lldp = deserialize_Ethernet_lldp_json(data.get('lldp'))
  access_list = deserialize_Ethernet_access_list_json(data.get('access-list'))
  lacp = deserialize_Ethernet_lacp_json(data.get('lacp'))
  ddos = deserialize_Ethernet_ddos_json(data.get('ddos'))
  ip = deserialize_Ethernet_ip_json(data.get('ip'))
  ipv6 = deserialize_Ethernet_ipv6_json(data.get('ipv6'))
  result = Ethernet(ifnum=ifnum, name=name, l3_vlan_fwd_disable=l3_vlan_fwd_disable, load_interval=load_interval, mtu=mtu, snmp_cfg=snmp_cfg, duplexity=duplexity, speed=speed, flow_control=flow_control, enable=enable, disable=disable, icmp_cfg=icmp_cfg, icmpv6_cfg=icmpv6_cfg, monitor_cfg=monitor_cfg, cpu_process=cpu_process, lldp=lldp, access_list=access_list, lacp=lacp, ddos=ddos, ip=ip, ipv6=ipv6)
  return result

def deserialize_string_json(obj):
  if obj is None:
    return None
  if isinstance(obj, str):
    return json.loads(obj)
  return obj

def serialize_Ethernet_snmp_cfg_json(obj):
  output = OrderedDict()
  if obj.snmp_server:
    output['snmp-server'] = obj.snmp_server
  if obj.trap_source:
    output['trap-source'] = obj.trap_source
  return output

def serialize_Ethernet_icmp_cfg_json(obj):
  output = OrderedDict()
  if obj.icmp_rate_limit:
    output['icmp-rate-limit'] = obj.icmp_rate_limit
  if obj.normal_val:
    output['normal-val'] = obj.normal_val
  if obj.lockup:
    output['lockup'] = obj.lockup
  if obj.lockup_period:
    output['lockup-period'] = obj.lockup_period
  return output

def serialize_Ethernet_icmpv6_cfg_json(obj):
  output = OrderedDict()
  if obj.icmpv6_rate_limit:
    output['icmpv6-rate-limit'] = obj.icmpv6_rate_limit
  if obj.normal_val:
    output['normal-val'] = obj.normal_val
  if obj.lockup:
    output['lockup'] = obj.lockup
  if obj.lockup_period:
    output['lockup-period'] = obj.lockup_period
  return output

def serialize_monitor_cfg_json(obj):
  output = OrderedDict()
  if obj.monitor:
    output['monitor'] = obj.monitor
  if obj.mirror_index:
    output['mirror-index'] = obj.mirror_index
  if obj.monitor_vlan:
    output['monitor-vlan'] = obj.monitor_vlan
  return output

def serialize_final_json(obj):
  return json.dumps(obj)

def serialize_list_monitor_cfg_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_monitor_cfg_json(item))
  return output

def serialize_Ethernet_lldp_rt_enable_json(obj):
  output = OrderedDict()
  if obj.rx:
    output['rx'] = obj.rx
  if obj.tx:
    output['tx'] = obj.tx
  return output

def serialize_Ethernet_lldp_notification_json(obj):
  output = OrderedDict()
  if obj.notif_enable:
    output['notif-enable'] = obj.notif_enable
  return output

def serialize_Ethernet_lldp_tx_dot1_tlvs_json(obj):
  output = OrderedDict()
  if obj.link_aggregation:
    output['link-aggregation'] = obj.link_aggregation
  if obj.vlan:
    output['vlan'] = obj.vlan
  return output

def serialize_Ethernet_lldp_tx_tlvs_json(obj):
  output = OrderedDict()
  if obj.management_address:
    output['management-address'] = obj.management_address
  if obj.port_description:
    output['port-description'] = obj.port_description
  if obj.system_capabilities:
    output['system-capabilities'] = obj.system_capabilities
  if obj.system_description:
    output['system-description'] = obj.system_description
  if obj.system_name:
    output['system-name'] = obj.system_name
  return output

def serialize_Ethernet_lldp_json(obj):
  output = OrderedDict()
  if obj.rt_enable:
    output['rt-enable'] = serialize_Ethernet_lldp_rt_enable_json(obj.rt_enable)
  if obj.notification:
    output['notification'] = serialize_Ethernet_lldp_notification_json(obj.notification)
  if obj.tx_dot1_tlvs:
    output['tx-dot1-tlvs'] = serialize_Ethernet_lldp_tx_dot1_tlvs_json(obj.tx_dot1_tlvs)
  if obj.tx_tlvs:
    output['tx-tlvs'] = serialize_Ethernet_lldp_tx_tlvs_json(obj.tx_tlvs)
  return output

def serialize_Ethernet_access_list_json(obj):
  output = OrderedDict()
  if obj.acl_id:
    output['acl-id'] = obj.acl_id
  if obj.acl_name:
    output['acl-name'] = obj.acl_name
  if obj.inbound:
    output['inbound'] = obj.inbound
  return output

def serialize_Ethernet_lacp_trunk_cfg_json(obj):
  output = OrderedDict()
  if obj.trunk:
    output['trunk'] = obj.trunk
  if obj.mode:
    output['mode'] = obj.mode
  if obj.admin_key:
    output['admin-key'] = obj.admin_key
  if obj.unidirectional_detection:
    output['unidirectional-detection'] = obj.unidirectional_detection
  return output

def serialize_Ethernet_lacp_udld_timeout_cfg_fast_json(obj):
  output = OrderedDict()
  if obj.udld_fast_timeout:
    output['udld-fast-timeout'] = obj.udld_fast_timeout
  return output

def serialize_Ethernet_lacp_udld_timeout_cfg_slow_json(obj):
  output = OrderedDict()
  if obj.udld_slow_timeout:
    output['udld-slow-timeout'] = obj.udld_slow_timeout
  return output

def serialize_Ethernet_lacp_udld_timeout_cfg_json(obj):
  output = OrderedDict()
  if obj.udld_timeout:
    output['udld-timeout'] = obj.udld_timeout
  if obj.fast:
    output['fast'] = serialize_Ethernet_lacp_udld_timeout_cfg_fast_json(obj.fast)
  if obj.slow:
    output['slow'] = serialize_Ethernet_lacp_udld_timeout_cfg_slow_json(obj.slow)
  return output

def serialize_Ethernet_lacp_json(obj):
  output = OrderedDict()
  output['trunk-cfg'] = serialize_Ethernet_lacp_trunk_cfg_json(obj.trunk_cfg)
  if obj.port_priority:
    output['port-priority'] = obj.port_priority
  if obj.timeout:
    output['timeout'] = obj.timeout
  if obj.udld_timeout_cfg:
    output['udld-timeout-cfg'] = serialize_Ethernet_lacp_udld_timeout_cfg_json(obj.udld_timeout_cfg)
  return output

def serialize_Ethernet_ddos_json(obj):
  output = OrderedDict()
  output['outside'] = obj.outside
  if obj.inside:
    output['inside'] = obj.inside
  return output

def serialize_ip_cfg_json(obj):
  output = OrderedDict()
  if obj.ipv4_address:
    output['ipv4-address'] = obj.ipv4_address
  if obj.ipv4_netmask:
    output['ipv4-netmask'] = obj.ipv4_netmask
  return output

def serialize_list_ip_cfg_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_ip_cfg_json(item))
  return output

def serialize_Ethernet_ip_address_json(obj):
  output = OrderedDict()
  if obj.ip_cfg:
    output['ip-cfg'] = serialize_list_ip_cfg_json(obj.ip_cfg)
  if obj.dhcp:
    output['dhcp'] = obj.dhcp
  return output

def serialize_Ethernet_ip_nat_json(obj):
  output = OrderedDict()
  if obj.inside:
    output['inside'] = obj.inside
  if obj.outside:
    output['outside'] = obj.outside
  return output

def serialize_Ethernet_ip_json(obj):
  output = OrderedDict()
  output['address'] = serialize_Ethernet_ip_address_json(obj.address)
  if obj.allow_promiscuous_vip:
    output['allow-promiscuous-vip'] = obj.allow_promiscuous_vip
  if obj.cache_spoofing_port:
    output['cache-spoofing-port'] = obj.cache_spoofing_port
  if obj.helper_address:
    output['helper-address'] = obj.helper_address
  if obj.nat:
    output['nat'] = serialize_Ethernet_ip_nat_json(obj.nat)
  if obj.slb_partition_redirect:
    output['slb-partition-redirect'] = obj.slb_partition_redirect
  if obj.igmp:
    output['igmp'] = obj.igmp
  if obj.generate_membership_query:
    output['generate-membership-query'] = obj.generate_membership_query
  if obj.generate_membership_query_val:
    output['generate-membership-query-val'] = obj.generate_membership_query_val
  if obj.max_resp_time:
    output['max-resp-time'] = obj.max_resp_time
  return output

def serialize_address_cfg_json(obj):
  output = OrderedDict()
  if obj.ipv6_addr:
    output['ipv6-addr'] = obj.ipv6_addr
  if obj.anycast:
    output['anycast'] = obj.anycast
  if obj.link_local:
    output['link-local'] = obj.link_local
  return output

def serialize_list_address_cfg_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_address_cfg_json(item))
  return output

def serialize_Ethernet_ipv6_access_list_cfg_json(obj):
  output = OrderedDict()
  if obj.v6_acl_name:
    output['v6-acl-name'] = obj.v6_acl_name
  if obj.inbound:
    output['inbound'] = obj.inbound
  return output

def serialize_Ethernet_ipv6_ndisc_router_adver_mtu_json(obj):
  output = OrderedDict()
  if obj.adver_mtu:
    output['adver-mtu'] = obj.adver_mtu
  if obj.adver_mtu_disable:
    output['adver-mtu-disable'] = obj.adver_mtu_disable
  return output

def serialize_prefix_cfg_json(obj):
  output = OrderedDict()
  if obj.prefix:
    output['prefix'] = obj.prefix
  if obj.not_autonomous:
    output['not-autonomous'] = obj.not_autonomous
  if obj.not_on_link:
    output['not-on-link'] = obj.not_on_link
  if obj.preferred_lifetime:
    output['preferred-lifetime'] = obj.preferred_lifetime
  if obj.valid_lifetime:
    output['valid-lifetime'] = obj.valid_lifetime
  return output

def serialize_list_prefix_cfg_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_prefix_cfg_json(item))
  return output

def serialize_Ethernet_ipv6_ndisc_router_adver_vrid_json(obj):
  output = OrderedDict()
  if obj.adver_vrid:
    output['adver-vrid'] = obj.adver_vrid
  if obj.adver_vrid_default:
    output['adver-vrid-default'] = obj.adver_vrid_default
  if obj.use_floating_ip:
    output['use-floating-ip'] = obj.use_floating_ip
  if obj.floating_ip:
    output['floating-ip'] = obj.floating_ip
  return output

def serialize_Ethernet_ipv6_ndisc_router_adver_ha_group_id_json(obj):
  output = OrderedDict()
  if obj.adver_ha_group_id:
    output['adver-ha-group-id'] = obj.adver_ha_group_id
  if obj.ha_use_floating_ip:
    output['ha-use-floating-ip'] = obj.ha_use_floating_ip
  if obj.ha_floating_ip:
    output['ha-floating-ip'] = obj.ha_floating_ip
  return output

def serialize_Ethernet_ipv6_ndisc_router_adver_json(obj):
  output = OrderedDict()
  if obj.adver_enable:
    output['adver-enable'] = obj.adver_enable
  if obj.adver_disable:
    output['adver-disable'] = obj.adver_disable
  if obj.default_lifetime:
    output['default-lifetime'] = obj.default_lifetime
  if obj.hop_limit:
    output['hop-limit'] = obj.hop_limit
  if obj.max_interval:
    output['max-interval'] = obj.max_interval
  if obj.min_interval:
    output['min-interval'] = obj.min_interval
  if obj.rate_limit:
    output['rate-limit'] = obj.rate_limit
  if obj.reachable_time:
    output['reachable-time'] = obj.reachable_time
  if obj.retransmit_timer:
    output['retransmit-timer'] = obj.retransmit_timer
  if obj.mtu:
    output['mtu'] = serialize_Ethernet_ipv6_ndisc_router_adver_mtu_json(obj.mtu)
  if obj.prefix_cfg:
    output['prefix-cfg'] = serialize_list_prefix_cfg_json(obj.prefix_cfg)
  if obj.vrid:
    output['vrid'] = serialize_Ethernet_ipv6_ndisc_router_adver_vrid_json(obj.vrid)
  if obj.ha_group_id:
    output['ha-group-id'] = serialize_Ethernet_ipv6_ndisc_router_adver_ha_group_id_json(obj.ha_group_id)
  return output

def serialize_Ethernet_ipv6_ndisc_json(obj):
  output = OrderedDict()
  if obj.router_adver:
    output['router-adver'] = serialize_Ethernet_ipv6_ndisc_router_adver_json(obj.router_adver)
  return output

def serialize_Ethernet_ipv6_json(obj):
  output = OrderedDict()
  output['address-cfg'] = serialize_list_address_cfg_json(obj.address_cfg)
  if obj.ipv6_enable:
    output['ipv6-enable'] = obj.ipv6_enable
  if obj.access_list_cfg:
    output['access-list-cfg'] = serialize_Ethernet_ipv6_access_list_cfg_json(obj.access_list_cfg)
  if obj.ndisc:
    output['ndisc'] = serialize_Ethernet_ipv6_ndisc_json(obj.ndisc)
  return output

def serialize_Ethernet_json(obj):
  output = OrderedDict()
  output['ifnum'] = obj.ifnum
  if obj.name:
    output['name'] = obj.name
  if obj.l3_vlan_fwd_disable:
    output['l3-vlan-fwd-disable'] = obj.l3_vlan_fwd_disable
  if obj.load_interval:
    output['load-interval'] = obj.load_interval
  if obj.mtu:
    output['mtu'] = obj.mtu
  if obj.snmp_cfg:
    output['snmp-cfg'] = serialize_Ethernet_snmp_cfg_json(obj.snmp_cfg)
  if obj.duplexity:
    output['duplexity'] = obj.duplexity
  if obj.speed:
    output['speed'] = obj.speed
  if obj.flow_control:
    output['flow-control'] = obj.flow_control
  if obj.enable:
    output['enable'] = obj.enable
  if obj.disable:
    output['disable'] = obj.disable
  if obj.icmp_cfg:
    output['icmp-cfg'] = serialize_Ethernet_icmp_cfg_json(obj.icmp_cfg)
  if obj.icmpv6_cfg:
    output['icmpv6-cfg'] = serialize_Ethernet_icmpv6_cfg_json(obj.icmpv6_cfg)
  if obj.monitor_cfg:
    output['monitor-cfg'] = serialize_list_monitor_cfg_json(obj.monitor_cfg)
  if obj.cpu_process:
    output['cpu-process'] = obj.cpu_process
  if obj.lldp:
    output['lldp'] = serialize_Ethernet_lldp_json(obj.lldp)
  if obj.access_list:
    output['access-list'] = serialize_Ethernet_access_list_json(obj.access_list)
  if obj.lacp:
    output['lacp'] = serialize_Ethernet_lacp_json(obj.lacp)
  if obj.ddos:
    output['ddos'] = serialize_Ethernet_ddos_json(obj.ddos)
  if obj.ip:
    output['ip'] = serialize_Ethernet_ip_json(obj.ip)
  if obj.ipv6:
    output['ipv6'] = serialize_Ethernet_ipv6_json(obj.ipv6)
  return output

def deserialize_list_Ethernet_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_Ethernet_json(item))
  return list(container)

class RemoteException(Exception):
  def __init__(self, status, cause, details):
    Exception.__init__(self, cause)
    self.status = status
    self.details = details

class AbstractResourceClient:
  def __init__(self, endpoint, sessionid, debug):
    if endpoint is not None:
      self.endpoint = endpoint
    else:
      self.endpoint = BASE_URL[0]
    self.sessionid = sessionid
    self.debug = debug

  def get_connection(self):
    result = urlparse(self.endpoint)
    ssl = result.scheme == 'https'
    if ssl:
      conn = httplib.HTTPSConnection(result.netloc)
    else:
      conn = httplib.HTTPConnection(result.netloc)
    if self.debug:
      conn.set_debuglevel(1)
    return conn

  def get_path(self):
    result = urlparse(BASE_URL[0])
    return result.path

  def get_output(self, response, expected, errors):
    status = response.status
    payload = response.read()
    if not errors and errors.has_key(status):
      raise RemoteException(status, errors[status], payload)
    elif status != expected:
      raise RemoteException(status, 'Unexpected return status: ' + str(status), payload)
    return payload

class Monitor_cfg:
  def __init__(self, monitor=None, mirror_index=None, monitor_vlan=None):
    self.monitor = monitor
    self.mirror_index = mirror_index
    self.monitor_vlan = monitor_vlan

class Ip_cfg:
  def __init__(self, ipv4_address=None, ipv4_netmask=None):
    self.ipv4_address = ipv4_address
    self.ipv4_netmask = ipv4_netmask

class Address_cfg:
  def __init__(self, ipv6_addr=None, anycast=None, link_local=None):
    self.ipv6_addr = ipv6_addr
    self.anycast = anycast
    self.link_local = link_local

class Prefix_cfg:
  def __init__(self, prefix=None, not_autonomous=None, not_on_link=None, preferred_lifetime=None, valid_lifetime=None):
    self.prefix = prefix
    self.not_autonomous = not_autonomous
    self.not_on_link = not_on_link
    self.preferred_lifetime = preferred_lifetime
    self.valid_lifetime = valid_lifetime

class Ethernet_ifnum:
  def __init__(self, ifnum):
    self.ifnum = ifnum

  def __str__(self):
    return str(self.ifnum)

class Ethernet_snmp_cfg:
  def __init__(self, snmp_server=None, trap_source=None):
    self.snmp_server = snmp_server
    self.trap_source = trap_source

class Ethernet_icmp_cfg:
  def __init__(self, icmp_rate_limit=None, normal_val=None, lockup=None, lockup_period=None):
    self.icmp_rate_limit = icmp_rate_limit
    self.normal_val = normal_val
    self.lockup = lockup
    self.lockup_period = lockup_period

class Ethernet_icmpv6_cfg:
  def __init__(self, icmpv6_rate_limit=None, normal_val=None, lockup=None, lockup_period=None):
    self.icmpv6_rate_limit = icmpv6_rate_limit
    self.normal_val = normal_val
    self.lockup = lockup
    self.lockup_period = lockup_period

class Ethernet_lldp_rt_enable:
  def __init__(self, rx=None, tx=None):
    self.rx = rx
    self.tx = tx

class Ethernet_lldp_notification:
  def __init__(self, notif_enable=None):
    self.notif_enable = notif_enable

class Ethernet_lldp_tx_dot1_tlvs:
  def __init__(self, link_aggregation=None, vlan=None):
    self.link_aggregation = link_aggregation
    self.vlan = vlan

class Ethernet_lldp_tx_tlvs:
  def __init__(self, management_address=None, port_description=None, system_capabilities=None, system_description=None, system_name=None):
    self.management_address = management_address
    self.port_description = port_description
    self.system_capabilities = system_capabilities
    self.system_description = system_description
    self.system_name = system_name

class Ethernet_lldp:
  def __init__(self, rt_enable=None, notification=None, tx_dot1_tlvs=None, tx_tlvs=None):
    self.rt_enable = rt_enable
    self.notification = notification
    self.tx_dot1_tlvs = tx_dot1_tlvs
    self.tx_tlvs = tx_tlvs

class Ethernet_access_list:
  def __init__(self, acl_id=None, acl_name=None, inbound=None):
    self.acl_id = acl_id
    self.acl_name = acl_name
    self.inbound = inbound

class Ethernet_lacp_trunk_cfg:
  def __init__(self, trunk=None, mode=None, admin_key=None, unidirectional_detection=None):
    self.trunk = trunk
    self.mode = mode
    self.admin_key = admin_key
    self.unidirectional_detection = unidirectional_detection

class Ethernet_lacp_udld_timeout_cfg_fast:
  def __init__(self, udld_fast_timeout=None):
    self.udld_fast_timeout = udld_fast_timeout

class Ethernet_lacp_udld_timeout_cfg_slow:
  def __init__(self, udld_slow_timeout=None):
    self.udld_slow_timeout = udld_slow_timeout

class Ethernet_lacp_udld_timeout_cfg:
  def __init__(self, udld_timeout=None, fast=None, slow=None):
    self.udld_timeout = udld_timeout
    self.fast = fast
    self.slow = slow

class Ethernet_lacp:
  def __init__(self, trunk_cfg, port_priority=None, timeout=None, udld_timeout_cfg=None):
    self.trunk_cfg = trunk_cfg
    self.port_priority = port_priority
    self.timeout = timeout
    self.udld_timeout_cfg = udld_timeout_cfg

class Ethernet_ddos:
  def __init__(self, outside, inside=None):
    self.outside = outside
    self.inside = inside

class Ethernet_ip_address:
  def __init__(self, ip_cfg=None, dhcp=None):
    self.ip_cfg = ip_cfg
    self.dhcp = dhcp

class Ethernet_ip_nat:
  def __init__(self, inside=None, outside=None):
    self.inside = inside
    self.outside = outside

class Ethernet_ip:
  def __init__(self, address, allow_promiscuous_vip=None, cache_spoofing_port=None, helper_address=None, nat=None, slb_partition_redirect=None, igmp=None, generate_membership_query=None, generate_membership_query_val=None, max_resp_time=None):
    self.address = address
    self.allow_promiscuous_vip = allow_promiscuous_vip
    self.cache_spoofing_port = cache_spoofing_port
    self.helper_address = helper_address
    self.nat = nat
    self.slb_partition_redirect = slb_partition_redirect
    self.igmp = igmp
    self.generate_membership_query = generate_membership_query
    self.generate_membership_query_val = generate_membership_query_val
    self.max_resp_time = max_resp_time

class Ethernet_ipv6_access_list_cfg:
  def __init__(self, v6_acl_name=None, inbound=None):
    self.v6_acl_name = v6_acl_name
    self.inbound = inbound

class Ethernet_ipv6_ndisc_router_adver_mtu:
  def __init__(self, adver_mtu=None, adver_mtu_disable=None):
    self.adver_mtu = adver_mtu
    self.adver_mtu_disable = adver_mtu_disable

class Ethernet_ipv6_ndisc_router_adver_vrid:
  def __init__(self, adver_vrid=None, adver_vrid_default=None, use_floating_ip=None, floating_ip=None):
    self.adver_vrid = adver_vrid
    self.adver_vrid_default = adver_vrid_default
    self.use_floating_ip = use_floating_ip
    self.floating_ip = floating_ip

class Ethernet_ipv6_ndisc_router_adver_ha_group_id:
  def __init__(self, adver_ha_group_id=None, ha_use_floating_ip=None, ha_floating_ip=None):
    self.adver_ha_group_id = adver_ha_group_id
    self.ha_use_floating_ip = ha_use_floating_ip
    self.ha_floating_ip = ha_floating_ip

class Ethernet_ipv6_ndisc_router_adver:
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

class Ethernet_ipv6_ndisc:
  def __init__(self, router_adver=None):
    self.router_adver = router_adver

class Ethernet_ipv6:
  def __init__(self, address_cfg, ipv6_enable=None, access_list_cfg=None, ndisc=None):
    self.address_cfg = address_cfg
    self.ipv6_enable = ipv6_enable
    self.access_list_cfg = access_list_cfg
    self.ndisc = ndisc

class Ethernet:
  def __init__(self, ifnum, name=None, l3_vlan_fwd_disable=None, load_interval=None, mtu=None, snmp_cfg=None, duplexity=None, speed=None, flow_control=None, enable=None, disable=None, icmp_cfg=None, icmpv6_cfg=None, monitor_cfg=None, cpu_process=None, lldp=None, access_list=None, lacp=None, ddos=None, ip=None, ipv6=None):
    self.ifnum = ifnum
    self.name = name
    self.l3_vlan_fwd_disable = l3_vlan_fwd_disable
    self.load_interval = load_interval
    self.mtu = mtu
    self.snmp_cfg = snmp_cfg
    self.duplexity = duplexity
    self.speed = speed
    self.flow_control = flow_control
    self.enable = enable
    self.disable = disable
    self.icmp_cfg = icmp_cfg
    self.icmpv6_cfg = icmpv6_cfg
    self.monitor_cfg = monitor_cfg
    self.cpu_process = cpu_process
    self.lldp = lldp
    self.access_list = access_list
    self.lacp = lacp
    self.ddos = ddos
    self.ip = ip
    self.ipv6 = ipv6

class InterfaceEthernetClient(AbstractResourceClient):
  def __init__(self, endpoint=None, sessionid=None, debug=False):
    AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

  def getInterfaceEthernet(self, ethernet_ifnum):
    """
    Retrieve the ethernet identified by the specified identifier
    
    Args:
      ethernet_ifnum Ethernet_ifnum
    
    Returns:
      An instance of the Ethernet class
    """
    query = ''
    conn = self.get_connection()
    headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
    conn.request('GET', self.get_path() + '/' + str(ethernet_ifnum)  + query, headers=headers)
    response = conn.getresponse()
    expected_status = 200
    errors = {500: 'An unexpected runtime exception', 404: 'Specified ethernet does not exist'}
    payload = self.get_output(response, expected_status, errors)
    conn.close()
    if self.debug:
      print 'payload:', payload
    data = json.loads(payload)
    payload= data.get('ethernet')
    return deserialize_Ethernet_json(payload)

  def deleteInterfaceEthernet(self, ethernet_ifnum):
    """
    Remove the ethernet identified by the specified identifier from the system
    
    Args:
      ethernet_ifnum Ethernet_ifnum
    
    Returns:
      An instance of the string class
    """
    query = ''
    conn = self.get_connection()
    headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
    conn.request('DELETE', self.get_path() + '/' + str(ethernet_ifnum)  + query, headers=headers)
    response = conn.getresponse()
    expected_status = 200
    errors = {500: 'An unexpected runtime exception', 404: 'Specified ethernet does not exist'}
    payload = self.get_output(response, expected_status, errors)
    conn.close()
    if self.debug:
      print 'payload:', payload
    return deserialize_string_json(payload)

class AllInterfaceEthernetsClient(AbstractResourceClient):
  def __init__(self, endpoint=None, sessionid=None, debug=False):
    AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

  def submitInterfaceEthernet(self, ethernet):
    """
    Create the object ethernet
    
    Args:
      ethernet An instance of the Ethernet class
    
    Returns:
      An instance of the string class
    """
    query = ''
    conn = self.get_connection()
    headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
    output=OrderedDict()
    output['ethernet']=serialize_Ethernet_json(ethernet)
    payload = serialize_final_json(output)
    conn.request('POST', self.get_path() + '/' + query, payload, headers)
    response = conn.getresponse()
    expected_status = 200
    errors = {500: 'An unexpected runtime exception'}
    payload = self.get_output(response, expected_status, errors)
    conn.close()
    if self.debug:
      print 'payload:', payload
    return deserialize_string_json(payload)

  def getAllInterfaceEthernets(self):
    """
    Retrieve all ethernet objects currently pending in the system
    
    Returns:
      A list of Ethernet objects
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
    data = json.loads(payload)
    payload= data.get('ethernetList')
    return deserialize_list_Ethernet_json(payload)


