########################################################################################################################
# File name: monitor.py
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
	'https://axapi.a10networks.com/axapi/v3/monitor',
]

def deserialize_Monitor_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	disk = data.get('disk')
	memory = data.get('memory')
	ctrl_cpu = data.get('ctrl-cpu')
	data_cpu = data.get('data-cpu')
	buffer_usage = data.get('buffer-usage')
	buffer_drop = data.get('buffer-drop')
	warn_temp = data.get('warn-temp')
	conn_type0 = data.get('conn-type0')
	conn_type1 = data.get('conn-type1')
	conn_type2 = data.get('conn-type2')
	conn_type3 = data.get('conn-type3')
	conn_type4 = data.get('conn-type4')
	smp_type0 = data.get('smp-type0')
	smp_type1 = data.get('smp-type1')
	smp_type2 = data.get('smp-type2')
	smp_type3 = data.get('smp-type3')
	smp_type4 = data.get('smp-type4')
	result = Monitor(disk=disk, memory=memory, ctrl_cpu=ctrl_cpu, data_cpu=data_cpu, buffer_usage=buffer_usage, buffer_drop=buffer_drop, warn_temp=warn_temp, conn_type0=conn_type0, conn_type1=conn_type1, conn_type2=conn_type2, conn_type3=conn_type3, conn_type4=conn_type4, smp_type0=smp_type0, smp_type1=smp_type1, smp_type2=smp_type2, smp_type3=smp_type3, smp_type4=smp_type4)
	return result

def serialize_Monitor_json(obj):
	output = OrderedDict()
	if obj.disk is not None:
		output['disk'] = obj.disk
	if obj.memory is not None:
		output['memory'] = obj.memory
	if obj.ctrl_cpu is not None:
		output['ctrl-cpu'] = obj.ctrl_cpu
	if obj.data_cpu is not None:
		output['data-cpu'] = obj.data_cpu
	if obj.buffer_usage is not None:
		output['buffer-usage'] = obj.buffer_usage
	if obj.buffer_drop is not None:
		output['buffer-drop'] = obj.buffer_drop
	if obj.warn_temp is not None:
		output['warn-temp'] = obj.warn_temp
	if obj.conn_type0 is not None:
		output['conn-type0'] = obj.conn_type0
	if obj.conn_type1 is not None:
		output['conn-type1'] = obj.conn_type1
	if obj.conn_type2 is not None:
		output['conn-type2'] = obj.conn_type2
	if obj.conn_type3 is not None:
		output['conn-type3'] = obj.conn_type3
	if obj.conn_type4 is not None:
		output['conn-type4'] = obj.conn_type4
	if obj.smp_type0 is not None:
		output['smp-type0'] = obj.smp_type0
	if obj.smp_type1 is not None:
		output['smp-type1'] = obj.smp_type1
	if obj.smp_type2 is not None:
		output['smp-type2'] = obj.smp_type2
	if obj.smp_type3 is not None:
		output['smp-type3'] = obj.smp_type3
	if obj.smp_type4 is not None:
		output['smp-type4'] = obj.smp_type4
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

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

class Monitor(AxapiObject):
	__metaclass__ = StructMeta 
	disk=PosRangedInteger(1, 100)
	memory=PosRangedInteger(1, 100)
	ctrl_cpu=PosRangedInteger(1, 100)
	data_cpu=PosRangedInteger(1, 100)
	buffer_usage=PosRangedInteger(60000, 4000000)
	buffer_drop=PosRangedInteger(1, 32767)
	warn_temp=PosRangedInteger(1, 68)
	conn_type0=PosRangedInteger(32767, 256000000)
	conn_type1=PosRangedInteger(32767, 256000000)
	conn_type2=PosRangedInteger(32767, 256000000)
	conn_type3=PosRangedInteger(32767, 256000000)
	conn_type4=PosRangedInteger(32767, 256000000)
	smp_type0=PosRangedInteger(32767, 256000000)
	smp_type1=PosRangedInteger(32767, 256000000)
	smp_type2=PosRangedInteger(32767, 256000000)
	smp_type3=PosRangedInteger(32767, 256000000)
	smp_type4=PosRangedInteger(32767, 256000000)
	def __init__(self, disk=None, memory=None, ctrl_cpu=None, data_cpu=None, buffer_usage=None, buffer_drop=None, warn_temp=None, conn_type0=None, conn_type1=None, conn_type2=None, conn_type3=None, conn_type4=None, smp_type0=None, smp_type1=None, smp_type2=None, smp_type3=None, smp_type4=None):
		self.disk = disk
		self.memory = memory
		self.ctrl_cpu = ctrl_cpu
		self.data_cpu = data_cpu
		self.buffer_usage = buffer_usage
		self.buffer_drop = buffer_drop
		self.warn_temp = warn_temp
		self.conn_type0 = conn_type0
		self.conn_type1 = conn_type1
		self.conn_type2 = conn_type2
		self.conn_type3 = conn_type3
		self.conn_type4 = conn_type4
		self.smp_type0 = smp_type0
		self.smp_type1 = smp_type1
		self.smp_type2 = smp_type2
		self.smp_type3 = smp_type3
		self.smp_type4 = smp_type4

	def __str__(self):
		return ""

class MonitorClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getMonitor(self):
		"""
		Retrieve the monitor identified by the specified identifier
		
		Returns:
			An instance of the Monitor class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
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

	def putMonitor(self, monitor):
		"""
		Replace the object monitor
		
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

	def deleteMonitor(self):
		"""
		Remove the monitor identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
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

class AllMonitorsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitMonitor(self, monitor):
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

	def getAllMonitors(self):
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

