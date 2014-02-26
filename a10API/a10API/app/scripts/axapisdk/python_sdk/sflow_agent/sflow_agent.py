########################################################################################################################
# File name: sflow_agent.py
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
	'https://axapi.a10networks.com/axapi/v3/sflow/agent',
]

def deserialize_Agent__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip = data.get('ip')
	ipv6 = data.get('ipv6')
	result = Agent__address(ip=ip, ipv6=ipv6)
	return result

def deserialize_Agent_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Agent__address_json(data.get('address'))
	result = Agent(address=address)
	return result

class Agent__address(AxapiObject):
	__metaclass__ = StructMeta 
	ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6=SizedString(1, 255)
	def __init__(self, ip=None, ipv6=None):
		self.ip = ip
		self.ipv6 = ipv6

	def __str__(self):
		return ""

class Agent(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address=None):
		self.address = address

	def __str__(self):
		return ""

class SflowAgentClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSflowAgent(self):
		"""
		Retrieve the agent identified by the specified identifier
		
		Returns:
			An instance of the Agent class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified agent does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('agent')
		return deserialize_Agent_json(payload)

