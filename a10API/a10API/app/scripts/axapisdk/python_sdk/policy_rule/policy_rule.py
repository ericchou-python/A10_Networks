########################################################################################################################
# File name: policy_rule.py
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
	'https://axapi.a10networks.com/axapi/v3/policy-rule',
]

def deserialize_Policy_rule_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	rule_name = data.get('rule-name')
	match = data.get('match')
	src_zone = data.get('src-zone')
	dst_zone = data.get('dst-zone')
	src_address = data.get('src-address')
	dst_address = data.get('dst-address')
	svc_group = data.get('svc-group')
	user_group = data.get('user-group')
	user = data.get('user')
	app_group = data.get('app-group')
	application = data.get('application')
	action = data.get('action')
	forwarding = data.get('forwarding')
	url_filtering = data.get('URL-filtering')
	header_info = data.get('header-info')
	aflex_logging = data.get('aflex-logging')
	virtual_service = data.get('virtual-service')
	move = data.get('move')
	above = data.get('above')
	below = data.get('below')
	result = Policy_rule(rule_name=rule_name, match=match, src_zone=src_zone, dst_zone=dst_zone, src_address=src_address, dst_address=dst_address, svc_group=svc_group, user_group=user_group, user=user, app_group=app_group, application=application, action=action, forwarding=forwarding, url_filtering=url_filtering, header_info=header_info, aflex_logging=aflex_logging, virtual_service=virtual_service, move=move, above=above, below=below)
	return result

def serialize_Policy_rule_json(obj):
	output = OrderedDict()
	output['rule-name'] = obj.rule_name
	if obj.match is not None:
		output['match'] = obj.match
	if obj.src_zone is not None:
		output['src-zone'] = obj.src_zone
	if obj.dst_zone is not None:
		output['dst-zone'] = obj.dst_zone
	if obj.src_address is not None:
		output['src-address'] = obj.src_address
	if obj.dst_address is not None:
		output['dst-address'] = obj.dst_address
	if obj.svc_group is not None:
		output['svc-group'] = obj.svc_group
	if obj.user_group is not None:
		output['user-group'] = obj.user_group
	if obj.user is not None:
		output['user'] = obj.user
	if obj.app_group is not None:
		output['app-group'] = obj.app_group
	if obj.application is not None:
		output['application'] = obj.application
	if obj.action is not None:
		output['action'] = obj.action
	if obj.forwarding is not None:
		output['forwarding'] = obj.forwarding
	if obj.url_filtering is not None:
		output['URL-filtering'] = obj.url_filtering
	if obj.header_info is not None:
		output['header-info'] = obj.header_info
	if obj.aflex_logging is not None:
		output['aflex-logging'] = obj.aflex_logging
	if obj.virtual_service is not None:
		output['virtual-service'] = obj.virtual_service
	if obj.move is not None:
		output['move'] = obj.move
	if obj.above is not None:
		output['above'] = obj.above
	if obj.below is not None:
		output['below'] = obj.below
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Policy_rule_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Policy_rule_json(item))
	return list(container)

class Policy_rule_rule_name(AxapiObject):
	__metaclass__ = StructMeta 
	rule_name=SizedString(1, 255)
	def __init__(self, rule_name):
		self.rule_name = rule_name

	def __str__(self):
		return str(self.rule_name)

class Policy_rule(AxapiObject):
	__metaclass__ = StructMeta 
	rule_name=SizedString(1, 255)
	match=PosRangedInteger(0, 1)
	src_zone=SizedString(1, 255)
	dst_zone=SizedString(1, 255)
	src_address=SizedString(1, 255)
	dst_address=SizedString(1, 255)
	svc_group=SizedString(1, 255)
	user_group=SizedString(1, 255)
	user=SizedString(1, 255)
	app_group=SizedString(1, 255)
	application=SizedString(1, 255)
	action=PosRangedInteger(0, 1)
	forwarding = Enum(['pass', 'deny'])
	url_filtering=SizedString(1, 255)
	header_info=PosRangedInteger(0, 1)
	aflex_logging=SizedString(1, 255)
	virtual_service=SizedString(1, 255)
	move=PosRangedInteger(0, 1)
	above=SizedString(1, 255)
	below=SizedString(1, 255)
	def __init__(self, rule_name, match=None, src_zone=None, dst_zone=None, src_address=None, dst_address=None, svc_group=None, user_group=None, user=None, app_group=None, application=None, action=None, forwarding=None, url_filtering=None, header_info=None, aflex_logging=None, virtual_service=None, move=None, above=None, below=None):
		self.rule_name = rule_name
		self.match = match
		self.src_zone = src_zone
		self.dst_zone = dst_zone
		self.src_address = src_address
		self.dst_address = dst_address
		self.svc_group = svc_group
		self.user_group = user_group
		self.user = user
		self.app_group = app_group
		self.application = application
		self.action = action
		self.forwarding = forwarding
		self.url_filtering = url_filtering
		self.header_info = header_info
		self.aflex_logging = aflex_logging
		self.virtual_service = virtual_service
		self.move = move
		self.above = above
		self.below = below

	def __str__(self):
		return str(self.rule_name)

class PolicyruleClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getPolicyrule(self, policy_rule_rule_name):
		"""
		Retrieve the policy_rule identified by the specified identifier
		
		Args:
			policy_rule_rule_name Policy_rule_rule_name
		
		Returns:
			An instance of the Policy_rule class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(policy_rule_rule_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified policy_rule does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('policy-rule')
		return deserialize_Policy_rule_json(payload)

	def putPolicyrule(self, policy_rule_rule_name, policy_rule):
		"""
		Replace the object policy_rule
		
		Args:
			policy_rule_rule_name Policy_rule_rule_name
			policy_rule An instance of the Policy_rule class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['policy-rule']=serialize_Policy_rule_json(policy_rule)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(policy_rule_rule_name) .replace("/", "%2f") + query, payload, headers)
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

	def deletePolicyrule(self, policy_rule_rule_name):
		"""
		Remove the policy_rule identified by the specified identifier from the system
		
		Args:
			policy_rule_rule_name Policy_rule_rule_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(policy_rule_rule_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified policy_rule does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllPolicyrulesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitPolicyrule(self, policy_rule):
		"""
		Create the object policy_rule
		
		Args:
			policy_rule An instance of the Policy_rule class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['policy-rule']=serialize_Policy_rule_json(policy_rule)
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

	def getAllPolicyrules(self):
		"""
		Retrieve all policy_rule objects currently pending in the system
		
		Returns:
			A list of Policy_rule objects
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
			payload= data.get('policy-ruleList')
		return deserialize_list_Policy_rule_json(payload)

