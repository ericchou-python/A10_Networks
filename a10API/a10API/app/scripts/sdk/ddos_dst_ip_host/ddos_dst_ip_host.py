import sys
from urlparse import urlparse
from collections import OrderedDict
import httplib
import json
import urllib

BASE_URL = [
  'https://axapi.a10networks.com/axapi/v3/ddos/dst-ip/host',
]

def deserialize_Host_sflow_polling_sflow_tcp_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  sflow_tcp_basic = data.get('sflow-tcp-basic')
  sflow_tcp_stateful = data.get('sflow-tcp-stateful')
  result = Host_sflow_polling_sflow_tcp(sflow_tcp_basic=sflow_tcp_basic, sflow_tcp_stateful=sflow_tcp_stateful)
  return result

def deserialize_Host_sflow_polling_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  sflow_packets = data.get('sflow-packets')
  sflow_layer_4 = data.get('sflow-layer-4')
  sflow_tcp = deserialize_Host_sflow_polling_sflow_tcp_json(data.get('sflow-tcp'))
  sflow_http = data.get('sflow-http')
  result = Host_sflow_polling(sflow_packets=sflow_packets, sflow_layer_4=sflow_layer_4, sflow_tcp=sflow_tcp, sflow_http=sflow_http)
  return result

def deserialize_Host_sflow_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  polling = deserialize_Host_sflow_polling_json(data.get('polling'))
  result = Host_sflow(polling=polling)
  return result

def deserialize_Ddos_dst_ip_host_l4_type_exceed_action_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  exceed_drop = data.get('exceed-drop')
  exceed_black_list = data.get('exceed-black-list')
  result = Ddos_dst_ip_host_l4_type_exceed_action(exceed_drop=exceed_drop, exceed_black_list=exceed_black_list)
  return result

def deserialize_Ddos_dst_ip_host_l4_type_class_list_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  check_all_class_list = data.get('check-all-class-list')
  result = Ddos_dst_ip_host_l4_type_class_list(check_all_class_list=check_all_class_list)
  return result

def deserialize_key_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  key = data.get('key')
  result = Key_cfg(key=key)
  return result

def deserialize_list_key_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_key_cfg_json(item))
  return list(container)

def deserialize_Ddos_dst_ip_host_l4_type_tunnel_decap_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  ip_decap = data.get('ip-decap')
  gre_decap = data.get('gre-decap')
  key_cfg = deserialize_list_key_cfg_json(data.get('key-cfg'))
  result = Ddos_dst_ip_host_l4_type_tunnel_decap(ip_decap=ip_decap, gre_decap=gre_decap, key_cfg=key_cfg)
  return result

def deserialize_Ddos_dst_ip_host_l4_type_tunnel_rate_limit_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  ip_rate_limit = data.get('ip-rate-limit')
  gre_rate_limit = data.get('gre-rate-limit')
  result = Ddos_dst_ip_host_l4_type_tunnel_rate_limit(ip_rate_limit=ip_rate_limit, gre_rate_limit=gre_rate_limit)
  return result

def deserialize_Ddos_dst_ip_host_l4_type_scanning_detection_action_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  threshold_drop = data.get('threshold-drop')
  threshold_black_list = data.get('threshold-black-list')
  result = Ddos_dst_ip_host_l4_type_scanning_detection_action(threshold_drop=threshold_drop, threshold_black_list=threshold_black_list)
  return result

def deserialize_Ddos_dst_ip_host_l4_type_scanning_detection_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  threshold = data.get('threshold')
  action = deserialize_Ddos_dst_ip_host_l4_type_scanning_detection_action_json(data.get('action'))
  result = Ddos_dst_ip_host_l4_type_scanning_detection(threshold=threshold, action=action)
  return result

