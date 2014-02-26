########################################################################################################################
# File name: ddos_template.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/template',
]

def deserialize_Ddos_template_ssl_l4_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ssl_l4_tmpl_name = data.get('ssl-l4-tmpl-name')
	action = data.get('action')
	disable = data.get('disable')
	renegotiation = data.get('renegotiation')
	request_rate_limit = data.get('request-rate-limit')
	result = Ddos_template_ssl_l4(ssl_l4_tmpl_name=ssl_l4_tmpl_name, action=action, disable=disable, renegotiation=renegotiation, request_rate_limit=request_rate_limit)
	return result

def deserialize_list_Ddos_template_ssl_l4_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_ssl_l4_json(item))
	return list(container)

def deserialize_Ddos_template_http__mss_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	mss_timeout = data.get('mss-timeout')
	mss_percent = data.get('mss-percent')
	number_packets = data.get('number-packets')
	result = Ddos_template_http__mss_cfg(mss_timeout=mss_timeout, mss_percent=mss_percent, number_packets=number_packets)
	return result

def deserialize_Ddos_template_http__challenge_method_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	method_302_redirect = data.get('method-302-redirect')
	method_javascript = data.get('method-javascript')
	result = Ddos_template_http__challenge_method(method_302_redirect=method_302_redirect, method_javascript=method_javascript)
	return result

def deserialize_Ddos_template_http__malformed_http_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	malformed_http_enabled = data.get('malformed-http-enabled')
	malformed_http_max_line_size = data.get('malformed-http-max-line-size')
	malformed_http_max_num_headers = data.get('malformed-http-max-num-headers')
	malformed_http_max_req_line_size = data.get('malformed-http-max-req-line-size')
	malformed_http_max_header_name_size = data.get('malformed-http-max-header-name-size')
	malformed_http_max_content_length = data.get('malformed-http-max-content-length')
	malformed_http_bad_chunk_mon_enabled = data.get('malformed-http-bad-chunk-mon-enabled')
	result = Ddos_template_http__malformed_http(malformed_http_enabled=malformed_http_enabled, malformed_http_max_line_size=malformed_http_max_line_size, malformed_http_max_num_headers=malformed_http_max_num_headers, malformed_http_max_req_line_size=malformed_http_max_req_line_size, malformed_http_max_header_name_size=malformed_http_max_header_name_size, malformed_http_max_content_length=malformed_http_max_content_length, malformed_http_bad_chunk_mon_enabled=malformed_http_bad_chunk_mon_enabled)
	return result

def deserialize_Ddos_template_http__use_hdr_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	use_hdr_ip_as_source = data.get('use-hdr-ip-as-source')
	l7_hdr_name = data.get('l7-hdr-name')
	result = Ddos_template_http__use_hdr_ip_cfg(use_hdr_ip_as_source=use_hdr_ip_as_source, l7_hdr_name=l7_hdr_name)
	return result

def deserialize_Ddos_template_http__request_header_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timeout = data.get('timeout')
	result = Ddos_template_http__request_header(timeout=timeout)
	return result

def deserialize_Ddos_template_uri__equal_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	url_equals = data.get('url-equals')
	url_rate = data.get('url-rate')
	result = Ddos_template_uri__equal_cfg(url_equals=url_equals, url_rate=url_rate)
	return result

def deserialize_Ddos_template_uri__contains_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	url_contains = data.get('url-contains')
	url_rate = data.get('url-rate')
	result = Ddos_template_uri__contains_cfg(url_contains=url_contains, url_rate=url_rate)
	return result

def deserialize_Ddos_template_uri__starts_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	url_starts_with = data.get('url-starts-with')
	url_rate = data.get('url-rate')
	result = Ddos_template_uri__starts_cfg(url_starts_with=url_starts_with, url_rate=url_rate)
	return result

def deserialize_Ddos_template_uri__ends_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	url_ends_with = data.get('url-ends-with')
	url_rate = data.get('url-rate')
	result = Ddos_template_uri__ends_cfg(url_ends_with=url_ends_with, url_rate=url_rate)
	return result

def deserialize_Ddos_template_uri_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	equal_cfg = deserialize_Ddos_template_uri__equal_cfg_json(data.get('equal-cfg'))
	contains_cfg = deserialize_Ddos_template_uri__contains_cfg_json(data.get('contains-cfg'))
	starts_cfg = deserialize_Ddos_template_uri__starts_cfg_json(data.get('starts-cfg'))
	ends_cfg = deserialize_Ddos_template_uri__ends_cfg_json(data.get('ends-cfg'))
	result = Ddos_template_uri(equal_cfg=equal_cfg, contains_cfg=contains_cfg, starts_cfg=starts_cfg, ends_cfg=ends_cfg)
	return result

def deserialize_list_Ddos_template_uri_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_uri_json(item))
	return list(container)

def deserialize_Ddos_template_http__request_rate_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	request_rate = data.get('request-rate')
	uri = deserialize_list_Ddos_template_uri_json(data.get('uri'))
	result = Ddos_template_http__request_rate_limit(request_rate=request_rate, uri=uri)
	return result

def deserialize_Ddos_template_obj_size__less_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	obj_less = data.get('obj-less')
	obj_rate = data.get('obj-rate')
	result = Ddos_template_obj_size__less_cfg(obj_less=obj_less, obj_rate=obj_rate)
	return result

def deserialize_Ddos_template_obj_size__greater_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	obj_greater = data.get('obj-greater')
	obj_rate = data.get('obj-rate')
	result = Ddos_template_obj_size__greater_cfg(obj_greater=obj_greater, obj_rate=obj_rate)
	return result

def deserialize_Ddos_template_obj_size__between_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	obj_between1 = data.get('obj-between1')
	obj_between2 = data.get('obj-between2')
	obj_rate = data.get('obj-rate')
	result = Ddos_template_obj_size__between_cfg(obj_between1=obj_between1, obj_between2=obj_between2, obj_rate=obj_rate)
	return result

