########################################################################################################################
# File name: ddos_template_dns.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/template/dns',
]

def deserialize_Dns__dns_auth_cfg__udp_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	udp = data.get('udp')
	udp_timeout = data.get('udp-timeout')
	result = Dns__dns_auth_cfg__udp_cfg(udp=udp, udp_timeout=udp_timeout)
	return result

def deserialize_Dns__dns_auth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns_auth = data.get('dns-auth')
	force_tcp = data.get('force-tcp')
	udp_cfg = deserialize_Dns__dns_auth_cfg__udp_cfg_json(data.get('udp-cfg'))
	result = Dns__dns_auth_cfg(dns_auth=dns_auth, force_tcp=force_tcp, udp_cfg=udp_cfg)
	return result

def deserialize_Dns__fqdn_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns_fqdn_rate_limit = data.get('dns-fqdn-rate-limit')
	dns_fqdn_rate = data.get('dns-fqdn-rate')
	by = data.get('by')
	result = Dns__fqdn_cfg(dns_fqdn_rate_limit=dns_fqdn_rate_limit, dns_fqdn_rate=dns_fqdn_rate, by=by)
	return result

def deserialize_Dns__nxdomain_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns_nxdomain_rate_limit = data.get('dns-nxdomain-rate-limit')
	dns_nxdomain_rate = data.get('dns-nxdomain-rate')
	action = data.get('action')
	result = Dns__nxdomain_cfg(dns_nxdomain_rate_limit=dns_nxdomain_rate_limit, dns_nxdomain_rate=dns_nxdomain_rate, action=action)
	return result

def deserialize_Dns__symtimeout_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sym_timeout = data.get('sym-timeout')
	sym_timeout_value = data.get('sym-timeout-value')
	result = Dns__symtimeout_cfg(sym_timeout=sym_timeout, sym_timeout_value=sym_timeout_value)
	return result

def deserialize_Dns__dns_request_rate_limit__type__a_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	a = data.get('A')
	dns_a_rate = data.get('dns-a-rate')
	result = Dns__dns_request_rate_limit__type__a_cfg(a=a, dns_a_rate=dns_a_rate)
	return result

def deserialize_Dns__dns_request_rate_limit__type__aaaa_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	aaaa = data.get('AAAA')
	dns_aaaa_rate = data.get('dns-aaaa-rate')
	result = Dns__dns_request_rate_limit__type__aaaa_cfg(aaaa=aaaa, dns_aaaa_rate=dns_aaaa_rate)
	return result

def deserialize_Dns__dns_request_rate_limit__type__cname_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	cname = data.get('CNAME')
	dns_cname_rate = data.get('dns-cname-rate')
	result = Dns__dns_request_rate_limit__type__cname_cfg(cname=cname, dns_cname_rate=dns_cname_rate)
	return result

def deserialize_Dns__dns_request_rate_limit__type__mx_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	mx = data.get('MX')
	dns_mx_rate = data.get('dns-mx-rate')
	result = Dns__dns_request_rate_limit__type__mx_cfg(mx=mx, dns_mx_rate=dns_mx_rate)
	return result

def deserialize_Dns__dns_request_rate_limit__type__ns_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ns = data.get('NS')
	dns_ns_rate = data.get('dns-ns-rate')
	result = Dns__dns_request_rate_limit__type__ns_cfg(ns=ns, dns_ns_rate=dns_ns_rate)
	return result

def deserialize_Dns__dns_request_rate_limit__type__srv_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	srv = data.get('SRV')
	dns_srv_rate = data.get('dns-srv-rate')
	result = Dns__dns_request_rate_limit__type__srv_cfg(srv=srv, dns_srv_rate=dns_srv_rate)
	return result

def deserialize_Ddos_template_dns_dns_type_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns_request_type = data.get('dns-request-type')
	dns_request_type_rate = data.get('dns-request-type-rate')
	result = Ddos_template_dns_dns_type_cfg(dns_request_type=dns_request_type, dns_request_type_rate=dns_request_type_rate)
	return result

def deserialize_list_Ddos_template_dns_dns_type_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_template_dns_dns_type_cfg_json(item))
	return list(container)

