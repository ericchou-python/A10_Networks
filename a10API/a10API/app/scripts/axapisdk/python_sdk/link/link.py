########################################################################################################################
# File name: link.py
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
	'https://axapi.a10networks.com/axapi/v3/link',
]

def deserialize_Link__startup_config__default_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default = data.get('default')
	file_name = data.get('file-name')
	primary = data.get('primary')
	secondary = data.get('secondary')
	result = Link__startup_config__default_cfg(default=default, file_name=file_name, primary=primary, secondary=secondary)
	return result

def deserialize_Link__startup_config_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	default_cfg = deserialize_Link__startup_config__default_cfg_json(data.get('default-cfg'))
	result = Link__startup_config(default_cfg=default_cfg)
	return result

def deserialize_Link_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	startup_config = deserialize_Link__startup_config_json(data.get('startup-config'))
	result = Link(startup_config=startup_config)
	return result

class Link__startup_config__default_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	default=PosRangedInteger(0, 1)
	file_name=SizedString(1, 31)
	primary=PosRangedInteger(0, 1)
	secondary=PosRangedInteger(0, 1)
	def __init__(self, default=None, file_name=None, primary=None, secondary=None):
		self.default = default
		self.file_name = file_name
		self.primary = primary
		self.secondary = secondary

	def __str__(self):
		return ""

class Link__startup_config(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, default_cfg=None):
		self.default_cfg = default_cfg

	def __str__(self):
		return ""

class Link(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, startup_config=None):
		self.startup_config = startup_config

	def __str__(self):
		return ""

class LinkClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLink(self):
		"""
		Retrieve the link identified by the specified identifier
		
		Returns:
			An instance of the Link class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified link does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('link')
		return deserialize_Link_json(payload)

