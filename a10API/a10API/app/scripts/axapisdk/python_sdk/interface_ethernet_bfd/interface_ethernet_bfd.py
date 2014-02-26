########################################################################################################################
# File name: interface_ethernet_bfd.py
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
	'https://axapi.a10networks.com/axapi/v3/interface/ethernet/bfd',
]

def deserialize_Bfd__authentication__key_id_cfg__md5_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	md5 = data.get('md5')
	password = data.get('password')
	encrypted = data.get('encrypted')
	result = Bfd__authentication__key_id_cfg__md5_cfg(md5=md5, password=password, encrypted=encrypted)
	return result

def deserialize_Bfd__authentication__key_id_cfg__meticulous_md5_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	meticulous_md5 = data.get('meticulous-md5')
	password = data.get('password')
	encrypted = data.get('encrypted')
	result = Bfd__authentication__key_id_cfg__meticulous_md5_cfg(meticulous_md5=meticulous_md5, password=password, encrypted=encrypted)
	return result

def deserialize_Bfd__authentication__key_id_cfg__meticulous_sha1_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	meticulous_sha1 = data.get('meticulous-sha1')
	password = data.get('password')
	encrypted = data.get('encrypted')
	result = Bfd__authentication__key_id_cfg__meticulous_sha1_cfg(meticulous_sha1=meticulous_sha1, password=password, encrypted=encrypted)
	return result

def deserialize_Bfd__authentication__key_id_cfg__sha1_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sha1 = data.get('sha1')
	password = data.get('password')
	encrypted = data.get('encrypted')
	result = Bfd__authentication__key_id_cfg__sha1_cfg(sha1=sha1, password=password, encrypted=encrypted)
	return result

def deserialize_Bfd__authentication__key_id_cfg__simple_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	simple = data.get('simple')
	password = data.get('password')
	encrypted = data.get('encrypted')
	result = Bfd__authentication__key_id_cfg__simple_cfg(simple=simple, password=password, encrypted=encrypted)
	return result

def deserialize_Bfd__authentication__key_id_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key_id = data.get('key-id')
	md5_cfg = deserialize_Bfd__authentication__key_id_cfg__md5_cfg_json(data.get('md5-cfg'))
	meticulous_md5_cfg = deserialize_Bfd__authentication__key_id_cfg__meticulous_md5_cfg_json(data.get('meticulous-md5-cfg'))
	meticulous_sha1_cfg = deserialize_Bfd__authentication__key_id_cfg__meticulous_sha1_cfg_json(data.get('meticulous-sha1-cfg'))
	sha1_cfg = deserialize_Bfd__authentication__key_id_cfg__sha1_cfg_json(data.get('sha1-cfg'))
	simple_cfg = deserialize_Bfd__authentication__key_id_cfg__simple_cfg_json(data.get('simple-cfg'))
	result = Bfd__authentication__key_id_cfg(key_id=key_id, md5_cfg=md5_cfg, meticulous_md5_cfg=meticulous_md5_cfg, meticulous_sha1_cfg=meticulous_sha1_cfg, sha1_cfg=sha1_cfg, simple_cfg=simple_cfg)
	return result

def deserialize_Bfd__authentication_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	key_id_cfg = deserialize_Bfd__authentication__key_id_cfg_json(data.get('key-id-cfg'))
	result = Bfd__authentication(key_id_cfg=key_id_cfg)
	return result

def deserialize_Bfd__echo_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	echo = data.get('echo')
	demand = data.get('demand')
	result = Bfd__echo_cfg(echo=echo, demand=demand)
	return result

def deserialize_Interface_ethernet_bfd_multiplier_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	multiplier_value = data.get('multiplier-value')
	result = Interface_ethernet_bfd_multiplier(multiplier_value=multiplier_value)
	return result

def deserialize_list_Interface_ethernet_bfd_multiplier_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Interface_ethernet_bfd_multiplier_json(item))
	return list(container)

def deserialize_Bfd__interval_cfg__min_rx_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	min_rx_value = data.get('min-rx-value')
	multiplier = deserialize_list_Interface_ethernet_bfd_multiplier_json(data.get('multiplier'))
	result = Bfd__interval_cfg__min_rx(min_rx_value=min_rx_value, multiplier=multiplier)
	return result

def deserialize_Bfd__interval_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	interval = data.get('interval')
	interval_value = data.get('interval-value')
	min_rx = deserialize_Bfd__interval_cfg__min_rx_json(data.get('min-rx'))
	result = Bfd__interval_cfg(interval=interval, interval_value=interval_value, min_rx=min_rx)
	return result

def deserialize_Bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	authentication = deserialize_Bfd__authentication_json(data.get('authentication'))
	echo_cfg = deserialize_Bfd__echo_cfg_json(data.get('echo-cfg'))
	interval_cfg = deserialize_Bfd__interval_cfg_json(data.get('interval-cfg'))
	result = Bfd(authentication=authentication, echo_cfg=echo_cfg, interval_cfg=interval_cfg)
	return result