def deserialize_Dns__dns_request_rate_limit__type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	a_cfg = deserialize_Dns__dns_request_rate_limit__type__a_cfg_json(data.get('A-cfg'))
	aaaa_cfg = deserialize_Dns__dns_request_rate_limit__type__aaaa_cfg_json(data.get('AAAA-cfg'))
	cname_cfg = deserialize_Dns__dns_request_rate_limit__type__cname_cfg_json(data.get('CNAME-cfg'))
	mx_cfg = deserialize_Dns__dns_request_rate_limit__type__mx_cfg_json(data.get('MX-cfg'))
	ns_cfg = deserialize_Dns__dns_request_rate_limit__type__ns_cfg_json(data.get('NS-cfg'))
	srv_cfg = deserialize_Dns__dns_request_rate_limit__type__srv_cfg_json(data.get('SRV-cfg'))
	dns_type_cfg = deserialize_list_Ddos_template_dns_dns_type_cfg_json(data.get('dns-type-cfg'))
	result = Dns__dns_request_rate_limit__type(a_cfg=a_cfg, aaaa_cfg=aaaa_cfg, cname_cfg=cname_cfg, mx_cfg=mx_cfg, ns_cfg=ns_cfg, srv_cfg=srv_cfg, dns_type_cfg=dns_type_cfg)
	return result

def deserialize_Dns__dns_request_rate_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type = deserialize_Dns__dns_request_rate_limit__type_json(data.get('type'))
	result = Dns__dns_request_rate_limit(type=type)
	return result

def deserialize_Dns_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	dns_any_check = data.get('dns-any-check')
	dns_auth_cfg = deserialize_Dns__dns_auth_cfg_json(data.get('dns-auth-cfg'))
	fqdn_cfg = deserialize_Dns__fqdn_cfg_json(data.get('fqdn-cfg'))
	nxdomain_cfg = deserialize_Dns__nxdomain_cfg_json(data.get('nxdomain-cfg'))
	symtimeout_cfg = deserialize_Dns__symtimeout_cfg_json(data.get('symtimeout-cfg'))
	dns_request_rate_limit = deserialize_Dns__dns_request_rate_limit_json(data.get('dns-request-rate-limit'))
	result = Dns(name=name, dns_any_check=dns_any_check, dns_auth_cfg=dns_auth_cfg, fqdn_cfg=fqdn_cfg, nxdomain_cfg=nxdomain_cfg, symtimeout_cfg=symtimeout_cfg, dns_request_rate_limit=dns_request_rate_limit)
	return result

def serialize_Dns__dns_auth_cfg__udp_cfg_json(obj):
	output = OrderedDict()
	if obj.udp is not None:
		output['udp'] = obj.udp
	if obj.udp_timeout is not None:
		output['udp-timeout'] = obj.udp_timeout
	return output

def serialize_Dns__dns_auth_cfg_json(obj):
	output = OrderedDict()
	if obj.dns_auth is not None:
		output['dns-auth'] = obj.dns_auth
	if obj.force_tcp is not None:
		output['force-tcp'] = obj.force_tcp
	if obj.udp_cfg is not None:
		output['udp-cfg'] = serialize_Dns__dns_auth_cfg__udp_cfg_json(obj.udp_cfg)
	return output

def serialize_Dns__fqdn_cfg_json(obj):
	output = OrderedDict()
	if obj.dns_fqdn_rate_limit is not None:
		output['dns-fqdn-rate-limit'] = obj.dns_fqdn_rate_limit
	if obj.dns_fqdn_rate is not None:
		output['dns-fqdn-rate'] = obj.dns_fqdn_rate
	if obj.by is not None:
		output['by'] = obj.by
	return output

def serialize_Dns__nxdomain_cfg_json(obj):
	output = OrderedDict()
	if obj.dns_nxdomain_rate_limit is not None:
		output['dns-nxdomain-rate-limit'] = obj.dns_nxdomain_rate_limit
	if obj.dns_nxdomain_rate is not None:
		output['dns-nxdomain-rate'] = obj.dns_nxdomain_rate
	if obj.action is not None:
		output['action'] = obj.action
	return output

def serialize_Dns__symtimeout_cfg_json(obj):
	output = OrderedDict()
	if obj.sym_timeout is not None:
		output['sym-timeout'] = obj.sym_timeout
	if obj.sym_timeout_value is not None:
		output['sym-timeout-value'] = obj.sym_timeout_value
	return output

def serialize_Dns__dns_request_rate_limit__type__a_cfg_json(obj):
	output = OrderedDict()
	if obj.a is not None:
		output['A'] = obj.a
	if obj.dns_a_rate is not None:
		output['dns-a-rate'] = obj.dns_a_rate
	return output

def serialize_Dns__dns_request_rate_limit__type__aaaa_cfg_json(obj):
	output = OrderedDict()
	if obj.aaaa is not None:
		output['AAAA'] = obj.aaaa
	if obj.dns_aaaa_rate is not None:
		output['dns-aaaa-rate'] = obj.dns_aaaa_rate
	return output

