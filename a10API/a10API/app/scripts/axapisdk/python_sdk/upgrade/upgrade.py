########################################################################################################################
# File name: upgrade.py
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
	'https://axapi.a10networks.com/axapi/v3/upgrade',
]

def deserialize_Upgrade__hd_cf_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	hd = data.get('hd')
	pri = data.get('pri')
	sec = data.get('sec')
	cf = data.get('cf')
	cf_pri = data.get('cf-pri')
	local = data.get('local')
	use_mgmt_port = data.get('use-mgmt-port')
	file_url = data.get('file-url')
	staggered_upgrade_mode = data.get('staggered-upgrade-mode')
	device = data.get('device')
	result = Upgrade__hd_cf_cfg(hd=hd, pri=pri, sec=sec, cf=cf, cf_pri=cf_pri, local=local, use_mgmt_port=use_mgmt_port, file_url=file_url, staggered_upgrade_mode=staggered_upgrade_mode, device=device)
	return result

def deserialize_Upgrade_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	hd_cf_cfg = deserialize_Upgrade__hd_cf_cfg_json(data.get('hd-cf-cfg'))
	result = Upgrade(hd_cf_cfg=hd_cf_cfg)
	return result

def serialize_Upgrade__hd_cf_cfg_json(obj):
	output = OrderedDict()
	if obj.hd is not None:
		output['hd'] = obj.hd
	if obj.pri is not None:
		output['pri'] = obj.pri
	if obj.sec is not None:
		output['sec'] = obj.sec
	if obj.cf is not None:
		output['cf'] = obj.cf
	if obj.cf_pri is not None:
		output['cf-pri'] = obj.cf_pri
	if obj.local is not None:
		output['local'] = obj.local
	if obj.use_mgmt_port is not None:
		output['use-mgmt-port'] = obj.use_mgmt_port
	if obj.file_url is not None:
		output['file-url'] = obj.file_url
	if obj.staggered_upgrade_mode is not None:
		output['staggered-upgrade-mode'] = obj.staggered_upgrade_mode
	if obj.device is not None:
		output['device'] = obj.device
	return output

def serialize_Upgrade_json(obj):
	output = OrderedDict()
	if obj.hd_cf_cfg is not None:
		output['hd-cf-cfg'] = serialize_Upgrade__hd_cf_cfg_json(obj.hd_cf_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Upgrade_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Upgrade_json(item))
	return list(container)

class Upgrade__hd_cf_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	hd=PosRangedInteger(0, 1)
	pri=PosRangedInteger(0, 1)
	sec=PosRangedInteger(0, 1)
	cf=PosRangedInteger(0, 1)
	cf_pri=PosRangedInteger(0, 1)
	local=SizedString(1, 255)
	use_mgmt_port=PosRangedInteger(0, 1)
	file_url=SizedString(1, 255)
	staggered_upgrade_mode=PosRangedInteger(0, 1)
	device=PosRangedInteger(1, 8)
	def __init__(self, hd=None, pri=None, sec=None, cf=None, cf_pri=None, local=None, use_mgmt_port=None, file_url=None, staggered_upgrade_mode=None, device=None):
		self.hd = hd
		self.pri = pri
		self.sec = sec
		self.cf = cf
		self.cf_pri = cf_pri
		self.local = local
		self.use_mgmt_port = use_mgmt_port
		self.file_url = file_url
		self.staggered_upgrade_mode = staggered_upgrade_mode
		self.device = device

	def __str__(self):
		return ""

class Upgrade(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, hd_cf_cfg=None):
		self.hd_cf_cfg = hd_cf_cfg

	def __str__(self):
		return ""

class UpgradeClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getUpgrade(self):
		"""
		Retrieve the upgrade identified by the specified identifier
		
		Returns:
			An instance of the Upgrade class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified upgrade does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('upgrade')
		return deserialize_Upgrade_json(payload)

	def putUpgrade(self, upgrade):
		"""
		Replace the object upgrade
		
		Args:
			upgrade An instance of the Upgrade class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['upgrade']=serialize_Upgrade_json(upgrade)
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

	def deleteUpgrade(self):
		"""
		Remove the upgrade identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified upgrade does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllUpgradesClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitUpgrade(self, upgrade):
		"""
		Create the object upgrade
		
		Args:
			upgrade An instance of the Upgrade class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['upgrade']=serialize_Upgrade_json(upgrade)
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

	def getAllUpgrades(self):
		"""
		Retrieve all upgrade objects currently pending in the system
		
		Returns:
			A list of Upgrade objects
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
			payload= data.get('upgradeList')
		return deserialize_list_Upgrade_json(payload)

