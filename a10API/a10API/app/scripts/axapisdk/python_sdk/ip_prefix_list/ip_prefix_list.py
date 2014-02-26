########################################################################################################################
# File name: ip_prefix_list.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/prefix-list',
]

def deserialize_Ip_prefix_list_rules__action_cfg__ipaddr_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipaddr = data.get('ipaddr')
	ge = data.get('ge')
	le = data.get('le')
	result = Ip_prefix_list_rules__action_cfg__ipaddr_cfg(ipaddr=ipaddr, ge=ge, le=le)
	return result

def deserialize_Ip_prefix_list_rules__action_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	action = data.get('action')
	any = data.get('any')
	ipaddr_cfg = deserialize_Ip_prefix_list_rules__action_cfg__ipaddr_cfg_json(data.get('ipaddr-cfg'))
	result = Ip_prefix_list_rules__action_cfg(action=action, any=any, ipaddr_cfg=ipaddr_cfg)
	return result

def deserialize_Ip_prefix_list_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	seq = data.get('seq')
	action_cfg = deserialize_Ip_prefix_list_rules__action_cfg_json(data.get('action-cfg'))
	result = Ip_prefix_list_rules(seq=seq, action_cfg=action_cfg)
	return result

def deserialize_list_Ip_prefix_list_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_prefix_list_rules_json(item))
	return list(container)

def deserialize_Prefix_list__name_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	rules = deserialize_list_Ip_prefix_list_rules_json(data.get('rules'))
	result = Prefix_list__name_cfg(name=name, rules=rules)
	return result

def deserialize_Prefix_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name_cfg = deserialize_Prefix_list__name_cfg_json(data.get('name-cfg'))
	result = Prefix_list(name_cfg=name_cfg)
	return result

def serialize_Ip_prefix_list_rules__action_cfg__ipaddr_cfg_json(obj):
	output = OrderedDict()
	if obj.ipaddr is not None:
		output['ipaddr'] = obj.ipaddr
	if obj.ge is not None:
		output['ge'] = obj.ge
	if obj.le is not None:
		output['le'] = obj.le
	return output

def serialize_Ip_prefix_list_rules__action_cfg_json(obj):
	output = OrderedDict()
	if obj.action is not None:
		output['action'] = obj.action
	if obj.any is not None:
		output['any'] = obj.any
	if obj.ipaddr_cfg is not None:
		output['ipaddr-cfg'] = serialize_Ip_prefix_list_rules__action_cfg__ipaddr_cfg_json(obj.ipaddr_cfg)
	return output

def serialize_Ip_prefix_list_rules_json(obj):
	output = OrderedDict()
	if obj.seq is not None:
		output['seq'] = obj.seq
	if obj.action_cfg is not None:
		output['action-cfg'] = serialize_Ip_prefix_list_rules__action_cfg_json(obj.action_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ip_prefix_list_rules_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_prefix_list_rules_json(item))
	return output

def serialize_Prefix_list__name_cfg_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.rules is not None:
		output['rules'] = serialize_list_Ip_prefix_list_rules_json(obj.rules)
	return output

def serialize_Prefix_list_json(obj):
	output = OrderedDict()
	output['name-cfg'] = serialize_Prefix_list__name_cfg_json(obj.name_cfg)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Prefix_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Prefix_list_json(item))
	return list(container)

class Prefix_list__name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name, rules=None):
		self.name = name
		self.rules = rules

	def __str__(self):
		return str(self.name)

class Prefix_list(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, name_cfg):
		self.name_cfg = name_cfg

	def __str__(self):
		return str(self.name_cfg)

class Prefix_list_name_cfg__name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name, rules=None):
		self.name = name
		self.rules = rules

	def __str__(self):
		return str(self.name)

class Prefix_list_name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, name_cfg):
		self.name_cfg = name_cfg

	def __str__(self):
		return str(self.name_cfg)

class Ip_prefix_list_rules__action_cfg__ipaddr_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipaddr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ge=PosRangedInteger(0, 32)
	le=PosRangedInteger(0, 32)
	def __init__(self, ipaddr=None, ge=None, le=None):
		self.ipaddr = ipaddr
		self.ge = ge
		self.le = le

	def __str__(self):
		return ""

class Ip_prefix_list_rules__action_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	action = Enum(['deny', 'permit'])
	any=PosRangedInteger(0, 1)
	def __init__(self, action=None, any=None, ipaddr_cfg=None):
		self.action = action
		self.any = any
		self.ipaddr_cfg = ipaddr_cfg

	def __str__(self):
		return ""

class Ip_prefix_list_rules(AxapiObject):
	__metaclass__ = StructMeta 
	seq=PosRangedInteger(1, 4294967295)
	def __init__(self, seq=None, action_cfg=None):
		self.seq = seq
		self.action_cfg = action_cfg

	def __str__(self):
		return ""

class IpPrefixlistClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpPrefixlist(self, prefix_list_name_cfg):
		"""
		Retrieve the prefix_list identified by the specified identifier
		
		Args:
			prefix_list_name_cfg Prefix_list_name_cfg
		
		Returns:
			An instance of the Prefix_list class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(prefix_list_name_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified prefix_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('prefix-list')
		return deserialize_Prefix_list_json(payload)

	def putIpPrefixlist(self, prefix_list_name_cfg, prefix_list):
		"""
		Replace the object prefix_list
		
		Args:
			prefix_list_name_cfg Prefix_list_name_cfg
			prefix_list An instance of the Prefix_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['prefix-list']=serialize_Prefix_list_json(prefix_list)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(prefix_list_name_cfg) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpPrefixlist(self, prefix_list_name_cfg):
		"""
		Remove the prefix_list identified by the specified identifier from the system
		
		Args:
			prefix_list_name_cfg Prefix_list_name_cfg
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(prefix_list_name_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified prefix_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpPrefixlistsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpPrefixlist(self, prefix_list):
		"""
		Create the object prefix_list
		
		Args:
			prefix_list An instance of the Prefix_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['prefix-list']=serialize_Prefix_list_json(prefix_list)
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

	def getAllIpPrefixlists(self):
		"""
		Retrieve all prefix_list objects currently pending in the system
		
		Returns:
			A list of Prefix_list objects
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
			payload= data.get('prefix-listList')
		return deserialize_list_Prefix_list_json(payload)

