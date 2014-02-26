########################################################################################################################
# File name: lldp.py
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
	'https://axapi.a10networks.com/axapi/v3/lldp',
]

def deserialize_Lldp__enable_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable = data.get('enable')
	rx = data.get('rx')
	tx = data.get('tx')
	result = Lldp__enable_cfg(enable=enable, rx=rx, tx=tx)
	return result

def deserialize_Lldp__notification_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	notification = data.get('notification')
	interval = data.get('interval')
	result = Lldp__notification_cfg(notification=notification, interval=interval)
	return result

def deserialize_Lldp__tx_set_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	fast_count = data.get('fast-count')
	fast_interval = data.get('fast-interval')
	hold = data.get('hold')
	tx_interval = data.get('tx-interval')
	reinit_delay = data.get('reinit-delay')
	result = Lldp__tx_set(fast_count=fast_count, fast_interval=fast_interval, hold=hold, tx_interval=tx_interval, reinit_delay=reinit_delay)
	return result

def deserialize_Lldp__management_address__dns_cfg__interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet = data.get('ethernet')
	ve = data.get('ve')
	management = data.get('management')
	result = Lldp__management_address__dns_cfg__interface(ethernet=ethernet, ve=ve, management=management)
	return result

def deserialize_Lldp__management_address__dns_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns = data.get('dns')
	interface = deserialize_Lldp__management_address__dns_cfg__interface_json(data.get('interface'))
	result = Lldp__management_address__dns_cfg(dns=dns, interface=interface)
	return result

def deserialize_Lldp__management_address__ipv4_cfg__interface_ipv4_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4_eth = data.get('ipv4-eth')
	ipv4_ve = data.get('ipv4-ve')
	ipv4_mgmt = data.get('ipv4-mgmt')
	result = Lldp__management_address__ipv4_cfg__interface_ipv4(ipv4_eth=ipv4_eth, ipv4_ve=ipv4_ve, ipv4_mgmt=ipv4_mgmt)
	return result

def deserialize_Lldp__management_address__ipv4_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv4 = data.get('ipv4')
	interface_ipv4 = deserialize_Lldp__management_address__ipv4_cfg__interface_ipv4_json(data.get('interface-ipv4'))
	result = Lldp__management_address__ipv4_cfg(ipv4=ipv4, interface_ipv4=interface_ipv4)
	return result

def deserialize_Lldp__management_address__ipv6_cfg__interface_ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6_eth = data.get('ipv6-eth')
	ipv6_ve = data.get('ipv6-ve')
	ipv6_mgmt = data.get('ipv6-mgmt')
	result = Lldp__management_address__ipv6_cfg__interface_ipv6(ipv6_eth=ipv6_eth, ipv6_ve=ipv6_ve, ipv6_mgmt=ipv6_mgmt)
	return result

def deserialize_Lldp__management_address__ipv6_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6 = data.get('ipv6')
	interface_ipv6 = deserialize_Lldp__management_address__ipv6_cfg__interface_ipv6_json(data.get('interface-ipv6'))
	result = Lldp__management_address__ipv6_cfg(ipv6=ipv6, interface_ipv6=interface_ipv6)
	return result

def deserialize_Lldp__management_address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns_cfg = deserialize_Lldp__management_address__dns_cfg_json(data.get('dns-cfg'))
	ipv4_cfg = deserialize_Lldp__management_address__ipv4_cfg_json(data.get('ipv4-cfg'))
	ipv6_cfg = deserialize_Lldp__management_address__ipv6_cfg_json(data.get('ipv6-cfg'))
	result = Lldp__management_address(dns_cfg=dns_cfg, ipv4_cfg=ipv4_cfg, ipv6_cfg=ipv6_cfg)
	return result

def deserialize_Lldp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	system_name = data.get('system-name')
	system_description = data.get('system-description')
	enable_cfg = deserialize_Lldp__enable_cfg_json(data.get('enable-cfg'))
	notification_cfg = deserialize_Lldp__notification_cfg_json(data.get('notification-cfg'))
	tx_set = deserialize_Lldp__tx_set_json(data.get('tx-set'))
	management_address = deserialize_Lldp__management_address_json(data.get('management-address'))
	result = Lldp(system_name=system_name, system_description=system_description, enable_cfg=enable_cfg, notification_cfg=notification_cfg, tx_set=tx_set, management_address=management_address)
	return result

def serialize_Lldp__enable_cfg_json(obj):
	output = OrderedDict()
	if obj.enable is not None:
		output['enable'] = obj.enable
	if obj.rx is not None:
		output['rx'] = obj.rx
	if obj.tx is not None:
		output['tx'] = obj.tx
	return output

