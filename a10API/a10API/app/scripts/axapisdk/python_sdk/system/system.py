########################################################################################################################
# File name: system.py
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
	'https://axapi.a10networks.com/axapi/v3/system',
]

def deserialize_System__resource_usage_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	class_list_ipv6_addr_count = data.get('class-list-ipv6-addr-count')
	client_ssl_template_count = data.get('client-ssl-template-count')
	conn_reuse_template_count = data.get('conn-reuse-template-count')
	fast_tcp_template_count = data.get('fast-tcp-template-count')
	fast_udp_template_count = data.get('fast-udp-template-count')
	http_template_count = data.get('http-template-count')
	l4_session_count = data.get('l4-session-count')
	nat_pool_addr_count = data.get('nat-pool-addr-count')
	persist_cookie_template_count = data.get('persist-cookie-template-count')
	persist_srcip_template_count = data.get('persist-srcip-template-count')
	proxy_template_count = data.get('proxy-template-count')
	real_port_count = data.get('real-port-count')
	real_server_count = data.get('real-server-count')
	server_ssl_template_count = data.get('server-ssl-template-count')
	service_group_count = data.get('service-group-count')
	stream_template_count = data.get('stream-template-count')
	virtual_port_count = data.get('virtual-port-count')
	virtual_server_count = data.get('virtual-server-count')
	result = System__resource_usage(class_list_ipv6_addr_count=class_list_ipv6_addr_count, client_ssl_template_count=client_ssl_template_count, conn_reuse_template_count=conn_reuse_template_count, fast_tcp_template_count=fast_tcp_template_count, fast_udp_template_count=fast_udp_template_count, http_template_count=http_template_count, l4_session_count=l4_session_count, nat_pool_addr_count=nat_pool_addr_count, persist_cookie_template_count=persist_cookie_template_count, persist_srcip_template_count=persist_srcip_template_count, proxy_template_count=proxy_template_count, real_port_count=real_port_count, real_server_count=real_server_count, server_ssl_template_count=server_ssl_template_count, service_group_count=service_group_count, stream_template_count=stream_template_count, virtual_port_count=virtual_port_count, virtual_server_count=virtual_server_count)
	return result

def deserialize_System__cpu_load_sharing__packets_per_second_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	min = data.get('min')
	result = System__cpu_load_sharing__packets_per_second(min=min)
	return result

def deserialize_System__cpu_load_sharing__cpu_usage_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	low = data.get('low')
	high = data.get('high')
	result = System__cpu_load_sharing__cpu_usage(low=low, high=high)
	return result

def deserialize_System__cpu_load_sharing_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	disable = data.get('disable')
	packets_per_second = deserialize_System__cpu_load_sharing__packets_per_second_json(data.get('packets-per-second'))
	cpu_usage = deserialize_System__cpu_load_sharing__cpu_usage_json(data.get('cpu-usage'))
	result = System__cpu_load_sharing(disable=disable, packets_per_second=packets_per_second, cpu_usage=cpu_usage)
	return result

def deserialize_System__per_vlan_limit_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	bcast = data.get('bcast')
	ipmcast = data.get('ipmcast')
	mcast = data.get('mcast')
	unknown_ucast = data.get('unknown-ucast')
	result = System__per_vlan_limit(bcast=bcast, ipmcast=ipmcast, mcast=mcast, unknown_ucast=unknown_ucast)
	return result

def deserialize_System_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	anomaly = data.get('anomaly')
	log = data.get('log')
	attack = data.get('attack')
	ddos_attack = data.get('ddos-attack')
	log_cpu_interval = data.get('log-cpu-interval')
	promiscuous_mode = data.get('promiscuous-mode')
	resource_usage = deserialize_System__resource_usage_json(data.get('resource-usage'))
	cpu_load_sharing = deserialize_System__cpu_load_sharing_json(data.get('cpu-load-sharing'))
	per_vlan_limit = deserialize_System__per_vlan_limit_json(data.get('per-vlan-limit'))
	result = System(anomaly=anomaly, log=log, attack=attack, ddos_attack=ddos_attack, log_cpu_interval=log_cpu_interval, promiscuous_mode=promiscuous_mode, resource_usage=resource_usage, cpu_load_sharing=cpu_load_sharing, per_vlan_limit=per_vlan_limit)
	return result

