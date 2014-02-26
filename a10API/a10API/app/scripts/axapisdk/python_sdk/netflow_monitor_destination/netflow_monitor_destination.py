########################################################################################################################
# File name: netflow_monitor_destination.py
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
	'https://axapi.a10networks.com/axapi/v3/netflow/monitor/destination',
]

def deserialize_Destination__ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip = data.get('ip')
	port4 = data.get('port4')
	result = Destination__ip_cfg(ip=ip, port4=port4)
	return result

def deserialize_Destination__ipv6_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6 = data.get('ipv6')
	port6 = data.get('port6')
	result = Destination__ipv6_cfg(ipv6=ipv6, port6=port6)
	return result

def deserialize_Destination_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_cfg = deserialize_Destination__ip_cfg_json(data.get('ip-cfg'))
	ipv6_cfg = deserialize_Destination__ipv6_cfg_json(data.get('ipv6-cfg'))
	result = Destination(ip_cfg=ip_cfg, ipv6_cfg=ipv6_cfg)
	return result

def serialize_Destination__ip_cfg_json(obj):
	output = OrderedDict()
	if obj.ip is not None:
		output['ip'] = obj.ip
	if obj.port4 is not None:
		output['port4'] = obj.port4
	return output

def serialize_Destination__ipv6_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv6 is not None:
		output['ipv6'] = obj.ipv6
	if obj.port6 is not None:
		output['port6'] = obj.port6
	return output

def serialize_Destination_json(obj):
	output = OrderedDict()
	if obj.ip_cfg is not None:
		output['ip-cfg'] = serialize_Destination__ip_cfg_json(obj.ip_cfg)
	if obj.ipv6_cfg is not None:
		output['ipv6-cfg'] = serialize_Destination__ipv6_cfg_json(obj.ipv6_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Destination_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Destination_json(item))
	return list(container)

class Destination__ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	port4=PosRangedInteger(1, 65535)
	def __init__(self, ip=None, port4=None):
		self.ip = ip
		self.port4 = port4

	def __str__(self):
		return ""

class Destination__ipv6_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6=SizedString(1, 255)
	port6=PosRangedInteger(1, 65535)
	def __init__(self, ipv6=None, port6=None):
		self.ipv6 = ipv6
		self.port6 = port6

	def __str__(self):
		return ""

class Destination(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ip_cfg=None, ipv6_cfg=None):
		self.ip_cfg = ip_cfg
		self.ipv6_cfg = ipv6_cfg

	def __str__(self):
		return ""

class NetflowMonitorDestinationClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getNetflowMonitorDestination(self):
		"""
		Retrieve the destination identified by the specified identifier
		
		Returns:
			An instance of the Destination class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified destination does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('destination')
		return deserialize_Destination_json(payload)

	def putNetflowMonitorDestination(self, destination):
		"""
		Replace the object destination
		
		Args:
			destination An instance of the Destination class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['destination']=serialize_Destination_json(destination)
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

	def deleteNetflowMonitorDestination(self):
		"""
		Remove the destination identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified destination does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllNetflowMonitorDestinationsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitNetflowMonitorDestination(self, destination):
		"""
		Create the object destination
		
		Args:
			destination An instance of the Destination class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['destination']=serialize_Destination_json(destination)
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

	def getAllNetflowMonitorDestinations(self):
		"""
		Retrieve all destination objects currently pending in the system
		
		Returns:
			A list of Destination objects
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
			payload= data.get('destinationList')
		return deserialize_list_Destination_json(payload)