def deserialize_Ddos_template_obj_size_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	less_cfg = deserialize_Ddos_template_obj_size__less_cfg_json(data.get('less-cfg'))
	greater_cfg = deserialize_Ddos_template_obj_size__greater_cfg_json(data.get('greater-cfg'))
	between_cfg = deserialize_Ddos_template_obj_size__between_cfg_json(data.get('between-cfg'))
	result = Ddos_template_obj_size(less_cfg=less_cfg, greater_cfg=greater_cfg, between_cfg=between_cfg)
	return result

def deserialize_list_Ddos_template_obj_size_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_obj_size_json(item))
	return list(container)

def deserialize_Ddos_template_http__response_rate_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	obj_size = deserialize_list_Ddos_template_obj_size_json(data.get('obj-size'))
	result = Ddos_template_http__response_rate_limit(obj_size=obj_size)
	return result

def deserialize_Ddos_template_http__slow_read_drop_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	min_window_size = data.get('min-window-size')
	min_window_count = data.get('min-window-count')
	result = Ddos_template_http__slow_read_drop(min_window_size=min_window_size, min_window_count=min_window_count)
	return result

def deserialize_Ddos_template_referer_filter_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ref_filter_blacklist = data.get('ref-filter-blacklist')
	referer_equals = data.get('referer-equals')
	referer_contains = data.get('referer-contains')
	referer_starts_with = data.get('referer-starts-with')
	referer_ends_with = data.get('referer-ends-with')
	result = Ddos_template_referer_filter(ref_filter_blacklist=ref_filter_blacklist, referer_equals=referer_equals, referer_contains=referer_contains, referer_starts_with=referer_starts_with, referer_ends_with=referer_ends_with)
	return result

def deserialize_list_Ddos_template_referer_filter_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_referer_filter_json(item))
	return list(container)

def deserialize_Ddos_template_agent_filter_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	agent_filter_blacklist = data.get('agent-filter-blacklist')
	agent_equals = data.get('agent-equals')
	agent_contains = data.get('agent-contains')
	agent_starts_with = data.get('agent-starts-with')
	agent_ends_with = data.get('agent-ends-with')
	result = Ddos_template_agent_filter(agent_filter_blacklist=agent_filter_blacklist, agent_equals=agent_equals, agent_contains=agent_contains, agent_starts_with=agent_starts_with, agent_ends_with=agent_ends_with)
	return result

def deserialize_list_Ddos_template_agent_filter_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_agent_filter_json(item))
	return list(container)

def deserialize_Ddos_template_http_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	http_tmpl_name = data.get('http-tmpl-name')
	action = data.get('action')
	disable = data.get('disable')
	mss_cfg = deserialize_Ddos_template_http__mss_cfg_json(data.get('mss-cfg'))
	challenge_method = deserialize_Ddos_template_http__challenge_method_json(data.get('challenge-method'))
	challenge_cookie_name = data.get('challenge-cookie-name')
	challenge_keep_cookie = data.get('challenge-keep-cookie')
	challenge_interval = data.get('challenge-interval')
	malformed_http = deserialize_Ddos_template_http__malformed_http_json(data.get('malformed-http'))
	use_hdr_ip_cfg = deserialize_Ddos_template_http__use_hdr_ip_cfg_json(data.get('use-hdr-ip-cfg'))
	request_header = deserialize_Ddos_template_http__request_header_json(data.get('request-header'))
	post_rate_limit = data.get('post-rate-limit')
	request_rate_limit = deserialize_Ddos_template_http__request_rate_limit_json(data.get('request-rate-limit'))
	response_rate_limit = deserialize_Ddos_template_http__response_rate_limit_json(data.get('response-rate-limit'))
	slow_read_drop = deserialize_Ddos_template_http__slow_read_drop_json(data.get('slow-read-drop'))
	idle_timeout = data.get('idle-timeout')
	ignore_zero_payload = data.get('ignore-zero-payload')
	referer_filter = deserialize_list_Ddos_template_referer_filter_json(data.get('referer-filter'))
	agent_filter = deserialize_list_Ddos_template_agent_filter_json(data.get('agent-filter'))
	result = Ddos_template_http(http_tmpl_name=http_tmpl_name, action=action, disable=disable, mss_cfg=mss_cfg, challenge_method=challenge_method, challenge_cookie_name=challenge_cookie_name, challenge_keep_cookie=challenge_keep_cookie, challenge_interval=challenge_interval, malformed_http=malformed_http, use_hdr_ip_cfg=use_hdr_ip_cfg, request_header=request_header, post_rate_limit=post_rate_limit, request_rate_limit=request_rate_limit, response_rate_limit=response_rate_limit, slow_read_drop=slow_read_drop, idle_timeout=idle_timeout, ignore_zero_payload=ignore_zero_payload, referer_filter=referer_filter, agent_filter=agent_filter)
	return result

def deserialize_list_Ddos_template_http_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_http_json(item))
	return list(container)

def deserialize_Ddos_template_dns__dns_auth_cfg__udp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	udp = data.get('udp')
	udp_timeout = data.get('udp-timeout')
	result = Ddos_template_dns__dns_auth_cfg__udp_cfg(udp=udp, udp_timeout=udp_timeout)
	return result

def deserialize_Ddos_template_dns__dns_auth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns_auth = data.get('dns-auth')
	force_tcp = data.get('force-tcp')
	udp_cfg = deserialize_Ddos_template_dns__dns_auth_cfg__udp_cfg_json(data.get('udp-cfg'))
	result = Ddos_template_dns__dns_auth_cfg(dns_auth=dns_auth, force_tcp=force_tcp, udp_cfg=udp_cfg)
	return result

def deserialize_Ddos_template_dns__fqdn_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns_fqdn_rate_limit = data.get('dns-fqdn-rate-limit')
	dns_fqdn_rate = data.get('dns-fqdn-rate')
	by = data.get('by')
	result = Ddos_template_dns__fqdn_cfg(dns_fqdn_rate_limit=dns_fqdn_rate_limit, dns_fqdn_rate=dns_fqdn_rate, by=by)
	return result

def deserialize_Ddos_template_dns__nxdomain_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns_nxdomain_rate_limit = data.get('dns-nxdomain-rate-limit')
	dns_nxdomain_rate = data.get('dns-nxdomain-rate')
	action = data.get('action')
	result = Ddos_template_dns__nxdomain_cfg(dns_nxdomain_rate_limit=dns_nxdomain_rate_limit, dns_nxdomain_rate=dns_nxdomain_rate, action=action)
	return result

