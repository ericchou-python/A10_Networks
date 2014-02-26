########################################################################################################################
# File name: glid.py
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
	'https://axapi.a10networks.com/axapi/v3/glid',
]

def deserialize_Glid__over_limit_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	over_limit_action = data.get('over-limit-action')
	drop = data.get('drop')
	result = Glid__over_limit_cfg(over_limit_action=over_limit_action, drop=drop)
	return result

def deserialize_Glid_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	num = data.get('num')
	conn_limit = data.get('conn-limit')
	conn_rate_limit = data.get('conn-rate-limit')
	over_limit_cfg = deserialize_Glid__over_limit_cfg_json(data.get('over-limit-cfg'))
	pkt_rate_limit = data.get('pkt-rate-limit')
	frag_pkt_rate_limit = data.get('frag-pkt-rate-limit')
	syn_cookie_thr = data.get('syn-cookie-thr')
	result = Glid(num=num, conn_limit=conn_limit, conn_rate_limit=conn_rate_limit, over_limit_cfg=over_limit_cfg, pkt_rate_limit=pkt_rate_limit, frag_pkt_rate_limit=frag_pkt_rate_limit, syn_cookie_thr=syn_cookie_thr)
	return result

def serialize_Glid__over_limit_cfg_json(obj):
	output = OrderedDict()
	if obj.over_limit_action is not None:
		output['over-limit-action'] = obj.over_limit_action
	if obj.drop is not None:
		output['drop'] = obj.drop
	return output

def serialize_Glid_json(obj):
	output = OrderedDict()
	output['num'] = obj.num
	if obj.conn_limit is not None:
		output['conn-limit'] = obj.conn_limit
	if obj.conn_rate_limit is not None:
		output['conn-rate-limit'] = obj.conn_rate_limit
	if obj.over_limit_cfg is not None:
		output['over-limit-cfg'] = serialize_Glid__over_limit_cfg_json(obj.over_limit_cfg)
	if obj.pkt_rate_limit is not None:
		output['pkt-rate-limit'] = obj.pkt_rate_limit
	if obj.frag_pkt_rate_limit is not None:
		output['frag-pkt-rate-limit'] = obj.frag_pkt_rate_limit
	if obj.syn_cookie_thr is not None:
		output['syn-cookie-thr'] = obj.syn_cookie_thr
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Glid_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Glid_json(item))
	return list(container)

class Glid_num(AxapiObject):
	__metaclass__ = StructMeta 
	num=PosRangedInteger(1, 32000)
	def __init__(self, num):
		self.num = num

	def __str__(self):
		return str(self.num)

class Glid__over_limit_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	over_limit_action=PosRangedInteger(0, 1)
	drop=PosRangedInteger(0, 1)
	def __init__(self, over_limit_action=None, drop=None):
		self.over_limit_action = over_limit_action
		self.drop = drop

	def __str__(self):
		return ""

class Glid(AxapiObject):
	__metaclass__ = StructMeta 
	num=PosRangedInteger(1, 32000)
	conn_limit=PosRangedInteger(1, 16000000)
	conn_rate_limit=PosRangedInteger(1, 16000000)
	pkt_rate_limit=PosRangedInteger(1, 16000000)
	frag_pkt_rate_limit=PosRangedInteger(1, 16000000)
	syn_cookie_thr=PosRangedInteger(1, 16)
	def __init__(self, num, conn_limit=None, conn_rate_limit=None, over_limit_cfg=None, pkt_rate_limit=None, frag_pkt_rate_limit=None, syn_cookie_thr=None):
		self.num = num
		self.conn_limit = conn_limit
		self.conn_rate_limit = conn_rate_limit
		self.over_limit_cfg = over_limit_cfg
		self.pkt_rate_limit = pkt_rate_limit
		self.frag_pkt_rate_limit = frag_pkt_rate_limit
		self.syn_cookie_thr = syn_cookie_thr

	def __str__(self):
		return str(self.num)

class GlidClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getGlid(self, glid_num):
		"""
		Retrieve the glid identified by the specified identifier
		
		Args:
			glid_num Glid_num
		
		Returns:
			An instance of the Glid class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(glid_num) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified glid does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('glid')
		return deserialize_Glid_json(payload)

	def putGlid(self, glid_num, glid):
		"""
		Replace the object glid
		
		Args:
			glid_num Glid_num
			glid An instance of the Glid class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['glid']=serialize_Glid_json(glid)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(glid_num) .replace("/", "%2f") + query, payload, headers)
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

	def deleteGlid(self, glid_num):
		"""
		Remove the glid identified by the specified identifier from the system
		
		Args:
			glid_num Glid_num
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(glid_num) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified glid does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllGlidsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitGlid(self, glid):
		"""
		Create the object glid
		
		Args:
			glid An instance of the Glid class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['glid']=serialize_Glid_json(glid)
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

	def getAllGlids(self):
		"""
		Retrieve all glid objects currently pending in the system
		
		Returns:
			A list of Glid objects
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
			payload= data.get('glidList')
		return deserialize_list_Glid_json(payload)

