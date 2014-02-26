########################################################################################################################
# File name: ddos_dst.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/dst',
]

def deserialize_Ddos_dst_default_l4_type__exceed_action_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	exceed_drop = data.get('exceed-drop')
	result = Ddos_dst_default_l4_type__exceed_action(exceed_drop=exceed_drop)
	return result

def deserialize_Ddos_dst_key_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key = data.get('key')
	result = Ddos_dst_key_cfg(key=key)
	return result

def deserialize_list_Ddos_dst_key_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_key_cfg_json(item))
	return list(container)

def deserialize_Ddos_dst_default_l4_type__tunnel_decap_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_decap = data.get('ip-decap')
	gre_decap = data.get('gre-decap')
	key_cfg = deserialize_list_Ddos_dst_key_cfg_json(data.get('key-cfg'))
	result = Ddos_dst_default_l4_type__tunnel_decap(ip_decap=ip_decap, gre_decap=gre_decap, key_cfg=key_cfg)
	return result

def deserialize_Ddos_dst_default_l4_type__tunnel_rate_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_rate_limit = data.get('ip-rate-limit')
	gre_rate_limit = data.get('gre-rate-limit')
	result = Ddos_dst_default_l4_type__tunnel_rate_limit(ip_rate_limit=ip_rate_limit, gre_rate_limit=gre_rate_limit)
	return result

def deserialize_Ddos_dst_default_l4_type__scanning_detection__action_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	threshold_drop = data.get('threshold-drop')
	threshold_black_list = data.get('threshold-black-list')
	result = Ddos_dst_default_l4_type__scanning_detection__action(threshold_drop=threshold_drop, threshold_black_list=threshold_black_list)
	return result

def deserialize_Ddos_dst_default_l4_type__scanning_detection_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	threshold = data.get('threshold')
	action = deserialize_Ddos_dst_default_l4_type__scanning_detection__action_json(data.get('action'))
	result = Ddos_dst_default_l4_type__scanning_detection(threshold=threshold, action=action)
	return result

def deserialize_Ddos_dst_default_l4_type_json(obj):
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
	exceed_action = deserialize_Ddos_dst_default_l4_type__exceed_action_json(data.get('exceed-action'))
	disable_syn_auth = data.get('disable-syn-auth')
	syn_cookie = data.get('syn-cookie')
	tcp_reset_client = data.get('tcp-reset-client')
	tcp_reset_server = data.get('tcp-reset-server')
	drop_on_no_port_match = data.get('drop-on-no-port-match')
	over_conn_limit_action = data.get('over-conn-limit-action')
	over_conn_rate_action = data.get('over-conn-rate-action')
	stateful = data.get('stateful')
	tunnel_decap = deserialize_Ddos_dst_default_l4_type__tunnel_decap_json(data.get('tunnel-decap'))
	tunnel_rate_limit = deserialize_Ddos_dst_default_l4_type__tunnel_rate_limit_json(data.get('tunnel-rate-limit'))
	drop_frag_pkt = data.get('drop-frag-pkt')
	scanning_detection = deserialize_Ddos_dst_default_l4_type__scanning_detection_json(data.get('scanning-detection'))
	result = Ddos_dst_default_l4_type(protocol=protocol, glid=glid, deny=deny, dns_any_check=dns_any_check, max_rexmit_syn_per_flow=max_rexmit_syn_per_flow, exceed_action=exceed_action, disable_syn_auth=disable_syn_auth, syn_cookie=syn_cookie, tcp_reset_client=tcp_reset_client, tcp_reset_server=tcp_reset_server, drop_on_no_port_match=drop_on_no_port_match, over_conn_limit_action=over_conn_limit_action, over_conn_rate_action=over_conn_rate_action, stateful=stateful, tunnel_decap=tunnel_decap, tunnel_rate_limit=tunnel_rate_limit, drop_frag_pkt=drop_frag_pkt, scanning_detection=scanning_detection)
	return result

def deserialize_list_Ddos_dst_default_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_default_l4_type_json(item))
	return list(container)

def deserialize_Ddos_dst_default_port__template_json(obj):
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
	result = Ddos_dst_default_port__template(dns=dns, http=http, ssl_l4=ssl_l4, tcp=tcp, udp=udp)
	return result

def deserialize_Ddos_dst_default_port_json(obj):
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
	template = deserialize_Ddos_dst_default_port__template_json(data.get('template'))
	result = Ddos_dst_default_port(port_num=port_num, protocol=protocol, deny=deny, glid=glid, template=template)
	return result