def deserialize_Ddos_template_dns__symtimeout_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sym_timeout = data.get('sym-timeout')
	sym_timeout_value = data.get('sym-timeout-value')
	result = Ddos_template_dns__symtimeout_cfg(sym_timeout=sym_timeout, sym_timeout_value=sym_timeout_value)
	return result

def deserialize_Ddos_template_dns__dns_request_rate_limit__type__a_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	a = data.get('A')
	dns_a_rate = data.get('dns-a-rate')
	result = Ddos_template_dns__dns_request_rate_limit__type__a_cfg(a=a, dns_a_rate=dns_a_rate)
	return result

def deserialize_Ddos_template_dns__dns_request_rate_limit__type__aaaa_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	aaaa = data.get('AAAA')
	dns_aaaa_rate = data.get('dns-aaaa-rate')
	result = Ddos_template_dns__dns_request_rate_limit__type__aaaa_cfg(aaaa=aaaa, dns_aaaa_rate=dns_aaaa_rate)
	return result

def deserialize_Ddos_template_dns__dns_request_rate_limit__type__cname_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	cname = data.get('CNAME')
	dns_cname_rate = data.get('dns-cname-rate')
	result = Ddos_template_dns__dns_request_rate_limit__type__cname_cfg(cname=cname, dns_cname_rate=dns_cname_rate)
	return result

def deserialize_Ddos_template_dns__dns_request_rate_limit__type__mx_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	mx = data.get('MX')
	dns_mx_rate = data.get('dns-mx-rate')
	result = Ddos_template_dns__dns_request_rate_limit__type__mx_cfg(mx=mx, dns_mx_rate=dns_mx_rate)
	return result

def deserialize_Ddos_template_dns__dns_request_rate_limit__type__ns_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ns = data.get('NS')
	dns_ns_rate = data.get('dns-ns-rate')
	result = Ddos_template_dns__dns_request_rate_limit__type__ns_cfg(ns=ns, dns_ns_rate=dns_ns_rate)
	return result

def deserialize_Ddos_template_dns__dns_request_rate_limit__type__srv_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	srv = data.get('SRV')
	dns_srv_rate = data.get('dns-srv-rate')
	result = Ddos_template_dns__dns_request_rate_limit__type__srv_cfg(srv=srv, dns_srv_rate=dns_srv_rate)
	return result

def deserialize_Ddos_template_dns_type_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns_request_type = data.get('dns-request-type')
	dns_request_type_rate = data.get('dns-request-type-rate')
	result = Ddos_template_dns_type_cfg(dns_request_type=dns_request_type, dns_request_type_rate=dns_request_type_rate)
	return result

def deserialize_list_Ddos_template_dns_type_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_dns_type_cfg_json(item))
	return list(container)

def deserialize_Ddos_template_dns__dns_request_rate_limit__type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	a_cfg = deserialize_Ddos_template_dns__dns_request_rate_limit__type__a_cfg_json(data.get('A-cfg'))
	aaaa_cfg = deserialize_Ddos_template_dns__dns_request_rate_limit__type__aaaa_cfg_json(data.get('AAAA-cfg'))
	cname_cfg = deserialize_Ddos_template_dns__dns_request_rate_limit__type__cname_cfg_json(data.get('CNAME-cfg'))
	mx_cfg = deserialize_Ddos_template_dns__dns_request_rate_limit__type__mx_cfg_json(data.get('MX-cfg'))
	ns_cfg = deserialize_Ddos_template_dns__dns_request_rate_limit__type__ns_cfg_json(data.get('NS-cfg'))
	srv_cfg = deserialize_Ddos_template_dns__dns_request_rate_limit__type__srv_cfg_json(data.get('SRV-cfg'))
	dns_type_cfg = deserialize_list_Ddos_template_dns_type_cfg_json(data.get('dns-type-cfg'))
	result = Ddos_template_dns__dns_request_rate_limit__type(a_cfg=a_cfg, aaaa_cfg=aaaa_cfg, cname_cfg=cname_cfg, mx_cfg=mx_cfg, ns_cfg=ns_cfg, srv_cfg=srv_cfg, dns_type_cfg=dns_type_cfg)
	return result

def deserialize_Ddos_template_dns__dns_request_rate_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type = deserialize_Ddos_template_dns__dns_request_rate_limit__type_json(data.get('type'))
	result = Ddos_template_dns__dns_request_rate_limit(type=type)
	return result

def deserialize_Ddos_template_dns_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	dns_any_check = data.get('dns-any-check')
	dns_auth_cfg = deserialize_Ddos_template_dns__dns_auth_cfg_json(data.get('dns-auth-cfg'))
	fqdn_cfg = deserialize_Ddos_template_dns__fqdn_cfg_json(data.get('fqdn-cfg'))
	nxdomain_cfg = deserialize_Ddos_template_dns__nxdomain_cfg_json(data.get('nxdomain-cfg'))
	symtimeout_cfg = deserialize_Ddos_template_dns__symtimeout_cfg_json(data.get('symtimeout-cfg'))
	dns_request_rate_limit = deserialize_Ddos_template_dns__dns_request_rate_limit_json(data.get('dns-request-rate-limit'))
	result = Ddos_template_dns(name=name, dns_any_check=dns_any_check, dns_auth_cfg=dns_auth_cfg, fqdn_cfg=fqdn_cfg, nxdomain_cfg=nxdomain_cfg, symtimeout_cfg=symtimeout_cfg, dns_request_rate_limit=dns_request_rate_limit)
	return result

def deserialize_list_Ddos_template_dns_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_dns_json(item))
	return list(container)

def deserialize_Ddos_template_tcp__action_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	action_on_ack = data.get('action-on-ack')
	reset = data.get('reset')
	timeout = data.get('timeout')
	result = Ddos_template_tcp__action_cfg(action_on_ack=action_on_ack, reset=reset, timeout=timeout)
	return result

