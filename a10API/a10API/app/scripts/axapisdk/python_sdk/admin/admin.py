########################################################################################################################
# File name: admin.py
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
	'https://axapi.a10networks.com/axapi/v3/admin',
]

def deserialize_Admin__access_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	axapi = data.get('axapi')
	cli = data.get('cli')
	web = data.get('web')
	result = Admin__access(axapi=axapi, cli=cli, web=web)
	return result

def deserialize_Admin__password_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	password_in_module = data.get('password-in-module')
	encrypted_in_module = data.get('encrypted-in-module')
	result = Admin__password(password_in_module=password_in_module, encrypted_in_module=encrypted_in_module)
	return result

def deserialize_Admin__lockout_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	duration = data.get('duration')
	enable = data.get('enable')
	reset_time = data.get('reset-time')
	threshold = data.get('threshold')
	result = Admin__lockout(duration=duration, enable=enable, reset_time=reset_time, threshold=threshold)
	return result

def deserialize_Admin_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	user = data.get('user')
	password_key = data.get('password-key')
	passwd_string = data.get('passwd-string')
	encrypted = data.get('encrypted')
	disable = data.get('disable')
	enable = data.get('enable')
	privilege = data.get('privilege')
	privilege_shell = data.get('privilege-shell')
	ssh_pubkey = data.get('ssh-pubkey')
	trusted_host = data.get('trusted-host')
	unlock = data.get('unlock')
	read = data.get('read')
	write = data.get('write')
	shell = data.get('shell')
	partition_read = data.get('partition-read')
	partition_write = data.get('partition-write')
	partition_enable_disable = data.get('partition-enable-disable')
	delete = data.get('delete')
	py_kw_rsvd_import = data.get('import')
	list = data.get('list')
	trusted_host_ipv4 = data.get('trusted-host-ipv4')
	netmask = data.get('netmask')
	access = deserialize_Admin__access_json(data.get('access'))
	password = deserialize_Admin__password_json(data.get('password'))
	lockout = deserialize_Admin__lockout_json(data.get('lockout'))
	result = Admin(user=user, password_key=password_key, passwd_string=passwd_string, encrypted=encrypted, disable=disable, enable=enable, privilege=privilege, privilege_shell=privilege_shell, ssh_pubkey=ssh_pubkey, trusted_host=trusted_host, unlock=unlock, read=read, write=write, shell=shell, partition_read=partition_read, partition_write=partition_write, partition_enable_disable=partition_enable_disable, delete=delete, py_kw_rsvd_import=py_kw_rsvd_import, list=list, trusted_host_ipv4=trusted_host_ipv4, netmask=netmask, access=access, password=password, lockout=lockout)
	return result

def serialize_Admin__access_json(obj):
	output = OrderedDict()
	if obj.axapi is not None:
		output['axapi'] = obj.axapi
	if obj.cli is not None:
		output['cli'] = obj.cli
	if obj.web is not None:
		output['web'] = obj.web
	return output

def serialize_Admin__password_json(obj):
	output = OrderedDict()
	if obj.password_in_module is not None:
		output['password-in-module'] = obj.password_in_module
	if obj.encrypted_in_module is not None:
		output['encrypted-in-module'] = obj.encrypted_in_module
	return output

def serialize_Admin__lockout_json(obj):
	output = OrderedDict()
	if obj.duration is not None:
		output['duration'] = obj.duration
	if obj.enable is not None:
		output['enable'] = obj.enable
	if obj.reset_time is not None:
		output['reset-time'] = obj.reset_time
	if obj.threshold is not None:
		output['threshold'] = obj.threshold
	return output

def serialize_Admin_json(obj):
	output = OrderedDict()
	output['user'] = obj.user
	if obj.password_key is not None:
		output['password-key'] = obj.password_key
	if obj.passwd_string is not None:
		output['passwd-string'] = obj.passwd_string
	if obj.encrypted is not None:
		output['encrypted'] = obj.encrypted
	if obj.disable is not None:
		output['disable'] = obj.disable
	if obj.enable is not None:
		output['enable'] = obj.enable
	if obj.privilege is not None:
		output['privilege'] = obj.privilege
	if obj.privilege_shell is not None:
		output['privilege-shell'] = obj.privilege_shell
	if obj.ssh_pubkey is not None:
		output['ssh-pubkey'] = obj.ssh_pubkey
	if obj.trusted_host is not None:
		output['trusted-host'] = obj.trusted_host
	if obj.unlock is not None:
		output['unlock'] = obj.unlock
	if obj.read is not None:
		output['read'] = obj.read
	if obj.write is not None:
		output['write'] = obj.write
	if obj.shell is not None:
		output['shell'] = obj.shell
	if obj.partition_read is not None:
		output['partition-read'] = obj.partition_read
	if obj.partition_write is not None:
		output['partition-write'] = obj.partition_write
	if obj.partition_enable_disable is not None:
		output['partition-enable-disable'] = obj.partition_enable_disable
	if obj.delete is not None:
		output['delete'] = obj.delete
	if obj.py_kw_rsvd_import is not None:
		output['import'] = obj.py_kw_rsvd_import
	if obj.list is not None:
		output['list'] = obj.list
	if obj.trusted_host_ipv4 is not None:
		output['trusted-host-ipv4'] = obj.trusted_host_ipv4
	if obj.netmask is not None:
		output['netmask'] = obj.netmask
	if obj.access is not None:
		output['access'] = serialize_Admin__access_json(obj.access)
	if obj.password is not None:
		output['password'] = serialize_Admin__password_json(obj.password)
	if obj.lockout is not None:
		output['lockout'] = serialize_Admin__lockout_json(obj.lockout)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Admin_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Admin_json(item))
	return list(container)

