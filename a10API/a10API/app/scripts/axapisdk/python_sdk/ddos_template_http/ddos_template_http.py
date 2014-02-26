########################################################################################################################
# File name: ddos_template_http.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/template/http',
]

def deserialize_Http__mss_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	mss_timeout = data.get('mss-timeout')
	mss_percent = data.get('mss-percent')
	number_packets = data.get('number-packets')
	result = Http__mss_cfg(mss_timeout=mss_timeout, mss_percent=mss_percent, number_packets=number_packets)
	return result

def deserialize_Http__challenge_method_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	method_302_redirect = data.get('method-302-redirect')
	method_javascript = data.get('method-javascript')
	result = Http__challenge_method(method_302_redirect=method_302_redirect, method_javascript=method_javascript)
	return result

def deserialize_Http__malformed_http_json(obj):
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
	result = Http__malformed_http(malformed_http_enabled=malformed_http_enabled, malformed_http_max_line_size=malformed_http_max_line_size, malformed_http_max_num_headers=malformed_http_max_num_headers, malformed_http_max_req_line_size=malformed_http_max_req_line_size, malformed_http_max_header_name_size=malformed_http_max_header_name_size, malformed_http_max_content_length=malformed_http_max_content_length, malformed_http_bad_chunk_mon_enabled=malformed_http_bad_chunk_mon_enabled)
	return result

def deserialize_Http__use_hdr_ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	use_hdr_ip_as_source = data.get('use-hdr-ip-as-source')
	l7_hdr_name = data.get('l7-hdr-name')
	result = Http__use_hdr_ip_cfg(use_hdr_ip_as_source=use_hdr_ip_as_source, l7_hdr_name=l7_hdr_name)
	return result

def deserialize_Http__request_header_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timeout = data.get('timeout')
	result = Http__request_header(timeout=timeout)
	return result

def deserialize_Ddos_template_http_uri__equal_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	url_equals = data.get('url-equals')
	url_rate = data.get('url-rate')
	result = Ddos_template_http_uri__equal_cfg(url_equals=url_equals, url_rate=url_rate)
	return result

def deserialize_Ddos_template_http_uri__contains_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	url_contains = data.get('url-contains')
	url_rate = data.get('url-rate')
	result = Ddos_template_http_uri__contains_cfg(url_contains=url_contains, url_rate=url_rate)
	return result

def deserialize_Ddos_template_http_uri__starts_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	url_starts_with = data.get('url-starts-with')
	url_rate = data.get('url-rate')
	result = Ddos_template_http_uri__starts_cfg(url_starts_with=url_starts_with, url_rate=url_rate)
	return result

def deserialize_Ddos_template_http_uri__ends_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	url_ends_with = data.get('url-ends-with')
	url_rate = data.get('url-rate')
	result = Ddos_template_http_uri__ends_cfg(url_ends_with=url_ends_with, url_rate=url_rate)
	return result

def deserialize_Ddos_template_http_uri_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	equal_cfg = deserialize_Ddos_template_http_uri__equal_cfg_json(data.get('equal-cfg'))
	contains_cfg = deserialize_Ddos_template_http_uri__contains_cfg_json(data.get('contains-cfg'))
	starts_cfg = deserialize_Ddos_template_http_uri__starts_cfg_json(data.get('starts-cfg'))
	ends_cfg = deserialize_Ddos_template_http_uri__ends_cfg_json(data.get('ends-cfg'))
	result = Ddos_template_http_uri(equal_cfg=equal_cfg, contains_cfg=contains_cfg, starts_cfg=starts_cfg, ends_cfg=ends_cfg)
	return result

def deserialize_list_Ddos_template_http_uri_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_http_uri_json(item))
	return list(container)

def deserialize_Http__request_rate_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	request_rate = data.get('request-rate')
	uri = deserialize_list_Ddos_template_http_uri_json(data.get('uri'))
	result = Http__request_rate_limit(request_rate=request_rate, uri=uri)
	return result

def deserialize_Ddos_template_http_obj_size__less_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	obj_less = data.get('obj-less')
	obj_rate = data.get('obj-rate')
	result = Ddos_template_http_obj_size__less_cfg(obj_less=obj_less, obj_rate=obj_rate)
	return result