def deserialize_Ddos_template_tcp__tunnel_encap__ip_cfg__always_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4_addr = data.get('ipv4-addr')
	ipv6_addr = data.get('ipv6-addr')
	result = Ddos_template_tcp__tunnel_encap__ip_cfg__always(ipv4_addr=ipv4_addr, ipv6_addr=ipv6_addr)
	return result

def deserialize_Ddos_template_tcp__tunnel_encap__ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_encap = data.get('ip-encap')
	always = deserialize_Ddos_template_tcp__tunnel_encap__ip_cfg__always_json(data.get('always'))
	result = Ddos_template_tcp__tunnel_encap__ip_cfg(ip_encap=ip_encap, always=always)
	return result

def deserialize_Ddos_template_tcp__tunnel_encap__gre_cfg__gre_always_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	gre_ipv4 = data.get('gre-ipv4')
	key_ipv4 = data.get('key-ipv4')
	gre_ipv6 = data.get('gre-ipv6')
	key_ipv6 = data.get('key-ipv6')
	result = Ddos_template_tcp__tunnel_encap__gre_cfg__gre_always(gre_ipv4=gre_ipv4, key_ipv4=key_ipv4, gre_ipv6=gre_ipv6, key_ipv6=key_ipv6)
	return result

def deserialize_Ddos_template_tcp__tunnel_encap__gre_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	gre_encap = data.get('gre-encap')
	gre_always = deserialize_Ddos_template_tcp__tunnel_encap__gre_cfg__gre_always_json(data.get('gre-always'))
	result = Ddos_template_tcp__tunnel_encap__gre_cfg(gre_encap=gre_encap, gre_always=gre_always)
	return result

def deserialize_Ddos_template_tcp__tunnel_encap_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_cfg = deserialize_Ddos_template_tcp__tunnel_encap__ip_cfg_json(data.get('ip-cfg'))
	gre_cfg = deserialize_Ddos_template_tcp__tunnel_encap__gre_cfg_json(data.get('gre-cfg'))
	result = Ddos_template_tcp__tunnel_encap(ip_cfg=ip_cfg, gre_cfg=gre_cfg)
	return result

def deserialize_Ddos_template_tcp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	action_cfg = deserialize_Ddos_template_tcp__action_cfg_json(data.get('action-cfg'))
	age = data.get('age')
	concurrent = data.get('concurrent')
	syn_cookie = data.get('syn-cookie')
	black_list_out_of_seq = data.get('black-list-out-of-seq')
	black_list_retransmit = data.get('black-list-retransmit')
	black_list_zero_win = data.get('black-list-zero-win')
	disable_syn_auth = data.get('disable-syn-auth')
	over_conn_limit_action = data.get('over-conn-limit-action')
	over_conn_rate_action = data.get('over-conn-rate-action')
	tunnel_encap = deserialize_Ddos_template_tcp__tunnel_encap_json(data.get('tunnel-encap'))
	tunnel_rate_limit = data.get('tunnel-rate-limit')
	result = Ddos_template_tcp(name=name, action_cfg=action_cfg, age=age, concurrent=concurrent, syn_cookie=syn_cookie, black_list_out_of_seq=black_list_out_of_seq, black_list_retransmit=black_list_retransmit, black_list_zero_win=black_list_zero_win, disable_syn_auth=disable_syn_auth, over_conn_limit_action=over_conn_limit_action, over_conn_rate_action=over_conn_rate_action, tunnel_encap=tunnel_encap, tunnel_rate_limit=tunnel_rate_limit)
	return result

def deserialize_list_Ddos_template_tcp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_tcp_json(item))
	return list(container)

def deserialize_Ddos_template_udp__tunnel_encap__always_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4_addr = data.get('ipv4-addr')
	ipv6_addr = data.get('ipv6-addr')
	result = Ddos_template_udp__tunnel_encap__always(ipv4_addr=ipv4_addr, ipv6_addr=ipv6_addr)
	return result

def deserialize_Ddos_template_udp__tunnel_encap__gre_always_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	gre_ipv4 = data.get('gre-ipv4')
	key_ipv4 = data.get('key-ipv4')
	gre_ipv6 = data.get('gre-ipv6')
	key_ipv6 = data.get('key-ipv6')
	result = Ddos_template_udp__tunnel_encap__gre_always(gre_ipv4=gre_ipv4, key_ipv4=key_ipv4, gre_ipv6=gre_ipv6, key_ipv6=key_ipv6)
	return result

def deserialize_Ddos_template_udp__tunnel_encap_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_encap = data.get('ip-encap')
	always = deserialize_Ddos_template_udp__tunnel_encap__always_json(data.get('always'))
	gre_encap = data.get('gre-encap')
	gre_always = deserialize_Ddos_template_udp__tunnel_encap__gre_always_json(data.get('gre-always'))
	result = Ddos_template_udp__tunnel_encap(ip_encap=ip_encap, always=always, gre_encap=gre_encap, gre_always=gre_always)
	return result

def deserialize_Ddos_template_udp__spoof_detect_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	spoof_detect = data.get('spoof-detect')
	spoof_detect_retry_timeout = data.get('spoof-detect-retry-timeout')
	result = Ddos_template_udp__spoof_detect_cfg(spoof_detect=spoof_detect, spoof_detect_retry_timeout=spoof_detect_retry_timeout)
	return result

def deserialize_Ddos_template_udp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	age = data.get('age')
	tunnel_encap = deserialize_Ddos_template_udp__tunnel_encap_json(data.get('tunnel-encap'))
	tunnel_rate_limit = data.get('tunnel-rate-limit')
	spoof_detect_cfg = deserialize_Ddos_template_udp__spoof_detect_cfg_json(data.get('spoof-detect-cfg'))
	max_payload_size = data.get('max-payload-size')
	min_payload_size = data.get('min-payload-size')
	result = Ddos_template_udp(name=name, age=age, tunnel_encap=tunnel_encap, tunnel_rate_limit=tunnel_rate_limit, spoof_detect_cfg=spoof_detect_cfg, max_payload_size=max_payload_size, min_payload_size=min_payload_size)
	return result

def deserialize_list_Ddos_template_udp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_udp_json(item))
	return list(container)

