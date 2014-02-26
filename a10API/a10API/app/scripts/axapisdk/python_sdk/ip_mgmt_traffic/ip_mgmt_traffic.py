########################################################################################################################
# File name: ip_mgmt_traffic.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/mgmt-traffic',
]

def deserialize_Mgmt_traffic__source_interface__loopback_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	loopback_num = data.get('loopback-num')
	result = Mgmt_traffic__source_interface__loopback(loopback_num=loopback_num)
	return result

def deserialize_Mgmt_traffic__source_interface_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	loopback = deserialize_Mgmt_traffic__source_interface__loopback_json(data.get('loopback'))
	result = Mgmt_traffic__source_interface(loopback=loopback)
	return result

def deserialize_Mgmt_traffic_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	traffic_type = data.get('traffic-type')
	source_interface = deserialize_Mgmt_traffic__source_interface_json(data.get('source-interface'))
	result = Mgmt_traffic(traffic_type=traffic_type, source_interface=source_interface)
	return result

def serialize_Mgmt_traffic__source_interface__loopback_json(obj):
	output = OrderedDict()
	if obj.loopback_num is not None:
		output['loopback-num'] = obj.loopback_num
	return output

def serialize_Mgmt_traffic__source_interface_json(obj):
	output = OrderedDict()
	if obj.loopback is not None:
		output['loopback'] = serialize_Mgmt_traffic__source_interface__loopback_json(obj.loopback)
	return output

def serialize_Mgmt_traffic_json(obj):
	output = OrderedDict()
	output['traffic-type'] = obj.traffic_type
	output['source-interface'] = serialize_Mgmt_traffic__source_interface_json(obj.source_interface)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Mgmt_traffic_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Mgmt_traffic_json(item))
	return list(container)

class Mgmt_traffic_traffic_type_source_interface_loopback_loopback_num__source_interface__loopback(AxapiObject):
	__metaclass__ = StructMeta 
	loopback_num=PosRangedInteger(1, 10)
	def __init__(self, loopback_num=None):
		self.loopback_num = loopback_num

	def __str__(self):
		return ""

class Mgmt_traffic_traffic_type_source_interface_loopback_loopback_num__source_interface(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, loopback=None):
		self.loopback = loopback

	def __str__(self):
		return ""

class Mgmt_traffic_traffic_type_source_interface_loopback_loopback_num(AxapiObject):
	__metaclass__ = StructMeta 
	traffic_type = Enum(['all', 'ftp', 'ntp', 'rcp', 'snmp', 'ssh', 'syslog', 'telnet', 'tftp', 'web'])
	def __init__(self, traffic_type, source_interface):
		self.traffic_type = traffic_type
		self.source_interface = source_interface

	def __str__(self):
		return str(self.traffic_type) + '+' + str(self.source_interface)

class Mgmt_traffic__source_interface__loopback(AxapiObject):
	__metaclass__ = StructMeta 
	loopback_num=PosRangedInteger(1, 10)
	def __init__(self, loopback_num=None):
		self.loopback_num = loopback_num

	def __str__(self):
		return ""

class Mgmt_traffic__source_interface(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, loopback=None):
		self.loopback = loopback

	def __str__(self):
		return ""

class Mgmt_traffic(AxapiObject):
	__metaclass__ = StructMeta 
	traffic_type = Enum(['all', 'ftp', 'ntp', 'rcp', 'snmp', 'ssh', 'syslog', 'telnet', 'tftp', 'web'])
	def __init__(self, traffic_type, source_interface):
		self.traffic_type = traffic_type
		self.source_interface = source_interface

	def __str__(self):
		return str(self.traffic_type) + '+' + str(self.source_interface)

class IpMgmttrafficClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpMgmttraffic(self, mgmt_traffic_traffic_type_source_interface_loopback_loopback_num):
		"""
		Retrieve the mgmt_traffic identified by the specified identifier
		
		Args:
			mgmt_traffic_traffic_type_source_interface_loopback_loopback_num Mgmt_traffic_traffic_type_source_interface_loopback_loopback_num
		
		Returns:
			An instance of the Mgmt_traffic class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(mgmt_traffic_traffic_type_source_interface_loopback_loopback_num) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified mgmt_traffic does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('mgmt-traffic')
		return deserialize_Mgmt_traffic_json(payload)

	def putIpMgmttraffic(self, mgmt_traffic_traffic_type_source_interface_loopback_loopback_num, mgmt_traffic):
		"""
		Replace the object mgmt_traffic
		
		Args:
			mgmt_traffic_traffic_type_source_interface_loopback_loopback_num Mgmt_traffic_traffic_type_source_interface_loopback_loopback_num
			mgmt_traffic An instance of the Mgmt_traffic class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['mgmt-traffic']=serialize_Mgmt_traffic_json(mgmt_traffic)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(mgmt_traffic_traffic_type_source_interface_loopback_loopback_num) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpMgmttraffic(self, mgmt_traffic_traffic_type_source_interface_loopback_loopback_num):
		"""
		Remove the mgmt_traffic identified by the specified identifier from the
		system
		
		Args:
			mgmt_traffic_traffic_type_source_interface_loopback_loopback_num Mgmt_traffic_traffic_type_source_interface_loopback_loopback_num
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(mgmt_traffic_traffic_type_source_interface_loopback_loopback_num) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified mgmt_traffic does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpMgmttrafficsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpMgmttraffic(self, mgmt_traffic):
		"""
		Create the object mgmt_traffic
		
		Args:
			mgmt_traffic An instance of the Mgmt_traffic class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['mgmt-traffic']=serialize_Mgmt_traffic_json(mgmt_traffic)
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

	def getAllIpMgmttraffics(self):
		"""
		Retrieve all mgmt_traffic objects currently pending in the system
		
		Returns:
			A list of Mgmt_traffic objects
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
			payload= data.get('mgmt-trafficList')
		return deserialize_list_Mgmt_traffic_json(payload)

