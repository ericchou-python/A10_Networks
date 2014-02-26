########################################################################################################################
# File name: snmp_server_community.py
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
	'https://axapi.a10networks.com/axapi/v3/snmp-server/community',
]

def deserialize_Snmp_server_community_read_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	user = data.get('user')
	oid = data.get('oid')
	remote = data.get('remote')
	ipv4_mask = data.get('ipv4-mask')
	result = Snmp_server_community_read(user=user, oid=oid, remote=remote, ipv4_mask=ipv4_mask)
	return result

def deserialize_list_Snmp_server_community_read_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Snmp_server_community_read_json(item))
	return list(container)

def deserialize_Community_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	read = deserialize_list_Snmp_server_community_read_json(data.get('read'))
	result = Community(read=read)
	return result

class Community(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, read=None):
		self.read = read

	def __str__(self):
		return ""

class Snmp_server_community_read(AxapiObject):
	__metaclass__ = StructMeta 
	user=SizedString(1, 31)
	oid=PosRangedInteger(0, 1)
	remote = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv4_mask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, user, oid=None, remote=None, ipv4_mask=None):
		self.user = user
		self.oid = oid
		self.remote = remote
		self.ipv4_mask = ipv4_mask

	def __str__(self):
		return str(self.user)

class SnmpserverCommunityClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSnmpserverCommunity(self):
		"""
		Retrieve the community identified by the specified identifier
		
		Returns:
			An instance of the Community class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified community does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('community')
		return deserialize_Community_json(payload)