def deserialize_Template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ssl_l4list = deserialize_list_Ddos_template_ssl_l4_json(data.get('ssl-l4List'))
	httplist = deserialize_list_Ddos_template_http_json(data.get('httpList'))
	dnslist = deserialize_list_Ddos_template_dns_json(data.get('dnsList'))
	tcplist = deserialize_list_Ddos_template_tcp_json(data.get('tcpList'))
	udplist = deserialize_list_Ddos_template_udp_json(data.get('udpList'))
	result = Template(ssl_l4list=ssl_l4list, httplist=httplist, dnslist=dnslist, tcplist=tcplist, udplist=udplist)
	return result

class Template(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ssl_l4list=None, httplist=None, dnslist=None, tcplist=None, udplist=None):
		self.ssl_l4list = ssl_l4list
		self.httplist = httplist
		self.dnslist = dnslist
		self.tcplist = tcplist
		self.udplist = udplist

	def __str__(self):
		return ""

class Ddos_template_ssl_l4(AxapiObject):
	__metaclass__ = StructMeta 
	ssl_l4_tmpl_name=SizedString(1, 63)
	action = Enum(['drop', 'reset'])
	disable=PosRangedInteger(0, 1)
	renegotiation=PosRangedInteger(0, 7)
	request_rate_limit=PosRangedInteger(1, 16000000)
	def __init__(self, ssl_l4_tmpl_name, action=None, disable=None, renegotiation=None, request_rate_limit=None):
		self.ssl_l4_tmpl_name = ssl_l4_tmpl_name
		self.action = action
		self.disable = disable
		self.renegotiation = renegotiation
		self.request_rate_limit = request_rate_limit

	def __str__(self):
		return str(self.ssl_l4_tmpl_name)

class Ddos_template_http__mss_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	mss_timeout=PosRangedInteger(0, 1)
	mss_percent=PosRangedInteger(1, 100)
	number_packets=PosRangedInteger(1, 31)
	def __init__(self, mss_timeout=None, mss_percent=None, number_packets=None):
		self.mss_timeout = mss_timeout
		self.mss_percent = mss_percent
		self.number_packets = number_packets

	def __str__(self):
		return ""

class Ddos_template_http__challenge_method(AxapiObject):
	__metaclass__ = StructMeta 
	method_302_redirect=PosRangedInteger(0, 1)
	method_javascript=PosRangedInteger(0, 1)
	def __init__(self, method_302_redirect=None, method_javascript=None):
		self.method_302_redirect = method_302_redirect
		self.method_javascript = method_javascript

	def __str__(self):
		return ""

class Ddos_template_http__malformed_http(AxapiObject):
	__metaclass__ = StructMeta 
	malformed_http_enabled=PosRangedInteger(0, 1)
	malformed_http_max_line_size=PosRangedInteger(1, 16128)
	malformed_http_max_num_headers=PosRangedInteger(1, 90)
	malformed_http_max_req_line_size=PosRangedInteger(1, 16128)
	malformed_http_max_header_name_size=PosRangedInteger(1, 64)
	malformed_http_max_content_length=PosRangedInteger(1, 2147483647)
	malformed_http_bad_chunk_mon_enabled=PosRangedInteger(0, 1)
	def __init__(self, malformed_http_enabled=None, malformed_http_max_line_size=None, malformed_http_max_num_headers=None, malformed_http_max_req_line_size=None, malformed_http_max_header_name_size=None, malformed_http_max_content_length=None, malformed_http_bad_chunk_mon_enabled=None):
		self.malformed_http_enabled = malformed_http_enabled
		self.malformed_http_max_line_size = malformed_http_max_line_size
		self.malformed_http_max_num_headers = malformed_http_max_num_headers
		self.malformed_http_max_req_line_size = malformed_http_max_req_line_size
		self.malformed_http_max_header_name_size = malformed_http_max_header_name_size
		self.malformed_http_max_content_length = malformed_http_max_content_length
		self.malformed_http_bad_chunk_mon_enabled = malformed_http_bad_chunk_mon_enabled

	def __str__(self):
		return ""

class Ddos_template_http__use_hdr_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	use_hdr_ip_as_source=PosRangedInteger(0, 1)
	l7_hdr_name=SizedString(1, 63)
	def __init__(self, use_hdr_ip_as_source=None, l7_hdr_name=None):
		self.use_hdr_ip_as_source = use_hdr_ip_as_source
		self.l7_hdr_name = l7_hdr_name

	def __str__(self):
		return ""

class Ddos_template_http__request_header(AxapiObject):
	__metaclass__ = StructMeta 
	timeout=PosRangedInteger(1, 63)
	def __init__(self, timeout=None):
		self.timeout = timeout

	def __str__(self):
		return ""

class Ddos_template_http__request_rate_limit(AxapiObject):
	__metaclass__ = StructMeta 
	request_rate=PosRangedInteger(1, 16000000)
	def __init__(self, request_rate=None, uri=None):
		self.request_rate = request_rate
		self.uri = uri

	def __str__(self):
		return ""

class Ddos_template_http__response_rate_limit(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, obj_size=None):
		self.obj_size = obj_size

	def __str__(self):
		return ""

class Ddos_template_http__slow_read_drop(AxapiObject):
	__metaclass__ = StructMeta 
	min_window_size=PosRangedInteger(1, 65535)
	min_window_count=PosRangedInteger(1, 31)
	def __init__(self, min_window_size=None, min_window_count=None):
		self.min_window_size = min_window_size
		self.min_window_count = min_window_count

	def __str__(self):
		return ""

