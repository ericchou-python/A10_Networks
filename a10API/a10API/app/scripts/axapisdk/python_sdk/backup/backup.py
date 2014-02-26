########################################################################################################################
# File name: backup.py
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
	'https://axapi.a10networks.com/axapi/v3/backup',
]

def deserialize_Backup__system_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	use_mgmt_port = data.get('use-mgmt-port')
	remote_file = data.get('remote-file')
	file_name = data.get('file_name')
	result = Backup__system(use_mgmt_port=use_mgmt_port, remote_file=remote_file, file_name=file_name)
	return result

def deserialize_Backup__log__expedite_cfg__period_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	period = data.get('period')
	date = data.get('date')
	day = data.get('day')
	month = data.get('month')
	week = data.get('week')
	all = data.get('all')
	result = Backup__log__expedite_cfg__period_cfg(period=period, date=date, day=day, month=month, week=week, all=all)
	return result

def deserialize_Backup__log__expedite_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	expedite = data.get('expedite')
	period_cfg = deserialize_Backup__log__expedite_cfg__period_cfg_json(data.get('period-cfg'))
	stats_data = data.get('stats-data')
	use_mgmt_port = data.get('use-mgmt-port')
	result = Backup__log__expedite_cfg(expedite=expedite, period_cfg=period_cfg, stats_data=stats_data, use_mgmt_port=use_mgmt_port)
	return result

def deserialize_Backup__log_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	expedite_cfg = deserialize_Backup__log__expedite_cfg_json(data.get('expedite-cfg'))
	remote_file = data.get('remote-file')
	file_name = data.get('file_name')
	result = Backup__log(expedite_cfg=expedite_cfg, remote_file=remote_file, file_name=file_name)
	return result

def deserialize_Backup__store__creat_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	create = data.get('create')
	store_name = data.get('store-name')
	remote_file = data.get('remote-file')
	result = Backup__store__creat_cfg(create=create, store_name=store_name, remote_file=remote_file)
	return result

def deserialize_Backup__store__delete_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	delete = data.get('delete')
	store_name_del = data.get('store-name-del')
	result = Backup__store__delete_cfg(delete=delete, store_name_del=store_name_del)
	return result

def deserialize_Backup__store_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	creat_cfg = deserialize_Backup__store__creat_cfg_json(data.get('creat-cfg'))
	delete_cfg = deserialize_Backup__store__delete_cfg_json(data.get('delete-cfg'))
	result = Backup__store(creat_cfg=creat_cfg, delete_cfg=delete_cfg)
	return result

def deserialize_Backup__periodically__period_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	day_2 = data.get('day-2')
	hour_2 = data.get('hour-2')
	week_2 = data.get('week-2')
	result = Backup__periodically__period_cfg(day_2=day_2, hour_2=hour_2, week_2=week_2)
	return result

def deserialize_Backup__periodically_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	system = data.get('system')
	log = data.get('log')
	use_mgmt_port = data.get('use-mgmt-port')
	remote_file = data.get('remote-file')
	file_name = data.get('file_name')
	period_cfg = deserialize_Backup__periodically__period_cfg_json(data.get('period-cfg'))
	use_mgmt_port_2 = data.get('use-mgmt-port-2')
	remote_file_2 = data.get('remote-file-2')
	file_name_2 = data.get('file_name-2')
	result = Backup__periodically(system=system, log=log, use_mgmt_port=use_mgmt_port, remote_file=remote_file, file_name=file_name, period_cfg=period_cfg, use_mgmt_port_2=use_mgmt_port_2, remote_file_2=remote_file_2, file_name_2=file_name_2)
	return result

def deserialize_Backup_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	system = deserialize_Backup__system_json(data.get('system'))
	log = deserialize_Backup__log_json(data.get('log'))
	store = deserialize_Backup__store_json(data.get('store'))
	periodically = deserialize_Backup__periodically_json(data.get('periodically'))
	result = Backup(system=system, log=log, store=store, periodically=periodically)
	return result

class Backup__system(AxapiObject):
	__metaclass__ = StructMeta 
	use_mgmt_port=PosRangedInteger(0, 1)
	remote_file=SizedString(1, 255)
	file_name=SizedString(1, 255)
	def __init__(self, use_mgmt_port=None, remote_file=None, file_name=None):
		self.use_mgmt_port = use_mgmt_port
		self.remote_file = remote_file
		self.file_name = file_name

	def __str__(self):
		return ""