def deserialize_Ddos_template_http_obj_size__greater_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	obj_greater = data.get('obj-greater')
	obj_rate = data.get('obj-rate')
	result = Ddos_template_http_obj_size__greater_cfg(obj_greater=obj_greater, obj_rate=obj_rate)
	return result

def deserialize_Ddos_template_http_obj_size__between_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	obj_between1 = data.get('obj-between1')
	obj_between2 = data.get('obj-between2')
	obj_rate = data.get('obj-rate')
	result = Ddos_template_http_obj_size__between_cfg(obj_between1=obj_between1, obj_between2=obj_between2, obj_rate=obj_rate)
	return result

def deserialize_Ddos_template_http_obj_size_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	less_cfg = deserialize_Ddos_template_http_obj_size__less_cfg_json(data.get('less-cfg'))
	greater_cfg = deserialize_Ddos_template_http_obj_size__greater_cfg_json(data.get('greater-cfg'))
	between_cfg = deserialize_Ddos_template_http_obj_size__between_cfg_json(data.get('between-cfg'))
	result = Ddos_template_http_obj_size(less_cfg=less_cfg, greater_cfg=greater_cfg, between_cfg=between_cfg)
	return result

def deserialize_list_Ddos_template_http_obj_size_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_http_obj_size_json(item))
	return list(container)

def deserialize_Http__response_rate_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	obj_size = deserialize_list_Ddos_template_http_obj_size_json(data.get('obj-size'))
	result = Http__response_rate_limit(obj_size=obj_size)
	return result

def deserialize_Http__slow_read_drop_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	min_window_size = data.get('min-window-size')
	min_window_count = data.get('min-window-count')
	result = Http__slow_read_drop(min_window_size=min_window_size, min_window_count=min_window_count)
	return result

def deserialize_Ddos_template_http_referer_filter_json(obj):
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
	result = Ddos_template_http_referer_filter(ref_filter_blacklist=ref_filter_blacklist, referer_equals=referer_equals, referer_contains=referer_contains, referer_starts_with=referer_starts_with, referer_ends_with=referer_ends_with)
	return result

def deserialize_list_Ddos_template_http_referer_filter_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_http_referer_filter_json(item))
	return list(container)

def deserialize_Ddos_template_http_agent_filter_json(obj):
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
	result = Ddos_template_http_agent_filter(agent_filter_blacklist=agent_filter_blacklist, agent_equals=agent_equals, agent_contains=agent_contains, agent_starts_with=agent_starts_with, agent_ends_with=agent_ends_with)
	return result

def deserialize_list_Ddos_template_http_agent_filter_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_http_agent_filter_json(item))
	return list(container)

def deserialize_Http_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	http_tmpl_name = data.get('http-tmpl-name')
	action = data.get('action')
	disable = data.get('disable')
	mss_cfg = deserialize_Http__mss_cfg_json(data.get('mss-cfg'))
	challenge_method = deserialize_Http__challenge_method_json(data.get('challenge-method'))
	challenge_cookie_name = data.get('challenge-cookie-name')
	challenge_keep_cookie = data.get('challenge-keep-cookie')
	challenge_interval = data.get('challenge-interval')
	malformed_http = deserialize_Http__malformed_http_json(data.get('malformed-http'))
	use_hdr_ip_cfg = deserialize_Http__use_hdr_ip_cfg_json(data.get('use-hdr-ip-cfg'))
	request_header = deserialize_Http__request_header_json(data.get('request-header'))
	post_rate_limit = data.get('post-rate-limit')
	request_rate_limit = deserialize_Http__request_rate_limit_json(data.get('request-rate-limit'))
	response_rate_limit = deserialize_Http__response_rate_limit_json(data.get('response-rate-limit'))
	slow_read_drop = deserialize_Http__slow_read_drop_json(data.get('slow-read-drop'))
	idle_timeout = data.get('idle-timeout')
	ignore_zero_payload = data.get('ignore-zero-payload')
	referer_filter = deserialize_list_Ddos_template_http_referer_filter_json(data.get('referer-filter'))
	agent_filter = deserialize_list_Ddos_template_http_agent_filter_json(data.get('agent-filter'))
	result = Http(http_tmpl_name=http_tmpl_name, action=action, disable=disable, mss_cfg=mss_cfg, challenge_method=challenge_method, challenge_cookie_name=challenge_cookie_name, challenge_keep_cookie=challenge_keep_cookie, challenge_interval=challenge_interval, malformed_http=malformed_http, use_hdr_ip_cfg=use_hdr_ip_cfg, request_header=request_header, post_rate_limit=post_rate_limit, request_rate_limit=request_rate_limit, response_rate_limit=response_rate_limit, slow_read_drop=slow_read_drop, idle_timeout=idle_timeout, ignore_zero_payload=ignore_zero_payload, referer_filter=referer_filter, agent_filter=agent_filter)
	return result

