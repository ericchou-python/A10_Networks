########################################################################################################################
# File name: ddos_dst_default.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/dst/default',
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

def deserialize_Ddos_dst_default_key_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key = data.get('key')
	result = Ddos_dst_default_key_cfg(key=key)
	return result

def deserialize_list_Ddos_dst_default_key_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_default_key_cfg_json(item))
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
	key_cfg = deserialize_list_Ddos_dst_default_key_cfg_json(data.get('key-cfg'))
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

def deserialize_Default_json(obj):
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
	result = Default(default_address_type=default_address_type, disable=disable, age=age, exceed_log_enable=exceed_log_enable, l4_typelist=l4_typelist, portlist=portlist, ip_protolist=ip_protolist)
	return result

def serialize_Ddos_dst_default_l4_type__exceed_action_json(obj):
	output = OrderedDict()
	if obj.exceed_drop is not None:
		output['exceed-drop'] = obj.exceed_drop
	return output

def serialize_Ddos_dst_default_key_cfg_json(obj):
	output = OrderedDict()
	if obj.key is not None:
		output['key'] = obj.key
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ddos_dst_default_key_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_dst_default_key_cfg_json(item))
	return output

def serialize_Ddos_dst_default_l4_type__tunnel_decap_json(obj):
	output = OrderedDict()
	if obj.ip_decap is not None:
		output['ip-decap'] = obj.ip_decap
	if obj.gre_decap is not None:
		output['gre-decap'] = obj.gre_decap
	if obj.key_cfg is not None:
		output['key-cfg'] = serialize_list_Ddos_dst_default_key_cfg_json(obj.key_cfg)
	return output

def serialize_Ddos_dst_default_l4_type__tunnel_rate_limit_json(obj):
	output = OrderedDict()
	if obj.ip_rate_limit is not None:
		output['ip-rate-limit'] = obj.ip_rate_limit
	if obj.gre_rate_limit is not None:
		output['gre-rate-limit'] = obj.gre_rate_limit
	return output

def serialize_Ddos_dst_default_l4_type__scanning_detection__action_json(obj):
	output = OrderedDict()
	if obj.threshold_drop is not None:
		output['threshold-drop'] = obj.threshold_drop
	if obj.threshold_black_list is not None:
		output['threshold-black-list'] = obj.threshold_black_list
	return output

def serialize_Ddos_dst_default_l4_type__scanning_detection_json(obj):
	output = OrderedDict()
	if obj.threshold is not None:
		output['threshold'] = obj.threshold
	if obj.action is not None:
		output['action'] = serialize_Ddos_dst_default_l4_type__scanning_detection__action_json(obj.action)
	return output

def serialize_Ddos_dst_default_l4_type_json(obj):
	output = OrderedDict()
	output['protocol'] = obj.protocol
	if obj.glid is not None:
		output['glid'] = obj.glid
	if obj.deny is not None:
		output['deny'] = obj.deny
	if obj.dns_any_check is not None:
		output['dns-any-check'] = obj.dns_any_check
	if obj.max_rexmit_syn_per_flow is not None:
		output['max-rexmit-syn-per-flow'] = obj.max_rexmit_syn_per_flow
	if obj.exceed_action is not None:
		output['exceed-action'] = serialize_Ddos_dst_default_l4_type__exceed_action_json(obj.exceed_action)
	if obj.disable_syn_auth is not None:
		output['disable-syn-auth'] = obj.disable_syn_auth
	if obj.syn_cookie is not None:
		output['syn-cookie'] = obj.syn_cookie
	if obj.tcp_reset_client is not None:
		output['tcp-reset-client'] = obj.tcp_reset_client
	if obj.tcp_reset_server is not None:
		output['tcp-reset-server'] = obj.tcp_reset_server
	if obj.drop_on_no_port_match is not None:
		output['drop-on-no-port-match'] = obj.drop_on_no_port_match
	if obj.over_conn_limit_action is not None:
		output['over-conn-limit-action'] = obj.over_conn_limit_action
	if obj.over_conn_rate_action is not None:
		output['over-conn-rate-action'] = obj.over_conn_rate_action
	if obj.stateful is not None:
		output['stateful'] = obj.stateful
	if obj.tunnel_decap is not None:
		output['tunnel-decap'] = serialize_Ddos_dst_default_l4_type__tunnel_decap_json(obj.tunnel_decap)
	if obj.tunnel_rate_limit is not None:
		output['tunnel-rate-limit'] = serialize_Ddos_dst_default_l4_type__tunnel_rate_limit_json(obj.tunnel_rate_limit)
	if obj.drop_frag_pkt is not None:
		output['drop-frag-pkt'] = obj.drop_frag_pkt
	if obj.scanning_detection is not None:
		output['scanning-detection'] = serialize_Ddos_dst_default_l4_type__scanning_detection_json(obj.scanning_detection)
	return output