def deserialize_list_Ddos_dst_default_port_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_default_port_json(item))
	return list(container)

def deserialize_Ddos_dst_default_ip_proto_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	port_num = data.get('port-num')
	deny = data.get('deny')
	glid = data.get('glid')
	result = Ddos_dst_default_ip_proto(port_num=port_num, deny=deny, glid=glid)
	return result

def deserialize_list_Ddos_dst_default_ip_proto_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_default_ip_proto_json(item))
	return list(container)

def deserialize_Ddos_dst_default_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default_address_type = data.get('default-address-type')
	disable = data.get('disable')
	age = data.get('age')
	exceed_log_enable = data.get('exceed-log-enable')
	l4_typelist = deserialize_list_Ddos_dst_default_l4_type_json(data.get('l4-typeList'))
	portlist = deserialize_list_Ddos_dst_default_port_json(data.get('portList'))
	ip_protolist = deserialize_list_Ddos_dst_default_ip_proto_json(data.get('ip-protoList'))
	result = Ddos_dst_default(default_address_type=default_address_type, disable=disable, age=age, exceed_log_enable=exceed_log_enable, l4_typelist=l4_typelist, portlist=portlist, ip_protolist=ip_protolist)
	return result

def deserialize_list_Ddos_dst_default_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_default_json(item))
	return list(container)

def deserialize_Ddos_dst_entry__sflow__polling__sflow_tcp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sflow_tcp_basic = data.get('sflow-tcp-basic')
	sflow_tcp_stateful = data.get('sflow-tcp-stateful')
	result = Ddos_dst_entry__sflow__polling__sflow_tcp(sflow_tcp_basic=sflow_tcp_basic, sflow_tcp_stateful=sflow_tcp_stateful)
	return result

def deserialize_Ddos_dst_entry__sflow__polling_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sflow_packets = data.get('sflow-packets')
	sflow_layer_4 = data.get('sflow-layer-4')
	sflow_tcp = deserialize_Ddos_dst_entry__sflow__polling__sflow_tcp_json(data.get('sflow-tcp'))
	sflow_http = data.get('sflow-http')
	result = Ddos_dst_entry__sflow__polling(sflow_packets=sflow_packets, sflow_layer_4=sflow_layer_4, sflow_tcp=sflow_tcp, sflow_http=sflow_http)
	return result

def deserialize_Ddos_dst_entry__sflow_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	polling = deserialize_Ddos_dst_entry__sflow__polling_json(data.get('polling'))
	result = Ddos_dst_entry__sflow(polling=polling)
	return result

def deserialize_Ddos_dst_entry_l4_type__exceed_action_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	exceed_drop = data.get('exceed-drop')
	exceed_black_list = data.get('exceed-black-list')
	result = Ddos_dst_entry_l4_type__exceed_action(exceed_drop=exceed_drop, exceed_black_list=exceed_black_list)
	return result

def deserialize_Ddos_dst_entry_l4_type__tunnel_decap_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_decap = data.get('ip-decap')
	gre_decap = data.get('gre-decap')
	key_cfg = deserialize_list_Ddos_dst_key_cfg_json(data.get('key-cfg'))
	result = Ddos_dst_entry_l4_type__tunnel_decap(ip_decap=ip_decap, gre_decap=gre_decap, key_cfg=key_cfg)
	return result

def deserialize_Ddos_dst_entry_l4_type__tunnel_rate_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_rate_limit = data.get('ip-rate-limit')
	gre_rate_limit = data.get('gre-rate-limit')
	result = Ddos_dst_entry_l4_type__tunnel_rate_limit(ip_rate_limit=ip_rate_limit, gre_rate_limit=gre_rate_limit)
	return result

def deserialize_Ddos_dst_entry_l4_type__scanning_detection__action_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	threshold_drop = data.get('threshold-drop')
	threshold_black_list = data.get('threshold-black-list')
	result = Ddos_dst_entry_l4_type__scanning_detection__action(threshold_drop=threshold_drop, threshold_black_list=threshold_black_list)
	return result

def deserialize_Ddos_dst_entry_l4_type__scanning_detection_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	threshold = data.get('threshold')
	action = deserialize_Ddos_dst_entry_l4_type__scanning_detection__action_json(data.get('action'))
	result = Ddos_dst_entry_l4_type__scanning_detection(threshold=threshold, action=action)
	return result