def serialize_Http__mss_cfg_json(obj):
	output = OrderedDict()
	if obj.mss_timeout is not None:
		output['mss-timeout'] = obj.mss_timeout
	if obj.mss_percent is not None:
		output['mss-percent'] = obj.mss_percent
	if obj.number_packets is not None:
		output['number-packets'] = obj.number_packets
	return output

def serialize_Http__challenge_method_json(obj):
	output = OrderedDict()
	if obj.method_302_redirect is not None:
		output['method-302-redirect'] = obj.method_302_redirect
	if obj.method_javascript is not None:
		output['method-javascript'] = obj.method_javascript
	return output

def serialize_Http__malformed_http_json(obj):
	output = OrderedDict()
	if obj.malformed_http_enabled is not None:
		output['malformed-http-enabled'] = obj.malformed_http_enabled
	if obj.malformed_http_max_line_size is not None:
		output['malformed-http-max-line-size'] = obj.malformed_http_max_line_size
	if obj.malformed_http_max_num_headers is not None:
		output['malformed-http-max-num-headers'] = obj.malformed_http_max_num_headers
	if obj.malformed_http_max_req_line_size is not None:
		output['malformed-http-max-req-line-size'] = obj.malformed_http_max_req_line_size
	if obj.malformed_http_max_header_name_size is not None:
		output['malformed-http-max-header-name-size'] = obj.malformed_http_max_header_name_size
	if obj.malformed_http_max_content_length is not None:
		output['malformed-http-max-content-length'] = obj.malformed_http_max_content_length
	if obj.malformed_http_bad_chunk_mon_enabled is not None:
		output['malformed-http-bad-chunk-mon-enabled'] = obj.malformed_http_bad_chunk_mon_enabled
	return output

def serialize_Http__use_hdr_ip_cfg_json(obj):
	output = OrderedDict()
	if obj.use_hdr_ip_as_source is not None:
		output['use-hdr-ip-as-source'] = obj.use_hdr_ip_as_source
	if obj.l7_hdr_name is not None:
		output['l7-hdr-name'] = obj.l7_hdr_name
	return output

def serialize_Http__request_header_json(obj):
	output = OrderedDict()
	if obj.timeout is not None:
		output['timeout'] = obj.timeout
	return output

def serialize_Ddos_template_http_uri__equal_cfg_json(obj):
	output = OrderedDict()
	if obj.url_equals is not None:
		output['url-equals'] = obj.url_equals
	if obj.url_rate is not None:
		output['url-rate'] = obj.url_rate
	return output

def serialize_Ddos_template_http_uri__contains_cfg_json(obj):
	output = OrderedDict()
	if obj.url_contains is not None:
		output['url-contains'] = obj.url_contains
	if obj.url_rate is not None:
		output['url-rate'] = obj.url_rate
	return output

def serialize_Ddos_template_http_uri__starts_cfg_json(obj):
	output = OrderedDict()
	if obj.url_starts_with is not None:
		output['url-starts-with'] = obj.url_starts_with
	if obj.url_rate is not None:
		output['url-rate'] = obj.url_rate
	return output

def serialize_Ddos_template_http_uri__ends_cfg_json(obj):
	output = OrderedDict()
	if obj.url_ends_with is not None:
		output['url-ends-with'] = obj.url_ends_with
	if obj.url_rate is not None:
		output['url-rate'] = obj.url_rate
	return output

def serialize_Ddos_template_http_uri_json(obj):
	output = OrderedDict()
	if obj.equal_cfg is not None:
		output['equal-cfg'] = serialize_Ddos_template_http_uri__equal_cfg_json(obj.equal_cfg)
	if obj.contains_cfg is not None:
		output['contains-cfg'] = serialize_Ddos_template_http_uri__contains_cfg_json(obj.contains_cfg)
	if obj.starts_cfg is not None:
		output['starts-cfg'] = serialize_Ddos_template_http_uri__starts_cfg_json(obj.starts_cfg)
	if obj.ends_cfg is not None:
		output['ends-cfg'] = serialize_Ddos_template_http_uri__ends_cfg_json(obj.ends_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ddos_template_http_uri_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_template_http_uri_json(item))
	return output