def deserialize_Ddos_dst_ip_host_l4_type_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  protocol = data.get('protocol')
  glid = data.get('glid')
  deny = data.get('deny')
  dns_any_check = data.get('dns-any-check')
  max_rexmit_syn_per_flow = data.get('max-rexmit-syn-per-flow')
  exceed_action = deserialize_Ddos_dst_ip_host_l4_type_exceed_action_json(data.get('exceed-action'))
  disable_syn_auth = data.get('disable-syn-auth')
  syn_cookie = data.get('syn-cookie')
  tcp_reset_client = data.get('tcp-reset-client')
  tcp_reset_server = data.get('tcp-reset-server')
  drop_on_no_port_match = data.get('drop-on-no-port-match')
  over_conn_limit_action = data.get('over-conn-limit-action')
  over_conn_rate_action = data.get('over-conn-rate-action')
  class_list = deserialize_Ddos_dst_ip_host_l4_type_class_list_json(data.get('class-list'))
  state = data.get('state')
  tunnel_decap = deserialize_Ddos_dst_ip_host_l4_type_tunnel_decap_json(data.get('tunnel-decap'))
  tunnel_rate_limit = deserialize_Ddos_dst_ip_host_l4_type_tunnel_rate_limit_json(data.get('tunnel-rate-limit'))
  drop_frag_pkt = data.get('drop-frag-pkt')
  scanning_detection = deserialize_Ddos_dst_ip_host_l4_type_scanning_detection_json(data.get('scanning-detection'))
  result = Ddos_dst_ip_host_l4_type(protocol=protocol, glid=glid, deny=deny, dns_any_check=dns_any_check, max_rexmit_syn_per_flow=max_rexmit_syn_per_flow, exceed_action=exceed_action, disable_syn_auth=disable_syn_auth, syn_cookie=syn_cookie, tcp_reset_client=tcp_reset_client, tcp_reset_server=tcp_reset_server, drop_on_no_port_match=drop_on_no_port_match, over_conn_limit_action=over_conn_limit_action, over_conn_rate_action=over_conn_rate_action, class_list=class_list, state=state, tunnel_decap=tunnel_decap, tunnel_rate_limit=tunnel_rate_limit, drop_frag_pkt=drop_frag_pkt, scanning_detection=scanning_detection)
  return result

def deserialize_list_Ddos_dst_ip_host_l4_type_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_Ddos_dst_ip_host_l4_type_json(item))
  return list(container)

def deserialize_aflex_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  aflex = data.get('aflex')
  result = Aflex_cfg(aflex=aflex)
  return result

def deserialize_list_aflex_cfg_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_aflex_cfg_json(item))
  return list(container)

def deserialize_Ddos_dst_ip_host_port_template_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  dns = data.get('dns')
  http = data.get('http')
  ssl_l4 = data.get('ssl-l4')
  tcp = data.get('tcp')
  udp = data.get('udp')
  result = Ddos_dst_ip_host_port_template(dns=dns, http=http, ssl_l4=ssl_l4, tcp=tcp, udp=udp)
  return result

def deserialize_Ddos_dst_ip_host_port_sflow_polling_sflow_tcp_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  sflow_tcp_basic = data.get('sflow-tcp-basic')
  sflow_tcp_stateful = data.get('sflow-tcp-stateful')
  result = Ddos_dst_ip_host_port_sflow_polling_sflow_tcp(sflow_tcp_basic=sflow_tcp_basic, sflow_tcp_stateful=sflow_tcp_stateful)
  return result

def deserialize_Ddos_dst_ip_host_port_sflow_polling_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  sflow_packets = data.get('sflow-packets')
  sflow_tcp = deserialize_Ddos_dst_ip_host_port_sflow_polling_sflow_tcp_json(data.get('sflow-tcp'))
  sflow_http = data.get('sflow-http')
  result = Ddos_dst_ip_host_port_sflow_polling(sflow_packets=sflow_packets, sflow_tcp=sflow_tcp, sflow_http=sflow_http)
  return result

def deserialize_Ddos_dst_ip_host_port_sflow_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  polling = deserialize_Ddos_dst_ip_host_port_sflow_polling_json(data.get('polling'))
  result = Ddos_dst_ip_host_port_sflow(polling=polling)
  return result