def deserialize_Ddos_dst_entry_l4_type_json(obj):
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
	exceed_action = deserialize_Ddos_dst_entry_l4_type__exceed_action_json(data.get('exceed-action'))
	disable_syn_auth = data.get('disable-syn-auth')
	syn_cookie = data.get('syn-cookie')
	tcp_reset_client = data.get('tcp-reset-client')
	tcp_reset_server = data.get('tcp-reset-server')
	drop_on_no_port_match = data.get('drop-on-no-port-match')
	over_conn_limit_action = data.get('over-conn-limit-action')
	over_conn_rate_action = data.get('over-conn-rate-action')
	stateful = data.get('stateful')
	tunnel_decap = deserialize_Ddos_dst_entry_l4_type__tunnel_decap_json(data.get('tunnel-decap'))
	tunnel_rate_limit = deserialize_Ddos_dst_entry_l4_type__tunnel_rate_limit_json(data.get('tunnel-rate-limit'))
	drop_frag_pkt = data.get('drop-frag-pkt')
	scanning_detection = deserialize_Ddos_dst_entry_l4_type__scanning_detection_json(data.get('scanning-detection'))
	result = Ddos_dst_entry_l4_type(protocol=protocol, glid=glid, deny=deny, dns_any_check=dns_any_check, max_rexmit_syn_per_flow=max_rexmit_syn_per_flow, exceed_action=exceed_action, disable_syn_auth=disable_syn_auth, syn_cookie=syn_cookie, tcp_reset_client=tcp_reset_client, tcp_reset_server=tcp_reset_server, drop_on_no_port_match=drop_on_no_port_match, over_conn_limit_action=over_conn_limit_action, over_conn_rate_action=over_conn_rate_action, stateful=stateful, tunnel_decap=tunnel_decap, tunnel_rate_limit=tunnel_rate_limit, drop_frag_pkt=drop_frag_pkt, scanning_detection=scanning_detection)
	return result

def deserialize_list_Ddos_dst_entry_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_entry_l4_type_json(item))
	return list(container)

def deserialize_Ddos_dst_aflex_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	aflex = data.get('aflex')
	result = Ddos_dst_aflex_cfg(aflex=aflex)
	return result

def deserialize_list_Ddos_dst_aflex_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_aflex_cfg_json(item))
	return list(container)

def deserialize_Ddos_dst_entry_port__template_json(obj):
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
	result = Ddos_dst_entry_port__template(dns=dns, http=http, ssl_l4=ssl_l4, tcp=tcp, udp=udp)
	return result

def deserialize_Ddos_dst_entry_port__sflow__polling__sflow_tcp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sflow_tcp_basic = data.get('sflow-tcp-basic')
	sflow_tcp_stateful = data.get('sflow-tcp-stateful')
	result = Ddos_dst_entry_port__sflow__polling__sflow_tcp(sflow_tcp_basic=sflow_tcp_basic, sflow_tcp_stateful=sflow_tcp_stateful)
	return result

def deserialize_Ddos_dst_entry_port__sflow__polling_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sflow_packets = data.get('sflow-packets')
	sflow_tcp = deserialize_Ddos_dst_entry_port__sflow__polling__sflow_tcp_json(data.get('sflow-tcp'))
	sflow_http = data.get('sflow-http')
	result = Ddos_dst_entry_port__sflow__polling(sflow_packets=sflow_packets, sflow_tcp=sflow_tcp, sflow_http=sflow_http)
	return result

def deserialize_Ddos_dst_entry_port__sflow_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	polling = deserialize_Ddos_dst_entry_port__sflow__polling_json(data.get('polling'))
	result = Ddos_dst_entry_port__sflow(polling=polling)
	return result

def deserialize_Ddos_dst_entry_port_json(obj):
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
	aflex_cfg = deserialize_list_Ddos_dst_aflex_cfg_json(data.get('aflex-cfg'))
	template = deserialize_Ddos_dst_entry_port__template_json(data.get('template'))
	sflow = deserialize_Ddos_dst_entry_port__sflow_json(data.get('sflow'))
	result = Ddos_dst_entry_port(port_num=port_num, protocol=protocol, deny=deny, glid=glid, aflex_cfg=aflex_cfg, template=template, sflow=sflow)
	return result

def deserialize_list_Ddos_dst_entry_port_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_entry_port_json(item))
	return list(container)