def serialize_Http__request_rate_limit_json(obj):
	output = OrderedDict()
	if obj.request_rate is not None:
		output['request-rate'] = obj.request_rate
	if obj.uri is not None:
		output['uri'] = serialize_list_Ddos_template_http_uri_json(obj.uri)
	return output

def serialize_Ddos_template_http_obj_size__less_cfg_json(obj):
	output = OrderedDict()
	if obj.obj_less is not None:
		output['obj-less'] = obj.obj_less
	if obj.obj_rate is not None:
		output['obj-rate'] = obj.obj_rate
	return output

def serialize_Ddos_template_http_obj_size__greater_cfg_json(obj):
	output = OrderedDict()
	if obj.obj_greater is not None:
		output['obj-greater'] = obj.obj_greater
	if obj.obj_rate is not None:
		output['obj-rate'] = obj.obj_rate
	return output

def serialize_Ddos_template_http_obj_size__between_cfg_json(obj):
	output = OrderedDict()
	if obj.obj_between1 is not None:
		output['obj-between1'] = obj.obj_between1
	if obj.obj_between2 is not None:
		output['obj-between2'] = obj.obj_between2
	if obj.obj_rate is not None:
		output['obj-rate'] = obj.obj_rate
	return output

def serialize_Ddos_template_http_obj_size_json(obj):
	output = OrderedDict()
	if obj.less_cfg is not None:
		output['less-cfg'] = serialize_Ddos_template_http_obj_size__less_cfg_json(obj.less_cfg)
	if obj.greater_cfg is not None:
		output['greater-cfg'] = serialize_Ddos_template_http_obj_size__greater_cfg_json(obj.greater_cfg)
	if obj.between_cfg is not None:
		output['between-cfg'] = serialize_Ddos_template_http_obj_size__between_cfg_json(obj.between_cfg)
	return output

def serialize_list_Ddos_template_http_obj_size_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_template_http_obj_size_json(item))
	return output

def serialize_Http__response_rate_limit_json(obj):
	output = OrderedDict()
	if obj.obj_size is not None:
		output['obj-size'] = serialize_list_Ddos_template_http_obj_size_json(obj.obj_size)
	return output

def serialize_Http__slow_read_drop_json(obj):
	output = OrderedDict()
	if obj.min_window_size is not None:
		output['min-window-size'] = obj.min_window_size
	if obj.min_window_count is not None:
		output['min-window-count'] = obj.min_window_count
	return output

def serialize_Ddos_template_http_referer_filter_json(obj):
	output = OrderedDict()
	if obj.ref_filter_blacklist is not None:
		output['ref-filter-blacklist'] = obj.ref_filter_blacklist
	if obj.referer_equals is not None:
		output['referer-equals'] = obj.referer_equals
	if obj.referer_contains is not None:
		output['referer-contains'] = obj.referer_contains
	if obj.referer_starts_with is not None:
		output['referer-starts-with'] = obj.referer_starts_with
	if obj.referer_ends_with is not None:
		output['referer-ends-with'] = obj.referer_ends_with
	return output

def serialize_list_Ddos_template_http_referer_filter_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_template_http_referer_filter_json(item))
	return output

def serialize_Ddos_template_http_agent_filter_json(obj):
	output = OrderedDict()
	if obj.agent_filter_blacklist is not None:
		output['agent-filter-blacklist'] = obj.agent_filter_blacklist
	if obj.agent_equals is not None:
		output['agent-equals'] = obj.agent_equals
	if obj.agent_contains is not None:
		output['agent-contains'] = obj.agent_contains
	if obj.agent_starts_with is not None:
		output['agent-starts-with'] = obj.agent_starts_with
	if obj.agent_ends_with is not None:
		output['agent-ends-with'] = obj.agent_ends_with
	return output

def serialize_list_Ddos_template_http_agent_filter_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_template_http_agent_filter_json(item))
	return output

