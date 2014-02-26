########################################################################################################################
# File name: arp.py
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
	'https://axapi.a10networks.com/axapi/v3/arp',
]

def deserialize_Arp__interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet = data.get('ethernet')
	trunk = data.get('trunk')
	vlan = data.get('vlan')
	result = Arp__interface(ethernet=ethernet, trunk=trunk, vlan=vlan)
	return result

def deserialize_Arp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_addr = data.get('ip-addr')
	mac_addr = data.get('mac-addr')
	interface = deserialize_Arp__interface_json(data.get('interface'))
	result = Arp(ip_addr=ip_addr, mac_addr=mac_addr, interface=interface)
	return result

def serialize_Arp__interface_json(obj):
	output = OrderedDict()
	if obj.ethernet is not None:
		output['ethernet'] = obj.ethernet
	if obj.trunk is not None:
		output['trunk'] = obj.trunk
	if obj.vlan is not None:
		output['vlan'] = obj.vlan
	return output

def serialize_Arp_json(obj):
	output = OrderedDict()
	output['ip-addr'] = obj.ip_addr
	if obj.mac_addr is not None:
		output['mac-addr'] = obj.mac_addr
	if obj.interface is not None:
		output['interface'] = serialize_Arp__interface_json(obj.interface)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Arp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Arp_json(item))
	return list(container)

class Arp_ip_addr(AxapiObject):
	__metaclass__ = StructMeta 
	ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, ip_addr):
		self.ip_addr = ip_addr

	def __str__(self):
		return str(self.ip_addr)

class Arp__interface(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet=PosRangedInteger(1, 2048)
	trunk=PosRangedInteger(1, 16)
	vlan=PosRangedInteger(1, 4094)
	def __init__(self, ethernet=None, trunk=None, vlan=None):
		self.ethernet = ethernet
		self.trunk = trunk
		self.vlan = vlan

	def __str__(self):
		return ""

class Arp(AxapiObject):
	__metaclass__ = StructMeta 
	ip_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	mac_addr=SizedString(1, 17)
	def __init__(self, ip_addr, mac_addr=None, interface=None):
		self.ip_addr = ip_addr
		self.mac_addr = mac_addr
		self.interface = interface

	def __str__(self):
		return str(self.ip_addr)

class ArpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getArp(self, arp_ip_addr):
		"""
		Retrieve the arp identified by the specified identifier
		
		Args:
			arp_ip_addr Arp_ip_addr
		
		Returns:
			An instance of the Arp class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(arp_ip_addr) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified arp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('arp')
		return deserialize_Arp_json(payload)

	def putArp(self, arp_ip_addr, arp):
		"""
		Replace the object arp
		
		Args:
			arp_ip_addr Arp_ip_addr
			arp An instance of the Arp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['arp']=serialize_Arp_json(arp)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(arp_ip_addr) .replace("/", "%2f") + query, payload, headers)
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

	def deleteArp(self, arp_ip_addr):
		"""
		Remove the arp identified by the specified identifier from the system
		
		Args:
			arp_ip_addr Arp_ip_addr
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(arp_ip_addr) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified arp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllArpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitArp(self, arp):
		"""
		Create the object arp
		
		Args:
			arp An instance of the Arp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['arp']=serialize_Arp_json(arp)
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

	def getAllArps(self):
		"""
		Retrieve all arp objects currently pending in the system
		
		Returns:
			A list of Arp objects
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
			payload= data.get('arpList')
		return deserialize_list_Arp_json(payload)