def deserialize_Ddos_dst_entry_ip_proto_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	port_num = data.get('port-num')
	deny = data.get('deny')
	glid = data.get('glid')
	result = Ddos_dst_entry_ip_proto(port_num=port_num, deny=deny, glid=glid)
	return result

def deserialize_list_Ddos_dst_entry_ip_proto_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_entry_ip_proto_json(item))
	return list(container)

def deserialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	result = Ddos_dst_entry_src_dst_pair_l4_type_src_dst__template(tcp=tcp, udp=udp)
	return result

def deserialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	glid = data.get('glid')
	template = deserialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst__template_json(data.get('template'))
	result = Ddos_dst_entry_src_dst_pair_l4_type_src_dst(protocol=protocol, glid=glid, template=template)
	return result

def deserialize_list_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(item))
	return list(container)

def deserialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ssl_l4 = data.get('ssl-l4')
	dns = data.get('dns')
	http = data.get('http')
	result = Ddos_dst_entry_src_dst_pair_app_type_src_dst__template(ssl_l4=ssl_l4, dns=dns, http=http)
	return result

def deserialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	template = deserialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst__template_json(data.get('template'))
	result = Ddos_dst_entry_src_dst_pair_app_type_src_dst(protocol=protocol, template=template)
	return result

def deserialize_list_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(item))
	return list(container)

def deserialize_Ddos_dst_entry_src_dst_pair_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	src = data.get('src')
	class_list_name = data.get('class-list-name')
	l4_type_src_dstlist = deserialize_list_Ddos_dst_entry_src_dst_pair_l4_type_src_dst_json(data.get('l4-type-src-dstList'))
	app_type_src_dstlist = deserialize_list_Ddos_dst_entry_src_dst_pair_app_type_src_dst_json(data.get('app-type-src-dstList'))
	result = Ddos_dst_entry_src_dst_pair(src=src, class_list_name=class_list_name, l4_type_src_dstlist=l4_type_src_dstlist, app_type_src_dstlist=app_type_src_dstlist)
	return result

def deserialize_list_Ddos_dst_entry_src_dst_pair_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_entry_src_dst_pair_json(item))
	return list(container)

def deserialize_Ddos_dst_entry_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dst_entry_name = data.get('dst-entry-name')
	ipv6_addr = data.get('ipv6-addr')
	ip_addr = data.get('ip-addr')
	subnet_ip_addr = data.get('subnet-ip-addr')
	subnet_ipv6_addr = data.get('subnet-ipv6-addr')
	exceed_log_enable = data.get('exceed-log-enable')
	enable_512_port = data.get('enable-512-port')
	sflow = deserialize_Ddos_dst_entry__sflow_json(data.get('sflow'))
	drop_on_no_src_dst_default = data.get('drop-on-no-src-dst-default')
	l4_typelist = deserialize_list_Ddos_dst_entry_l4_type_json(data.get('l4-typeList'))
	portlist = deserialize_list_Ddos_dst_entry_port_json(data.get('portList'))
	ip_protolist = deserialize_list_Ddos_dst_entry_ip_proto_json(data.get('ip-protoList'))
	src_dst_pairlist = deserialize_list_Ddos_dst_entry_src_dst_pair_json(data.get('src-dst-pairList'))
	result = Ddos_dst_entry(dst_entry_name=dst_entry_name, ipv6_addr=ipv6_addr, ip_addr=ip_addr, subnet_ip_addr=subnet_ip_addr, subnet_ipv6_addr=subnet_ipv6_addr, exceed_log_enable=exceed_log_enable, enable_512_port=enable_512_port, sflow=sflow, drop_on_no_src_dst_default=drop_on_no_src_dst_default, l4_typelist=l4_typelist, portlist=portlist, ip_protolist=ip_protolist, src_dst_pairlist=src_dst_pairlist)
	return result

def deserialize_list_Ddos_dst_entry_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_entry_json(item))
	return list(container)

def deserialize_Dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	defaultlist = deserialize_list_Ddos_dst_default_json(data.get('defaultList'))
	entrylist = deserialize_list_Ddos_dst_entry_json(data.get('entryList'))
	result = Dst(defaultlist=defaultlist, entrylist=entrylist)
	return result

class Dst(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, defaultlist=None, entrylist=None):
		self.defaultlist = defaultlist
		self.entrylist = entrylist

	def __str__(self):
		return ""

