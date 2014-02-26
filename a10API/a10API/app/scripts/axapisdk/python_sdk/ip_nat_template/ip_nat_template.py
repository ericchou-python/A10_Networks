########################################################################################################################
# File name: ip_nat_template.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/nat/template',
]

def deserialize_Ip_nat_template_logging__log__port_mappings_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	both = data.get('both')
	creation = data.get('creation')
	result = Ip_nat_template_logging__log__port_mappings(both=both, creation=creation)
	return result

def deserialize_Ip_nat_template_logging__log_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sessions = data.get('sessions')
	port_mappings = deserialize_Ip_nat_template_logging__log__port_mappings_json(data.get('port-mappings'))
	result = Ip_nat_template_logging__log(sessions=sessions, port_mappings=port_mappings)
	return result

def deserialize_Ip_nat_template_logging__source_port_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	source_port_num = data.get('source-port-num')
	any = data.get('any')
	result = Ip_nat_template_logging__source_port(source_port_num=source_port_num, any=any)
	return result

def deserialize_Ip_nat_template_logging_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	facility = data.get('facility')
	include_destination = data.get('include-destination')
	include_rip_rport = data.get('include-rip-rport')
	log = deserialize_Ip_nat_template_logging__log_json(data.get('log'))
	severity = data.get('severity')
	source_port = deserialize_Ip_nat_template_logging__source_port_json(data.get('source-port'))
	result = Ip_nat_template_logging(name=name, facility=facility, include_destination=include_destination, include_rip_rport=include_rip_rport, log=log, severity=severity, source_port=source_port)
	return result

def deserialize_list_Ip_nat_template_logging_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_nat_template_logging_json(item))
	return list(container)

def deserialize_Template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	logginglist = deserialize_list_Ip_nat_template_logging_json(data.get('loggingList'))
	result = Template(logginglist=logginglist)
	return result

class Template(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, logginglist=None):
		self.logginglist = logginglist

	def __str__(self):
		return ""

class Ip_nat_template_logging__log__port_mappings(AxapiObject):
	__metaclass__ = StructMeta 
	both=PosRangedInteger(0, 1)
	creation=PosRangedInteger(0, 1)
	def __init__(self, both, creation):
		self.both = both
		self.creation = creation

	def __str__(self):
		return str(self.both) + '+' + str(self.creation)

class Ip_nat_template_logging__log(AxapiObject):
	__metaclass__ = StructMeta 
	sessions=PosRangedInteger(0, 1)
	def __init__(self, sessions, port_mappings):
		self.sessions = sessions
		self.port_mappings = port_mappings

	def __str__(self):
		return str(self.sessions) + '+' + str(self.port_mappings)

class Ip_nat_template_logging__source_port(AxapiObject):
	__metaclass__ = StructMeta 
	source_port_num=PosRangedInteger(1, 65535)
	any=PosRangedInteger(0, 1)
	def __init__(self, source_port_num, any):
		self.source_port_num = source_port_num
		self.any = any

	def __str__(self):
		return str(self.source_port_num) + '+' + str(self.any)

class Ip_nat_template_logging(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	facility = Enum(['kernel', 'user', 'mail', 'daemon', 'security-authorization', 'syslog', 'line-printer', 'news', 'uucp', 'cron', 'security-authorization-private', 'ftp', 'ntp', 'audit', 'alert', 'clock', 'local0', 'local1', 'local2', 'local3', 'local4', 'local5', 'local6', 'local7'])
	include_destination=PosRangedInteger(0, 1)
	include_rip_rport=PosRangedInteger(0, 1)
	severity = Enum(['emergency', 'alert', 'critical', 'error', 'warning', 'notice', 'informational', 'debugging'])
	def __init__(self, name, facility=None, include_destination=None, include_rip_rport=None, log=None, severity=None, source_port=None):
		self.name = name
		self.facility = facility
		self.include_destination = include_destination
		self.include_rip_rport = include_rip_rport
		self.log = log
		self.severity = severity
		self.source_port = source_port

	def __str__(self):
		return str(self.name)

class IpNatTemplateClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpNatTemplate(self):
		"""
		Retrieve the template identified by the specified identifier
		
		Returns:
			An instance of the Template class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified template does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('template')
		return deserialize_Template_json(payload)