def serialize_System__resource_usage_json(obj):
	output = OrderedDict()
	if obj.class_list_ipv6_addr_count is not None:
		output['class-list-ipv6-addr-count'] = obj.class_list_ipv6_addr_count
	if obj.client_ssl_template_count is not None:
		output['client-ssl-template-count'] = obj.client_ssl_template_count
	if obj.conn_reuse_template_count is not None:
		output['conn-reuse-template-count'] = obj.conn_reuse_template_count
	if obj.fast_tcp_template_count is not None:
		output['fast-tcp-template-count'] = obj.fast_tcp_template_count
	if obj.fast_udp_template_count is not None:
		output['fast-udp-template-count'] = obj.fast_udp_template_count
	if obj.http_template_count is not None:
		output['http-template-count'] = obj.http_template_count
	if obj.l4_session_count is not None:
		output['l4-session-count'] = obj.l4_session_count
	if obj.nat_pool_addr_count is not None:
		output['nat-pool-addr-count'] = obj.nat_pool_addr_count
	if obj.persist_cookie_template_count is not None:
		output['persist-cookie-template-count'] = obj.persist_cookie_template_count
	if obj.persist_srcip_template_count is not None:
		output['persist-srcip-template-count'] = obj.persist_srcip_template_count
	if obj.proxy_template_count is not None:
		output['proxy-template-count'] = obj.proxy_template_count
	if obj.real_port_count is not None:
		output['real-port-count'] = obj.real_port_count
	if obj.real_server_count is not None:
		output['real-server-count'] = obj.real_server_count
	if obj.server_ssl_template_count is not None:
		output['server-ssl-template-count'] = obj.server_ssl_template_count
	if obj.service_group_count is not None:
		output['service-group-count'] = obj.service_group_count
	if obj.stream_template_count is not None:
		output['stream-template-count'] = obj.stream_template_count
	if obj.virtual_port_count is not None:
		output['virtual-port-count'] = obj.virtual_port_count
	if obj.virtual_server_count is not None:
		output['virtual-server-count'] = obj.virtual_server_count
	return output

def serialize_System__cpu_load_sharing__packets_per_second_json(obj):
	output = OrderedDict()
	if obj.min is not None:
		output['min'] = obj.min
	return output

def serialize_System__cpu_load_sharing__cpu_usage_json(obj):
	output = OrderedDict()
	if obj.low is not None:
		output['low'] = obj.low
	if obj.high is not None:
		output['high'] = obj.high
	return output

def serialize_System__cpu_load_sharing_json(obj):
	output = OrderedDict()
	if obj.disable is not None:
		output['disable'] = obj.disable
	if obj.packets_per_second is not None:
		output['packets-per-second'] = serialize_System__cpu_load_sharing__packets_per_second_json(obj.packets_per_second)
	if obj.cpu_usage is not None:
		output['cpu-usage'] = serialize_System__cpu_load_sharing__cpu_usage_json(obj.cpu_usage)
	return output

def serialize_System__per_vlan_limit_json(obj):
	output = OrderedDict()
	if obj.bcast is not None:
		output['bcast'] = obj.bcast
	if obj.ipmcast is not None:
		output['ipmcast'] = obj.ipmcast
	if obj.mcast is not None:
		output['mcast'] = obj.mcast
	if obj.unknown_ucast is not None:
		output['unknown-ucast'] = obj.unknown_ucast
	return output

def serialize_System_json(obj):
	output = OrderedDict()
	if obj.anomaly is not None:
		output['anomaly'] = obj.anomaly
	if obj.log is not None:
		output['log'] = obj.log
	if obj.attack is not None:
		output['attack'] = obj.attack
	if obj.ddos_attack is not None:
		output['ddos-attack'] = obj.ddos_attack
	if obj.log_cpu_interval is not None:
		output['log-cpu-interval'] = obj.log_cpu_interval
	if obj.promiscuous_mode is not None:
		output['promiscuous-mode'] = obj.promiscuous_mode
	if obj.resource_usage is not None:
		output['resource-usage'] = serialize_System__resource_usage_json(obj.resource_usage)
	if obj.cpu_load_sharing is not None:
		output['cpu-load-sharing'] = serialize_System__cpu_load_sharing_json(obj.cpu_load_sharing)
	if obj.per_vlan_limit is not None:
		output['per-vlan-limit'] = serialize_System__per_vlan_limit_json(obj.per_vlan_limit)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_System_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_System_json(item))
	return list(container)

