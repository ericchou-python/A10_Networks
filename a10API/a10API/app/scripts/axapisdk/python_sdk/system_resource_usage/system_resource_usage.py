########################################################################################################################
# File name: system_resource_usage.py
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
	'https://axapi.a10networks.com/axapi/v3/system/resource-usage',
]

def deserialize_Resource_usage_json(obj):
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
	result = Resource_usage(class_list_ipv6_addr_count=class_list_ipv6_addr_count, client_ssl_template_count=client_ssl_template_count, conn_reuse_template_count=conn_reuse_template_count, fast_tcp_template_count=fast_tcp_template_count, fast_udp_template_count=fast_udp_template_count, http_template_count=http_template_count, l4_session_count=l4_session_count, nat_pool_addr_count=nat_pool_addr_count, persist_cookie_template_count=persist_cookie_template_count, persist_srcip_template_count=persist_srcip_template_count, proxy_template_count=proxy_template_count, real_port_count=real_port_count, real_server_count=real_server_count, server_ssl_template_count=server_ssl_template_count, service_group_count=service_group_count, stream_template_count=stream_template_count, virtual_port_count=virtual_port_count, virtual_server_count=virtual_server_count)
	return result

def serialize_Resource_usage_json(obj):
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

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Resource_usage_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Resource_usage_json(item))
	return list(container)

class Resource_usage(AxapiObject):
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

class SystemResourceusageClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSystemResourceusage(self):
		"""
		Retrieve the resource_usage identified by the specified identifier
		
		Returns:
			An instance of the Resource_usage class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified resource_usage does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('resource-usage')
		return deserialize_Resource_usage_json(payload)

	def putSystemResourceusage(self, resource_usage):
		"""
		Replace the object resource_usage
		
		Args:
			resource_usage An instance of the Resource_usage class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['resource-usage']=serialize_Resource_usage_json(resource_usage)
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

	def deleteSystemResourceusage(self):
		"""
		Remove the resource_usage identified by the specified identifier from the
		system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified resource_usage does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllSystemResourceusagesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitSystemResourceusage(self, resource_usage):
		"""
		Create the object resource_usage
		
		Args:
			resource_usage An instance of the Resource_usage class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['resource-usage']=serialize_Resource_usage_json(resource_usage)
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

	def getAllSystemResourceusages(self):
		"""
		Retrieve all resource_usage objects currently pending in the system
		
		Returns:
			A list of Resource_usage objects
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
			payload= data.get('resource-usageList')
		return deserialize_list_Resource_usage_json(payload)

