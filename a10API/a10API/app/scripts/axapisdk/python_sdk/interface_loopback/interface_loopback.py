########################################################################################################################
# File name: interface_loopback.py
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
	'https://axapi.a10networks.com/axapi/v3/interface/loopback',
]

def deserialize_Loopback__snmp_server_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	snmp_server = data.get('snmp-server')
	trap_source = data.get('trap-source')
	result = Loopback__snmp_server_cfg(snmp_server=snmp_server, trap_source=trap_source)
	return result

def deserialize_Interface_loopback_address_val_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val = data.get('address_val')
	netmask = data.get('netmask')
	result = Interface_loopback_address_val_cfg(address_val=address_val, netmask=netmask)
	return result

def deserialize_list_Interface_loopback_address_val_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_loopback_address_val_cfg_json(item))
	return list(container)

def deserialize_Loopback__ip__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_val_cfg = deserialize_list_Interface_loopback_address_val_cfg_json(data.get('address_val-cfg'))
	result = Loopback__ip__address(address_val_cfg=address_val_cfg)
	return result

def deserialize_Loopback__ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Loopback__ip__address_json(data.get('address'))
	result = Loopback__ip(address=address)
	return result

def deserialize_Interface_loopback_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_addr = data.get('ipv6-addr')
	anycast = data.get('anycast')
	link_local = data.get('link-local')
	result = Interface_loopback_address_cfg(ipv6_addr=ipv6_addr, anycast=anycast, link_local=link_local)
	return result

def deserialize_list_Interface_loopback_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_loopback_address_cfg_json(item))
	return list(container)

def deserialize_Loopback__ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address_cfg = deserialize_list_Interface_loopback_address_cfg_json(data.get('address-cfg'))
	ipv6_enable = data.get('ipv6-enable')
	result = Loopback__ipv6(address_cfg=address_cfg, ipv6_enable=ipv6_enable)
	return result

def deserialize_Loopback_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ifnum = data.get('ifnum')
	snmp_server_cfg = deserialize_Loopback__snmp_server_cfg_json(data.get('snmp-server-cfg'))
	ip = deserialize_Loopback__ip_json(data.get('ip'))
	ipv6 = deserialize_Loopback__ipv6_json(data.get('ipv6'))
	result = Loopback(ifnum=ifnum, snmp_server_cfg=snmp_server_cfg, ip=ip, ipv6=ipv6)
	return result

def serialize_Loopback__snmp_server_cfg_json(obj):
	output = OrderedDict()
	if obj.snmp_server is not None:
		output['snmp-server'] = obj.snmp_server
	if obj.trap_source is not None:
		output['trap-source'] = obj.trap_source
	return output

def serialize_Interface_loopback_address_val_cfg_json(obj):
	output = OrderedDict()
	if obj.address_val is not None:
		output['address_val'] = obj.address_val
	if obj.netmask is not None:
		output['netmask'] = obj.netmask
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Interface_loopback_address_val_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_loopback_address_val_cfg_json(item))
	return output

def serialize_Loopback__ip__address_json(obj):
	output = OrderedDict()
	if obj.address_val_cfg is not None:
		output['address_val-cfg'] = serialize_list_Interface_loopback_address_val_cfg_json(obj.address_val_cfg)
	return output

def serialize_Loopback__ip_json(obj):
	output = OrderedDict()
	if obj.address is not None:
		output['address'] = serialize_Loopback__ip__address_json(obj.address)
	return output

def serialize_Interface_loopback_address_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv6_addr is not None:
		output['ipv6-addr'] = obj.ipv6_addr
	if obj.anycast is not None:
		output['anycast'] = obj.anycast
	if obj.link_local is not None:
		output['link-local'] = obj.link_local
	return output

def serialize_list_Interface_loopback_address_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_loopback_address_cfg_json(item))
	return output

def serialize_Loopback__ipv6_json(obj):
	output = OrderedDict()
	if obj.address_cfg is not None:
		output['address-cfg'] = serialize_list_Interface_loopback_address_cfg_json(obj.address_cfg)
	if obj.ipv6_enable is not None:
		output['ipv6-enable'] = obj.ipv6_enable
	return output

