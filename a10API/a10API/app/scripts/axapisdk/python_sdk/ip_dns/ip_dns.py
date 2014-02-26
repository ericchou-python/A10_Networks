########################################################################################################################
# File name: ip_dns.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/dns',
]

def deserialize_Dns__primary_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_v4_addr = data.get('ip-v4-addr')
	ip_v6_addr = data.get('ip-v6-addr')
	result = Dns__primary(ip_v4_addr=ip_v4_addr, ip_v6_addr=ip_v6_addr)
	return result

def deserialize_Dns__secondary_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip_v4_addr = data.get('ip-v4-addr')
	ip_v6_addr = data.get('ip-v6-addr')
	result = Dns__secondary(ip_v4_addr=ip_v4_addr, ip_v6_addr=ip_v6_addr)
	return result

def deserialize_Dns__suffix_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	domain_name = data.get('domain-name')
	result = Dns__suffix(domain_name=domain_name)
	return result

def deserialize_Dns_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	primary = deserialize_Dns__primary_json(data.get('primary'))
	secondary = deserialize_Dns__secondary_json(data.get('secondary'))
	suffix = deserialize_Dns__suffix_json(data.get('suffix'))
	result = Dns(primary=primary, secondary=secondary, suffix=suffix)
	return result

class Dns__primary(AxapiObject):
	__metaclass__ = StructMeta 
	ip_v4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_v6_addr=SizedString(1, 255)
	def __init__(self, ip_v4_addr=None, ip_v6_addr=None):
		self.ip_v4_addr = ip_v4_addr
		self.ip_v6_addr = ip_v6_addr

	def __str__(self):
		return ""

class Dns__secondary(AxapiObject):
	__metaclass__ = StructMeta 
	ip_v4_addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_v6_addr=SizedString(1, 255)
	def __init__(self, ip_v4_addr=None, ip_v6_addr=None):
		self.ip_v4_addr = ip_v4_addr
		self.ip_v6_addr = ip_v6_addr

	def __str__(self):
		return ""

class Dns__suffix(AxapiObject):
	__metaclass__ = StructMeta 
	domain_name=SizedString(1, 32)
	def __init__(self, domain_name=None):
		self.domain_name = domain_name

	def __str__(self):
		return ""

class Dns(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, primary=None, secondary=None, suffix=None):
		self.primary = primary
		self.secondary = secondary
		self.suffix = suffix

	def __str__(self):
		return ""

class IpDnsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpDns(self):
		"""
		Retrieve the dns identified by the specified identifier
		
		Returns:
			An instance of the Dns class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified dns does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('dns')
		return deserialize_Dns_json(payload)