class Ddos_template_http(AxapiObject):
	__metaclass__ = StructMeta 
	http_tmpl_name=SizedString(1, 63)
	action = Enum(['drop', 'reset'])
	disable=PosRangedInteger(0, 1)
	challenge_cookie_name=SizedString(1, 63)
	challenge_keep_cookie=PosRangedInteger(0, 1)
	challenge_interval=PosRangedInteger(1, 31)
	post_rate_limit=PosRangedInteger(1, 16000000)
	idle_timeout=PosRangedInteger(1, 63)
	ignore_zero_payload=PosRangedInteger(0, 1)
	def __init__(self, http_tmpl_name, action=None, disable=None, mss_cfg=None, challenge_method=None, challenge_cookie_name=None, challenge_keep_cookie=None, challenge_interval=None, malformed_http=None, use_hdr_ip_cfg=None, request_header=None, post_rate_limit=None, request_rate_limit=None, response_rate_limit=None, slow_read_drop=None, idle_timeout=None, ignore_zero_payload=None, referer_filter=None, agent_filter=None):
		self.http_tmpl_name = http_tmpl_name
		self.action = action
		self.disable = disable
		self.mss_cfg = mss_cfg
		self.challenge_method = challenge_method
		self.challenge_cookie_name = challenge_cookie_name
		self.challenge_keep_cookie = challenge_keep_cookie
		self.challenge_interval = challenge_interval
		self.malformed_http = malformed_http
		self.use_hdr_ip_cfg = use_hdr_ip_cfg
		self.request_header = request_header
		self.post_rate_limit = post_rate_limit
		self.request_rate_limit = request_rate_limit
		self.response_rate_limit = response_rate_limit
		self.slow_read_drop = slow_read_drop
		self.idle_timeout = idle_timeout
		self.ignore_zero_payload = ignore_zero_payload
		self.referer_filter = referer_filter
		self.agent_filter = agent_filter

	def __str__(self):
		return str(self.http_tmpl_name)

class Ddos_template_uri__equal_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	url_equals=SizedString(1, 127)
	url_rate=PosRangedInteger(1, 16000000)
	def __init__(self, url_equals=None, url_rate=None):
		self.url_equals = url_equals
		self.url_rate = url_rate

	def __str__(self):
		return ""

class Ddos_template_uri__contains_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	url_contains=SizedString(1, 127)
	url_rate=PosRangedInteger(1, 16000000)
	def __init__(self, url_contains=None, url_rate=None):
		self.url_contains = url_contains
		self.url_rate = url_rate

	def __str__(self):
		return ""

class Ddos_template_uri__starts_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	url_starts_with=SizedString(1, 127)
	url_rate=PosRangedInteger(1, 16000000)
	def __init__(self, url_starts_with=None, url_rate=None):
		self.url_starts_with = url_starts_with
		self.url_rate = url_rate

	def __str__(self):
		return ""

class Ddos_template_uri__ends_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	url_ends_with=SizedString(1, 127)
	url_rate=PosRangedInteger(1, 16000000)
	def __init__(self, url_ends_with=None, url_rate=None):
		self.url_ends_with = url_ends_with
		self.url_rate = url_rate

	def __str__(self):
		return ""

class Ddos_template_uri(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, equal_cfg=None, contains_cfg=None, starts_cfg=None, ends_cfg=None):
		self.equal_cfg = equal_cfg
		self.contains_cfg = contains_cfg
		self.starts_cfg = starts_cfg
		self.ends_cfg = ends_cfg

	def __str__(self):
		return ""

class Ddos_template_obj_size__less_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	obj_less=PosRangedInteger(1, 16000000)
	obj_rate=PosRangedInteger(1, 16000000)
	def __init__(self, obj_less=None, obj_rate=None):
		self.obj_less = obj_less
		self.obj_rate = obj_rate

	def __str__(self):
		return ""

class Ddos_template_obj_size__greater_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	obj_greater=PosRangedInteger(1, 16000000)
	obj_rate=PosRangedInteger(1, 16000000)
	def __init__(self, obj_greater=None, obj_rate=None):
		self.obj_greater = obj_greater
		self.obj_rate = obj_rate

	def __str__(self):
		return ""

class Ddos_template_obj_size__between_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	obj_between1=PosRangedInteger(1, 16000000)
	obj_between2=PosRangedInteger(1, 16000000)
	obj_rate=PosRangedInteger(1, 16000000)
	def __init__(self, obj_between1=None, obj_between2=None, obj_rate=None):
		self.obj_between1 = obj_between1
		self.obj_between2 = obj_between2
		self.obj_rate = obj_rate

	def __str__(self):
		return ""

class Ddos_template_obj_size(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, less_cfg=None, greater_cfg=None, between_cfg=None):
		self.less_cfg = less_cfg
		self.greater_cfg = greater_cfg
		self.between_cfg = between_cfg

	def __str__(self):
		return ""

class Ddos_template_referer_filter(AxapiObject):
	__metaclass__ = StructMeta 
	ref_filter_blacklist=PosRangedInteger(0, 1)
	referer_equals=SizedString(1, 63)
	referer_contains=SizedString(1, 63)
	referer_starts_with=SizedString(1, 63)
	referer_ends_with=SizedString(1, 63)
	def __init__(self, ref_filter_blacklist=None, referer_equals=None, referer_contains=None, referer_starts_with=None, referer_ends_with=None):
		self.ref_filter_blacklist = ref_filter_blacklist
		self.referer_equals = referer_equals
		self.referer_contains = referer_contains
		self.referer_starts_with = referer_starts_with
		self.referer_ends_with = referer_ends_with

	def __str__(self):
		return ""

class Ddos_template_agent_filter(AxapiObject):
	__metaclass__ = StructMeta 
	agent_filter_blacklist=PosRangedInteger(0, 1)
	agent_equals=SizedString(1, 63)
	agent_contains=SizedString(1, 63)
	agent_starts_with=SizedString(1, 63)
	agent_ends_with=SizedString(1, 63)
	def __init__(self, agent_filter_blacklist=None, agent_equals=None, agent_contains=None, agent_starts_with=None, agent_ends_with=None):
		self.agent_filter_blacklist = agent_filter_blacklist
		self.agent_equals = agent_equals
		self.agent_contains = agent_contains
		self.agent_starts_with = agent_starts_with
		self.agent_ends_with = agent_ends_with

	def __str__(self):
		return ""

class Ddos_template_dns__dns_auth_cfg__udp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	udp=PosRangedInteger(0, 1)
	udp_timeout=PosRangedInteger(1, 16)
	def __init__(self, udp=None, udp_timeout=None):
		self.udp = udp
		self.udp_timeout = udp_timeout

	def __str__(self):
		return ""