def serialize_Loopback_json(obj):
	output = OrderedDict()
	output['ifnum'] = obj.ifnum
	if obj.snmp_server_cfg is not None:
		output['snmp-server-cfg'] = serialize_Loopback__snmp_server_cfg_json(obj.snmp_server_cfg)
	if obj.ip is not None:
		output['ip'] = serialize_Loopback__ip_json(obj.ip)
	if obj.ipv6 is not None:
		output['ipv6'] = serialize_Loopback__ipv6_json(obj.ipv6)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Loopback_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Loopback_json(item))
	return list(container)

class Loopback__snmp_server_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	snmp_server=PosRangedInteger(0, 1)
	trap_source=PosRangedInteger(0, 1)
	def __init__(self, snmp_server=None, trap_source=None):
		self.snmp_server = snmp_server
		self.trap_source = trap_source

	def __str__(self):
		return ""

class Loopback__ip__address(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address_val_cfg=None):
		self.address_val_cfg = address_val_cfg

	def __str__(self):
		return ""

class Loopback__ip(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address=None):
		self.address = address

	def __str__(self):
		return ""

class Loopback__ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_enable=PosRangedInteger(0, 1)
	def __init__(self, address_cfg=None, ipv6_enable=None):
		self.address_cfg = address_cfg
		self.ipv6_enable = ipv6_enable

	def __str__(self):
		return ""

class Loopback(AxapiObject):
	__metaclass__ = StructMeta 
	ifnum=PosRangedInteger(0, 9)
	def __init__(self, ifnum, snmp_server_cfg=None, ip=None, ipv6=None):
		self.ifnum = ifnum
		self.snmp_server_cfg = snmp_server_cfg
		self.ip = ip
		self.ipv6 = ipv6

	def __str__(self):
		return str(self.ifnum)

class Interface_loopback_address_val_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	address_val = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, address_val=None, netmask=None):
		self.address_val = address_val
		self.netmask = netmask

	def __str__(self):
		return ""

class Loopback_ifnum(AxapiObject):
	__metaclass__ = StructMeta 
	ifnum=PosRangedInteger(0, 9)
	def __init__(self, ifnum):
		self.ifnum = ifnum

	def __str__(self):
		return str(self.ifnum)

class Interface_loopback_address_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_addr=SizedString(1, 255)
	anycast=PosRangedInteger(0, 1)
	link_local=PosRangedInteger(0, 1)
	def __init__(self, ipv6_addr=None, anycast=None, link_local=None):
		self.ipv6_addr = ipv6_addr
		self.anycast = anycast
		self.link_local = link_local

	def __str__(self):
		return ""

class InterfaceLoopbackClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getInterfaceLoopback(self, loopback_ifnum):
		"""
		Retrieve the loopback identified by the specified identifier
		
		Args:
			loopback_ifnum Loopback_ifnum
		
		Returns:
			An instance of the Loopback class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(loopback_ifnum) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified loopback does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('loopback')
		return deserialize_Loopback_json(payload)

	def putInterfaceLoopback(self, loopback_ifnum, loopback):
		"""
		Replace the object loopback
		
		Args:
			loopback_ifnum Loopback_ifnum
			loopback An instance of the Loopback class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['loopback']=serialize_Loopback_json(loopback)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(loopback_ifnum) .replace("/", "%2f") + query, payload, headers)
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

	def deleteInterfaceLoopback(self, loopback_ifnum):
		"""
		Remove the loopback identified by the specified identifier from the system
		
		Args:
			loopback_ifnum Loopback_ifnum
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(loopback_ifnum) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified loopback does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllInterfaceLoopbacksClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitInterfaceLoopback(self, loopback):
		"""
		Create the object loopback
		
		Args:
			loopback An instance of the Loopback class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['loopback']=serialize_Loopback_json(loopback)
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

	def getAllInterfaceLoopbacks(self):
		"""
		Retrieve all loopback objects currently pending in the system
		
		Returns:
			A list of Loopback objects
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
			payload= data.get('loopbackList')
		return deserialize_list_Loopback_json(payload)

