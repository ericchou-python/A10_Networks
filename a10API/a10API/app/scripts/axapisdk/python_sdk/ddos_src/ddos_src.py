########################################################################################################################
# File name: ddos_src.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/src',
]

def deserialize_Ddos_src_default_l4_type__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	result = Ddos_src_default_l4_type__template(tcp=tcp, udp=udp)
	return result

def deserialize_Ddos_src_default_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	deny = data.get('deny')
	glid = data.get('glid')
	template = deserialize_Ddos_src_default_l4_type__template_json(data.get('template'))
	result = Ddos_src_default_l4_type(protocol=protocol, deny=deny, glid=glid, template=template)
	return result

def deserialize_list_Ddos_src_default_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_default_l4_type_json(item))
	return list(container)

def deserialize_Ddos_src_default_app_type__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns = data.get('dns')
	http = data.get('http')
	ssl_l4 = data.get('ssl-l4')
	result = Ddos_src_default_app_type__template(dns=dns, http=http, ssl_l4=ssl_l4)
	return result

def deserialize_Ddos_src_default_app_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	template = deserialize_Ddos_src_default_app_type__template_json(data.get('template'))
	result = Ddos_src_default_app_type(protocol=protocol, template=template)
	return result

def deserialize_list_Ddos_src_default_app_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_default_app_type_json(item))
	return list(container)

def deserialize_Ddos_src_default_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default_address_type = data.get('default-address-type')
	disable = data.get('disable')
	age = data.get('age')
	l4_typelist = deserialize_list_Ddos_src_default_l4_type_json(data.get('l4-typeList'))
	app_typelist = deserialize_list_Ddos_src_default_app_type_json(data.get('app-typeList'))
	result = Ddos_src_default(default_address_type=default_address_type, disable=disable, age=age, l4_typelist=l4_typelist, app_typelist=app_typelist)
	return result

def deserialize_list_Ddos_src_default_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_default_json(item))
	return list(container)

def deserialize_Ddos_src_entry_l4_type__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	result = Ddos_src_entry_l4_type__template(tcp=tcp, udp=udp)
	return result

def deserialize_Ddos_src_entry_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	action = data.get('action')
	glid = data.get('glid')
	template = deserialize_Ddos_src_entry_l4_type__template_json(data.get('template'))
	result = Ddos_src_entry_l4_type(protocol=protocol, action=action, glid=glid, template=template)
	return result

def deserialize_list_Ddos_src_entry_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_entry_l4_type_json(item))
	return list(container)

def deserialize_Ddos_src_entry_app_type__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ssl_l4 = data.get('ssl-l4')
	dns = data.get('dns')
	http = data.get('http')
	result = Ddos_src_entry_app_type__template(ssl_l4=ssl_l4, dns=dns, http=http)
	return result

def deserialize_Ddos_src_entry_app_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	template = deserialize_Ddos_src_entry_app_type__template_json(data.get('template'))
	result = Ddos_src_entry_app_type(protocol=protocol, template=template)
	return result

def deserialize_list_Ddos_src_entry_app_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_entry_app_type_json(item))
	return list(container)

def deserialize_Ddos_src_entry_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	src_entry_name = data.get('src-entry-name')
	ipv6_addr = data.get('ipv6-addr')
	ip_addr = data.get('ip-addr')
	subnet_ip_addr = data.get('subnet-ip-addr')
	subnet_ipv6_addr = data.get('subnet-ipv6-addr')
	l4_typelist = deserialize_list_Ddos_src_entry_l4_type_json(data.get('l4-typeList'))
	app_typelist = deserialize_list_Ddos_src_entry_app_type_json(data.get('app-typeList'))
	result = Ddos_src_entry(src_entry_name=src_entry_name, ipv6_addr=ipv6_addr, ip_addr=ip_addr, subnet_ip_addr=subnet_ip_addr, subnet_ipv6_addr=subnet_ipv6_addr, l4_typelist=l4_typelist, app_typelist=app_typelist)
	return result

