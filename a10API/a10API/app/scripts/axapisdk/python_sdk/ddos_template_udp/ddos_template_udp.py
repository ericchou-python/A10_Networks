########################################################################################################################
# File name: ddos_template_udp.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/template/udp',
]

def deserialize_Udp__tunnel_encap__always_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4_addr = data.get('ipv4-addr')
	ipv6_addr = data.get('ipv6-addr')
	result = Udp__tunnel_encap__always(ipv4_addr=ipv4_addr, ipv6_addr=ipv6_addr)
	return result

def deserialize_Udp__tunnel_encap__gre_always_json(obj):
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
	result = Udp__tunnel_encap__gre_always(gre_ipv4=gre_ipv4, key_ipv4=key_ipv4, gre_ipv6=gre_ipv6, key_ipv6=key_ipv6)
	return result

def deserialize_Udp__tunnel_encap_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_encap = data.get('ip-encap')
	always = deserialize_Udp__tunnel_encap__always_json(data.get('always'))
	gre_encap = data.get('gre-encap')
	gre_always = deserialize_Udp__tunnel_encap__gre_always_json(data.get('gre-always'))
	result = Udp__tunnel_encap(ip_encap=ip_encap, always=always, gre_encap=gre_encap, gre_always=gre_always)
	return result

def deserialize_Udp__spoof_detect_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	spoof_detect = data.get('spoof-detect')
	spoof_detect_retry_timeout = data.get('spoof-detect-retry-timeout')
	result = Udp__spoof_detect_cfg(spoof_detect=spoof_detect, spoof_detect_retry_timeout=spoof_detect_retry_timeout)
	return result

def deserialize_Udp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	age = data.get('age')
	tunnel_encap = deserialize_Udp__tunnel_encap_json(data.get('tunnel-encap'))
	tunnel_rate_limit = data.get('tunnel-rate-limit')
	spoof_detect_cfg = deserialize_Udp__spoof_detect_cfg_json(data.get('spoof-detect-cfg'))
	max_payload_size = data.get('max-payload-size')
	min_payload_size = data.get('min-payload-size')
	result = Udp(name=name, age=age, tunnel_encap=tunnel_encap, tunnel_rate_limit=tunnel_rate_limit, spoof_detect_cfg=spoof_detect_cfg, max_payload_size=max_payload_size, min_payload_size=min_payload_size)
	return result

def serialize_Udp__tunnel_encap__always_json(obj):
	output = OrderedDict()
	if obj.ipv4_addr is not None:
		output['ipv4-addr'] = obj.ipv4_addr
	if obj.ipv6_addr is not None:
		output['ipv6-addr'] = obj.ipv6_addr
	return output

def serialize_Udp__tunnel_encap__gre_always_json(obj):
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

def serialize_Udp__tunnel_encap_json(obj):
	output = OrderedDict()
	if obj.ip_encap is not None:
		output['ip-encap'] = obj.ip_encap
	if obj.always is not None:
		output['always'] = serialize_Udp__tunnel_encap__always_json(obj.always)
	if obj.gre_encap is not None:
		output['gre-encap'] = obj.gre_encap
	if obj.gre_always is not None:
		output['gre-always'] = serialize_Udp__tunnel_encap__gre_always_json(obj.gre_always)
	return output

def serialize_Udp__spoof_detect_cfg_json(obj):
	output = OrderedDict()
	if obj.spoof_detect is not None:
		output['spoof-detect'] = obj.spoof_detect
	if obj.spoof_detect_retry_timeout is not None:
		output['spoof-detect-retry-timeout'] = obj.spoof_detect_retry_timeout
	return output

def serialize_Udp_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.age is not None:
		output['age'] = obj.age
	if obj.tunnel_encap is not None:
		output['tunnel-encap'] = serialize_Udp__tunnel_encap_json(obj.tunnel_encap)
	if obj.tunnel_rate_limit is not None:
		output['tunnel-rate-limit'] = obj.tunnel_rate_limit
	if obj.spoof_detect_cfg is not None:
		output['spoof-detect-cfg'] = serialize_Udp__spoof_detect_cfg_json(obj.spoof_detect_cfg)
	if obj.max_payload_size is not None:
		output['max-payload-size'] = obj.max_payload_size
	if obj.min_payload_size is not None:
		output['min-payload-size'] = obj.min_payload_size
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Udp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Udp_json(item))
	return list(container)

class Udp_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class Udp__tunnel_encap__always(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6_addr=SizedString(1, 255)
	def __init__(self, ipv4_addr=None, ipv6_addr=None):
		self.ipv4_addr = ipv4_addr
		self.ipv6_addr = ipv6_addr

	def __str__(self):
		return ""

class Udp__tunnel_encap__gre_always(AxapiObject):
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

class Udp__tunnel_encap(AxapiObject):
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

class Udp__spoof_detect_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	spoof_detect=PosRangedInteger(0, 1)
	spoof_detect_retry_timeout=PosRangedInteger(1, 31)
	def __init__(self, spoof_detect=None, spoof_detect_retry_timeout=None):
		self.spoof_detect = spoof_detect
		self.spoof_detect_retry_timeout = spoof_detect_retry_timeout

	def __str__(self):
		return ""

class Udp(AxapiObject):
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

class DdosTemplateUdpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosTemplateUdp(self, udp_name):
		"""
		Retrieve the udp identified by the specified identifier
		
		Args:
			udp_name Udp_name
		
		Returns:
			An instance of the Udp class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(udp_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified udp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('udp')
		return deserialize_Udp_json(payload)

	def putDdosTemplateUdp(self, udp_name, udp):
		"""
		Replace the object udp
		
		Args:
			udp_name Udp_name
			udp An instance of the Udp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['udp']=serialize_Udp_json(udp)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(udp_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosTemplateUdp(self, udp_name):
		"""
		Remove the udp identified by the specified identifier from the system
		
		Args:
			udp_name Udp_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(udp_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified udp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosTemplateUdpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosTemplateUdp(self, udp):
		"""
		Create the object udp
		
		Args:
			udp An instance of the Udp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['udp']=serialize_Udp_json(udp)
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

	def getAllDdosTemplateUdps(self):
		"""
		Retrieve all udp objects currently pending in the system
		
		Returns:
			A list of Udp objects
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
			payload= data.get('udpList')
		return deserialize_list_Udp_json(payload)