class Ddos_dst_default(AxapiObject):
	__metaclass__ = StructMeta 
	default_address_type = Enum(['ip', 'ipv6'])
	disable=PosRangedInteger(0, 1)
	age=PosRangedInteger(5, 1023)
	exceed_log_enable=PosRangedInteger(0, 1)
	def __init__(self, default_address_type, disable=None, age=None, exceed_log_enable=None, l4_typelist=None, portlist=None, ip_protolist=None):
		self.default_address_type = default_address_type
		self.disable = disable
		self.age = age
		self.exceed_log_enable = exceed_log_enable
		self.l4_typelist = l4_typelist
		self.portlist = portlist
		self.ip_protolist = ip_protolist

	def __str__(self):
		return str(self.default_address_type)

class Ddos_dst_default_l4_type__exceed_action(AxapiObject):
	__metaclass__ = StructMeta 
	exceed_drop=PosRangedInteger(0, 1)
	def __init__(self, exceed_drop=None):
		self.exceed_drop = exceed_drop

	def __str__(self):
		return ""

class Ddos_dst_default_l4_type__tunnel_decap(AxapiObject):
	__metaclass__ = StructMeta 
	ip_decap=PosRangedInteger(0, 1)
	gre_decap=PosRangedInteger(0, 1)
	def __init__(self, ip_decap=None, gre_decap=None, key_cfg=None):
		self.ip_decap = ip_decap
		self.gre_decap = gre_decap
		self.key_cfg = key_cfg

	def __str__(self):
		return ""

class Ddos_dst_default_l4_type__tunnel_rate_limit(AxapiObject):
	__metaclass__ = StructMeta 
	ip_rate_limit=PosRangedInteger(0, 1)
	gre_rate_limit=PosRangedInteger(0, 1)
	def __init__(self, ip_rate_limit=None, gre_rate_limit=None):
		self.ip_rate_limit = ip_rate_limit
		self.gre_rate_limit = gre_rate_limit

	def __str__(self):
		return ""

class Ddos_dst_default_l4_type__scanning_detection__action(AxapiObject):
	__metaclass__ = StructMeta 
	threshold_drop=PosRangedInteger(0, 1)
	threshold_black_list=PosRangedInteger(0, 1)
	def __init__(self, threshold_drop=None, threshold_black_list=None):
		self.threshold_drop = threshold_drop
		self.threshold_black_list = threshold_black_list

	def __str__(self):
		return ""

class Ddos_dst_default_l4_type__scanning_detection(AxapiObject):
	__metaclass__ = StructMeta 
	threshold=PosRangedInteger(1, 31)
	def __init__(self, threshold=None, action=None):
		self.threshold = threshold
		self.action = action

	def __str__(self):
		return ""

class Ddos_dst_default_l4_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['tcp', 'udp', 'icmp', 'other'])
	glid=PosRangedInteger(1, 32000)
	deny=PosRangedInteger(0, 1)
	dns_any_check=PosRangedInteger(0, 1)
	max_rexmit_syn_per_flow=PosRangedInteger(1, 7)
	disable_syn_auth=PosRangedInteger(0, 1)
	syn_cookie=PosRangedInteger(0, 1)
	tcp_reset_client=PosRangedInteger(0, 1)
	tcp_reset_server=PosRangedInteger(0, 1)
	drop_on_no_port_match=SizedString(1, 255)
	over_conn_limit_action=SizedString(1, 255)
	over_conn_rate_action=SizedString(1, 255)
	stateful=PosRangedInteger(0, 1)
	drop_frag_pkt=PosRangedInteger(0, 1)
	def __init__(self, protocol, glid=None, deny=None, dns_any_check=None, max_rexmit_syn_per_flow=None, exceed_action=None, disable_syn_auth=None, syn_cookie=None, tcp_reset_client=None, tcp_reset_server=None, drop_on_no_port_match=None, over_conn_limit_action=None, over_conn_rate_action=None, stateful=None, tunnel_decap=None, tunnel_rate_limit=None, drop_frag_pkt=None, scanning_detection=None):
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
		self.stateful = stateful
		self.tunnel_decap = tunnel_decap
		self.tunnel_rate_limit = tunnel_rate_limit
		self.drop_frag_pkt = drop_frag_pkt
		self.scanning_detection = scanning_detection

	def __str__(self):
		return str(self.protocol)

class Ddos_dst_key_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	key=SizedString(1, 8)
	def __init__(self, key=None):
		self.key = key

	def __str__(self):
		return ""

