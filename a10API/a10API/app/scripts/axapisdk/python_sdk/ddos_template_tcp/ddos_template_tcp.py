########################################################################################################################
# File name: ddos_template_tcp.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/template/tcp',
]

def deserialize_Tcp__action_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	action_on_ack = data.get('action-on-ack')
	reset = data.get('reset')
	timeout = data.get('timeout')
	result = Tcp__action_cfg(action_on_ack=action_on_ack, reset=reset, timeout=timeout)
	return result

def deserialize_Tcp__tunnel_encap__ip_cfg__always_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4_addr = data.get('ipv4-addr')
	ipv6_addr = data.get('ipv6-addr')
	result = Tcp__tunnel_encap__ip_cfg__always(ipv4_addr=ipv4_addr, ipv6_addr=ipv6_addr)
	return result

def deserialize_Tcp__tunnel_encap__ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_encap = data.get('ip-encap')
	always = deserialize_Tcp__tunnel_encap__ip_cfg__always_json(data.get('always'))
	result = Tcp__tunnel_encap__ip_cfg(ip_encap=ip_encap, always=always)
	return result

def deserialize_Tcp__tunnel_encap__gre_cfg__gre_always_json(obj):
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
	result = Tcp__tunnel_encap__gre_cfg__gre_always(gre_ipv4=gre_ipv4, key_ipv4=key_ipv4, gre_ipv6=gre_ipv6, key_ipv6=key_ipv6)
	return result

def deserialize_Tcp__tunnel_encap__gre_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	gre_encap = data.get('gre-encap')
	gre_always = deserialize_Tcp__tunnel_encap__gre_cfg__gre_always_json(data.get('gre-always'))
	result = Tcp__tunnel_encap__gre_cfg(gre_encap=gre_encap, gre_always=gre_always)
	return result

def deserialize_Tcp__tunnel_encap_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_cfg = deserialize_Tcp__tunnel_encap__ip_cfg_json(data.get('ip-cfg'))
	gre_cfg = deserialize_Tcp__tunnel_encap__gre_cfg_json(data.get('gre-cfg'))
	result = Tcp__tunnel_encap(ip_cfg=ip_cfg, gre_cfg=gre_cfg)
	return result

def deserialize_Tcp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	action_cfg = deserialize_Tcp__action_cfg_json(data.get('action-cfg'))
	age = data.get('age')
	concurrent = data.get('concurrent')
	syn_cookie = data.get('syn-cookie')
	black_list_out_of_seq = data.get('black-list-out-of-seq')
	black_list_retransmit = data.get('black-list-retransmit')
	black_list_zero_win = data.get('black-list-zero-win')
	disable_syn_auth = data.get('disable-syn-auth')
	over_conn_limit_action = data.get('over-conn-limit-action')
	over_conn_rate_action = data.get('over-conn-rate-action')
	tunnel_encap = deserialize_Tcp__tunnel_encap_json(data.get('tunnel-encap'))
	tunnel_rate_limit = data.get('tunnel-rate-limit')
	result = Tcp(name=name, action_cfg=action_cfg, age=age, concurrent=concurrent, syn_cookie=syn_cookie, black_list_out_of_seq=black_list_out_of_seq, black_list_retransmit=black_list_retransmit, black_list_zero_win=black_list_zero_win, disable_syn_auth=disable_syn_auth, over_conn_limit_action=over_conn_limit_action, over_conn_rate_action=over_conn_rate_action, tunnel_encap=tunnel_encap, tunnel_rate_limit=tunnel_rate_limit)
	return result

def serialize_Tcp__action_cfg_json(obj):
	output = OrderedDict()
	if obj.action_on_ack is not None:
		output['action-on-ack'] = obj.action_on_ack
	if obj.reset is not None:
		output['reset'] = obj.reset
	if obj.timeout is not None:
		output['timeout'] = obj.timeout
	return output

def serialize_Tcp__tunnel_encap__ip_cfg__always_json(obj):
	output = OrderedDict()
	if obj.ipv4_addr is not None:
		output['ipv4-addr'] = obj.ipv4_addr
	if obj.ipv6_addr is not None:
		output['ipv6-addr'] = obj.ipv6_addr
	return output

def serialize_Tcp__tunnel_encap__ip_cfg_json(obj):
	output = OrderedDict()
	if obj.ip_encap is not None:
		output['ip-encap'] = obj.ip_encap
	if obj.always is not None:
		output['always'] = serialize_Tcp__tunnel_encap__ip_cfg__always_json(obj.always)
	return output

def serialize_Tcp__tunnel_encap__gre_cfg__gre_always_json(obj):
	output = OrderedDict()
	if obj.gre_ipv4 is not None:
		output['gre-ipv4'] = obj.gre_ipv4
	if obj.key_ipv4 is not None:
		output['key-ipv4'] = obj.key_ipv4
	if obj.gre_ipv6 is not None:
		output['gre-ipv6'] = obj.gre_ipv6
	if obj.key_ipv6 is not None:
		output['key-ipv6'] = obj.key_ipv6
	return output