def deserialize_Ddos_dst_ip_host_port_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  port_num = data.get('port-num')
  protocol = data.get('protocol')
  deny = data.get('deny')
  glid = data.get('glid')
  aflex_cfg = deserialize_list_aflex_cfg_json(data.get('aflex-cfg'))
  template = deserialize_Ddos_dst_ip_host_port_template_json(data.get('template'))
  sflow = deserialize_Ddos_dst_ip_host_port_sflow_json(data.get('sflow'))
  result = Ddos_dst_ip_host_port(port_num=port_num, protocol=protocol, deny=deny, glid=glid, aflex_cfg=aflex_cfg, template=template, sflow=sflow)
  return result

def deserialize_list_Ddos_dst_ip_host_port_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_Ddos_dst_ip_host_port_json(item))
  return list(container)

def deserialize_Ddos_dst_ip_host_ip_proto_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  port_num = data.get('port-num')
  deny = data.get('deny')
  glid = data.get('glid')
  result = Ddos_dst_ip_host_ip_proto(port_num=port_num, deny=deny, glid=glid)
  return result

def deserialize_list_Ddos_dst_ip_host_ip_proto_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_Ddos_dst_ip_host_ip_proto_json(item))
  return list(container)

def deserialize_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_template_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  tcp = data.get('tcp')
  udp = data.get('udp')
  result = Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_template(tcp=tcp, udp=udp)
  return result

def deserialize_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  protocol = data.get('protocol')
  glid = data.get('glid')
  template = deserialize_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_template_json(data.get('template'))
  result = Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst(protocol=protocol, glid=glid, template=template)
  return result

def deserialize_list_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_json(item))
  return list(container)

def deserialize_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_template_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  ssl_l4 = data.get('ssl-l4')
  dns = data.get('dns')
  http = data.get('http')
  result = Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_template(ssl_l4=ssl_l4, dns=dns, http=http)
  return result

def deserialize_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  protocol = data.get('protocol')
  template = deserialize_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_template_json(data.get('template'))
  result = Ddos_dst_ip_host_src_dst_pair_app_type_src_dst(protocol=protocol, template=template)
  return result

def deserialize_list_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_json(item))
  return list(container)

def deserialize_Ddos_dst_ip_host_src_dst_pair_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  src = data.get('src')
  l4_type_src_dstList = deserialize_list_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_json(data.get('l4-type-src-dstList'))
  app_type_src_dstList = deserialize_list_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_json(data.get('app-type-src-dstList'))
  result = Ddos_dst_ip_host_src_dst_pair(src=src, l4_type_src_dstList=l4_type_src_dstList, app_type_src_dstList=app_type_src_dstList)
  return result

def deserialize_list_Ddos_dst_ip_host_src_dst_pair_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_Ddos_dst_ip_host_src_dst_pair_json(item))
  return list(container)

def deserialize_Host_json(obj):
  if obj is None:
    return None
  if isinstance(obj, dict):
    data = obj
  else:
    data = json.loads(obj)
  ip_addr = data.get('ip-addr')
  exceed_log_enable = data.get('exceed-log-enable')
  enable_512_port = data.get('enable-512-port')
  sflow = deserialize_Host_sflow_json(data.get('sflow'))
  l4_typeList = deserialize_list_Ddos_dst_ip_host_l4_type_json(data.get('l4-typeList'))
  portList = deserialize_list_Ddos_dst_ip_host_port_json(data.get('portList'))
  ip_protoList = deserialize_list_Ddos_dst_ip_host_ip_proto_json(data.get('ip-protoList'))
  src_dst_pairList = deserialize_list_Ddos_dst_ip_host_src_dst_pair_json(data.get('src-dst-pairList'))
  result = Host(ip_addr=ip_addr, exceed_log_enable=exceed_log_enable, enable_512_port=enable_512_port, sflow=sflow, l4_typeList=l4_typeList, portList=portList, ip_protoList=ip_protoList, src_dst_pairList=src_dst_pairList)
  return result

def deserialize_string_json(obj):
  if obj is None:
    return None
  if isinstance(obj, str):
    return json.loads(obj)
  return obj