class Ddos_template_dns__dns_auth_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dns_auth=PosRangedInteger(0, 1)
	force_tcp=PosRangedInteger(0, 1)
	def __init__(self, dns_auth=None, force_tcp=None, udp_cfg=None):
		self.dns_auth = dns_auth
		self.force_tcp = force_tcp
		self.udp_cfg = udp_cfg

	def __str__(self):
		return ""

class Ddos_template_dns__fqdn_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dns_fqdn_rate_limit=PosRangedInteger(0, 1)
	dns_fqdn_rate=PosRangedInteger(1, 255)
	by = Enum(['domain-name', 'src-ip', 'both'])
	def __init__(self, dns_fqdn_rate_limit=None, dns_fqdn_rate=None, by=None):
		self.dns_fqdn_rate_limit = dns_fqdn_rate_limit
		self.dns_fqdn_rate = dns_fqdn_rate
		self.by = by

	def __str__(self):
		return ""

class Ddos_template_dns__nxdomain_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dns_nxdomain_rate_limit=PosRangedInteger(0, 1)
	dns_nxdomain_rate=PosRangedInteger(1, 16000000)
	action = Enum(['drop', 'black-list'])
	def __init__(self, dns_nxdomain_rate_limit=None, dns_nxdomain_rate=None, action=None):
		self.dns_nxdomain_rate_limit = dns_nxdomain_rate_limit
		self.dns_nxdomain_rate = dns_nxdomain_rate
		self.action = action

	def __str__(self):
		return ""

class Ddos_template_dns__symtimeout_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	sym_timeout=PosRangedInteger(0, 1)
	sym_timeout_value=PosRangedInteger(1, 31)
	def __init__(self, sym_timeout=None, sym_timeout_value=None):
		self.sym_timeout = sym_timeout
		self.sym_timeout_value = sym_timeout_value

	def __str__(self):
		return ""

class Ddos_template_dns__dns_request_rate_limit__type__a_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	a=PosRangedInteger(0, 1)
	dns_a_rate=PosRangedInteger(1, 16000000)
	def __init__(self, a=None, dns_a_rate=None):
		self.a = a
		self.dns_a_rate = dns_a_rate

	def __str__(self):
		return ""

class Ddos_template_dns__dns_request_rate_limit__type__aaaa_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	aaaa=PosRangedInteger(0, 1)
	dns_aaaa_rate=PosRangedInteger(1, 16000000)
	def __init__(self, aaaa=None, dns_aaaa_rate=None):
		self.aaaa = aaaa
		self.dns_aaaa_rate = dns_aaaa_rate

	def __str__(self):
		return ""

class Ddos_template_dns__dns_request_rate_limit__type__cname_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	cname=PosRangedInteger(0, 1)
	dns_cname_rate=PosRangedInteger(1, 16000000)
	def __init__(self, cname=None, dns_cname_rate=None):
		self.cname = cname
		self.dns_cname_rate = dns_cname_rate

	def __str__(self):
		return ""

class Ddos_template_dns__dns_request_rate_limit__type__mx_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	mx=PosRangedInteger(0, 1)
	dns_mx_rate=PosRangedInteger(1, 16000000)
	def __init__(self, mx=None, dns_mx_rate=None):
		self.mx = mx
		self.dns_mx_rate = dns_mx_rate

	def __str__(self):
		return ""

class Ddos_template_dns__dns_request_rate_limit__type__ns_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ns=PosRangedInteger(0, 1)
	dns_ns_rate=PosRangedInteger(1, 16000000)
	def __init__(self, ns=None, dns_ns_rate=None):
		self.ns = ns
		self.dns_ns_rate = dns_ns_rate

	def __str__(self):
		return ""

class Ddos_template_dns__dns_request_rate_limit__type__srv_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	srv=PosRangedInteger(0, 1)
	dns_srv_rate=PosRangedInteger(1, 16000000)
	def __init__(self, srv=None, dns_srv_rate=None):
		self.srv = srv
		self.dns_srv_rate = dns_srv_rate

	def __str__(self):
		return ""

class Ddos_template_dns__dns_request_rate_limit__type(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, a_cfg=None, aaaa_cfg=None, cname_cfg=None, mx_cfg=None, ns_cfg=None, srv_cfg=None, dns_type_cfg=None):
		self.a_cfg = a_cfg
		self.aaaa_cfg = aaaa_cfg
		self.cname_cfg = cname_cfg
		self.mx_cfg = mx_cfg
		self.ns_cfg = ns_cfg
		self.srv_cfg = srv_cfg
		self.dns_type_cfg = dns_type_cfg

	def __str__(self):
		return ""

class Ddos_template_dns__dns_request_rate_limit(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, type=None):
		self.type = type

	def __str__(self):
		return ""