def serialize_Bfd__authentication__key_id_cfg__md5_cfg_json(obj):
	output = OrderedDict()
	if obj.md5 is not None:
		output['md5'] = obj.md5
	if obj.password is not None:
		output['password'] = obj.password
	if obj.encrypted is not None:
		output['encrypted'] = obj.encrypted
	return output

def serialize_Bfd__authentication__key_id_cfg__meticulous_md5_cfg_json(obj):
	output = OrderedDict()
	if obj.meticulous_md5 is not None:
		output['meticulous-md5'] = obj.meticulous_md5
	if obj.password is not None:
		output['password'] = obj.password
	if obj.encrypted is not None:
		output['encrypted'] = obj.encrypted
	return output

def serialize_Bfd__authentication__key_id_cfg__meticulous_sha1_cfg_json(obj):
	output = OrderedDict()
	if obj.meticulous_sha1 is not None:
		output['meticulous-sha1'] = obj.meticulous_sha1
	if obj.password is not None:
		output['password'] = obj.password
	if obj.encrypted is not None:
		output['encrypted'] = obj.encrypted
	return output

def serialize_Bfd__authentication__key_id_cfg__sha1_cfg_json(obj):
	output = OrderedDict()
	if obj.sha1 is not None:
		output['sha1'] = obj.sha1
	if obj.password is not None:
		output['password'] = obj.password
	if obj.encrypted is not None:
		output['encrypted'] = obj.encrypted
	return output

def serialize_Bfd__authentication__key_id_cfg__simple_cfg_json(obj):
	output = OrderedDict()
	if obj.simple is not None:
		output['simple'] = obj.simple
	if obj.password is not None:
		output['password'] = obj.password
	if obj.encrypted is not None:
		output['encrypted'] = obj.encrypted
	return output

def serialize_Bfd__authentication__key_id_cfg_json(obj):
	output = OrderedDict()
	if obj.key_id is not None:
		output['key-id'] = obj.key_id
	if obj.md5_cfg is not None:
		output['md5-cfg'] = serialize_Bfd__authentication__key_id_cfg__md5_cfg_json(obj.md5_cfg)
	if obj.meticulous_md5_cfg is not None:
		output['meticulous-md5-cfg'] = serialize_Bfd__authentication__key_id_cfg__meticulous_md5_cfg_json(obj.meticulous_md5_cfg)
	if obj.meticulous_sha1_cfg is not None:
		output['meticulous-sha1-cfg'] = serialize_Bfd__authentication__key_id_cfg__meticulous_sha1_cfg_json(obj.meticulous_sha1_cfg)
	if obj.sha1_cfg is not None:
		output['sha1-cfg'] = serialize_Bfd__authentication__key_id_cfg__sha1_cfg_json(obj.sha1_cfg)
	if obj.simple_cfg is not None:
		output['simple-cfg'] = serialize_Bfd__authentication__key_id_cfg__simple_cfg_json(obj.simple_cfg)
	return output

def serialize_Bfd__authentication_json(obj):
	output = OrderedDict()
	if obj.key_id_cfg is not None:
		output['key-id-cfg'] = serialize_Bfd__authentication__key_id_cfg_json(obj.key_id_cfg)
	return output

def serialize_Bfd__echo_cfg_json(obj):
	output = OrderedDict()
	if obj.echo is not None:
		output['echo'] = obj.echo
	if obj.demand is not None:
		output['demand'] = obj.demand
	return output

def serialize_Interface_ethernet_bfd_multiplier_json(obj):
	output = OrderedDict()
	if obj.multiplier_value is not None:
		output['multiplier-value'] = obj.multiplier_value
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Interface_ethernet_bfd_multiplier_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Interface_ethernet_bfd_multiplier_json(item))
	return output

def serialize_Bfd__interval_cfg__min_rx_json(obj):
	output = OrderedDict()
	if obj.min_rx_value is not None:
		output['min-rx-value'] = obj.min_rx_value
	if obj.multiplier is not None:
		output['multiplier'] = serialize_list_Interface_ethernet_bfd_multiplier_json(obj.multiplier)
	return output

def serialize_Bfd__interval_cfg_json(obj):
	output = OrderedDict()
	if obj.interval is not None:
		output['interval'] = obj.interval
	if obj.interval_value is not None:
		output['interval-value'] = obj.interval_value
	if obj.min_rx is not None:
		output['min-rx'] = serialize_Bfd__interval_cfg__min_rx_json(obj.min_rx)
	return output

def serialize_Bfd_json(obj):
	output = OrderedDict()
	if obj.authentication is not None:
		output['authentication'] = serialize_Bfd__authentication_json(obj.authentication)
	if obj.echo_cfg is not None:
		output['echo-cfg'] = serialize_Bfd__echo_cfg_json(obj.echo_cfg)
	if obj.interval_cfg is not None:
		output['interval-cfg'] = serialize_Bfd__interval_cfg_json(obj.interval_cfg)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Bfd_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Bfd_json(item))
	return list(container)

