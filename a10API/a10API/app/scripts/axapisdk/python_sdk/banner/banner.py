########################################################################################################################
# File name: banner.py
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
	'https://axapi.a10networks.com/axapi/v3/banner',
]

def deserialize_Banner__exec_banner_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	py_kw_rsvd_exec = data.get('exec')
	multi_line = data.get('multi-line')
	terminator = data.get('terminator')
	exec_banner = data.get('exec-banner')
	result = Banner__exec_banner_cfg(py_kw_rsvd_exec=py_kw_rsvd_exec, multi_line=multi_line, terminator=terminator, exec_banner=exec_banner)
	return result

def deserialize_Banner__login_banner_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	login = data.get('login')
	multi_line = data.get('multi-line')
	terminator = data.get('terminator')
	login_banner = data.get('login-banner')
	result = Banner__login_banner_cfg(login=login, multi_line=multi_line, terminator=terminator, login_banner=login_banner)
	return result

def deserialize_Banner_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	exec_banner_cfg = deserialize_Banner__exec_banner_cfg_json(data.get('exec-banner-cfg'))
	login_banner_cfg = deserialize_Banner__login_banner_cfg_json(data.get('login-banner-cfg'))
	result = Banner(exec_banner_cfg=exec_banner_cfg, login_banner_cfg=login_banner_cfg)
	return result

def serialize_Banner__exec_banner_cfg_json(obj):
	output = OrderedDict()
	if obj.py_kw_rsvd_exec is not None:
		output['exec'] = obj.py_kw_rsvd_exec
	if obj.multi_line is not None:
		output['multi-line'] = obj.multi_line
	if obj.terminator is not None:
		output['terminator'] = obj.terminator
	if obj.exec_banner is not None:
		output['exec-banner'] = obj.exec_banner
	return output

def serialize_Banner__login_banner_cfg_json(obj):
	output = OrderedDict()
	if obj.login is not None:
		output['login'] = obj.login
	if obj.multi_line is not None:
		output['multi-line'] = obj.multi_line
	if obj.terminator is not None:
		output['terminator'] = obj.terminator
	if obj.login_banner is not None:
		output['login-banner'] = obj.login_banner
	return output

def serialize_Banner_json(obj):
	output = OrderedDict()
	if obj.exec_banner_cfg is not None:
		output['exec-banner-cfg'] = serialize_Banner__exec_banner_cfg_json(obj.exec_banner_cfg)
	if obj.login_banner_cfg is not None:
		output['login-banner-cfg'] = serialize_Banner__login_banner_cfg_json(obj.login_banner_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Banner_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Banner_json(item))
	return list(container)

class Banner__exec_banner_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	py_kw_rsvd_exec=PosRangedInteger(0, 1)
	multi_line=PosRangedInteger(0, 1)
	terminator=SizedString(1, 2)
	exec_banner=SizedString(0, 255)
	def __init__(self, py_kw_rsvd_exec=None, multi_line=None, terminator=None, exec_banner=None):
		self.py_kw_rsvd_exec = py_kw_rsvd_exec
		self.multi_line = multi_line
		self.terminator = terminator
		self.exec_banner = exec_banner

	def __str__(self):
		return ""

class Banner__login_banner_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	login=PosRangedInteger(0, 1)
	multi_line=PosInteger()
	terminator=SizedString(1, 2)
	login_banner=SizedString(0, 255)
	def __init__(self, login=None, multi_line=None, terminator=None, login_banner=None):
		self.login = login
		self.multi_line = multi_line
		self.terminator = terminator
		self.login_banner = login_banner

	def __str__(self):
		return ""

class Banner(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, exec_banner_cfg=None, login_banner_cfg=None):
		self.exec_banner_cfg = exec_banner_cfg
		self.login_banner_cfg = login_banner_cfg

	def __str__(self):
		return ""

class BannerClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getBanner(self):
		"""
		Retrieve the banner identified by the specified identifier
		
		Returns:
			An instance of the Banner class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified banner does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('banner')
		return deserialize_Banner_json(payload)

	def putBanner(self, banner):
		"""
		Replace the object banner
		
		Args:
			banner An instance of the Banner class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['banner']=serialize_Banner_json(banner)
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

	def deleteBanner(self):
		"""
		Remove the banner identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified banner does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllBannersClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitBanner(self, banner):
		"""
		Create the object banner
		
		Args:
			banner An instance of the Banner class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['banner']=serialize_Banner_json(banner)
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

	def getAllBanners(self):
		"""
		Retrieve all banner objects currently pending in the system
		
		Returns:
			A list of Banner objects
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
			payload= data.get('bannerList')
		return deserialize_list_Banner_json(payload)

