########################################################################################################################
# File name: netflow_monitor.py
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
	'https://axapi.a10networks.com/axapi/v3/netflow/monitor',
]

def deserialize_Monitor__protocol_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	version = data.get('version')
	result = Monitor__protocol(version=version)
	return result

def deserialize_Netflow_monitor_record_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	template = data.get('template')
	result = Netflow_monitor_record(template=template)
	return result

def deserialize_list_Netflow_monitor_record_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Netflow_monitor_record_json(item))
	return list(container)

def deserialize_Monitor__destination__ip_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip = data.get('ip')
	port4 = data.get('port4')
	result = Monitor__destination__ip_cfg(ip=ip, port4=port4)
	return result

def deserialize_Monitor__destination__ipv6_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ipv6 = data.get('ipv6')
	port6 = data.get('port6')
	result = Monitor__destination__ipv6_cfg(ipv6=ipv6, port6=port6)
	return result

def deserialize_Monitor__destination_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_cfg = deserialize_Monitor__destination__ip_cfg_json(data.get('ip-cfg'))
	ipv6_cfg = deserialize_Monitor__destination__ipv6_cfg_json(data.get('ipv6-cfg'))
	result = Monitor__destination(ip_cfg=ip_cfg, ipv6_cfg=ipv6_cfg)
	return result

def deserialize_Monitor__source_address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip = data.get('ip')
	ipv6 = data.get('ipv6')
	result = Monitor__source_address(ip=ip, ipv6=ipv6)
	return result

def deserialize_Monitor__resend_template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	timeout = data.get('timeout')
	records = data.get('records')
	result = Monitor__resend_template(timeout=timeout, records=records)
	return result

def deserialize_Monitor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	enable = data.get('enable')
	disable = data.get('disable')
	source_ip_use_mgmt = data.get('source-ip-use-mgmt')
	flow_timeout = data.get('flow-timeout')
	protocol = deserialize_Monitor__protocol_json(data.get('protocol'))
	recordlist = deserialize_list_Netflow_monitor_record_json(data.get('recordList'))
	destination = deserialize_Monitor__destination_json(data.get('destination'))
	source_address = deserialize_Monitor__source_address_json(data.get('source-address'))
	resend_template = deserialize_Monitor__resend_template_json(data.get('resend-template'))
	result = Monitor(name=name, enable=enable, disable=disable, source_ip_use_mgmt=source_ip_use_mgmt, flow_timeout=flow_timeout, protocol=protocol, recordlist=recordlist, destination=destination, source_address=source_address, resend_template=resend_template)
	return result

def serialize_Monitor__protocol_json(obj):
	output = OrderedDict()
	if obj.version is not None:
		output['version'] = obj.version
	return output

def serialize_Netflow_monitor_record_json(obj):
	output = OrderedDict()
	output['template'] = obj.template
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Netflow_monitor_record_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Netflow_monitor_record_json(item))
	return output

def serialize_Monitor__destination__ip_cfg_json(obj):
	output = OrderedDict()
	if obj.ip is not None:
		output['ip'] = obj.ip
	if obj.port4 is not None:
		output['port4'] = obj.port4
	return output

def serialize_Monitor__destination__ipv6_cfg_json(obj):
	output = OrderedDict()
	if obj.ipv6 is not None:
		output['ipv6'] = obj.ipv6
	if obj.port6 is not None:
		output['port6'] = obj.port6
	return output

def serialize_Monitor__destination_json(obj):
	output = OrderedDict()
	if obj.ip_cfg is not None:
		output['ip-cfg'] = serialize_Monitor__destination__ip_cfg_json(obj.ip_cfg)
	if obj.ipv6_cfg is not None:
		output['ipv6-cfg'] = serialize_Monitor__destination__ipv6_cfg_json(obj.ipv6_cfg)
	return output

def serialize_Monitor__source_address_json(obj):
	output = OrderedDict()
	if obj.ip is not None:
		output['ip'] = obj.ip
	if obj.ipv6 is not None:
		output['ipv6'] = obj.ipv6
	return output

def serialize_Monitor__resend_template_json(obj):
	output = OrderedDict()
	if obj.timeout is not None:
		output['timeout'] = obj.timeout
	if obj.records is not None:
		output['records'] = obj.records
	return output