def serialize_Dns__dns_request_rate_limit__type__cname_cfg_json(obj):
	output = OrderedDict()
	if obj.cname is not None:
		output['CNAME'] = obj.cname
	if obj.dns_cname_rate is not None:
		output['dns-cname-rate'] = obj.dns_cname_rate
	return output

def serialize_Dns__dns_request_rate_limit__type__mx_cfg_json(obj):
	output = OrderedDict()
	if obj.mx is not None:
		output['MX'] = obj.mx
	if obj.dns_mx_rate is not None:
		output['dns-mx-rate'] = obj.dns_mx_rate
	return output

def serialize_Dns__dns_request_rate_limit__type__ns_cfg_json(obj):
	output = OrderedDict()
	if obj.ns is not None:
		output['NS'] = obj.ns
	if obj.dns_ns_rate is not None:
		output['dns-ns-rate'] = obj.dns_ns_rate
	return output

def serialize_Dns__dns_request_rate_limit__type__srv_cfg_json(obj):
	output = OrderedDict()
	if obj.srv is not None:
		output['SRV'] = obj.srv
	if obj.dns_srv_rate is not None:
		output['dns-srv-rate'] = obj.dns_srv_rate
	return output

def serialize_Ddos_template_dns_dns_type_cfg_json(obj):
	output = OrderedDict()
	if obj.dns_request_type is not None:
		output['dns-request-type'] = obj.dns_request_type
	if obj.dns_request_type_rate is not None:
		output['dns-request-type-rate'] = obj.dns_request_type_rate
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ddos_template_dns_dns_type_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_template_dns_dns_type_cfg_json(item))
	return output

def serialize_Dns__dns_request_rate_limit__type_json(obj):
	output = OrderedDict()
	if obj.a_cfg is not None:
		output['A-cfg'] = serialize_Dns__dns_request_rate_limit__type__a_cfg_json(obj.a_cfg)
	if obj.aaaa_cfg is not None:
		output['AAAA-cfg'] = serialize_Dns__dns_request_rate_limit__type__aaaa_cfg_json(obj.aaaa_cfg)
	if obj.cname_cfg is not None:
		output['CNAME-cfg'] = serialize_Dns__dns_request_rate_limit__type__cname_cfg_json(obj.cname_cfg)
	if obj.mx_cfg is not None:
		output['MX-cfg'] = serialize_Dns__dns_request_rate_limit__type__mx_cfg_json(obj.mx_cfg)
	if obj.ns_cfg is not None:
		output['NS-cfg'] = serialize_Dns__dns_request_rate_limit__type__ns_cfg_json(obj.ns_cfg)
	if obj.srv_cfg is not None:
		output['SRV-cfg'] = serialize_Dns__dns_request_rate_limit__type__srv_cfg_json(obj.srv_cfg)
	if obj.dns_type_cfg is not None:
		output['dns-type-cfg'] = serialize_list_Ddos_template_dns_dns_type_cfg_json(obj.dns_type_cfg)
	return output

def serialize_Dns__dns_request_rate_limit_json(obj):
	output = OrderedDict()
	if obj.type is not None:
		output['type'] = serialize_Dns__dns_request_rate_limit__type_json(obj.type)
	return output

def serialize_Dns_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.dns_any_check is not None:
		output['dns-any-check'] = obj.dns_any_check
	if obj.dns_auth_cfg is not None:
		output['dns-auth-cfg'] = serialize_Dns__dns_auth_cfg_json(obj.dns_auth_cfg)
	if obj.fqdn_cfg is not None:
		output['fqdn-cfg'] = serialize_Dns__fqdn_cfg_json(obj.fqdn_cfg)
	if obj.nxdomain_cfg is not None:
		output['nxdomain-cfg'] = serialize_Dns__nxdomain_cfg_json(obj.nxdomain_cfg)
	if obj.symtimeout_cfg is not None:
		output['symtimeout-cfg'] = serialize_Dns__symtimeout_cfg_json(obj.symtimeout_cfg)
	if obj.dns_request_rate_limit is not None:
		output['dns-request-rate-limit'] = serialize_Dns__dns_request_rate_limit_json(obj.dns_request_rate_limit)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Dns_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Dns_json(item))
	return list(container)

class Dns__dns_auth_cfg__udp_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	udp=PosRangedInteger(0, 1)
	udp_timeout=PosRangedInteger(1, 16)
	def __init__(self, udp=None, udp_timeout=None):
		self.udp = udp
		self.udp_timeout = udp_timeout

	def __str__(self):
		return ""