class Ddos_dst_default_port__template(AxapiObject):
	__metaclass__ = StructMeta 
	dns=SizedString(1, 255)
	http=SizedString(1, 255)
	ssl_l4=SizedString(1, 255)
	tcp=SizedString(1, 255)
	udp=SizedString(1, 255)
	def __init__(self, dns=None, http=None, ssl_l4=None, tcp=None, udp=None):
		self.dns = dns
		self.http = http
		self.ssl_l4 = ssl_l4
		self.tcp = tcp
		self.udp = udp

	def __str__(self):
		return ""

class Ddos_dst_default_port(AxapiObject):
	__metaclass__ = StructMeta 
	port_num=PosRangedInteger(1, 65534)
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'tcp', 'udp', 'ssl-l4'])
	deny=PosRangedInteger(0, 1)
	glid=PosRangedInteger(1, 32000)
	def __init__(self, port_num, protocol, deny=None, glid=None, template=None):
		self.port_num = port_num
		self.protocol = protocol
		self.deny = deny
		self.glid = glid
		self.template = template

	def __str__(self):
		return str(self.port_num) + '+' + str(self.protocol)

class Ddos_dst_default_ip_proto(AxapiObject):
	__metaclass__ = StructMeta 
	port_num=PosRangedInteger(1, 255)
	deny=PosRangedInteger(0, 1)
	glid=PosRangedInteger(1, 32000)
	def __init__(self, port_num, deny=None, glid=None):
		self.port_num = port_num
		self.deny = deny
		self.glid = glid

	def __str__(self):
		return str(self.port_num)

class Ddos_dst_entry__sflow__polling__sflow_tcp(AxapiObject):
	__metaclass__ = StructMeta 
	sflow_tcp_basic=PosRangedInteger(0, 1)
	sflow_tcp_stateful=PosRangedInteger(0, 1)
	def __init__(self, sflow_tcp_basic=None, sflow_tcp_stateful=None):
		self.sflow_tcp_basic = sflow_tcp_basic
		self.sflow_tcp_stateful = sflow_tcp_stateful

	def __str__(self):
		return ""

class Ddos_dst_entry__sflow__polling(AxapiObject):
	__metaclass__ = StructMeta 
	sflow_packets=PosRangedInteger(0, 1)
	sflow_layer_4=PosRangedInteger(0, 1)
	sflow_http=PosRangedInteger(0, 1)
	def __init__(self, sflow_packets=None, sflow_layer_4=None, sflow_tcp=None, sflow_http=None):
		self.sflow_packets = sflow_packets
		self.sflow_layer_4 = sflow_layer_4
		self.sflow_tcp = sflow_tcp
		self.sflow_http = sflow_http

	def __str__(self):
		return ""

class Ddos_dst_entry__sflow(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, polling=None):
		self.polling = polling

	def __str__(self):
		return ""

class Ddos_dst_entry(AxapiObject):
	__metaclass__ = StructMeta 
	dst_entry_name=SizedString(1, 63)
	ipv6_addr=SizedString(1, 255)
	ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_ipv6_addr=SizedString(1, 255)
	exceed_log_enable=PosRangedInteger(0, 1)
	enable_512_port=PosRangedInteger(0, 1)
	drop_on_no_src_dst_default=PosRangedInteger(0, 1)
	def __init__(self, dst_entry_name, ipv6_addr=None, ip_addr=None, subnet_ip_addr=None, subnet_ipv6_addr=None, exceed_log_enable=None, enable_512_port=None, sflow=None, drop_on_no_src_dst_default=None, l4_typelist=None, portlist=None, ip_protolist=None, src_dst_pairlist=None):
		self.dst_entry_name = dst_entry_name
		self.ipv6_addr = ipv6_addr
		self.ip_addr = ip_addr
		self.subnet_ip_addr = subnet_ip_addr
		self.subnet_ipv6_addr = subnet_ipv6_addr
		self.exceed_log_enable = exceed_log_enable
		self.enable_512_port = enable_512_port
		self.sflow = sflow
		self.drop_on_no_src_dst_default = drop_on_no_src_dst_default
		self.l4_typelist = l4_typelist
		self.portlist = portlist
		self.ip_protolist = ip_protolist
		self.src_dst_pairlist = src_dst_pairlist

	def __str__(self):
		return str(self.dst_entry_name)

