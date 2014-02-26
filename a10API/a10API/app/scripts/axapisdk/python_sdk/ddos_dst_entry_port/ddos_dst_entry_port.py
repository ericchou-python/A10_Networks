########################################################################################################################
# File name: ddos_dst_entry_port.py
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
	'https://axapi.a10networks.com/axapi/v3/ddos/dst/entry/port',
]

def deserialize_Ddos_dst_entry_port_aflex_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	aflex = data.get('aflex')
	result = Ddos_dst_entry_port_aflex_cfg(aflex=aflex)
	return result

def deserialize_list_Ddos_dst_entry_port_aflex_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ddos_dst_entry_port_aflex_cfg_json(item))
	return list(container)

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

def deserialize_Port__sflow__polling__sflow_tcp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sflow_tcp_basic = data.get('sflow-tcp-basic')
	sflow_tcp_stateful = data.get('sflow-tcp-stateful')
	result = Port__sflow__polling__sflow_tcp(sflow_tcp_basic=sflow_tcp_basic, sflow_tcp_stateful=sflow_tcp_stateful)
	return result

def deserialize_Port__sflow__polling_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	sflow_packets = data.get('sflow-packets')
	sflow_tcp = deserialize_Port__sflow__polling__sflow_tcp_json(data.get('sflow-tcp'))
	sflow_http = data.get('sflow-http')
	result = Port__sflow__polling(sflow_packets=sflow_packets, sflow_tcp=sflow_tcp, sflow_http=sflow_http)
	return result

def deserialize_Port__sflow_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	polling = deserialize_Port__sflow__polling_json(data.get('polling'))
	result = Port__sflow(polling=polling)
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
	aflex_cfg = deserialize_list_Ddos_dst_entry_port_aflex_cfg_json(data.get('aflex-cfg'))
	template = deserialize_Port__template_json(data.get('template'))
	sflow = deserialize_Port__sflow_json(data.get('sflow'))
	result = Port(port_num=port_num, protocol=protocol, deny=deny, glid=glid, aflex_cfg=aflex_cfg, template=template, sflow=sflow)
	return result

def serialize_Ddos_dst_entry_port_aflex_cfg_json(obj):
	output = OrderedDict()
	if obj.aflex is not None:
		output['aflex'] = obj.aflex
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ddos_dst_entry_port_aflex_cfg_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ddos_dst_entry_port_aflex_cfg_json(item))
	return output

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

def serialize_Port__sflow__polling__sflow_tcp_json(obj):
	output = OrderedDict()
	if obj.sflow_tcp_basic is not None:
		output['sflow-tcp-basic'] = obj.sflow_tcp_basic
	if obj.sflow_tcp_stateful is not None:
		output['sflow-tcp-stateful'] = obj.sflow_tcp_stateful
	return output

def serialize_Port__sflow__polling_json(obj):
	output = OrderedDict()
	if obj.sflow_packets is not None:
		output['sflow-packets'] = obj.sflow_packets
	if obj.sflow_tcp is not None:
		output['sflow-tcp'] = serialize_Port__sflow__polling__sflow_tcp_json(obj.sflow_tcp)
	if obj.sflow_http is not None:
		output['sflow-http'] = obj.sflow_http
	return output

def serialize_Port__sflow_json(obj):
	output = OrderedDict()
	if obj.polling is not None:
		output['polling'] = serialize_Port__sflow__polling_json(obj.polling)
	return output

def serialize_Port_json(obj):
	output = OrderedDict()
	output['port-num'] = obj.port_num
	output['protocol'] = obj.protocol
	if obj.deny is not None:
		output['deny'] = obj.deny
	if obj.glid is not None:
		output['glid'] = obj.glid
	if obj.aflex_cfg is not None:
		output['aflex-cfg'] = serialize_list_Ddos_dst_entry_port_aflex_cfg_json(obj.aflex_cfg)
	if obj.template is not None:
		output['template'] = serialize_Port__template_json(obj.template)
	if obj.sflow is not None:
		output['sflow'] = serialize_Port__sflow_json(obj.sflow)
	return output

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

class Port__sflow__polling__sflow_tcp(AxapiObject):
	__metaclass__ = StructMeta 
	sflow_tcp_basic=PosRangedInteger(0, 1)
	sflow_tcp_stateful=PosRangedInteger(0, 1)
	def __init__(self, sflow_tcp_basic=None, sflow_tcp_stateful=None):
		self.sflow_tcp_basic = sflow_tcp_basic
		self.sflow_tcp_stateful = sflow_tcp_stateful

	def __str__(self):
		return ""

class Port__sflow__polling(AxapiObject):
	__metaclass__ = StructMeta 
	sflow_packets=PosRangedInteger(0, 1)
	sflow_http=PosRangedInteger(0, 1)
	def __init__(self, sflow_packets=None, sflow_tcp=None, sflow_http=None):
		self.sflow_packets = sflow_packets
		self.sflow_tcp = sflow_tcp
		self.sflow_http = sflow_http

	def __str__(self):
		return ""

class Port__sflow(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, polling=None):
		self.polling = polling

	def __str__(self):
		return ""

class Port(AxapiObject):
	__metaclass__ = StructMeta 
	port_num=PosRangedInteger(1, 65534)
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'tcp', 'udp', 'ssl-l4'])
	deny=PosRangedInteger(0, 1)
	glid=PosRangedInteger(1, 32000)
	def __init__(self, port_num, protocol, deny=None, glid=None, aflex_cfg=None, template=None, sflow=None):
		self.port_num = port_num
		self.protocol = protocol
		self.deny = deny
		self.glid = glid
		self.aflex_cfg = aflex_cfg
		self.template = template
		self.sflow = sflow

	def __str__(self):
		return str(self.port_num) + '+' + str(self.protocol)

class Port_port_num_protocol(AxapiObject):
	__metaclass__ = StructMeta 
	port_num=PosRangedInteger(1, 65534)
	protocol = Enum(['dns-tcp', 'dns-udp', 'http', 'tcp', 'udp', 'ssl-l4'])
	def __init__(self, port_num, protocol):
		self.port_num = port_num
		self.protocol = protocol

	def __str__(self):
		return str(self.port_num) + '+' + str(self.protocol)

class Ddos_dst_entry_port_aflex_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	aflex=SizedString(1, 63)
	def __init__(self, aflex=None):
		self.aflex = aflex

	def __str__(self):
		return ""

class DdosDstEntryPortClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosDstEntryPort(self, port_port_num_protocol):
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

	def putDdosDstEntryPort(self, port_port_num_protocol, port):
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

	def deleteDdosDstEntryPort(self, port_port_num_protocol):
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

class AllDdosDstEntryPortsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosDstEntryPort(self, port):
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

	def getAllDdosDstEntryPorts(self):
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