def serialize_Host_sflow_polling_sflow_tcp_json(obj):
  output = OrderedDict()
  if obj.sflow_tcp_basic:
    output['sflow-tcp-basic'] = obj.sflow_tcp_basic
  if obj.sflow_tcp_stateful:
    output['sflow-tcp-stateful'] = obj.sflow_tcp_stateful
  return output

def serialize_Host_sflow_polling_json(obj):
  output = OrderedDict()
  if obj.sflow_packets:
    output['sflow-packets'] = obj.sflow_packets
  if obj.sflow_layer_4:
    output['sflow-layer-4'] = obj.sflow_layer_4
  if obj.sflow_tcp:
    output['sflow-tcp'] = serialize_Host_sflow_polling_sflow_tcp_json(obj.sflow_tcp)
  if obj.sflow_http:
    output['sflow-http'] = obj.sflow_http
  return output

def serialize_Host_sflow_json(obj):
  output = OrderedDict()
  if obj.polling:
    output['polling'] = serialize_Host_sflow_polling_json(obj.polling)
  return output

def serialize_Ddos_dst_ip_host_l4_type_exceed_action_json(obj):
  output = OrderedDict()
  if obj.exceed_drop:
    output['exceed-drop'] = obj.exceed_drop
  if obj.exceed_black_list:
    output['exceed-black-list'] = obj.exceed_black_list
  return output

def serialize_Ddos_dst_ip_host_l4_type_class_list_json(obj):
  output = OrderedDict()
  if obj.check_all_class_list:
    output['check-all-class-list'] = obj.check_all_class_list
  return output

def serialize_key_cfg_json(obj):
  output = OrderedDict()
  if obj.key:
    output['key'] = obj.key
  return output

def serialize_final_json(obj):
  return json.dumps(obj)

def serialize_list_key_cfg_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_key_cfg_json(item))
  return output

def serialize_Ddos_dst_ip_host_l4_type_tunnel_decap_json(obj):
  output = OrderedDict()
  if obj.ip_decap:
    output['ip-decap'] = obj.ip_decap
  if obj.gre_decap:
    output['gre-decap'] = obj.gre_decap
  if obj.key_cfg:
    output['key-cfg'] = serialize_list_key_cfg_json(obj.key_cfg)
  return output

def serialize_Ddos_dst_ip_host_l4_type_tunnel_rate_limit_json(obj):
  output = OrderedDict()
  if obj.ip_rate_limit:
    output['ip-rate-limit'] = obj.ip_rate_limit
  if obj.gre_rate_limit:
    output['gre-rate-limit'] = obj.gre_rate_limit
  return output

def serialize_Ddos_dst_ip_host_l4_type_scanning_detection_action_json(obj):
  output = OrderedDict()
  if obj.threshold_drop:
    output['threshold-drop'] = obj.threshold_drop
  if obj.threshold_black_list:
    output['threshold-black-list'] = obj.threshold_black_list
  return output

def serialize_Ddos_dst_ip_host_l4_type_scanning_detection_json(obj):
  output = OrderedDict()
  if obj.threshold:
    output['threshold'] = obj.threshold
  if obj.action:
    output['action'] = serialize_Ddos_dst_ip_host_l4_type_scanning_detection_action_json(obj.action)
  return output