def serialize_Tcp__tunnel_encap__gre_cfg_json(obj):
	output = OrderedDict()
	if obj.gre_encap is not None:
		output['gre-encap'] = obj.gre_encap
	if obj.gre_always is not None:
		output['gre-always'] = serialize_Tcp__tunnel_encap__gre_cfg__gre_always_json(obj.gre_always)
	return output

def serialize_Tcp__tunnel_encap_json(obj):
	output = OrderedDict()
	if obj.ip_cfg is not None:
		output['ip-cfg'] = serialize_Tcp__tunnel_encap__ip_cfg_json(obj.ip_cfg)
	if obj.gre_cfg is not None:
		output['gre-cfg'] = serialize_Tcp__tunnel_encap__gre_cfg_json(obj.gre_cfg)
	return output

def serialize_Tcp_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.action_cfg is not None:
		output['action-cfg'] = serialize_Tcp__action_cfg_json(obj.action_cfg)
	if obj.age is not None:
		output['age'] = obj.age
	if obj.concurrent is not None:
		output['concurrent'] = obj.concurrent
	if obj.syn_cookie is not None:
		output['syn-cookie'] = obj.syn_cookie
	if obj.black_list_out_of_seq is not None:
		output['black-list-out-of-seq'] = obj.black_list_out_of_seq
	if obj.black_list_retransmit is not None:
		output['black-list-retransmit'] = obj.black_list_retransmit
	if obj.black_list_zero_win is not None:
		output['black-list-zero-win'] = obj.black_list_zero_win
	if obj.disable_syn_auth is not None:
		output['disable-syn-auth'] = obj.disable_syn_auth
	if obj.over_conn_limit_action is not None:
		output['over-conn-limit-action'] = obj.over_conn_limit_action
	if obj.over_conn_rate_action is not None:
		output['over-conn-rate-action'] = obj.over_conn_rate_action
	if obj.tunnel_encap is not None:
		output['tunnel-encap'] = serialize_Tcp__tunnel_encap_json(obj.tunnel_encap)
	if obj.tunnel_rate_limit is not None:
		output['tunnel-rate-limit'] = obj.tunnel_rate_limit
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Tcp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Tcp_json(item))
	return list(container)

class Tcp_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class Tcp__action_cfg(AxapiObject):
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

class Tcp__tunnel_encap__ip_cfg__always(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6_addr=SizedString(1, 255)
	def __init__(self, ipv4_addr=None, ipv6_addr=None):
		self.ipv4_addr = ipv4_addr
		self.ipv6_addr = ipv6_addr

	def __str__(self):
		return ""

class Tcp__tunnel_encap__ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip_encap=PosRangedInteger(0, 1)
	def __init__(self, ip_encap=None, always=None):
		self.ip_encap = ip_encap
		self.always = always

	def __str__(self):
		return ""

class Tcp__tunnel_encap__gre_cfg__gre_always(AxapiObject):
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

class Tcp__tunnel_encap__gre_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	gre_encap=PosRangedInteger(0, 1)
	def __init__(self, gre_encap=None, gre_always=None):
		self.gre_encap = gre_encap
		self.gre_always = gre_always

	def __str__(self):
		return ""

class Tcp__tunnel_encap(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ip_cfg=None, gre_cfg=None):
		self.ip_cfg = ip_cfg
		self.gre_cfg = gre_cfg

	def __str__(self):
		return ""

class Tcp(AxapiObject):
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

class DdosTemplateTcpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosTemplateTcp(self, tcp_name):
		"""
		Retrieve the tcp identified by the specified identifier
		
		Args:
			tcp_name Tcp_name
		
		Returns:
			An instance of the Tcp class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(tcp_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified tcp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('tcp')
		return deserialize_Tcp_json(payload)

	def putDdosTemplateTcp(self, tcp_name, tcp):
		"""
		Replace the object tcp
		
		Args:
			tcp_name Tcp_name
			tcp An instance of the Tcp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['tcp']=serialize_Tcp_json(tcp)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(tcp_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosTemplateTcp(self, tcp_name):
		"""
		Remove the tcp identified by the specified identifier from the system
		
		Args:
			tcp_name Tcp_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(tcp_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified tcp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosTemplateTcpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosTemplateTcp(self, tcp):
		"""
		Create the object tcp
		
		Args:
			tcp An instance of the Tcp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['tcp']=serialize_Tcp_json(tcp)
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

	def getAllDdosTemplateTcps(self):
		"""
		Retrieve all tcp objects currently pending in the system
		
		Returns:
			A list of Tcp objects
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
			payload= data.get('tcpList')
		return deserialize_list_Tcp_json(payload)