def serialize_Monitor_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.enable is not None:
		output['enable'] = obj.enable
	if obj.disable is not None:
		output['disable'] = obj.disable
	if obj.source_ip_use_mgmt is not None:
		output['source-ip-use-mgmt'] = obj.source_ip_use_mgmt
	if obj.flow_timeout is not None:
		output['flow-timeout'] = obj.flow_timeout
	if obj.protocol is not None:
		output['protocol'] = serialize_Monitor__protocol_json(obj.protocol)
	if obj.recordlist is not None:
		output['recordList'] = serialize_list_Netflow_monitor_record_json(obj.recordlist)
	if obj.destination is not None:
		output['destination'] = serialize_Monitor__destination_json(obj.destination)
	if obj.source_address is not None:
		output['source-address'] = serialize_Monitor__source_address_json(obj.source_address)
	if obj.resend_template is not None:
		output['resend-template'] = serialize_Monitor__resend_template_json(obj.resend_template)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Monitor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Monitor_json(item))
	return list(container)

class Monitor__protocol(AxapiObject):
	__metaclass__ = StructMeta 
	version = Enum(['v9', 'v10'])
	def __init__(self, version=None):
		self.version = version

	def __str__(self):
		return ""

class Monitor__destination__ip_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	port4=PosRangedInteger(1, 65535)
	def __init__(self, ip=None, port4=None):
		self.ip = ip
		self.port4 = port4

	def __str__(self):
		return ""

class Monitor__destination__ipv6_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ipv6=SizedString(1, 255)
	port6=PosRangedInteger(1, 65535)
	def __init__(self, ipv6=None, port6=None):
		self.ipv6 = ipv6
		self.port6 = port6

	def __str__(self):
		return ""

class Monitor__destination(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ip_cfg=None, ipv6_cfg=None):
		self.ip_cfg = ip_cfg
		self.ipv6_cfg = ipv6_cfg

	def __str__(self):
		return ""

class Monitor__source_address(AxapiObject):
	__metaclass__ = StructMeta 
	ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6=SizedString(1, 255)
	def __init__(self, ip=None, ipv6=None):
		self.ip = ip
		self.ipv6 = ipv6

	def __str__(self):
		return ""

class Monitor__resend_template(AxapiObject):
	__metaclass__ = StructMeta 
	timeout=PosRangedInteger(0, 86400)
	records=PosRangedInteger(0, 1000000)
	def __init__(self, timeout=None, records=None):
		self.timeout = timeout
		self.records = records

	def __str__(self):
		return ""

class Monitor(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	enable=PosRangedInteger(0, 1)
	disable=PosRangedInteger(0, 1)
	source_ip_use_mgmt=PosRangedInteger(0, 1)
	flow_timeout=PosRangedInteger(0, 1440)
	def __init__(self, name, enable=None, disable=None, source_ip_use_mgmt=None, flow_timeout=None, protocol=None, recordlist=None, destination=None, source_address=None, resend_template=None):
		self.name = name
		self.enable = enable
		self.disable = disable
		self.source_ip_use_mgmt = source_ip_use_mgmt
		self.flow_timeout = flow_timeout
		self.protocol = protocol
		self.recordlist = recordlist
		self.destination = destination
		self.source_address = source_address
		self.resend_template = resend_template

	def __str__(self):
		return str(self.name)

class Monitor_name(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 63)
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class Netflow_monitor_record(AxapiObject):
	__metaclass__ = StructMeta 
	template = Enum(['netflow-v5'])
	def __init__(self, template):
		self.template = template

	def __str__(self):
		return str(self.template)

class NetflowMonitorClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getNetflowMonitor(self, monitor_name):
		"""
		Retrieve the monitor identified by the specified identifier
		
		Args:
			monitor_name Monitor_name
		
		Returns:
			An instance of the Monitor class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(monitor_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified monitor does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('monitor')
		return deserialize_Monitor_json(payload)

	def putNetflowMonitor(self, monitor_name, monitor):
		"""
		Replace the object monitor
		
		Args:
			monitor_name Monitor_name
			monitor An instance of the Monitor class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['monitor']=serialize_Monitor_json(monitor)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(monitor_name) .replace("/", "%2f") + query, payload, headers)
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

	def deleteNetflowMonitor(self, monitor_name):
		"""
		Remove the monitor identified by the specified identifier from the system
		
		Args:
			monitor_name Monitor_name
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(monitor_name) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified monitor does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllNetflowMonitorsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitNetflowMonitor(self, monitor):
		"""
		Create the object monitor
		
		Args:
			monitor An instance of the Monitor class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['monitor']=serialize_Monitor_json(monitor)
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

	def getAllNetflowMonitors(self):
		"""
		Retrieve all monitor objects currently pending in the system
		
		Returns:
			A list of Monitor objects
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
			payload= data.get('monitorList')
		return deserialize_list_Monitor_json(payload)

