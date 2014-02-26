########################################################################################################################
# File name: terminal.py
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
	'https://axapi.a10networks.com/axapi/v3/terminal',
]

def deserialize_Terminal__gslb_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	gslb_prompt = data.get('gslb-prompt')
	disable = data.get('disable')
	group_role = data.get('group-role')
	symbol = data.get('symbol')
	result = Terminal__gslb_cfg(gslb_prompt=gslb_prompt, disable=disable, group_role=group_role, symbol=symbol)
	return result

def deserialize_Terminal__history_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	history = data.get('history')
	size = data.get('size')
	result = Terminal__history_cfg(history=history, size=size)
	return result

def deserialize_Terminal__prompt_cfg__vcs_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	vcs_status = data.get('vcs-status')
	result = Terminal__prompt_cfg__vcs_cfg(vcs_status=vcs_status)
	return result

def deserialize_Terminal__prompt_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	prompt = data.get('prompt')
	ha_status = data.get('ha-status')
	hostname = data.get('hostname')
	vcs_cfg = deserialize_Terminal__prompt_cfg__vcs_cfg_json(data.get('vcs-cfg'))
	result = Terminal__prompt_cfg(prompt=prompt, ha_status=ha_status, hostname=hostname, vcs_cfg=vcs_cfg)
	return result

def deserialize_Terminal_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	auto_size = data.get('auto-size')
	editing = data.get('editing')
	gslb_cfg = deserialize_Terminal__gslb_cfg_json(data.get('gslb-cfg'))
	history_cfg = deserialize_Terminal__history_cfg_json(data.get('history-cfg'))
	idle_timeout = data.get('idle-timeout')
	length = data.get('length')
	prompt_cfg = deserialize_Terminal__prompt_cfg_json(data.get('prompt-cfg'))
	width = data.get('width')
	result = Terminal(auto_size=auto_size, editing=editing, gslb_cfg=gslb_cfg, history_cfg=history_cfg, idle_timeout=idle_timeout, length=length, prompt_cfg=prompt_cfg, width=width)
	return result

def serialize_Terminal__gslb_cfg_json(obj):
	output = OrderedDict()
	if obj.gslb_prompt is not None:
		output['gslb-prompt'] = obj.gslb_prompt
	if obj.disable is not None:
		output['disable'] = obj.disable
	if obj.group_role is not None:
		output['group-role'] = obj.group_role
	if obj.symbol is not None:
		output['symbol'] = obj.symbol
	return output

def serialize_Terminal__history_cfg_json(obj):
	output = OrderedDict()
	if obj.history is not None:
		output['history'] = obj.history
	if obj.size is not None:
		output['size'] = obj.size
	return output

def serialize_Terminal__prompt_cfg__vcs_cfg_json(obj):
	output = OrderedDict()
	if obj.vcs_status is not None:
		output['vcs-status'] = obj.vcs_status
	return output

def serialize_Terminal__prompt_cfg_json(obj):
	output = OrderedDict()
	if obj.prompt is not None:
		output['prompt'] = obj.prompt
	if obj.ha_status is not None:
		output['ha-status'] = obj.ha_status
	if obj.hostname is not None:
		output['hostname'] = obj.hostname
	if obj.vcs_cfg is not None:
		output['vcs-cfg'] = serialize_Terminal__prompt_cfg__vcs_cfg_json(obj.vcs_cfg)
	return output

def serialize_Terminal_json(obj):
	output = OrderedDict()
	if obj.auto_size is not None:
		output['auto-size'] = obj.auto_size
	if obj.editing is not None:
		output['editing'] = obj.editing
	if obj.gslb_cfg is not None:
		output['gslb-cfg'] = serialize_Terminal__gslb_cfg_json(obj.gslb_cfg)
	if obj.history_cfg is not None:
		output['history-cfg'] = serialize_Terminal__history_cfg_json(obj.history_cfg)
	if obj.idle_timeout is not None:
		output['idle-timeout'] = obj.idle_timeout
	if obj.length is not None:
		output['length'] = obj.length
	if obj.prompt_cfg is not None:
		output['prompt-cfg'] = serialize_Terminal__prompt_cfg_json(obj.prompt_cfg)
	if obj.width is not None:
		output['width'] = obj.width
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Terminal_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Terminal_json(item))
	return list(container)

class Terminal__gslb_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	gslb_prompt=PosRangedInteger(0, 1)
	disable=PosRangedInteger(0, 1)
	group_role=PosRangedInteger(0, 1)
	symbol=PosRangedInteger(0, 1)
	def __init__(self, gslb_prompt=None, disable=None, group_role=None, symbol=None):
		self.gslb_prompt = gslb_prompt
		self.disable = disable
		self.group_role = group_role
		self.symbol = symbol

	def __str__(self):
		return ""

class Terminal__history_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	history=PosRangedInteger(0, 1)
	size=PosRangedInteger(0, 1000)
	def __init__(self, history=None, size=None):
		self.history = history
		self.size = size

	def __str__(self):
		return ""

class Terminal__prompt_cfg__vcs_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	vcs_status=PosRangedInteger(0, 1)
	def __init__(self, vcs_status=None):
		self.vcs_status = vcs_status

	def __str__(self):
		return ""

class Terminal__prompt_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	prompt=PosRangedInteger(0, 1)
	ha_status=PosRangedInteger(0, 1)
	hostname=PosRangedInteger(0, 1)
	def __init__(self, prompt=None, ha_status=None, hostname=None, vcs_cfg=None):
		self.prompt = prompt
		self.ha_status = ha_status
		self.hostname = hostname
		self.vcs_cfg = vcs_cfg

	def __str__(self):
		return ""

class Terminal(AxapiObject):
	__metaclass__ = StructMeta 
	auto_size=PosRangedInteger(0, 1)
	editing=PosRangedInteger(0, 1)
	idle_timeout=PosRangedInteger(0, 60)
	length=PosRangedInteger(0, 512)
	width=PosRangedInteger(0, 512)
	def __init__(self, auto_size=None, editing=None, gslb_cfg=None, history_cfg=None, idle_timeout=None, length=None, prompt_cfg=None, width=None):
		self.auto_size = auto_size
		self.editing = editing
		self.gslb_cfg = gslb_cfg
		self.history_cfg = history_cfg
		self.idle_timeout = idle_timeout
		self.length = length
		self.prompt_cfg = prompt_cfg
		self.width = width

	def __str__(self):
		return ""

class TerminalClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getTerminal(self):
		"""
		Retrieve the terminal identified by the specified identifier
		
		Returns:
			An instance of the Terminal class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified terminal does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('terminal')
		return deserialize_Terminal_json(payload)

	def putTerminal(self, terminal):
		"""
		Replace the object terminal
		
		Args:
			terminal An instance of the Terminal class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['terminal']=serialize_Terminal_json(terminal)
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

	def deleteTerminal(self):
		"""
		Remove the terminal identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified terminal does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllTerminalsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitTerminal(self, terminal):
		"""
		Create the object terminal
		
		Args:
			terminal An instance of the Terminal class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['terminal']=serialize_Terminal_json(terminal)
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

	def getAllTerminals(self):
		"""
		Retrieve all terminal objects currently pending in the system
		
		Returns:
			A list of Terminal objects
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
			payload= data.get('terminalList')
		return deserialize_list_Terminal_json(payload)

