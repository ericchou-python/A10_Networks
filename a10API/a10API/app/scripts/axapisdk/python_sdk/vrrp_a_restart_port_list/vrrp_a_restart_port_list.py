########################################################################################################################
# File name: vrrp_a_restart_port_list.py
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
	'https://axapi.a10networks.com/axapi/v3/vrrp-a/restart-port-list',
]

def deserialize_Vrrp_a_restart_port_list_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	flap_ethernet_start = data.get('flap-ethernet-start')
	flap_ethernet_end = data.get('flap-ethernet-end')
	result = Vrrp_a_restart_port_list_eth_cfg(flap_ethernet_start=flap_ethernet_start, flap_ethernet_end=flap_ethernet_end)
	return result

def deserialize_list_Vrrp_a_restart_port_list_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Vrrp_a_restart_port_list_eth_cfg_json(item))
	return list(container)

def deserialize_Restart_port_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	eth_cfg = deserialize_list_Vrrp_a_restart_port_list_eth_cfg_json(data.get('eth-cfg'))
	result = Restart_port_list(eth_cfg=eth_cfg)
	return result

def serialize_Vrrp_a_restart_port_list_eth_cfg_json(obj):
	output = OrderedDict()
	if obj.flap_ethernet_start is not None:
		output['flap-ethernet-start'] = obj.flap_ethernet_start
	if obj.flap_ethernet_end is not None:
		output['flap-ethernet-end'] = obj.flap_ethernet_end
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Vrrp_a_restart_port_list_eth_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Vrrp_a_restart_port_list_eth_cfg_json(item))
	return output

def serialize_Restart_port_list_json(obj):
	output = OrderedDict()
	if obj.eth_cfg is not None:
		output['eth-cfg'] = serialize_list_Vrrp_a_restart_port_list_eth_cfg_json(obj.eth_cfg)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Restart_port_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Restart_port_list_json(item))
	return list(container)

class Restart_port_list(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, eth_cfg=None):
		self.eth_cfg = eth_cfg

	def __str__(self):
		return ""

class Vrrp_a_restart_port_list_eth_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	flap_ethernet_start=PosRangedInteger(1, 2048)
	flap_ethernet_end=PosRangedInteger(1, 2048)
	def __init__(self, flap_ethernet_start=None, flap_ethernet_end=None):
		self.flap_ethernet_start = flap_ethernet_start
		self.flap_ethernet_end = flap_ethernet_end

	def __str__(self):
		return ""

class VrrpaRestartportlistClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getVrrpaRestartportlist(self):
		"""
		Retrieve the restart_port_list identified by the specified identifier
		
		Returns:
			An instance of the Restart_port_list class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified restart_port_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('restart-port-list')
		return deserialize_Restart_port_list_json(payload)

	def putVrrpaRestartportlist(self, restart_port_list):
		"""
		Replace the object restart_port_list
		
		Args:
			restart_port_list An instance of the Restart_port_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['restart-port-list']=serialize_Restart_port_list_json(restart_port_list)
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

	def deleteVrrpaRestartportlist(self):
		"""
		Remove the restart_port_list identified by the specified identifier from
		the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified restart_port_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllVrrpaRestartportlistsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitVrrpaRestartportlist(self, restart_port_list):
		"""
		Create the object restart_port_list
		
		Args:
			restart_port_list An instance of the Restart_port_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['restart-port-list']=serialize_Restart_port_list_json(restart_port_list)
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

	def getAllVrrpaRestartportlists(self):
		"""
		Retrieve all restart_port_list objects currently pending in the system
		
		Returns:
			A list of Restart_port_list objects
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
			payload= data.get('restart-port-listList')
		return deserialize_list_Restart_port_list_json(payload)