def serialize_list_Ddos_dst_default_l4_type_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_dst_default_l4_type_json(item))
	return output

def serialize_Ddos_dst_default_port__template_json(obj):
	output = OrderedDict()
	if obj.dns is not None:
		output['dns'] = obj.dns
	if obj.http is not None:
		output['http'] = obj.http
	if obj.ssl_l4 is not None:
		output['ssl-l4'] = obj.ssl_l4
	if obj.tcp is not None:
		output['tcp'] = obj.tcp
	if obj.udp is not None:
		output['udp'] = obj.udp
	return output

def serialize_Ddos_dst_default_port_json(obj):
	output = OrderedDict()
	output['port-num'] = obj.port_num
	output['protocol'] = obj.protocol
	if obj.deny is not None:
		output['deny'] = obj.deny
	if obj.glid is not None:
		output['glid'] = obj.glid
	if obj.template is not None:
		output['template'] = serialize_Ddos_dst_default_port__template_json(obj.template)
	return output

def serialize_list_Ddos_dst_default_port_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_dst_default_port_json(item))
	return output

def serialize_Ddos_dst_default_ip_proto_json(obj):
	output = OrderedDict()
	output['port-num'] = obj.port_num
	if obj.deny is not None:
		output['deny'] = obj.deny
	if obj.glid is not None:
		output['glid'] = obj.glid
	return output

def serialize_list_Ddos_dst_default_ip_proto_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_dst_default_ip_proto_json(item))
	return output

def serialize_Default_json(obj):
	output = OrderedDict()
	output['default-address-type'] = obj.default_address_type
	if obj.disable is not None:
		output['disable'] = obj.disable
	if obj.age is not None:
		output['age'] = obj.age
	if obj.exceed_log_enable is not None:
		output['exceed-log-enable'] = obj.exceed_log_enable
	if obj.l4_typelist is not None:
		output['l4-typeList'] = serialize_list_Ddos_dst_default_l4_type_json(obj.l4_typelist)
	if obj.portlist is not None:
		output['portList'] = serialize_list_Ddos_dst_default_port_json(obj.portlist)
	if obj.ip_protolist is not None:
		output['ip-protoList'] = serialize_list_Ddos_dst_default_ip_proto_json(obj.ip_protolist)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Default_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Default_json(item))
	return list(container)

class Default(AxapiObject):
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

class Ddos_dst_default_key_cfg(AxapiObject):
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

class Default_default_address_type(AxapiObject):
	__metaclass__ = StructMeta 
	default_address_type = Enum(['ip', 'ipv6'])
	def __init__(self, default_address_type):
		self.default_address_type = default_address_type

	def __str__(self):
		return str(self.default_address_type)

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

class DdosDstDefaultClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosDstDefault(self, default_default_address_type):
		"""
		Retrieve the default identified by the specified identifier
		
		Args:
			default_default_address_type Default_default_address_type
		
		Returns:
			An instance of the Default class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(default_default_address_type) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified default does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('default')
		return deserialize_Default_json(payload)

	def putDdosDstDefault(self, default_default_address_type, default):
		"""
		Replace the object default
		
		Args:
			default_default_address_type Default_default_address_type
			default An instance of the Default class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['default']=serialize_Default_json(default)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(default_default_address_type) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosDstDefault(self, default_default_address_type):
		"""
		Remove the default identified by the specified identifier from the system
		
		Args:
			default_default_address_type Default_default_address_type
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(default_default_address_type) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified default does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosDstDefaultsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosDstDefault(self, default):
		"""
		Create the object default
		
		Args:
			default An instance of the Default class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['default']=serialize_Default_json(default)
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

	def getAllDdosDstDefaults(self):
		"""
		Retrieve all default objects currently pending in the system
		
		Returns:
			A list of Default objects
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
			payload= data.get('defaultList')
		return deserialize_list_Default_json(payload)

