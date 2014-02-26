########################################################################################################################
# File name: lacp_passthrough.py
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
	'https://axapi.a10networks.com/axapi/v3/lacp-passthrough',
]

def deserialize_Lacp_passthrough__ethernet_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	peer_from = data.get('peer-from')
	peer_to = data.get('peer-to')
	result = Lacp_passthrough__ethernet_cfg(peer_from=peer_from, peer_to=peer_to)
	return result

def deserialize_Lacp_passthrough_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet_cfg = deserialize_Lacp_passthrough__ethernet_cfg_json(data.get('ethernet-cfg'))
	result = Lacp_passthrough(ethernet_cfg=ethernet_cfg)
	return result

def serialize_Lacp_passthrough__ethernet_cfg_json(obj):
	output = OrderedDict()
	output['peer-from'] = obj.peer_from
	output['peer-to'] = obj.peer_to
	return output

def serialize_Lacp_passthrough_json(obj):
	output = OrderedDict()
	output['ethernet-cfg'] = serialize_Lacp_passthrough__ethernet_cfg_json(obj.ethernet_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Lacp_passthrough_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Lacp_passthrough_json(item))
	return list(container)

class Lacp_passthrough_ethernet_cfg_peer_from_peer_to__ethernet_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	peer_from=PosRangedInteger(1, 2048)
	peer_to=PosRangedInteger(1, 2048)
	def __init__(self, peer_from, peer_to):
		self.peer_from = peer_from
		self.peer_to = peer_to

	def __str__(self):
		return str(self.peer_from) + '+' + str(self.peer_to)

class Lacp_passthrough_ethernet_cfg_peer_from_peer_to(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ethernet_cfg):
		self.ethernet_cfg = ethernet_cfg

	def __str__(self):
		return str(self.ethernet_cfg)

class Lacp_passthrough__ethernet_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	peer_from=PosRangedInteger(1, 2048)
	peer_to=PosRangedInteger(1, 2048)
	def __init__(self, peer_from, peer_to):
		self.peer_from = peer_from
		self.peer_to = peer_to

	def __str__(self):
		return str(self.peer_from) + '+' + str(self.peer_to)

class Lacp_passthrough(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ethernet_cfg):
		self.ethernet_cfg = ethernet_cfg

	def __str__(self):
		return str(self.ethernet_cfg)

class LacppassthroughClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLacppassthrough(self, lacp_passthrough_ethernet_cfg_peer_from_peer_to):
		"""
		Retrieve the lacp_passthrough identified by the specified identifier
		
		Args:
			lacp_passthrough_ethernet_cfg_peer_from_peer_to Lacp_passthrough_ethernet_cfg_peer_from_peer_to
		
		Returns:
			An instance of the Lacp_passthrough class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(lacp_passthrough_ethernet_cfg_peer_from_peer_to) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified lacp_passthrough does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('lacp-passthrough')
		return deserialize_Lacp_passthrough_json(payload)

	def putLacppassthrough(self, lacp_passthrough_ethernet_cfg_peer_from_peer_to, lacp_passthrough):
		"""
		Replace the object lacp_passthrough
		
		Args:
			lacp_passthrough_ethernet_cfg_peer_from_peer_to Lacp_passthrough_ethernet_cfg_peer_from_peer_to
			lacp_passthrough An instance of the Lacp_passthrough class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['lacp-passthrough']=serialize_Lacp_passthrough_json(lacp_passthrough)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(lacp_passthrough_ethernet_cfg_peer_from_peer_to) .replace("/", "%2f") + query, payload, headers)
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

	def deleteLacppassthrough(self, lacp_passthrough_ethernet_cfg_peer_from_peer_to):
		"""
		Remove the lacp_passthrough identified by the specified identifier from
		the system
		
		Args:
			lacp_passthrough_ethernet_cfg_peer_from_peer_to Lacp_passthrough_ethernet_cfg_peer_from_peer_to
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(lacp_passthrough_ethernet_cfg_peer_from_peer_to) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified lacp_passthrough does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllLacppassthroughsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitLacppassthrough(self, lacp_passthrough):
		"""
		Create the object lacp_passthrough
		
		Args:
			lacp_passthrough An instance of the Lacp_passthrough class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['lacp-passthrough']=serialize_Lacp_passthrough_json(lacp_passthrough)
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

	def getAllLacppassthroughs(self):
		"""
		Retrieve all lacp_passthrough objects currently pending in the system
		
		Returns:
			A list of Lacp_passthrough objects
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
			payload= data.get('lacp-passthroughList')
		return deserialize_list_Lacp_passthrough_json(payload)