class Backup__log__expedite_cfg__period_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	period=PosRangedInteger(0, 1)
	date=PosRangedInteger(1, 31)
	day=PosRangedInteger(0, 1)
	month=PosRangedInteger(0, 1)
	week=PosRangedInteger(0, 1)
	all=PosRangedInteger(0, 1)
	def __init__(self, period=None, date=None, day=None, month=None, week=None, all=None):
		self.period = period
		self.date = date
		self.day = day
		self.month = month
		self.week = week
		self.all = all

	def __str__(self):
		return ""

class Backup__log__expedite_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	expedite=PosRangedInteger(0, 1)
	stats_data=PosRangedInteger(0, 1)
	use_mgmt_port=PosRangedInteger(0, 1)
	def __init__(self, expedite=None, period_cfg=None, stats_data=None, use_mgmt_port=None):
		self.expedite = expedite
		self.period_cfg = period_cfg
		self.stats_data = stats_data
		self.use_mgmt_port = use_mgmt_port

	def __str__(self):
		return ""

class Backup__log(AxapiObject):
	__metaclass__ = StructMeta 
	remote_file=SizedString(1, 255)
	file_name=SizedString(1, 255)
	def __init__(self, expedite_cfg=None, remote_file=None, file_name=None):
		self.expedite_cfg = expedite_cfg
		self.remote_file = remote_file
		self.file_name = file_name

	def __str__(self):
		return ""

class Backup__store__creat_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	create=PosRangedInteger(0, 1)
	store_name=SizedString(1, 31)
	remote_file=SizedString(1, 255)
	def __init__(self, create=None, store_name=None, remote_file=None):
		self.create = create
		self.store_name = store_name
		self.remote_file = remote_file

	def __str__(self):
		return ""

class Backup__store__delete_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	delete=PosRangedInteger(0, 1)
	store_name_del=SizedString(1, 31)
	def __init__(self, delete=None, store_name_del=None):
		self.delete = delete
		self.store_name_del = store_name_del

	def __str__(self):
		return ""

class Backup__store(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, creat_cfg=None, delete_cfg=None):
		self.creat_cfg = creat_cfg
		self.delete_cfg = delete_cfg

	def __str__(self):
		return ""

class Backup__periodically__period_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	day_2=PosRangedInteger(1, 199)
	hour_2=PosRangedInteger(1, 65534)
	week_2=PosRangedInteger(1, 199)
	def __init__(self, day_2=None, hour_2=None, week_2=None):
		self.day_2 = day_2
		self.hour_2 = hour_2
		self.week_2 = week_2

	def __str__(self):
		return ""

class Backup__periodically(AxapiObject):
	__metaclass__ = StructMeta 
	system=PosRangedInteger(0, 1)
	log=PosRangedInteger(0, 1)
	use_mgmt_port=PosRangedInteger(0, 1)
	remote_file=SizedString(1, 255)
	file_name=SizedString(1, 255)
	use_mgmt_port_2=PosRangedInteger(0, 1)
	remote_file_2=SizedString(1, 255)
	file_name_2=SizedString(1, 255)
	def __init__(self, system=None, log=None, use_mgmt_port=None, remote_file=None, file_name=None, period_cfg=None, use_mgmt_port_2=None, remote_file_2=None, file_name_2=None):
		self.system = system
		self.log = log
		self.use_mgmt_port = use_mgmt_port
		self.remote_file = remote_file
		self.file_name = file_name
		self.period_cfg = period_cfg
		self.use_mgmt_port_2 = use_mgmt_port_2
		self.remote_file_2 = remote_file_2
		self.file_name_2 = file_name_2

	def __str__(self):
		return ""

class Backup(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, system=None, log=None, store=None, periodically=None):
		self.system = system
		self.log = log
		self.store = store
		self.periodically = periodically

	def __str__(self):
		return ""

class BackupClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getBackup(self):
		"""
		Retrieve the backup identified by the specified identifier
		
		Returns:
			An instance of the Backup class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified backup does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('backup')
		return deserialize_Backup_json(payload)