class Dns__dns_auth_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dns_auth=PosRangedInteger(0, 1)
	force_tcp=PosRangedInteger(0, 1)
	def __init__(self, dns_auth=None, force_tcp=None, udp_cfg=None):
		self.dns_auth = dns_auth
		self.force_tcp = force_tcp
		self.udp_cfg = udp_cfg

	def __str__(self):
		return ""

class Dns__fqdn_cfg(AxapiObject):
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

class Dns__nxdomain_cfg(AxapiObject):
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

class Dns__symtimeout_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	sym_timeout=PosRangedInteger(0, 1)
	sym_timeout_value=PosRangedInteger(1, 31)
	def __init__(self, sym_timeout=None, sym_timeout_value=None):
		self.sym_timeout = sym_timeout
		self.sym_timeout_value = sym_timeout_value

	def __str__(self):
		return ""

class Dns__dns_request_rate_limit__type__a_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	a=PosRangedInteger(0, 1)
	dns_a_rate=PosRangedInteger(1, 16000000)
	def __init__(self, a=None, dns_a_rate=None):
		self.a = a
		self.dns_a_rate = dns_a_rate

	def __str__(self):
		return ""

class Dns__dns_request_rate_limit__type__aaaa_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	aaaa=PosRangedInteger(0, 1)
	dns_aaaa_rate=PosRangedInteger(1, 16000000)
	def __init__(self, aaaa=None, dns_aaaa_rate=None):
		self.aaaa = aaaa
		self.dns_aaaa_rate = dns_aaaa_rate

	def __str__(self):
		return ""

class Dns__dns_request_rate_limit__type__cname_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	cname=PosRangedInteger(0, 1)
	dns_cname_rate=PosRangedInteger(1, 16000000)
	def __init__(self, cname=None, dns_cname_rate=None):
		self.cname = cname
		self.dns_cname_rate = dns_cname_rate

	def __str__(self):
		return ""

class Dns__dns_request_rate_limit__type__mx_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	mx=PosRangedInteger(0, 1)
	dns_mx_rate=PosRangedInteger(1, 16000000)
	def __init__(self, mx=None, dns_mx_rate=None):
		self.mx = mx
		self.dns_mx_rate = dns_mx_rate

	def __str__(self):
		return ""

class Dns__dns_request_rate_limit__type__ns_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ns=PosRangedInteger(0, 1)
	dns_ns_rate=PosRangedInteger(1, 16000000)
	def __init__(self, ns=None, dns_ns_rate=None):
		self.ns = ns
		self.dns_ns_rate = dns_ns_rate

	def __str__(self):
		return ""

class Dns__dns_request_rate_limit__type__srv_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	srv=PosRangedInteger(0, 1)
	dns_srv_rate=PosRangedInteger(1, 16000000)
	def __init__(self, srv=None, dns_srv_rate=None):
		self.srv = srv
		self.dns_srv_rate = dns_srv_rate

	def __str__(self):
		return ""

class Dns__dns_request_rate_limit__type(AxapiObject):
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

class Dns__dns_request_rate_limit(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, type=None):
		self.type = type

	def __str__(self):
		return ""

class Dns(AxapiObject):
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

class Dns_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class Ddos_template_dns_dns_type_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dns_request_type=PosRangedInteger(1, 65535)
	dns_request_type_rate=PosRangedInteger(1, 16000000)
	def __init__(self, dns_request_type=None, dns_request_type_rate=None):
		self.dns_request_type = dns_request_type
		self.dns_request_type_rate = dns_request_type_rate

	def __str__(self):
		return ""

class DdosTemplateDnsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosTemplateDns(self, dns_name):
		"""
		Retrieve the dns identified by the specified identifier
		
		Args:
			dns_name Dns_name
		
		Returns:
			An instance of the Dns class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(dns_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified dns does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('dns')
		return deserialize_Dns_json(payload)

	def putDdosTemplateDns(self, dns_name, dns):
		"""
		Replace the object dns
		
		Args:
			dns_name Dns_name
			dns An instance of the Dns class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['dns']=serialize_Dns_json(dns)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(dns_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosTemplateDns(self, dns_name):
		"""
		Remove the dns identified by the specified identifier from the system
		
		Args:
			dns_name Dns_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(dns_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified dns does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosTemplateDnssClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosTemplateDns(self, dns):
		"""
		Create the object dns
		
		Args:
			dns An instance of the Dns class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['dns']=serialize_Dns_json(dns)
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

	def getAllDdosTemplateDnss(self):
		"""
		Retrieve all dns objects currently pending in the system
		
		Returns:
			A list of Dns objects
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
			payload= data.get('dnsList')
		return deserialize_list_Dns_json(payload)