def serialize_Http_json(obj):
	output = OrderedDict()
	output['http-tmpl-name'] = obj.http_tmpl_name
	if obj.action is not None:
		output['action'] = obj.action
	if obj.disable is not None:
		output['disable'] = obj.disable
	if obj.mss_cfg is not None:
		output['mss-cfg'] = serialize_Http__mss_cfg_json(obj.mss_cfg)
	if obj.challenge_method is not None:
		output['challenge-method'] = serialize_Http__challenge_method_json(obj.challenge_method)
	if obj.challenge_cookie_name is not None:
		output['challenge-cookie-name'] = obj.challenge_cookie_name
	if obj.challenge_keep_cookie is not None:
		output['challenge-keep-cookie'] = obj.challenge_keep_cookie
	if obj.challenge_interval is not None:
		output['challenge-interval'] = obj.challenge_interval
	if obj.malformed_http is not None:
		output['malformed-http'] = serialize_Http__malformed_http_json(obj.malformed_http)
	if obj.use_hdr_ip_cfg is not None:
		output['use-hdr-ip-cfg'] = serialize_Http__use_hdr_ip_cfg_json(obj.use_hdr_ip_cfg)
	if obj.request_header is not None:
		output['request-header'] = serialize_Http__request_header_json(obj.request_header)
	if obj.post_rate_limit is not None:
		output['post-rate-limit'] = obj.post_rate_limit
	if obj.request_rate_limit is not None:
		output['request-rate-limit'] = serialize_Http__request_rate_limit_json(obj.request_rate_limit)
	if obj.response_rate_limit is not None:
		output['response-rate-limit'] = serialize_Http__response_rate_limit_json(obj.response_rate_limit)
	if obj.slow_read_drop is not None:
		output['slow-read-drop'] = serialize_Http__slow_read_drop_json(obj.slow_read_drop)
	if obj.idle_timeout is not None:
		output['idle-timeout'] = obj.idle_timeout
	if obj.ignore_zero_payload is not None:
		output['ignore-zero-payload'] = obj.ignore_zero_payload
	if obj.referer_filter is not None:
		output['referer-filter'] = serialize_list_Ddos_template_http_referer_filter_json(obj.referer_filter)
	if obj.agent_filter is not None:
		output['agent-filter'] = serialize_list_Ddos_template_http_agent_filter_json(obj.agent_filter)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Http_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Http_json(item))
	return list(container)

class Http__mss_cfg(AxapiObject):
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

class Http__challenge_method(AxapiObject):
	__metaclass__ = StructMeta 
	method_302_redirect=PosRangedInteger(0, 1)
	method_javascript=PosRangedInteger(0, 1)
	def __init__(self, method_302_redirect=None, method_javascript=None):
		self.method_302_redirect = method_302_redirect
		self.method_javascript = method_javascript

	def __str__(self):
		return ""

class Http__malformed_http(AxapiObject):
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

class Http__use_hdr_ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	use_hdr_ip_as_source=PosRangedInteger(0, 1)
	l7_hdr_name=SizedString(1, 63)
	def __init__(self, use_hdr_ip_as_source=None, l7_hdr_name=None):
		self.use_hdr_ip_as_source = use_hdr_ip_as_source
		self.l7_hdr_name = l7_hdr_name

	def __str__(self):
		return ""

class Http__request_header(AxapiObject):
	__metaclass__ = StructMeta 
	timeout=PosRangedInteger(1, 63)
	def __init__(self, timeout=None):
		self.timeout = timeout

	def __str__(self):
		return ""

class Http__request_rate_limit(AxapiObject):
	__metaclass__ = StructMeta 
	request_rate=PosRangedInteger(1, 16000000)
	def __init__(self, request_rate=None, uri=None):
		self.request_rate = request_rate
		self.uri = uri

	def __str__(self):
		return ""

class Http__response_rate_limit(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, obj_size=None):
		self.obj_size = obj_size

	def __str__(self):
		return ""

class Http__slow_read_drop(AxapiObject):
	__metaclass__ = StructMeta 
	min_window_size=PosRangedInteger(1, 65535)
	min_window_count=PosRangedInteger(1, 31)
	def __init__(self, min_window_size=None, min_window_count=None):
		self.min_window_size = min_window_size
		self.min_window_count = min_window_count

	def __str__(self):
		return ""

class Http(AxapiObject):
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