def serialize_Lldp__notification_cfg_json(obj):
	output = OrderedDict()
	if obj.notification is not None:
		output['notification'] = obj.notification
	if obj.interval is not None:
		output['interval'] = obj.interval
	return output

def serialize_Lldp__tx_set_json(obj):
	output = OrderedDict()
	if obj.fast_count is not None:
		output['fast-count'] = obj.fast_count
	if obj.fast_interval is not None:
		output['fast-interval'] = obj.fast_interval
	if obj.hold is not None:
		output['hold'] = obj.hold
	if obj.tx_interval is not None:
		output['tx-interval'] = obj.tx_interval
	if obj.reinit_delay is not None:
		output['reinit-delay'] = obj.reinit_delay
	return output

def serialize_Lldp__management_address__dns_cfg__interface_json(obj):
	output = OrderedDict()
	if obj.ethernet is not None:
		output['ethernet'] = obj.ethernet
	if obj.ve is not None:
		output['ve'] = obj.ve
	if obj.management is not None:
		output['management'] = obj.management
	return output

def serialize_Lldp__management_address__dns_cfg_json(obj):
	output = OrderedDict()
	if obj.dns is not None:
		output['dns'] = obj.dns
	if obj.interface is not None:
		output['interface'] = serialize_Lldp__management_address__dns_cfg__interface_json(obj.interface)
	return output

def serialize_Lldp__management_address__ipv4_cfg__interface_ipv4_json(obj):
	output = OrderedDict()
	if obj.ipv4_eth is not None:
		output['ipv4-eth'] = obj.ipv4_eth
	if obj.ipv4_ve is not None:
		output['ipv4-ve'] = obj.ipv4_ve
	if obj.ipv4_mgmt is not None:
		output['ipv4-mgmt'] = obj.ipv4_mgmt
	return output

def serialize_Lldp__management_address__ipv4_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv4 is not None:
		output['ipv4'] = obj.ipv4
	if obj.interface_ipv4 is not None:
		output['interface-ipv4'] = serialize_Lldp__management_address__ipv4_cfg__interface_ipv4_json(obj.interface_ipv4)
	return output

def serialize_Lldp__management_address__ipv6_cfg__interface_ipv6_json(obj):
	output = OrderedDict()
	if obj.ipv6_eth is not None:
		output['ipv6-eth'] = obj.ipv6_eth
	if obj.ipv6_ve is not None:
		output['ipv6-ve'] = obj.ipv6_ve
	if obj.ipv6_mgmt is not None:
		output['ipv6-mgmt'] = obj.ipv6_mgmt
	return output

def serialize_Lldp__management_address__ipv6_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv6 is not None:
		output['ipv6'] = obj.ipv6
	if obj.interface_ipv6 is not None:
		output['interface-ipv6'] = serialize_Lldp__management_address__ipv6_cfg__interface_ipv6_json(obj.interface_ipv6)
	return output

def serialize_Lldp__management_address_json(obj):
	output = OrderedDict()
	if obj.dns_cfg is not None:
		output['dns-cfg'] = serialize_Lldp__management_address__dns_cfg_json(obj.dns_cfg)
	if obj.ipv4_cfg is not None:
		output['ipv4-cfg'] = serialize_Lldp__management_address__ipv4_cfg_json(obj.ipv4_cfg)
	if obj.ipv6_cfg is not None:
		output['ipv6-cfg'] = serialize_Lldp__management_address__ipv6_cfg_json(obj.ipv6_cfg)
	return output

def serialize_Lldp_json(obj):
	output = OrderedDict()
	if obj.system_name is not None:
		output['system-name'] = obj.system_name
	if obj.system_description is not None:
		output['system-description'] = obj.system_description
	if obj.enable_cfg is not None:
		output['enable-cfg'] = serialize_Lldp__enable_cfg_json(obj.enable_cfg)
	if obj.notification_cfg is not None:
		output['notification-cfg'] = serialize_Lldp__notification_cfg_json(obj.notification_cfg)
	if obj.tx_set is not None:
		output['tx-set'] = serialize_Lldp__tx_set_json(obj.tx_set)
	if obj.management_address is not None:
		output['management-address'] = serialize_Lldp__management_address_json(obj.management_address)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Lldp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Lldp_json(item))
	return list(container)

class Lldp__enable_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	enable=PosRangedInteger(0, 1)
	rx=PosRangedInteger(0, 1)
	tx=PosRangedInteger(0, 1)
	def __init__(self, enable=None, rx=None, tx=None):
		self.enable = enable
		self.rx = rx
		self.tx = tx

	def __str__(self):
		return ""