def serialize_Ddos_dst_ip_host_l4_type_json(obj):
  output = OrderedDict()
  output['protocol'] = obj.protocol
  if obj.glid:
    output['glid'] = obj.glid
  if obj.deny:
    output['deny'] = obj.deny
  if obj.dns_any_check:
    output['dns-any-check'] = obj.dns_any_check
  if obj.max_rexmit_syn_per_flow:
    output['max-rexmit-syn-per-flow'] = obj.max_rexmit_syn_per_flow
  if obj.exceed_action:
    output['exceed-action'] = serialize_Ddos_dst_ip_host_l4_type_exceed_action_json(obj.exceed_action)
  if obj.disable_syn_auth:
    output['disable-syn-auth'] = obj.disable_syn_auth
  if obj.syn_cookie:
    output['syn-cookie'] = obj.syn_cookie
  if obj.tcp_reset_client:
    output['tcp-reset-client'] = obj.tcp_reset_client
  if obj.tcp_reset_server:
    output['tcp-reset-server'] = obj.tcp_reset_server
  if obj.drop_on_no_port_match:
    output['drop-on-no-port-match'] = obj.drop_on_no_port_match
  if obj.over_conn_limit_action:
    output['over-conn-limit-action'] = obj.over_conn_limit_action
  if obj.over_conn_rate_action:
    output['over-conn-rate-action'] = obj.over_conn_rate_action
  if obj.class_list:
    output['class-list'] = serialize_Ddos_dst_ip_host_l4_type_class_list_json(obj.class_list)
  if obj.state:
    output['state'] = obj.state
  if obj.tunnel_decap:
    output['tunnel-decap'] = serialize_Ddos_dst_ip_host_l4_type_tunnel_decap_json(obj.tunnel_decap)
  if obj.tunnel_rate_limit:
    output['tunnel-rate-limit'] = serialize_Ddos_dst_ip_host_l4_type_tunnel_rate_limit_json(obj.tunnel_rate_limit)
  if obj.drop_frag_pkt:
    output['drop-frag-pkt'] = obj.drop_frag_pkt
  if obj.scanning_detection:
    output['scanning-detection'] = serialize_Ddos_dst_ip_host_l4_type_scanning_detection_json(obj.scanning_detection)
  return output

def serialize_list_Ddos_dst_ip_host_l4_type_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_Ddos_dst_ip_host_l4_type_json(item))
  return output

def serialize_aflex_cfg_json(obj):
  output = OrderedDict()
  if obj.aflex:
    output['aflex'] = obj.aflex
  return output

def serialize_list_aflex_cfg_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_aflex_cfg_json(item))
  return output

def serialize_Ddos_dst_ip_host_port_template_json(obj):
  output = OrderedDict()
  if obj.dns:
    output['dns'] = obj.dns
  if obj.http:
    output['http'] = obj.http
  if obj.ssl_l4:
    output['ssl-l4'] = obj.ssl_l4
  if obj.tcp:
    output['tcp'] = obj.tcp
  if obj.udp:
    output['udp'] = obj.udp
  return output

def serialize_Ddos_dst_ip_host_port_sflow_polling_sflow_tcp_json(obj):
  output = OrderedDict()
  if obj.sflow_tcp_basic:
    output['sflow-tcp-basic'] = obj.sflow_tcp_basic
  if obj.sflow_tcp_stateful:
    output['sflow-tcp-stateful'] = obj.sflow_tcp_stateful
  return output

def serialize_Ddos_dst_ip_host_port_sflow_polling_json(obj):
  output = OrderedDict()
  if obj.sflow_packets:
    output['sflow-packets'] = obj.sflow_packets
  if obj.sflow_tcp:
    output['sflow-tcp'] = serialize_Ddos_dst_ip_host_port_sflow_polling_sflow_tcp_json(obj.sflow_tcp)
  if obj.sflow_http:
    output['sflow-http'] = obj.sflow_http
  return output

def serialize_Ddos_dst_ip_host_port_sflow_json(obj):
  output = OrderedDict()
  if obj.polling:
    output['polling'] = serialize_Ddos_dst_ip_host_port_sflow_polling_json(obj.polling)
  return output

def serialize_Ddos_dst_ip_host_port_json(obj):
  output = OrderedDict()
  output['port-num'] = obj.port_num
  output['protocol'] = obj.protocol
  if obj.deny:
    output['deny'] = obj.deny
  if obj.glid:
    output['glid'] = obj.glid
  if obj.aflex_cfg:
    output['aflex-cfg'] = serialize_list_aflex_cfg_json(obj.aflex_cfg)
  if obj.template:
    output['template'] = serialize_Ddos_dst_ip_host_port_template_json(obj.template)
  if obj.sflow:
    output['sflow'] = serialize_Ddos_dst_ip_host_port_sflow_json(obj.sflow)
  return output

def serialize_list_Ddos_dst_ip_host_port_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_Ddos_dst_ip_host_port_json(item))
  return output