class Ddos_template_http_uri__equal_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	url_equals=SizedString(1, 127)
	url_rate=PosRangedInteger(1, 16000000)
	def __init__(self, url_equals=None, url_rate=None):
		self.url_equals = url_equals
		self.url_rate = url_rate

	def __str__(self):
		return ""

class Ddos_template_http_uri__contains_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	url_contains=SizedString(1, 127)
	url_rate=PosRangedInteger(1, 16000000)
	def __init__(self, url_contains=None, url_rate=None):
		self.url_contains = url_contains
		self.url_rate = url_rate

	def __str__(self):
		return ""

class Ddos_template_http_uri__starts_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	url_starts_with=SizedString(1, 127)
	url_rate=PosRangedInteger(1, 16000000)
	def __init__(self, url_starts_with=None, url_rate=None):
		self.url_starts_with = url_starts_with
		self.url_rate = url_rate

	def __str__(self):
		return ""

class Ddos_template_http_uri__ends_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	url_ends_with=SizedString(1, 127)
	url_rate=PosRangedInteger(1, 16000000)
	def __init__(self, url_ends_with=None, url_rate=None):
		self.url_ends_with = url_ends_with
		self.url_rate = url_rate

	def __str__(self):
		return ""

class Ddos_template_http_uri(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, equal_cfg=None, contains_cfg=None, starts_cfg=None, ends_cfg=None):
		self.equal_cfg = equal_cfg
		self.contains_cfg = contains_cfg
		self.starts_cfg = starts_cfg
		self.ends_cfg = ends_cfg

	def __str__(self):
		return ""

class Ddos_template_http_obj_size__less_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	obj_less=PosRangedInteger(1, 16000000)
	obj_rate=PosRangedInteger(1, 16000000)
	def __init__(self, obj_less=None, obj_rate=None):
		self.obj_less = obj_less
		self.obj_rate = obj_rate

	def __str__(self):
		return ""

class Ddos_template_http_obj_size__greater_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	obj_greater=PosRangedInteger(1, 16000000)
	obj_rate=PosRangedInteger(1, 16000000)
	def __init__(self, obj_greater=None, obj_rate=None):
		self.obj_greater = obj_greater
		self.obj_rate = obj_rate

	def __str__(self):
		return ""

class Ddos_template_http_obj_size__between_cfg(AxapiObject):
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

class Ddos_template_http_obj_size(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, less_cfg=None, greater_cfg=None, between_cfg=None):
		self.less_cfg = less_cfg
		self.greater_cfg = greater_cfg
		self.between_cfg = between_cfg

	def __str__(self):
		return ""

class Ddos_template_http_referer_filter(AxapiObject):
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

class Http_http_tmpl_name(AxapiObject):
	__metaclass__ = StructMeta 
	http_tmpl_name=SizedString(1, 63)
	def __init__(self, http_tmpl_name):
		self.http_tmpl_name = http_tmpl_name

	def __str__(self):
		return str(self.http_tmpl_name)

class Ddos_template_http_agent_filter(AxapiObject):
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

class DdosTemplateHttpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosTemplateHttp(self, http_http_tmpl_name):
		"""
		Retrieve the http identified by the specified identifier
		
		Args:
			http_http_tmpl_name Http_http_tmpl_name
		
		Returns:
			An instance of the Http class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(http_http_tmpl_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified http does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('http')
		return deserialize_Http_json(payload)

	def putDdosTemplateHttp(self, http_http_tmpl_name, http):
		"""
		Replace the object http
		
		Args:
			http_http_tmpl_name Http_http_tmpl_name
			http An instance of the Http class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['http']=serialize_Http_json(http)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(http_http_tmpl_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosTemplateHttp(self, http_http_tmpl_name):
		"""
		Remove the http identified by the specified identifier from the system
		
		Args:
			http_http_tmpl_name Http_http_tmpl_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(http_http_tmpl_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified http does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosTemplateHttpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosTemplateHttp(self, http):
		"""
		Create the object http
		
		Args:
			http An instance of the Http class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['http']=serialize_Http_json(http)
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

	def getAllDdosTemplateHttps(self):
		"""
		Retrieve all http objects currently pending in the system
		
		Returns:
			A list of Http objects
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
			payload= data.get('httpList')
		return deserialize_list_Http_json(payload)

