########################################################################################################################
# File name: ddos_dst_default_port.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/dst/default/port',
]

def deserialize_Port__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	dns = data.get('dns')
	http = data.get('http')
	ssl_l4 = data.get('ssl-l4')
	tcp = data.get('tcp')
	udp = data.get('udp')
	result = Port__template(dns=dns, http=http, ssl_l4=ssl_l4, tcp=tcp, udp=udp)
	return result

def deserialize_Port_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	port_num = data.get('port-num')
	protocol = data.get('protocol')
	deny = data.get('deny')
	glid = data.get('glid')
	template = deserialize_Port__template_json(data.get('template'))
	result = Port(port_num=port_num, protocol=protocol, deny=deny, glid=glid, template=template)
	return result

def serialize_Port__template_json(obj):
	output = OrderedDict()
	if obj.dns is not None:
		output['dns'] = obj.dns
	if obj.http is not None:
		output['http'] = obj.http
	if obj.ssl_l4 is not None:
		output['ssl-l4'] = obj.ssl_l4
	if obj.tcp is not None:
		output['tcp'] = obj.tcp
	if obj.udp is not None:
		output['udp'] = obj.udp
	return output

def serialize_Port_json(obj):
	output = OrderedDict()
	output['port-num'] = obj.port_num
	output['protocol'] = obj.protocol
	if obj.deny is not None:
		output['deny'] = obj.deny
	if obj.glid is not None:
		output['glid'] = obj.glid
	if obj.template is not None:
		output['template'] = serialize_Port__template_json(obj.template)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Port_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Port_json(item))
	return list(container)

class Port_port_num_protocol(AxapiObject):
	__metaclass__ = StructMeta 
	port_num=PosRangedInteger(1, 65534)
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'tcp', 'udp', 'ssl-l4'])
	def __init__(self, port_num, protocol):
		self.port_num = port_num
		self.protocol = protocol

	def __str__(self):
		return str(self.port_num) + '+' + str(self.protocol)

class Port__template(AxapiObject):
	__metaclass__ = StructMeta 
	dns=SizedString(1, 255)
	http=SizedString(1, 255)
	ssl_l4=SizedString(1, 255)
	tcp=SizedString(1, 255)
	udp=SizedString(1, 255)
	def __init__(self, dns=None, http=None, ssl_l4=None, tcp=None, udp=None):
		self.dns = dns
		self.http = http
		self.ssl_l4 = ssl_l4
		self.tcp = tcp
		self.udp = udp

	def __str__(self):
		return ""

class Port(AxapiObject):
	__metaclass__ = StructMeta 
	port_num=PosRangedInteger(1, 65534)
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'tcp', 'udp', 'ssl-l4'])
	deny=PosRangedInteger(0, 1)
	glid=PosRangedInteger(1, 32000)
	def __init__(self, port_num, protocol, deny=None, glid=None, template=None):
		self.port_num = port_num
		self.protocol = protocol
		self.deny = deny
		self.glid = glid
		self.template = template

	def __str__(self):
		return str(self.port_num) + '+' + str(self.protocol)

class DdosDstDefaultPortClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosDstDefaultPort(self, port_port_num_protocol):
		"""
		Retrieve the port identified by the specified identifier
		
		Args:
			port_port_num_protocol Port_port_num_protocol
		
		Returns:
			An instance of the Port class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(port_port_num_protocol) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified port does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('port')
		return deserialize_Port_json(payload)

	def putDdosDstDefaultPort(self, port_port_num_protocol, port):
		"""
		Replace the object port
		
		Args:
			port_port_num_protocol Port_port_num_protocol
			port An instance of the Port class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['port']=serialize_Port_json(port)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(port_port_num_protocol) .replace("/", "%2f") + query, payload, headers)
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

	def deleteDdosDstDefaultPort(self, port_port_num_protocol):
		"""
		Remove the port identified by the specified identifier from the system
		
		Args:
			port_port_num_protocol Port_port_num_protocol
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(port_port_num_protocol) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified port does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosDstDefaultPortsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosDstDefaultPort(self, port):
		"""
		Create the object port
		
		Args:
			port An instance of the Port class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['port']=serialize_Port_json(port)
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

	def getAllDdosDstDefaultPorts(self):
		"""
		Retrieve all port objects currently pending in the system
		
		Returns:
			A list of Port objects
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
			payload= data.get('portList')
		return deserialize_list_Port_json(payload)

