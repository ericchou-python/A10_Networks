########################################################################################################################
# File name: zone.py
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
	'https://axapi.a10networks.com/axapi/v3/zone',
]

def deserialize_Zone_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	interface = data.get('interface')
	interface_ethernet_start = data.get('interface-ethernet-start')
	interface_ethernet_end = data.get('interface-ethernet-end')
	interface_trunk_start = data.get('interface-trunk-start')
	interface_trunk_end = data.get('interface-trunk-end')
	interface_ve_start = data.get('interface-ve-start')
	interface_ve_end = data.get('interface-ve-end')
	result = Zone(name=name, interface=interface, interface_ethernet_start=interface_ethernet_start, interface_ethernet_end=interface_ethernet_end, interface_trunk_start=interface_trunk_start, interface_trunk_end=interface_trunk_end, interface_ve_start=interface_ve_start, interface_ve_end=interface_ve_end)
	return result

def serialize_Zone_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.interface is not None:
		output['interface'] = obj.interface
	if obj.interface_ethernet_start is not None:
		output['interface-ethernet-start'] = obj.interface_ethernet_start
	if obj.interface_ethernet_end is not None:
		output['interface-ethernet-end'] = obj.interface_ethernet_end
	if obj.interface_trunk_start is not None:
		output['interface-trunk-start'] = obj.interface_trunk_start
	if obj.interface_trunk_end is not None:
		output['interface-trunk-end'] = obj.interface_trunk_end
	if obj.interface_ve_start is not None:
		output['interface-ve-start'] = obj.interface_ve_start
	if obj.interface_ve_end is not None:
		output['interface-ve-end'] = obj.interface_ve_end
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Zone_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Zone_json(item))
	return list(container)

class Zone_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class Zone(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	interface=PosRangedInteger(0, 1)
	interface_ethernet_start=PosRangedInteger(1, 2048)
	interface_ethernet_end=PosRangedInteger(1, 2048)
	interface_trunk_start=PosRangedInteger(1, 16)
	interface_trunk_end=PosRangedInteger(1, 16)
	interface_ve_start=PosRangedInteger(2, 4094)
	interface_ve_end=PosRangedInteger(2, 4094)
	def __init__(self, name, interface=None, interface_ethernet_start=None, interface_ethernet_end=None, interface_trunk_start=None, interface_trunk_end=None, interface_ve_start=None, interface_ve_end=None):
		self.name = name
		self.interface = interface
		self.interface_ethernet_start = interface_ethernet_start
		self.interface_ethernet_end = interface_ethernet_end
		self.interface_trunk_start = interface_trunk_start
		self.interface_trunk_end = interface_trunk_end
		self.interface_ve_start = interface_ve_start
		self.interface_ve_end = interface_ve_end

	def __str__(self):
		return str(self.name)

class ZoneClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getZone(self, zone_name):
		"""
		Retrieve the zone identified by the specified identifier
		
		Args:
			zone_name Zone_name
		
		Returns:
			An instance of the Zone class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(zone_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified zone does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('zone')
		return deserialize_Zone_json(payload)

	def putZone(self, zone_name, zone):
		"""
		Replace the object zone
		
		Args:
			zone_name Zone_name
			zone An instance of the Zone class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['zone']=serialize_Zone_json(zone)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(zone_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteZone(self, zone_name):
		"""
		Remove the zone identified by the specified identifier from the system
		
		Args:
			zone_name Zone_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(zone_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified zone does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllZonesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitZone(self, zone):
		"""
		Create the object zone
		
		Args:
			zone An instance of the Zone class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['zone']=serialize_Zone_json(zone)
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

	def getAllZones(self):
		"""
		Retrieve all zone objects currently pending in the system
		
		Returns:
			A list of Zone objects
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
			payload= data.get('zoneList')
		return deserialize_list_Zone_json(payload)