def serialize_Ddos_dst_ip_host_ip_proto_json(obj):
  output = OrderedDict()
  output['port-num'] = obj.port_num
  if obj.deny:
    output['deny'] = obj.deny
  if obj.glid:
    output['glid'] = obj.glid
  return output

def serialize_list_Ddos_dst_ip_host_ip_proto_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_Ddos_dst_ip_host_ip_proto_json(item))
  return output

def serialize_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_template_json(obj):
  output = OrderedDict()
  if obj.tcp:
    output['tcp'] = obj.tcp
  if obj.udp:
    output['udp'] = obj.udp
  return output

def serialize_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_json(obj):
  output = OrderedDict()
  output['protocol'] = obj.protocol
  if obj.glid:
    output['glid'] = obj.glid
  if obj.template:
    output['template'] = serialize_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_template_json(obj.template)
  return output

def serialize_list_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_json(item))
  return output

def serialize_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_template_json(obj):
  output = OrderedDict()
  if obj.ssl_l4:
    output['ssl-l4'] = obj.ssl_l4
  if obj.dns:
    output['dns'] = obj.dns
  if obj.http:
    output['http'] = obj.http
  return output

def serialize_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_json(obj):
  output = OrderedDict()
  output['protocol'] = obj.protocol
  if obj.template:
    output['template'] = serialize_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_template_json(obj.template)
  return output

def serialize_list_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_json(item))
  return output

def serialize_Ddos_dst_ip_host_src_dst_pair_json(obj):
  output = OrderedDict()
  output['src'] = obj.src
  if obj.l4_type_src_dstList:
    output['l4-type-src-dstList'] = serialize_list_Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_json(obj.l4_type_src_dstList)
  if obj.app_type_src_dstList:
    output['app-type-src-dstList'] = serialize_list_Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_json(obj.app_type_src_dstList)
  return output

def serialize_list_Ddos_dst_ip_host_src_dst_pair_json(obj):
  output = list()
  for item in obj:
    output.append(serialize_Ddos_dst_ip_host_src_dst_pair_json(item))
  return output

def serialize_Host_json(obj):
  output = OrderedDict()
  output['ip-addr'] = obj.ip_addr
  if obj.exceed_log_enable:
    output['exceed-log-enable'] = obj.exceed_log_enable
  if obj.enable_512_port:
    output['enable-512-port'] = obj.enable_512_port
  if obj.sflow:
    output['sflow'] = serialize_Host_sflow_json(obj.sflow)
  if obj.l4_typeList:
    output['l4-typeList'] = serialize_list_Ddos_dst_ip_host_l4_type_json(obj.l4_typeList)
  if obj.portList:
    output['portList'] = serialize_list_Ddos_dst_ip_host_port_json(obj.portList)
  if obj.ip_protoList:
    output['ip-protoList'] = serialize_list_Ddos_dst_ip_host_ip_proto_json(obj.ip_protoList)
  if obj.src_dst_pairList:
    output['src-dst-pairList'] = serialize_list_Ddos_dst_ip_host_src_dst_pair_json(obj.src_dst_pairList)
  return output

def deserialize_list_Host_json(obj):
  if obj is None:
    return None
  if isinstance(obj, list):
    data = obj
  else:
    data = json.loads(obj)
  container = []
  for item in data:
    container.append(deserialize_Host_json(item))
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

class Ddos_dst_ip_host_l4_type_exceed_action:
  def __init__(self, exceed_drop=None, exceed_black_list=None):
    self.exceed_drop = exceed_drop
    self.exceed_black_list = exceed_black_list

class Ddos_dst_ip_host_l4_type_class_list:
  def __init__(self, check_all_class_list=None):
    self.check_all_class_list = check_all_class_list

class Ddos_dst_ip_host_l4_type_tunnel_decap:
  def __init__(self, ip_decap=None, gre_decap=None, key_cfg=None):
    self.ip_decap = ip_decap
    self.gre_decap = gre_decap
    self.key_cfg = key_cfg

class Ddos_dst_ip_host_l4_type_tunnel_rate_limit:
  def __init__(self, ip_rate_limit=None, gre_rate_limit=None):
    self.ip_rate_limit = ip_rate_limit
    self.gre_rate_limit = gre_rate_limit