def deserialize_list_Ddos_src_entry_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_entry_json(item))
	return list(container)

def deserialize_Ddos_src_geo_location_l4_type__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	result = Ddos_src_geo_location_l4_type__template(tcp=tcp, udp=udp)
	return result

def deserialize_Ddos_src_geo_location_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	deny = data.get('deny')
	glid = data.get('glid')
	template = deserialize_Ddos_src_geo_location_l4_type__template_json(data.get('template'))
	result = Ddos_src_geo_location_l4_type(protocol=protocol, deny=deny, glid=glid, template=template)
	return result

def deserialize_list_Ddos_src_geo_location_l4_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_geo_location_l4_type_json(item))
	return list(container)

def deserialize_Ddos_src_geo_location_app_type__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns = data.get('dns')
	http = data.get('http')
	result = Ddos_src_geo_location_app_type__template(dns=dns, http=http)
	return result

def deserialize_Ddos_src_geo_location_app_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	template = deserialize_Ddos_src_geo_location_app_type__template_json(data.get('template'))
	result = Ddos_src_geo_location_app_type(protocol=protocol, template=template)
	return result

def deserialize_list_Ddos_src_geo_location_app_type_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_geo_location_app_type_json(item))
	return list(container)

def deserialize_Ddos_src_geo_location_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	geolocation_name = data.get('geolocation-name')
	l4_typelist = deserialize_list_Ddos_src_geo_location_l4_type_json(data.get('l4-typeList'))
	app_typelist = deserialize_list_Ddos_src_geo_location_app_type_json(data.get('app-typeList'))
	result = Ddos_src_geo_location(geolocation_name=geolocation_name, l4_typelist=l4_typelist, app_typelist=app_typelist)
	return result

def deserialize_list_Ddos_src_geo_location_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_src_geo_location_json(item))
	return list(container)

def deserialize_Src_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	defaultlist = deserialize_list_Ddos_src_default_json(data.get('defaultList'))
	entrylist = deserialize_list_Ddos_src_entry_json(data.get('entryList'))
	geo_locationlist = deserialize_list_Ddos_src_geo_location_json(data.get('geo-locationList'))
	result = Src(defaultlist=defaultlist, entrylist=entrylist, geo_locationlist=geo_locationlist)
	return result

class Src(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, defaultlist=None, entrylist=None, geo_locationlist=None):
		self.defaultlist = defaultlist
		self.entrylist = entrylist
		self.geo_locationlist = geo_locationlist

	def __str__(self):
		return ""

class Ddos_src_default(AxapiObject):
	__metaclass__ = StructMeta 
	default_address_type = Enum(['ip', 'ipv6'])
	disable=PosRangedInteger(0, 1)
	age=PosRangedInteger(5, 1023)
	def __init__(self, default_address_type, disable=None, age=None, l4_typelist=None, app_typelist=None):
		self.default_address_type = default_address_type
		self.disable = disable
		self.age = age
		self.l4_typelist = l4_typelist
		self.app_typelist = app_typelist

	def __str__(self):
		return str(self.default_address_type)

class Ddos_src_default_l4_type__template(AxapiObject):
	__metaclass__ = StructMeta 
	tcp=SizedString(1, 255)
	udp=SizedString(1, 255)
	def __init__(self, tcp=None, udp=None):
		self.tcp = tcp
		self.udp = udp

	def __str__(self):
		return ""

class Ddos_src_default_l4_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['tcp', 'udp', 'icmp', 'other'])
	deny=PosRangedInteger(0, 1)
	glid=PosRangedInteger(1, 32000)
	def __init__(self, protocol, deny=None, glid=None, template=None):
		self.protocol = protocol
		self.deny = deny
		self.glid = glid
		self.template = template

	def __str__(self):
		return str(self.protocol)

class Ddos_src_default_app_type__template(AxapiObject):
	__metaclass__ = StructMeta 
	dns=SizedString(1, 255)
	http=SizedString(1, 255)
	ssl_l4=SizedString(1, 255)
	def __init__(self, dns=None, http=None, ssl_l4=None):
		self.dns = dns
		self.http = http
		self.ssl_l4 = ssl_l4

	def __str__(self):
		return ""