class Ddos_dst_entry_l4_type__exceed_action(AxapiObject):
	__metaclass__ = StructMeta 
	exceed_drop=PosRangedInteger(0, 1)
	exceed_black_list=PosRangedInteger(0, 1)
	def __init__(self, exceed_drop=None, exceed_black_list=None):
		self.exceed_drop = exceed_drop
		self.exceed_black_list = exceed_black_list

	def __str__(self):
		return ""

class Ddos_dst_entry_l4_type__tunnel_decap(AxapiObject):
	__metaclass__ = StructMeta 
	ip_decap=PosRangedInteger(0, 1)
	gre_decap=PosRangedInteger(0, 1)
	def __init__(self, ip_decap=None, gre_decap=None, key_cfg=None):
		self.ip_decap = ip_decap
		self.gre_decap = gre_decap
		self.key_cfg = key_cfg

	def __str__(self):
		return ""

class Ddos_dst_entry_l4_type__tunnel_rate_limit(AxapiObject):
	__metaclass__ = StructMeta 
	ip_rate_limit=PosRangedInteger(0, 1)
	gre_rate_limit=PosRangedInteger(0, 1)
	def __init__(self, ip_rate_limit=None, gre_rate_limit=None):
		self.ip_rate_limit = ip_rate_limit
		self.gre_rate_limit = gre_rate_limit

	def __str__(self):
		return ""

class Ddos_dst_entry_l4_type__scanning_detection__action(AxapiObject):
	__metaclass__ = StructMeta 
	threshold_drop=PosRangedInteger(0, 1)
	threshold_black_list=PosRangedInteger(0, 1)
	def __init__(self, threshold_drop=None, threshold_black_list=None):
		self.threshold_drop = threshold_drop
		self.threshold_black_list = threshold_black_list

	def __str__(self):
		return ""

class Ddos_dst_entry_l4_type__scanning_detection(AxapiObject):
	__metaclass__ = StructMeta 
	threshold=PosRangedInteger(1, 31)
	def __init__(self, threshold=None, action=None):
		self.threshold = threshold
		self.action = action

	def __str__(self):
		return ""

class Ddos_dst_entry_l4_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['tcp', 'udp', 'icmp', 'other'])
	glid=PosRangedInteger(1, 32000)
	deny=PosRangedInteger(0, 1)
	dns_any_check=PosRangedInteger(0, 1)
	max_rexmit_syn_per_flow=PosRangedInteger(1, 7)
	disable_syn_auth=PosRangedInteger(0, 1)
	syn_cookie=PosRangedInteger(0, 1)
	tcp_reset_client=PosRangedInteger(0, 1)
	tcp_reset_server=PosRangedInteger(0, 1)
	drop_on_no_port_match=SizedString(1, 255)
	over_conn_limit_action=SizedString(1, 255)
	over_conn_rate_action=SizedString(1, 255)
	stateful=PosRangedInteger(0, 1)
	drop_frag_pkt=PosRangedInteger(0, 1)
	def __init__(self, protocol, glid=None, deny=None, dns_any_check=None, max_rexmit_syn_per_flow=None, exceed_action=None, disable_syn_auth=None, syn_cookie=None, tcp_reset_client=None, tcp_reset_server=None, drop_on_no_port_match=None, over_conn_limit_action=None, over_conn_rate_action=None, stateful=None, tunnel_decap=None, tunnel_rate_limit=None, drop_frag_pkt=None, scanning_detection=None):
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
		self.stateful = stateful
		self.tunnel_decap = tunnel_decap
		self.tunnel_rate_limit = tunnel_rate_limit
		self.drop_frag_pkt = drop_frag_pkt
		self.scanning_detection = scanning_detection

	def __str__(self):
		return str(self.protocol)

class Ddos_dst_entry_port__template(AxapiObject):
	__metaclass__ = StructMeta 
	dns=SizedString(1, 255)
	http=SizedString(1, 255)
	ssl_l4=SizedString(1, 255)
	tcp=SizedString(1, 255)
	udp=SizedString(1, 255)
	def __init__(self, dns=None, http=None, ssl_l4=None, tcp=None, udp=None):
		self.dns = dns
		self.http = http
		self.ssl_l4 = ssl_l4
		self.tcp = tcp
		self.udp = udp

	def __str__(self):
		return ""