class System__resource_usage(AxapiObject):
	__metaclass__ = StructMeta 
	class_list_ipv6_addr_count=PosRangedInteger(4096000, 8192000)
	client_ssl_template_count=PosRangedInteger(32, 16384)
	conn_reuse_template_count=PosRangedInteger(32, 8192)
	fast_tcp_template_count=PosRangedInteger(32, 8192)
	fast_udp_template_count=PosRangedInteger(32, 8192)
	http_template_count=PosRangedInteger(32, 8192)
	l4_session_count=PosRangedInteger(4194304, 268435456)
	nat_pool_addr_count=PosRangedInteger(500, 10000)
	persist_cookie_template_count=PosRangedInteger(32, 8192)
	persist_srcip_template_count=PosRangedInteger(32, 8192)
	proxy_template_count=PosRangedInteger(32, 8192)
	real_port_count=PosRangedInteger(512, 32768)
	real_server_count=PosRangedInteger(512, 16384)
	server_ssl_template_count=PosRangedInteger(32, 16384)
	service_group_count=PosRangedInteger(512, 16384)
	stream_template_count=PosRangedInteger(32, 8192)
	virtual_port_count=PosRangedInteger(256, 16384)
	virtual_server_count=PosRangedInteger(512, 8192)
	def __init__(self, class_list_ipv6_addr_count=None, client_ssl_template_count=None, conn_reuse_template_count=None, fast_tcp_template_count=None, fast_udp_template_count=None, http_template_count=None, l4_session_count=None, nat_pool_addr_count=None, persist_cookie_template_count=None, persist_srcip_template_count=None, proxy_template_count=None, real_port_count=None, real_server_count=None, server_ssl_template_count=None, service_group_count=None, stream_template_count=None, virtual_port_count=None, virtual_server_count=None):
		self.class_list_ipv6_addr_count = class_list_ipv6_addr_count
		self.client_ssl_template_count = client_ssl_template_count
		self.conn_reuse_template_count = conn_reuse_template_count
		self.fast_tcp_template_count = fast_tcp_template_count
		self.fast_udp_template_count = fast_udp_template_count
		self.http_template_count = http_template_count
		self.l4_session_count = l4_session_count
		self.nat_pool_addr_count = nat_pool_addr_count
		self.persist_cookie_template_count = persist_cookie_template_count
		self.persist_srcip_template_count = persist_srcip_template_count
		self.proxy_template_count = proxy_template_count
		self.real_port_count = real_port_count
		self.real_server_count = real_server_count
		self.server_ssl_template_count = server_ssl_template_count
		self.service_group_count = service_group_count
		self.stream_template_count = stream_template_count
		self.virtual_port_count = virtual_port_count
		self.virtual_server_count = virtual_server_count

	def __str__(self):
		return ""

class System__cpu_load_sharing__packets_per_second(AxapiObject):
	__metaclass__ = StructMeta 
	min=PosRangedInteger(0, 30000000)
	def __init__(self, min=None):
		self.min = min

	def __str__(self):
		return ""

class System__cpu_load_sharing__cpu_usage(AxapiObject):
	__metaclass__ = StructMeta 
	low=PosRangedInteger(0, 100)
	high=PosRangedInteger(0, 100)
	def __init__(self, low=None, high=None):
		self.low = low
		self.high = high

	def __str__(self):
		return ""

class System__cpu_load_sharing(AxapiObject):
	__metaclass__ = StructMeta 
	disable=PosRangedInteger(0, 1)
	def __init__(self, disable=None, packets_per_second=None, cpu_usage=None):
		self.disable = disable
		self.packets_per_second = packets_per_second
		self.cpu_usage = cpu_usage

	def __str__(self):
		return ""

class System__per_vlan_limit(AxapiObject):
	__metaclass__ = StructMeta 
	bcast=PosRangedInteger(1, 65535)
	ipmcast=PosRangedInteger(1, 65535)
	mcast=PosRangedInteger(1, 65535)
	unknown_ucast=PosRangedInteger(1, 65535)
	def __init__(self, bcast=None, ipmcast=None, mcast=None, unknown_ucast=None):
		self.bcast = bcast
		self.ipmcast = ipmcast
		self.mcast = mcast
		self.unknown_ucast = unknown_ucast

	def __str__(self):
		return ""

class System(AxapiObject):
	__metaclass__ = StructMeta 
	anomaly=PosRangedInteger(0, 1)
	log=PosRangedInteger(0, 1)
	attack=PosRangedInteger(0, 1)
	ddos_attack=PosRangedInteger(0, 1)
	log_cpu_interval=PosRangedInteger(15, 255)
	promiscuous_mode=PosRangedInteger(0, 1)
	def __init__(self, anomaly=None, log=None, attack=None, ddos_attack=None, log_cpu_interval=None, promiscuous_mode=None, resource_usage=None, cpu_load_sharing=None, per_vlan_limit=None):
		self.anomaly = anomaly
		self.log = log
		self.attack = attack
		self.ddos_attack = ddos_attack
		self.log_cpu_interval = log_cpu_interval
		self.promiscuous_mode = promiscuous_mode
		self.resource_usage = resource_usage
		self.cpu_load_sharing = cpu_load_sharing
		self.per_vlan_limit = per_vlan_limit

	def __str__(self):
		return ""

class SystemClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSystem(self):
		"""
		Retrieve the system identified by the specified identifier
		
		Returns:
			An instance of the System class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified system does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('system')
		return deserialize_System_json(payload)

	def putSystem(self, system):
		"""
		Replace the object system
		
		Args:
			system An instance of the System class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['system']=serialize_System_json(system)
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

	def deleteSystem(self):
		"""
		Remove the system identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified system does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSystemsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSystem(self, system):
		"""
		Create the object system
		
		Args:
			system An instance of the System class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['system']=serialize_System_json(system)
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

	def getAllSystems(self):
		"""
		Retrieve all system objects currently pending in the system
		
		Returns:
			A list of System objects
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
			payload= data.get('systemList')
		return deserialize_list_System_json(payload)