class Bfd__authentication__key_id_cfg__md5_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	md5=PosRangedInteger(0, 1)
	password=SizedString(1, 16)
	encrypted=SizedString(1, 255)
	def __init__(self, md5=None, password=None, encrypted=None):
		self.md5 = md5
		self.password = password
		self.encrypted = encrypted

	def __str__(self):
		return ""

class Bfd__authentication__key_id_cfg__meticulous_md5_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	meticulous_md5=PosRangedInteger(0, 1)
	password=SizedString(1, 16)
	encrypted=SizedString(1, 255)
	def __init__(self, meticulous_md5=None, password=None, encrypted=None):
		self.meticulous_md5 = meticulous_md5
		self.password = password
		self.encrypted = encrypted

	def __str__(self):
		return ""

class Bfd__authentication__key_id_cfg__meticulous_sha1_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	meticulous_sha1=PosRangedInteger(0, 1)
	password=SizedString(1, 16)
	encrypted=SizedString(1, 255)
	def __init__(self, meticulous_sha1=None, password=None, encrypted=None):
		self.meticulous_sha1 = meticulous_sha1
		self.password = password
		self.encrypted = encrypted

	def __str__(self):
		return ""

class Bfd__authentication__key_id_cfg__sha1_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	sha1=PosRangedInteger(0, 1)
	password=SizedString(1, 16)
	encrypted=SizedString(1, 255)
	def __init__(self, sha1=None, password=None, encrypted=None):
		self.sha1 = sha1
		self.password = password
		self.encrypted = encrypted

	def __str__(self):
		return ""

class Bfd__authentication__key_id_cfg__simple_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	simple=PosRangedInteger(0, 1)
	password=SizedString(1, 16)
	encrypted=SizedString(1, 255)
	def __init__(self, simple=None, password=None, encrypted=None):
		self.simple = simple
		self.password = password
		self.encrypted = encrypted

	def __str__(self):
		return ""

class Bfd__authentication__key_id_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	key_id=PosRangedInteger(0, 255)
	def __init__(self, key_id=None, md5_cfg=None, meticulous_md5_cfg=None, meticulous_sha1_cfg=None, sha1_cfg=None, simple_cfg=None):
		self.key_id = key_id
		self.md5_cfg = md5_cfg
		self.meticulous_md5_cfg = meticulous_md5_cfg
		self.meticulous_sha1_cfg = meticulous_sha1_cfg
		self.sha1_cfg = sha1_cfg
		self.simple_cfg = simple_cfg

	def __str__(self):
		return ""

class Bfd__authentication(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, key_id_cfg=None):
		self.key_id_cfg = key_id_cfg

	def __str__(self):
		return ""

class Bfd__echo_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	echo=PosRangedInteger(0, 1)
	demand=PosRangedInteger(0, 1)
	def __init__(self, echo=None, demand=None):
		self.echo = echo
		self.demand = demand

	def __str__(self):
		return ""

class Bfd__interval_cfg__min_rx(AxapiObject):
	__metaclass__ = StructMeta 
	min_rx_value=PosRangedInteger(48, 1000)
	def __init__(self, min_rx_value=None, multiplier=None):
		self.min_rx_value = min_rx_value
		self.multiplier = multiplier

	def __str__(self):
		return ""

class Bfd__interval_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	interval=PosRangedInteger(0, 1)
	interval_value=PosRangedInteger(48, 1000)
	def __init__(self, interval=None, interval_value=None, min_rx=None):
		self.interval = interval
		self.interval_value = interval_value
		self.min_rx = min_rx

	def __str__(self):
		return ""

class Bfd(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, authentication=None, echo_cfg=None, interval_cfg=None):
		self.authentication = authentication
		self.echo_cfg = echo_cfg
		self.interval_cfg = interval_cfg

	def __str__(self):
		return ""

class Interface_ethernet_bfd_multiplier(AxapiObject):
	__metaclass__ = StructMeta 
	multiplier_value=PosRangedInteger(3, 50)
	def __init__(self, multiplier_value=None):
		self.multiplier_value = multiplier_value

	def __str__(self):
		return ""

class InterfaceEthernetBfdClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getInterfaceEthernetBfd(self):
		"""
		Retrieve the bfd identified by the specified identifier
		
		Returns:
			An instance of the Bfd class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bfd does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('bfd')
		return deserialize_Bfd_json(payload)

	def putInterfaceEthernetBfd(self, bfd):
		"""
		Replace the object bfd
		
		Args:
			bfd An instance of the Bfd class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bfd']=serialize_Bfd_json(bfd)
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

	def deleteInterfaceEthernetBfd(self):
		"""
		Remove the bfd identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified bfd does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllInterfaceEthernetBfdsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitInterfaceEthernetBfd(self, bfd):
		"""
		Create the object bfd
		
		Args:
			bfd An instance of the Bfd class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['bfd']=serialize_Bfd_json(bfd)
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

	def getAllInterfaceEthernetBfds(self):
		"""
		Retrieve all bfd objects currently pending in the system
		
		Returns:
			A list of Bfd objects
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
			payload= data.get('bfdList')
		return deserialize_list_Bfd_json(payload)

