########################################################################################################################
# File name: disable_management_service.py
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
	'https://axapi.a10networks.com/axapi/v3/disable-management/service',
]

def deserialize_Disable_management_service_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernet_start = data.get('ethernet-start')
	ethernet_end = data.get('ethernet-end')
	result = Disable_management_service_eth_cfg(ethernet_start=ethernet_start, ethernet_end=ethernet_end)
	return result

def deserialize_list_Disable_management_service_eth_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Disable_management_service_eth_cfg_json(item))
	return list(container)

def deserialize_Disable_management_service_ve_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ve_start = data.get('ve-start')
	ve_end = data.get('ve-end')
	result = Disable_management_service_ve_cfg(ve_start=ve_start, ve_end=ve_end)
	return result

def deserialize_list_Disable_management_service_ve_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Disable_management_service_ve_cfg_json(item))
	return list(container)

def deserialize_Service__ping_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	management = data.get('management')
	eth_cfg = deserialize_list_Disable_management_service_eth_cfg_json(data.get('eth-cfg'))
	ve_cfg = deserialize_list_Disable_management_service_ve_cfg_json(data.get('ve-cfg'))
	result = Service__ping(management=management, eth_cfg=eth_cfg, ve_cfg=ve_cfg)
	return result

def deserialize_Service__ssh_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	management = data.get('management')
	result = Service__ssh(management=management)
	return result

def deserialize_Service__http_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	management = data.get('management')
	result = Service__http(management=management)
	return result

def deserialize_Service__https_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	management = data.get('management')
	result = Service__https(management=management)
	return result

def deserialize_Service__snmp_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	management = data.get('management')
	result = Service__snmp(management=management)
	return result

def deserialize_Service_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ping = deserialize_Service__ping_json(data.get('ping'))
	ssh = deserialize_Service__ssh_json(data.get('ssh'))
	http = deserialize_Service__http_json(data.get('http'))
	https = deserialize_Service__https_json(data.get('https'))
	snmp = deserialize_Service__snmp_json(data.get('snmp'))
	result = Service(ping=ping, ssh=ssh, http=http, https=https, snmp=snmp)
	return result

class Service__ping(AxapiObject):
	__metaclass__ = StructMeta 
	management=PosRangedInteger(0, 1)
	def __init__(self, management=None, eth_cfg=None, ve_cfg=None):
		self.management = management
		self.eth_cfg = eth_cfg
		self.ve_cfg = ve_cfg

	def __str__(self):
		return ""

class Service__ssh(AxapiObject):
	__metaclass__ = StructMeta 
	management=PosRangedInteger(0, 1)
	def __init__(self, management=None):
		self.management = management

	def __str__(self):
		return ""

class Service__http(AxapiObject):
	__metaclass__ = StructMeta 
	management=PosRangedInteger(0, 1)
	def __init__(self, management=None):
		self.management = management

	def __str__(self):
		return ""

class Service__https(AxapiObject):
	__metaclass__ = StructMeta 
	management=PosRangedInteger(0, 1)
	def __init__(self, management=None):
		self.management = management

	def __str__(self):
		return ""

class Service__snmp(AxapiObject):
	__metaclass__ = StructMeta 
	management=PosRangedInteger(0, 1)
	def __init__(self, management=None):
		self.management = management

	def __str__(self):
		return ""

class Service(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ping=None, ssh=None, http=None, https=None, snmp=None):
		self.ping = ping
		self.ssh = ssh
		self.http = http
		self.https = https
		self.snmp = snmp

	def __str__(self):
		return ""

class Disable_management_service_eth_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ethernet_start=PosRangedInteger(1, 2048)
	ethernet_end=PosRangedInteger(1, 2048)
	def __init__(self, ethernet_start=None, ethernet_end=None):
		self.ethernet_start = ethernet_start
		self.ethernet_end = ethernet_end

	def __str__(self):
		return ""

class Disable_management_service_ve_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ve_start=PosRangedInteger(1, 4094)
	ve_end=PosRangedInteger(1, 4094)
	def __init__(self, ve_start=None, ve_end=None):
		self.ve_start = ve_start
		self.ve_end = ve_end

	def __str__(self):
		return ""

class DisablemanagementServiceClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDisablemanagementService(self):
		"""
		Retrieve the service identified by the specified identifier
		
		Returns:
			An instance of the Service class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified service does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('service')
		return deserialize_Service_json(payload)