class Ddos_dst_ip_host_l4_type_scanning_detection_action:
  def __init__(self, threshold_drop=None, threshold_black_list=None):
    self.threshold_drop = threshold_drop
    self.threshold_black_list = threshold_black_list

class Ddos_dst_ip_host_l4_type_scanning_detection:
  def __init__(self, threshold=None, action=None):
    self.threshold = threshold
    self.action = action

class Ddos_dst_ip_host_l4_type:
  def __init__(self, protocol, glid=None, deny=None, dns_any_check=None, max_rexmit_syn_per_flow=None, exceed_action=None, disable_syn_auth=None, syn_cookie=None, tcp_reset_client=None, tcp_reset_server=None, drop_on_no_port_match=None, over_conn_limit_action=None, over_conn_rate_action=None, class_list=None, state=None, tunnel_decap=None, tunnel_rate_limit=None, drop_frag_pkt=None, scanning_detection=None):
    self.protocol = protocol
    self.glid = glid
    self.deny = deny
    self.dns_any_check = dns_any_check
    self.max_rexmit_syn_per_flow = max_rexmit_syn_per_flow
    self.exceed_action = exceed_action
    self.disable_syn_auth = disable_syn_auth
    self.syn_cookie = syn_cookie
    self.tcp_reset_client = tcp_reset_client
    self.tcp_reset_server = tcp_reset_server
    self.drop_on_no_port_match = drop_on_no_port_match
    self.over_conn_limit_action = over_conn_limit_action
    self.over_conn_rate_action = over_conn_rate_action
    self.class_list = class_list
    self.state = state
    self.tunnel_decap = tunnel_decap
    self.tunnel_rate_limit = tunnel_rate_limit
    self.drop_frag_pkt = drop_frag_pkt
    self.scanning_detection = scanning_detection

class Key_cfg:
  def __init__(self, key=None):
    self.key = key

class Ddos_dst_ip_host_port_template:
  def __init__(self, dns=None, http=None, ssl_l4=None, tcp=None, udp=None):
    self.dns = dns
    self.http = http
    self.ssl_l4 = ssl_l4
    self.tcp = tcp
    self.udp = udp

class Ddos_dst_ip_host_port_sflow_polling_sflow_tcp:
  def __init__(self, sflow_tcp_basic=None, sflow_tcp_stateful=None):
    self.sflow_tcp_basic = sflow_tcp_basic
    self.sflow_tcp_stateful = sflow_tcp_stateful

class Ddos_dst_ip_host_port_sflow_polling:
  def __init__(self, sflow_packets=None, sflow_tcp=None, sflow_http=None):
    self.sflow_packets = sflow_packets
    self.sflow_tcp = sflow_tcp
    self.sflow_http = sflow_http

class Ddos_dst_ip_host_port_sflow:
  def __init__(self, polling=None):
    self.polling = polling

class Ddos_dst_ip_host_port:
  def __init__(self, port_num, protocol, deny=None, glid=None, aflex_cfg=None, template=None, sflow=None):
    self.port_num = port_num
    self.protocol = protocol
    self.deny = deny
    self.glid = glid
    self.aflex_cfg = aflex_cfg
    self.template = template
    self.sflow = sflow

class Aflex_cfg:
  def __init__(self, aflex=None):
    self.aflex = aflex

class Ddos_dst_ip_host_ip_proto:
  def __init__(self, port_num, deny=None, glid=None):
    self.port_num = port_num
    self.deny = deny
    self.glid = glid

class Ddos_dst_ip_host_src_dst_pair:
  def __init__(self, src, l4_type_src_dstList=None, app_type_src_dstList=None):
    self.src = src
    self.l4_type_src_dstList = l4_type_src_dstList
    self.app_type_src_dstList = app_type_src_dstList

class Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst_template:
  def __init__(self, tcp=None, udp=None):
    self.tcp = tcp
    self.udp = udp

class Ddos_dst_ip_host_src_dst_pair_l4_type_src_dst:
  def __init__(self, protocol, glid=None, template=None):
    self.protocol = protocol
    self.glid = glid
    self.template = template