class Admin_user(AxapiObject):
	__metaclass__ = StructMeta 
	user=SizedString(1, 31)
	def __init__(self, user):
		self.user = user

	def __str__(self):
		return str(self.user)

class Admin__access(AxapiObject):
	__metaclass__ = StructMeta 
	axapi=PosRangedInteger(0, 1)
	cli=PosRangedInteger(0, 1)
	web=PosRangedInteger(0, 1)
	def __init__(self, axapi=None, cli=None, web=None):
		self.axapi = axapi
		self.cli = cli
		self.web = web

	def __str__(self):
		return ""

class Admin__password(AxapiObject):
	__metaclass__ = StructMeta 
	password_in_module=SizedString(1, 63)
	encrypted_in_module=SizedString(1, 255)
	def __init__(self, password_in_module=None, encrypted_in_module=None):
		self.password_in_module = password_in_module
		self.encrypted_in_module = encrypted_in_module

	def __str__(self):
		return ""

class Admin__lockout(AxapiObject):
	__metaclass__ = StructMeta 
	duration=PosRangedInteger(0, 1440)
	enable=PosRangedInteger(0, 1)
	reset_time=PosRangedInteger(1, 1440)
	threshold=PosRangedInteger(1, 10)
	def __init__(self, duration=None, enable=None, reset_time=None, threshold=None):
		self.duration = duration
		self.enable = enable
		self.reset_time = reset_time
		self.threshold = threshold

	def __str__(self):
		return ""

class Admin(AxapiObject):
	__metaclass__ = StructMeta 
	user=SizedString(1, 31)
	password_key=PosRangedInteger(0, 1)
	passwd_string=SizedString(1, 63)
	encrypted=SizedString(1, 255)
	disable=PosRangedInteger(0, 1)
	enable=PosRangedInteger(0, 1)
	privilege=PosRangedInteger(0, 1)
	privilege_shell=PosRangedInteger(0, 1)
	ssh_pubkey=PosRangedInteger(0, 1)
	trusted_host=PosRangedInteger(0, 1)
	unlock=PosRangedInteger(0, 1)
	read=PosRangedInteger(0, 1)
	write=PosRangedInteger(0, 1)
	shell=PosRangedInteger(0, 1)
	partition_read=PosRangedInteger(0, 1)
	partition_write=PosRangedInteger(0, 1)
	partition_enable_disable=PosRangedInteger(0, 1)
	delete=PosRangedInteger(1, 1000000)
	py_kw_rsvd_import=PosRangedInteger(0, 1)
	list=PosRangedInteger(0, 1)
	trusted_host_ipv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	netmask = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	def __init__(self, user, password_key=None, passwd_string=None, encrypted=None, disable=None, enable=None, privilege=None, privilege_shell=None, ssh_pubkey=None, trusted_host=None, unlock=None, read=None, write=None, shell=None, partition_read=None, partition_write=None, partition_enable_disable=None, delete=None, py_kw_rsvd_import=None, list=None, trusted_host_ipv4=None, netmask=None, access=None, password=None, lockout=None):
		self.user = user
		self.password_key = password_key
		self.passwd_string = passwd_string
		self.encrypted = encrypted
		self.disable = disable
		self.enable = enable
		self.privilege = privilege
		self.privilege_shell = privilege_shell
		self.ssh_pubkey = ssh_pubkey
		self.trusted_host = trusted_host
		self.unlock = unlock
		self.read = read
		self.write = write
		self.shell = shell
		self.partition_read = partition_read
		self.partition_write = partition_write
		self.partition_enable_disable = partition_enable_disable
		self.delete = delete
		self.py_kw_rsvd_import = py_kw_rsvd_import
		self.list = list
		self.trusted_host_ipv4 = trusted_host_ipv4
		self.netmask = netmask
		self.access = access
		self.password = password
		self.lockout = lockout

	def __str__(self):
		return str(self.user)

class AdminClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getAdmin(self, admin_user):
		"""
		Retrieve the admin identified by the specified identifier
		
		Args:
			admin_user Admin_user
		
		Returns:
			An instance of the Admin class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(admin_user) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified admin does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('admin')
		return deserialize_Admin_json(payload)

	def putAdmin(self, admin_user, admin):
		"""
		Replace the object admin
		
		Args:
			admin_user Admin_user
			admin An instance of the Admin class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['admin']=serialize_Admin_json(admin)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(admin_user) .replace("/", "%2f") + query, payload, headers)
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

	def deleteAdmin(self, admin_user):
		"""
		Remove the admin identified by the specified identifier from the system
		
		Args:
			admin_user Admin_user
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(admin_user) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified admin does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllAdminsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitAdmin(self, admin):
		"""
		Create the object admin
		
		Args:
			admin An instance of the Admin class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['admin']=serialize_Admin_json(admin)
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

	def getAllAdmins(self):
		"""
		Retrieve all admin objects currently pending in the system
		
		Returns:
			A list of Admin objects
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
			payload= data.get('adminList')
		return deserialize_list_Admin_json(payload)

