########################################################################################################################
# File name: smtp.py
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
	'https://axapi.a10networks.com/axapi/v3/smtp',
]

def deserialize_Smtp__username_cfg__password__encrypted_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	encrypted = data.get('encrypted')
	enc_pass = data.get('enc-pass')
	result = Smtp__username_cfg__password__encrypted_cfg(encrypted=encrypted, enc_pass=enc_pass)
	return result

def deserialize_Smtp__username_cfg__password_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	encrypted_cfg = deserialize_Smtp__username_cfg__password__encrypted_cfg_json(data.get('encrypted-cfg'))
	smtp_password = data.get('smtp-password')
	result = Smtp__username_cfg__password(encrypted_cfg=encrypted_cfg, smtp_password=smtp_password)
	return result

def deserialize_Smtp__username_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	username = data.get('username')
	password = deserialize_Smtp__username_cfg__password_json(data.get('password'))
	result = Smtp__username_cfg(username=username, password=password)
	return result

def deserialize_Smtp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	smtp_server = data.get('smtp-server')
	smtp_server_v6 = data.get('smtp-server-v6')
	port = data.get('port')
	needauthentication = data.get('needauthentication')
	mailfrom = data.get('mailfrom')
	username_cfg = deserialize_Smtp__username_cfg_json(data.get('username-cfg'))
	result = Smtp(smtp_server=smtp_server, smtp_server_v6=smtp_server_v6, port=port, needauthentication=needauthentication, mailfrom=mailfrom, username_cfg=username_cfg)
	return result

def serialize_Smtp__username_cfg__password__encrypted_cfg_json(obj):
	output = OrderedDict()
	if obj.encrypted is not None:
		output['encrypted'] = obj.encrypted
	if obj.enc_pass is not None:
		output['enc-pass'] = obj.enc_pass
	return output

def serialize_Smtp__username_cfg__password_json(obj):
	output = OrderedDict()
	if obj.encrypted_cfg is not None:
		output['encrypted-cfg'] = serialize_Smtp__username_cfg__password__encrypted_cfg_json(obj.encrypted_cfg)
	if obj.smtp_password is not None:
		output['smtp-password'] = obj.smtp_password
	return output

def serialize_Smtp__username_cfg_json(obj):
	output = OrderedDict()
	if obj.username is not None:
		output['username'] = obj.username
	if obj.password is not None:
		output['password'] = serialize_Smtp__username_cfg__password_json(obj.password)
	return output

def serialize_Smtp_json(obj):
	output = OrderedDict()
	if obj.smtp_server is not None:
		output['smtp-server'] = obj.smtp_server
	if obj.smtp_server_v6 is not None:
		output['smtp-server-v6'] = obj.smtp_server_v6
	if obj.port is not None:
		output['port'] = obj.port
	if obj.needauthentication is not None:
		output['needauthentication'] = obj.needauthentication
	if obj.mailfrom is not None:
		output['mailfrom'] = obj.mailfrom
	if obj.username_cfg is not None:
		output['username-cfg'] = serialize_Smtp__username_cfg_json(obj.username_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Smtp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Smtp_json(item))
	return list(container)

class Smtp__username_cfg__password__encrypted_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	encrypted=PosRangedInteger(0, 1)
	enc_pass=SizedString(1, 255)
	def __init__(self, encrypted=None, enc_pass=None):
		self.encrypted = encrypted
		self.enc_pass = enc_pass

	def __str__(self):
		return ""

class Smtp__username_cfg__password(AxapiObject):
	__metaclass__ = StructMeta 
	smtp_password=SizedString(1, 31)
	def __init__(self, encrypted_cfg=None, smtp_password=None):
		self.encrypted_cfg = encrypted_cfg
		self.smtp_password = smtp_password

	def __str__(self):
		return ""

class Smtp__username_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	username=SizedString(1, 31)
	def __init__(self, username=None, password=None):
		self.username = username
		self.password = password

	def __str__(self):
		return ""

class Smtp(AxapiObject):
	__metaclass__ = StructMeta 
	smtp_server=SizedString(1, 31)
	smtp_server_v6=SizedString(1, 255)
	port=PosRangedInteger(1, 65535)
	needauthentication=PosRangedInteger(0, 1)
	mailfrom=SizedString(1, 31)
	def __init__(self, smtp_server=None, smtp_server_v6=None, port=None, needauthentication=None, mailfrom=None, username_cfg=None):
		self.smtp_server = smtp_server
		self.smtp_server_v6 = smtp_server_v6
		self.port = port
		self.needauthentication = needauthentication
		self.mailfrom = mailfrom
		self.username_cfg = username_cfg

	def __str__(self):
		return ""

class SmtpClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSmtp(self):
		"""
		Retrieve the smtp identified by the specified identifier
		
		Returns:
			An instance of the Smtp class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified smtp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('smtp')
		return deserialize_Smtp_json(payload)

	def putSmtp(self, smtp):
		"""
		Replace the object smtp
		
		Args:
			smtp An instance of the Smtp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['smtp']=serialize_Smtp_json(smtp)
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

	def deleteSmtp(self):
		"""
		Remove the smtp identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified smtp does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSmtpsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSmtp(self, smtp):
		"""
		Create the object smtp
		
		Args:
			smtp An instance of the Smtp class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['smtp']=serialize_Smtp_json(smtp)
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

	def getAllSmtps(self):
		"""
		Retrieve all smtp objects currently pending in the system
		
		Returns:
			A list of Smtp objects
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
			payload= data.get('smtpList')
		return deserialize_list_Smtp_json(payload)

