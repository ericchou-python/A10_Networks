########################################################################################################################
# File name: ddos_protection.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/protection',
]

def deserialize_Protection_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	toggle = data.get('toggle')
	rate_interval = data.get('rate-interval')
	force_routing_on_transp = data.get('force-routing-on-transp')
	disable_on_reboot = data.get('disable-on-reboot')
	use_route = data.get('use-route')
	enable_now = data.get('enable-now')
	result = Protection(toggle=toggle, rate_interval=rate_interval, force_routing_on_transp=force_routing_on_transp, disable_on_reboot=disable_on_reboot, use_route=use_route, enable_now=enable_now)
	return result

def serialize_Protection_json(obj):
	output = OrderedDict()
	if obj.toggle is not None:
		output['toggle'] = obj.toggle
	if obj.rate_interval is not None:
		output['rate-interval'] = obj.rate_interval
	if obj.force_routing_on_transp is not None:
		output['force-routing-on-transp'] = obj.force_routing_on_transp
	if obj.disable_on_reboot is not None:
		output['disable-on-reboot'] = obj.disable_on_reboot
	if obj.use_route is not None:
		output['use-route'] = obj.use_route
	if obj.enable_now is not None:
		output['enable-now'] = obj.enable_now
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Protection_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Protection_json(item))
	return list(container)

class Protection(AxapiObject):
	__metaclass__ = StructMeta 
	toggle = Enum(['enable', 'disable'])
	rate_interval = Enum(['100ms', '1sec'])
	force_routing_on_transp=PosRangedInteger(0, 1)
	disable_on_reboot=PosRangedInteger(0, 1)
	use_route=PosRangedInteger(0, 1)
	enable_now=PosRangedInteger(0, 1)
	def __init__(self, toggle=None, rate_interval=None, force_routing_on_transp=None, disable_on_reboot=None, use_route=None, enable_now=None):
		self.toggle = toggle
		self.rate_interval = rate_interval
		self.force_routing_on_transp = force_routing_on_transp
		self.disable_on_reboot = disable_on_reboot
		self.use_route = use_route
		self.enable_now = enable_now

	def __str__(self):
		return ""

class DdosProtectionClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosProtection(self):
		"""
		Retrieve the protection identified by the specified identifier
		
		Returns:
			An instance of the Protection class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified protection does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('protection')
		return deserialize_Protection_json(payload)

	def putDdosProtection(self, protection):
		"""
		Replace the object protection
		
		Args:
			protection An instance of the Protection class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['protection']=serialize_Protection_json(protection)
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

	def deleteDdosProtection(self):
		"""
		Remove the protection identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified protection does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosProtectionsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosProtection(self, protection):
		"""
		Create the object protection
		
		Args:
			protection An instance of the Protection class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['protection']=serialize_Protection_json(protection)
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

	def getAllDdosProtections(self):
		"""
		Retrieve all protection objects currently pending in the system
		
		Returns:
			A list of Protection objects
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
			payload= data.get('protectionList')
		return deserialize_list_Protection_json(payload)