class Ddos_template_dns(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	dns_any_check=PosRangedInteger(0, 1)
	def __init__(self, name, dns_any_check=None, dns_auth_cfg=None, fqdn_cfg=None, nxdomain_cfg=None, symtimeout_cfg=None, dns_request_rate_limit=None):
		self.name = name
		self.dns_any_check = dns_any_check
		self.dns_auth_cfg = dns_auth_cfg
		self.fqdn_cfg = fqdn_cfg
		self.nxdomain_cfg = nxdomain_cfg
		self.symtimeout_cfg = symtimeout_cfg
		self.dns_request_rate_limit = dns_request_rate_limit

	def __str__(self):
		return str(self.name)

class Ddos_template_dns_type_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dns_request_type=PosRangedInteger(1, 65535)
	dns_request_type_rate=PosRangedInteger(1, 16000000)
	def __init__(self, dns_request_type=None, dns_request_type_rate=None):
		self.dns_request_type = dns_request_type
		self.dns_request_type_rate = dns_request_type_rate

	def __str__(self):
		return ""

class Ddos_template_tcp__action_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	action_on_ack=PosRangedInteger(0, 1)
	reset=PosRangedInteger(0, 1)
	timeout=PosRangedInteger(1, 31)
	def __init__(self, action_on_ack=None, reset=None, timeout=None):
		self.action_on_ack = action_on_ack
		self.reset = reset
		self.timeout = timeout

	def __str__(self):
		return ""

class Ddos_template_tcp__tunnel_encap__ip_cfg__always(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6_addr=SizedString(1, 255)
	def __init__(self, ipv4_addr=None, ipv6_addr=None):
		self.ipv4_addr = ipv4_addr
		self.ipv6_addr = ipv6_addr

	def __str__(self):
		return ""

class Ddos_template_tcp__tunnel_encap__ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip_encap=PosRangedInteger(0, 1)
	def __init__(self, ip_encap=None, always=None):
		self.ip_encap = ip_encap
		self.always = always

	def __str__(self):
		return ""

class Ddos_template_tcp__tunnel_encap__gre_cfg__gre_always(AxapiObject):
	__metaclass__ = StructMeta 
	gre_ipv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	key_ipv4=SizedString(1, 8)
	gre_ipv6=SizedString(1, 255)
	key_ipv6=SizedString(1, 8)
	def __init__(self, gre_ipv4=None, key_ipv4=None, gre_ipv6=None, key_ipv6=None):
		self.gre_ipv4 = gre_ipv4
		self.key_ipv4 = key_ipv4
		self.gre_ipv6 = gre_ipv6
		self.key_ipv6 = key_ipv6

	def __str__(self):
		return ""

class Ddos_template_tcp__tunnel_encap__gre_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	gre_encap=PosRangedInteger(0, 1)
	def __init__(self, gre_encap=None, gre_always=None):
		self.gre_encap = gre_encap
		self.gre_always = gre_always

	def __str__(self):
		return ""

class Ddos_template_tcp__tunnel_encap(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ip_cfg=None, gre_cfg=None):
		self.ip_cfg = ip_cfg
		self.gre_cfg = gre_cfg

	def __str__(self):
		return ""

class Ddos_template_tcp(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	age=PosRangedInteger(1, 63)
	concurrent=PosRangedInteger(0, 1)
	syn_cookie=PosRangedInteger(0, 1)
	black_list_out_of_seq=PosRangedInteger(1, 128)
	black_list_retransmit=PosRangedInteger(1, 128)
	black_list_zero_win=PosRangedInteger(1, 128)
	disable_syn_auth=PosRangedInteger(0, 1)
	over_conn_limit_action = Enum(['authentication ', 'syn-cookie'])
	over_conn_rate_action = Enum(['authentication', 'syn-cookie'])
	tunnel_rate_limit=PosRangedInteger(0, 1)
	def __init__(self, name, action_cfg=None, age=None, concurrent=None, syn_cookie=None, black_list_out_of_seq=None, black_list_retransmit=None, black_list_zero_win=None, disable_syn_auth=None, over_conn_limit_action=None, over_conn_rate_action=None, tunnel_encap=None, tunnel_rate_limit=None):
		self.name = name
		self.action_cfg = action_cfg
		self.age = age
		self.concurrent = concurrent
		self.syn_cookie = syn_cookie
		self.black_list_out_of_seq = black_list_out_of_seq
		self.black_list_retransmit = black_list_retransmit
		self.black_list_zero_win = black_list_zero_win
		self.disable_syn_auth = disable_syn_auth
		self.over_conn_limit_action = over_conn_limit_action
		self.over_conn_rate_action = over_conn_rate_action
		self.tunnel_encap = tunnel_encap
		self.tunnel_rate_limit = tunnel_rate_limit

	def __str__(self):
		return str(self.name)

class Ddos_template_udp__tunnel_encap__always(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6_addr=SizedString(1, 255)
	def __init__(self, ipv4_addr=None, ipv6_addr=None):
		self.ipv4_addr = ipv4_addr
		self.ipv6_addr = ipv6_addr

	def __str__(self):
		return ""

class Ddos_template_udp__tunnel_encap__gre_always(AxapiObject):
	__metaclass__ = StructMeta 
	gre_ipv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	key_ipv4=SizedString(1, 8)
	gre_ipv6=SizedString(1, 255)
	key_ipv6=SizedString(1, 8)
	def __init__(self, gre_ipv4=None, key_ipv4=None, gre_ipv6=None, key_ipv6=None):
		self.gre_ipv4 = gre_ipv4
		self.key_ipv4 = key_ipv4
		self.gre_ipv6 = gre_ipv6
		self.key_ipv6 = key_ipv6

	def __str__(self):
		return ""

class Ddos_template_udp__tunnel_encap(AxapiObject):
	__metaclass__ = StructMeta 
	ip_encap=PosRangedInteger(0, 1)
	gre_encap=PosRangedInteger(0, 1)
	def __init__(self, ip_encap=None, always=None, gre_encap=None, gre_always=None):
		self.ip_encap = ip_encap
		self.always = always
		self.gre_encap = gre_encap
		self.gre_always = gre_always

	def __str__(self):
		return ""

class Ddos_template_udp__spoof_detect_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	spoof_detect=PosRangedInteger(0, 1)
	spoof_detect_retry_timeout=PosRangedInteger(1, 31)
	def __init__(self, spoof_detect=None, spoof_detect_retry_timeout=None):
		self.spoof_detect = spoof_detect
		self.spoof_detect_retry_timeout = spoof_detect_retry_timeout

	def __str__(self):
		return ""

class Ddos_template_udp(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	age=PosRangedInteger(1, 63)
	tunnel_rate_limit=PosRangedInteger(0, 1)
	max_payload_size=PosRangedInteger(1, 1470)
	min_payload_size=PosRangedInteger(1, 1470)
	def __init__(self, name, age=None, tunnel_encap=None, tunnel_rate_limit=None, spoof_detect_cfg=None, max_payload_size=None, min_payload_size=None):
		self.name = name
		self.age = age
		self.tunnel_encap = tunnel_encap
		self.tunnel_rate_limit = tunnel_rate_limit
		self.spoof_detect_cfg = spoof_detect_cfg
		self.max_payload_size = max_payload_size
		self.min_payload_size = min_payload_size

	def __str__(self):
		return str(self.name)

class DdosTemplateClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosTemplate(self):
		"""
		Retrieve the template identified by the specified identifier
		
		Returns:
			An instance of the Template class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified template does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('template')
		return deserialize_Template_json(payload)