class Ddos_src_default_app_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'ssl-l4'])
	def __init__(self, protocol, template=None):
		self.protocol = protocol
		self.template = template

	def __str__(self):
		return str(self.protocol)

class Ddos_src_entry(AxapiObject):
	__metaclass__ = StructMeta 
	src_entry_name=SizedString(1, 63)
	ipv6_addr=SizedString(1, 255)
	ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	subnet_ipv6_addr=SizedString(1, 255)
	def __init__(self, src_entry_name, ipv6_addr=None, ip_addr=None, subnet_ip_addr=None, subnet_ipv6_addr=None, l4_typelist=None, app_typelist=None):
		self.src_entry_name = src_entry_name
		self.ipv6_addr = ipv6_addr
		self.ip_addr = ip_addr
		self.subnet_ip_addr = subnet_ip_addr
		self.subnet_ipv6_addr = subnet_ipv6_addr
		self.l4_typelist = l4_typelist
		self.app_typelist = app_typelist

	def __str__(self):
		return str(self.src_entry_name)

class Ddos_src_entry_l4_type__template(AxapiObject):
	__metaclass__ = StructMeta 
	tcp=SizedString(1, 255)
	udp=SizedString(1, 255)
	def __init__(self, tcp=None, udp=None):
		self.tcp = tcp
		self.udp = udp

	def __str__(self):
		return ""

class Ddos_src_entry_l4_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['tcp', 'udp', 'icmp', 'other'])
	action = Enum(['permit', 'deny'])
	glid=PosRangedInteger(1, 32000)
	def __init__(self, protocol, action=None, glid=None, template=None):
		self.protocol = protocol
		self.action = action
		self.glid = glid
		self.template = template

	def __str__(self):
		return str(self.protocol)

class Ddos_src_entry_app_type__template(AxapiObject):
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

class Ddos_src_entry_app_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'ssl-l4'])
	def __init__(self, protocol, template=None):
		self.protocol = protocol
		self.template = template

	def __str__(self):
		return str(self.protocol)

class Ddos_src_geo_location(AxapiObject):
	__metaclass__ = StructMeta 
	geolocation_name=SizedString(1, 255)
	def __init__(self, geolocation_name, l4_typelist=None, app_typelist=None):
		self.geolocation_name = geolocation_name
		self.l4_typelist = l4_typelist
		self.app_typelist = app_typelist

	def __str__(self):
		return str(self.geolocation_name)

class Ddos_src_geo_location_l4_type__template(AxapiObject):
	__metaclass__ = StructMeta 
	tcp=SizedString(1, 255)
	udp=SizedString(1, 255)
	def __init__(self, tcp=None, udp=None):
		self.tcp = tcp
		self.udp = udp

	def __str__(self):
		return ""

class Ddos_src_geo_location_l4_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['tcp', 'udp', 'icmp', 'other'])
	deny=PosRangedInteger(0, 1)
	glid=PosRangedInteger(1, 32000)
	def __init__(self, protocol, deny=None, glid=None, template=None):
		self.protocol = protocol
		self.deny = deny
		self.glid = glid
		self.template = template

	def __str__(self):
		return str(self.protocol)

class Ddos_src_geo_location_app_type__template(AxapiObject):
	__metaclass__ = StructMeta 
	dns=SizedString(1, 255)
	http=SizedString(1, 255)
	def __init__(self, dns=None, http=None):
		self.dns = dns
		self.http = http

	def __str__(self):
		return ""

class Ddos_src_geo_location_app_type(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['dns-tcp', 'dns-udp', 'http'])
	def __init__(self, protocol, template=None):
		self.protocol = protocol
		self.template = template

	def __str__(self):
		return str(self.protocol)

class DdosSrcClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosSrc(self):
		"""
		Retrieve the src identified by the specified identifier
		
		Returns:
			An instance of the Src class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified src does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('src')
		return deserialize_Src_json(payload)