class Ddos_dst_ip_host_src_dst_pair_app_type_src_dst_template:
  def __init__(self, ssl_l4=None, dns=None, http=None):
    self.ssl_l4 = ssl_l4
    self.dns = dns
    self.http = http

class Ddos_dst_ip_host_src_dst_pair_app_type_src_dst:
  def __init__(self, protocol, template=None):
    self.protocol = protocol
    self.template = template

class Host_ip_addr:
  def __init__(self, ip_addr):
    self.ip_addr = ip_addr

  def __str__(self):
    return str(self.ip_addr)

class Host_sflow_polling_sflow_tcp:
  def __init__(self, sflow_tcp_basic=None, sflow_tcp_stateful=None):
    self.sflow_tcp_basic = sflow_tcp_basic
    self.sflow_tcp_stateful = sflow_tcp_stateful

class Host_sflow_polling:
  def __init__(self, sflow_packets=None, sflow_layer_4=None, sflow_tcp=None, sflow_http=None):
    self.sflow_packets = sflow_packets
    self.sflow_layer_4 = sflow_layer_4
    self.sflow_tcp = sflow_tcp
    self.sflow_http = sflow_http

class Host_sflow:
  def __init__(self, polling=None):
    self.polling = polling

class Host:
  def __init__(self, ip_addr, exceed_log_enable=None, enable_512_port=None, sflow=None, l4_typeList=None, portList=None, ip_protoList=None, src_dst_pairList=None):
    self.ip_addr = ip_addr
    self.exceed_log_enable = exceed_log_enable
    self.enable_512_port = enable_512_port
    self.sflow = sflow
    self.l4_typeList = l4_typeList
    self.portList = portList
    self.ip_protoList = ip_protoList
    self.src_dst_pairList = src_dst_pairList

class DdosDstipHostClient(AbstractResourceClient):
  def __init__(self, endpoint=None, sessionid=None, debug=False):
    AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

  def getDdosDstipHost(self, host_ip_addr):
    """
    Retrieve the host identified by the specified identifier
    
    Args:
      host_ip_addr Host_ip_addr
    
    Returns:
      An instance of the Host class
    """
    query = ''
    conn = self.get_connection()
    headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
    conn.request('GET', self.get_path() + '/' + str(host_ip_addr)  + query, headers=headers)
    response = conn.getresponse()
    expected_status = 200
    errors = {500: 'An unexpected runtime exception', 404: 'Specified host does not exist'}
    payload = self.get_output(response, expected_status, errors)
    conn.close()
    if self.debug:
      print 'payload:', payload
    data = json.loads(payload)
    payload= data.get('host')
    return deserialize_Host_json(payload)

  def deleteDdosDstipHost(self, host_ip_addr):
    """
    Remove the host identified by the specified identifier from the system
    
    Args:
      host_ip_addr Host_ip_addr
    
    Returns:
      An instance of the string class
    """
    query = ''
    conn = self.get_connection()
    headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
    conn.request('DELETE', self.get_path() + '/' + str(host_ip_addr)  + query, headers=headers)
    response = conn.getresponse()
    expected_status = 200
    errors = {500: 'An unexpected runtime exception', 404: 'Specified host does not exist'}
    payload = self.get_output(response, expected_status, errors)
    conn.close()
    if self.debug:
      print 'payload:', payload
    return deserialize_string_json(payload)

class AllDdosDstipHostsClient(AbstractResourceClient):
  def __init__(self, endpoint=None, sessionid=None, debug=False):
    AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

  def submitDdosDstipHost(self, host):
    """
    Create the object host
    
    Args:
      host An instance of the Host class
    
    Returns:
      An instance of the string class
    """
    query = ''
    conn = self.get_connection()
    headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
    output=OrderedDict()
    output['host']=serialize_Host_json(host)
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

  def getAllDdosDstipHosts(self):
    """
    Retrieve all host objects currently pending in the system
    
    Returns:
      A list of Host objects
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
    payload= data.get('hostList')
    return deserialize_list_Host_json(payload)