class Lldp__notification_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	notification=PosRangedInteger(0, 1)
	interval=PosRangedInteger(5, 3600)
	def __init__(self, notification=None, interval=None):
		self.notification = notification
		self.interval = interval

	def __str__(self):
		return ""

class Lldp__tx_set(AxapiObject):
	__metaclass__ = StructMeta 
	fast_count=PosRangedInteger(1, 8)
	fast_interval=PosRangedInteger(1, 3600)
	hold=PosRangedInteger(1, 10)
	tx_interval=PosRangedInteger(1, 3600)
	reinit_delay=PosRangedInteger(1, 10)
	def __init__(self, fast_count=None, fast_interval=None, hold=None, tx_interval=None, reinit_delay=None):
		self.fast_count = fast_count
		self.fast_interval = fast_interval
		self.hold = hold
		self.tx_interval = tx_interval
		self.reinit_delay = reinit_delay

	def __str__(self):
		return ""

class Lldp__management_address__dns_cfg__interface(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet=PosRangedInteger(1, 2048)
	ve=PosRangedInteger(1, 4094)
	management=PosRangedInteger(0, 1)
	def __init__(self, ethernet=None, ve=None, management=None):
		self.ethernet = ethernet
		self.ve = ve
		self.management = management

	def __str__(self):
		return ""

class Lldp__management_address__dns_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	dns=SizedString(1, 31)
	def __init__(self, dns=None, interface=None):
		self.dns = dns
		self.interface = interface

	def __str__(self):
		return ""

class Lldp__management_address__ipv4_cfg__interface_ipv4(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4_eth=PosRangedInteger(1, 2048)
	ipv4_ve=PosRangedInteger(1, 4094)
	ipv4_mgmt=PosRangedInteger(0, 1)
	def __init__(self, ipv4_eth=None, ipv4_ve=None, ipv4_mgmt=None):
		self.ipv4_eth = ipv4_eth
		self.ipv4_ve = ipv4_ve
		self.ipv4_mgmt = ipv4_mgmt

	def __str__(self):
		return ""

class Lldp__management_address__ipv4_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ipv4=None, interface_ipv4=None):
		self.ipv4 = ipv4
		self.interface_ipv4 = interface_ipv4

	def __str__(self):
		return ""

class Lldp__management_address__ipv6_cfg__interface_ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6_eth=PosRangedInteger(1, 2048)
	ipv6_ve=PosRangedInteger(1, 4094)
	ipv6_mgmt=PosRangedInteger(0, 1)
	def __init__(self, ipv6_eth=None, ipv6_ve=None, ipv6_mgmt=None):
		self.ipv6_eth = ipv6_eth
		self.ipv6_ve = ipv6_ve
		self.ipv6_mgmt = ipv6_mgmt

	def __str__(self):
		return ""

class Lldp__management_address__ipv6_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6=SizedString(1, 255)
	def __init__(self, ipv6=None, interface_ipv6=None):
		self.ipv6 = ipv6
		self.interface_ipv6 = interface_ipv6

	def __str__(self):
		return ""

class Lldp__management_address(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, dns_cfg=None, ipv4_cfg=None, ipv6_cfg=None):
		self.dns_cfg = dns_cfg
		self.ipv4_cfg = ipv4_cfg
		self.ipv6_cfg = ipv6_cfg

	def __str__(self):
		return ""

class Lldp(AxapiObject):
	__metaclass__ = StructMeta 
	system_name=SizedString(1, 255)
	system_description=SizedString(1, 127)
	def __init__(self, system_name=None, system_description=None, enable_cfg=None, notification_cfg=None, tx_set=None, management_address=None):
		self.system_name = system_name
		self.system_description = system_description
		self.enable_cfg = enable_cfg
		self.notification_cfg = notification_cfg
		self.tx_set = tx_set
		self.management_address = management_address

	def __str__(self):
		return ""

class LldpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLldp(self):
		"""
		Retrieve the lldp identified by the specified identifier
		
		Returns:
			An instance of the Lldp class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified lldp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('lldp')
		return deserialize_Lldp_json(payload)

	def putLldp(self, lldp):
		"""
		Replace the object lldp
		
		Args:
			lldp An instance of the Lldp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['lldp']=serialize_Lldp_json(lldp)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + query, payload, headers)
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

	def deleteLldp(self):
		"""
		Remove the lldp identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified lldp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllLldpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitLldp(self, lldp):
		"""
		Create the object lldp
		
		Args:
			lldp An instance of the Lldp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['lldp']=serialize_Lldp_json(lldp)
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

	def getAllLldps(self):
		"""
		Retrieve all lldp objects currently pending in the system
		
		Returns:
			A list of Lldp objects
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
			payload= data.get('lldpList')
		return deserialize_list_Lldp_json(payload)

