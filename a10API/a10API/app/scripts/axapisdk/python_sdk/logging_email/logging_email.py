########################################################################################################################
# File name: logging_email.py
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
	'https://axapi.a10networks.com/axapi/v3/logging/email',
]

def deserialize_Email__levelnum_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	levelnum = data.get('levelnum')
	email_levelname = data.get('email-levelname')
	result = Email__levelnum_cfg(levelnum=levelnum, email_levelname=email_levelname)
	return result

def deserialize_Email__buffer_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	number = data.get('number')
	time = data.get('time')
	result = Email__buffer(number=number, time=time)
	return result

def deserialize_Email__filter_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	filter_id = data.get('filter-id')
	expression = data.get('expression')
	trigger = data.get('trigger')
	result = Email__filter(filter_id=filter_id, expression=expression, trigger=trigger)
	return result

def deserialize_Email_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	levelnum_cfg = deserialize_Email__levelnum_cfg_json(data.get('levelnum-cfg'))
	buffer = deserialize_Email__buffer_json(data.get('buffer'))
	filter = deserialize_Email__filter_json(data.get('filter'))
	result = Email(levelnum_cfg=levelnum_cfg, buffer=buffer, filter=filter)
	return result

def serialize_Email__levelnum_cfg_json(obj):
	output = OrderedDict()
	if obj.levelnum is not None:
		output['levelnum'] = obj.levelnum
	if obj.email_levelname is not None:
		output['email-levelname'] = obj.email_levelname
	return output

def serialize_Email__buffer_json(obj):
	output = OrderedDict()
	if obj.number is not None:
		output['number'] = obj.number
	if obj.time is not None:
		output['time'] = obj.time
	return output

def serialize_Email__filter_json(obj):
	output = OrderedDict()
	if obj.filter_id is not None:
		output['filter-id'] = obj.filter_id
	if obj.expression is not None:
		output['expression'] = obj.expression
	if obj.trigger is not None:
		output['trigger'] = obj.trigger
	return output

def serialize_Email_json(obj):
	output = OrderedDict()
	if obj.levelnum_cfg is not None:
		output['levelnum-cfg'] = serialize_Email__levelnum_cfg_json(obj.levelnum_cfg)
	if obj.buffer is not None:
		output['buffer'] = serialize_Email__buffer_json(obj.buffer)
	if obj.filter is not None:
		output['filter'] = serialize_Email__filter_json(obj.filter)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Email_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Email_json(item))
	return list(container)

class Email__levelnum_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	levelnum = Enum([])
	email_levelname = Enum(['emergency', 'alert', 'critical', 'notification'])
	def __init__(self, levelnum=None, email_levelname=None):
		self.levelnum = levelnum
		self.email_levelname = email_levelname

	def __str__(self):
		return ""

class Email__buffer(AxapiObject):
	__metaclass__ = StructMeta 
	number=PosRangedInteger(16, 256)
	time=PosRangedInteger(10, 1440)
	def __init__(self, number=None, time=None):
		self.number = number
		self.time = time

	def __str__(self):
		return ""

class Email__filter(AxapiObject):
	__metaclass__ = StructMeta 
	filter_id=PosRangedInteger(1, 8)
	expression=SizedString(1, 511)
	trigger=PosRangedInteger(0, 1)
	def __init__(self, filter_id=None, expression=None, trigger=None):
		self.filter_id = filter_id
		self.expression = expression
		self.trigger = trigger

	def __str__(self):
		return ""

class Email(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, levelnum_cfg=None, buffer=None, filter=None):
		self.levelnum_cfg = levelnum_cfg
		self.buffer = buffer
		self.filter = filter

	def __str__(self):
		return ""

class LoggingEmailClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLoggingEmail(self):
		"""
		Retrieve the email identified by the specified identifier
		
		Returns:
			An instance of the Email class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified email does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('email')
		return deserialize_Email_json(payload)

	def putLoggingEmail(self, email):
		"""
		Replace the object email
		
		Args:
			email An instance of the Email class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['email']=serialize_Email_json(email)
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

	def deleteLoggingEmail(self):
		"""
		Remove the email identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified email does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllLoggingEmailsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitLoggingEmail(self, email):
		"""
		Create the object email
		
		Args:
			email An instance of the Email class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['email']=serialize_Email_json(email)
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

	def getAllLoggingEmails(self):
		"""
		Retrieve all email objects currently pending in the system
		
		Returns:
			A list of Email objects
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
			payload= data.get('emailList')
		return deserialize_list_Email_json(payload)