class Ddos_dst_entry_port__sflow__polling__sflow_tcp(AxapiObject):
	__metaclass__ = StructMeta 
	sflow_tcp_basic=PosRangedInteger(0, 1)
	sflow_tcp_stateful=PosRangedInteger(0, 1)
	def __init__(self, sflow_tcp_basic=None, sflow_tcp_stateful=None):
		self.sflow_tcp_basic = sflow_tcp_basic
		self.sflow_tcp_stateful = sflow_tcp_stateful

	def __str__(self):
		return ""

class Ddos_dst_entry_port__sflow__polling(AxapiObject):
	__metaclass__ = StructMeta 
	sflow_packets=PosRangedInteger(0, 1)
	sflow_http=PosRangedInteger(0, 1)
	def __init__(self, sflow_packets=None, sflow_tcp=None, sflow_http=None):
		self.sflow_packets = sflow_packets
		self.sflow_tcp = sflow_tcp
		self.sflow_http = sflow_http

	def __str__(self):
		return ""

class Ddos_dst_entry_port__sflow(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, polling=None):
		self.polling = polling

	def __str__(self):
		return ""

class Ddos_dst_entry_port(AxapiObject):
	__metaclass__ = StructMeta 
	port_num=PosRangedInteger(1, 65534)
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'tcp', 'udp', 'ssl-l4'])
	deny=PosRangedInteger(0, 1)
	glid=PosRangedInteger(1, 32000)
	def __init__(self, port_num, protocol, deny=None, glid=None, aflex_cfg=None, template=None, sflow=None):
		self.port_num = port_num
		self.protocol = protocol
		self.deny = deny
		self.glid = glid
		self.aflex_cfg = aflex_cfg
		self.template = template
		self.sflow = sflow

	def __str__(self):
		return str(self.port_num) + '+' + str(self.protocol)

class Ddos_dst_aflex_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	aflex=SizedString(1, 63)
	def __init__(self, aflex=None):
		self.aflex = aflex

	def __str__(self):
		return ""

class Ddos_dst_entry_ip_proto(AxapiObject):
	__metaclass__ = StructMeta 
	port_num=PosRangedInteger(1, 255)
	deny=PosRangedInteger(0, 1)
	glid=PosRangedInteger(1, 32000)
	def __init__(self, port_num, deny=None, glid=None):
		self.port_num = port_num
		self.deny = deny
		self.glid = glid

	def __str__(self):
		return str(self.port_num)

class Ddos_dst_entry_src_dst_pair(AxapiObject):
	__metaclass__ = StructMeta 
	src = Enum(['default', 'class-list'])
	class_list_name=SizedString(1, 63)
	def __init__(self, src, class_list_name=None, l4_type_src_dstlist=None, app_type_src_dstlist=None):
		self.src = src
		self.class_list_name = class_list_name
		self.l4_type_src_dstlist = l4_type_src_dstlist
		self.app_type_src_dstlist = app_type_src_dstlist

	def __str__(self):
		return str(self.src)

class Ddos_dst_entry_src_dst_pair_l4_type_src_dst__template(AxapiObject):
	__metaclass__ = StructMeta 
	tcp=SizedString(1, 255)
	udp=SizedString(1, 255)
	def __init__(self, tcp=None, udp=None):
		self.tcp = tcp
		self.udp = udp

	def __str__(self):
		return ""

class Ddos_dst_entry_src_dst_pair_l4_type_src_dst(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['tcp', 'udp', 'icmp', 'other'])
	glid=PosRangedInteger(1, 32000)
	def __init__(self, protocol, glid=None, template=None):
		self.protocol = protocol
		self.glid = glid
		self.template = template

	def __str__(self):
		return str(self.protocol)

class Ddos_dst_entry_src_dst_pair_app_type_src_dst__template(AxapiObject):
	__metaclass__ = StructMeta 
	ssl_l4=SizedString(1, 255)
	dns=SizedString(1, 255)
	http=SizedString(1, 255)
	def __init__(self, ssl_l4=None, dns=None, http=None):
		self.ssl_l4 = ssl_l4
		self.dns = dns
		self.http = http

	def __str__(self):
		return ""

class Ddos_dst_entry_src_dst_pair_app_type_src_dst(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'ssl-l4'])
	def __init__(self, protocol, template=None):
		self.protocol = protocol
		self.template = template

	def __str__(self):
		return str(self.protocol)

class DdosDstClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosDst(self):
		"""
		Retrieve the dst identified by the specified identifier
		
		Returns:
			An instance of the Dst class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified dst does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('dst')
		return deserialize_Dst_json(payload)

