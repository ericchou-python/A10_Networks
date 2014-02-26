########################################################################################################################
# File name: logging.py
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
	'https://axapi.a10networks.com/axapi/v3/logging',
]

def deserialize_Logging__auditlog_cfg__audit_host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	host6 = data.get('host6')
	host4 = data.get('host4')
	audit_facility = data.get('audit-facility')
	result = Logging__auditlog_cfg__audit_host(host6=host6, host4=host4, audit_facility=audit_facility)
	return result

def deserialize_Logging__auditlog_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	auditlog = data.get('auditlog')
	audit_host = deserialize_Logging__auditlog_cfg__audit_host_json(data.get('audit-host'))
	result = Logging__auditlog_cfg(auditlog=auditlog, audit_host=audit_host)
	return result

def deserialize_Logging__email_address_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	email_add1 = data.get('email-add1')
	email_address2 = data.get('email-address2')
	result = Logging__email_address_cfg(email_add1=email_add1, email_address2=email_address2)
	return result

def deserialize_Logging__export_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	export = data.get('export')
	all = data.get('all')
	use_mgmt_port = data.get('use-mgmt-port')
	tftp = data.get('tftp')
	ftp = data.get('ftp')
	scp = data.get('scp')
	rcp = data.get('rcp')
	sftp = data.get('sftp')
	result = Logging__export_cfg(export=export, all=all, use_mgmt_port=use_mgmt_port, tftp=tftp, ftp=ftp, scp=scp, rcp=rcp, sftp=sftp)
	return result

def deserialize_Logging__monitor_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	monitor = data.get('monitor')
	monitor_log_severity = data.get('monitor-log-severity')
	monitor_levelname = data.get('monitor-levelname')
	result = Logging__monitor_cfg(monitor=monitor, monitor_log_severity=monitor_log_severity, monitor_levelname=monitor_levelname)
	return result

def deserialize_Logging__syslog_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	syslog = data.get('syslog')
	syslog_log_severity = data.get('syslog-log-severity')
	syslog_levelname = data.get('syslog-levelname')
	result = Logging__syslog_cfg(syslog=syslog, syslog_log_severity=syslog_log_severity, syslog_levelname=syslog_levelname)
	return result

def deserialize_Logging__trap_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	trap = data.get('trap')
	trap_log_severity = data.get('trap-log-severity')
	trap_levelname = data.get('trap-levelname')
	result = Logging__trap_cfg(trap=trap, trap_log_severity=trap_log_severity, trap_levelname=trap_levelname)
	return result

def deserialize_Logging__console_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	console_levelnum = data.get('console-levelnum')
	console_levelname = data.get('console-levelname')
	result = Logging__console(console_levelnum=console_levelnum, console_levelname=console_levelname)
	return result

def deserialize_Logging__email__levelnum_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	levelnum = data.get('levelnum')
	email_levelname = data.get('email-levelname')
	result = Logging__email__levelnum_cfg(levelnum=levelnum, email_levelname=email_levelname)
	return result

def deserialize_Logging__email__buffer_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	number = data.get('number')
	time = data.get('time')
	result = Logging__email__buffer(number=number, time=time)
	return result

def deserialize_Logging__email__filter_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	filter_id = data.get('filter-id')
	expression = data.get('expression')
	trigger = data.get('trigger')
	result = Logging__email__filter(filter_id=filter_id, expression=expression, trigger=trigger)
	return result

def deserialize_Logging__email_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	levelnum_cfg = deserialize_Logging__email__levelnum_cfg_json(data.get('levelnum-cfg'))
	buffer = deserialize_Logging__email__buffer_json(data.get('buffer'))
	filter = deserialize_Logging__email__filter_json(data.get('filter'))
	result = Logging__email(levelnum_cfg=levelnum_cfg, buffer=buffer, filter=filter)
	return result

def deserialize_Logging_host__host_ipv4_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	host_ipv4 = data.get('host-ipv4')
	host_ipv6 = data.get('host-ipv6')
	port = data.get('port')
	tcp = data.get('tcp')
	udp = data.get('udp')
	use_mgmt_port = data.get('use-mgmt-port')
	use_data_port = data.get('use-data-port')
	result = Logging_host__host_ipv4(host_ipv4=host_ipv4, host_ipv6=host_ipv6, port=port, tcp=tcp, udp=udp, use_mgmt_port=use_mgmt_port, use_data_port=use_data_port)
	return result

def deserialize_Logging_host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	host_ipv4 = deserialize_Logging_host__host_ipv4_json(data.get('host-ipv4'))
	result = Logging_host(host_ipv4=host_ipv4)
	return result

def deserialize_list_Logging_host_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Logging_host_json(item))
	return list(container)

def deserialize_Logging_single_priority_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	log_severity = data.get('log-severity')
	levelname = data.get('levelname')
	result = Logging_single_priority(log_severity=log_severity, levelname=levelname)
	return result

def deserialize_list_Logging_single_priority_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Logging_single_priority_json(item))
	return list(container)

def deserialize_Logging__buffered_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	buffersize = data.get('buffersize')
	levelnum = data.get('levelnum')
	levelname = data.get('levelname')
	result = Logging__buffered(buffersize=buffersize, levelnum=levelnum, levelname=levelname)
	return result

def deserialize_Logging_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	auditlog_cfg = deserialize_Logging__auditlog_cfg_json(data.get('auditlog-cfg'))
	email_address_cfg = deserialize_Logging__email_address_cfg_json(data.get('email-address-cfg'))
	export_cfg = deserialize_Logging__export_cfg_json(data.get('export-cfg'))
	facility = data.get('facility')
	monitor_cfg = deserialize_Logging__monitor_cfg_json(data.get('monitor-cfg'))
	syslog_cfg = deserialize_Logging__syslog_cfg_json(data.get('syslog-cfg'))
	trap_cfg = deserialize_Logging__trap_cfg_json(data.get('trap-cfg'))
	console = deserialize_Logging__console_json(data.get('console'))
	email = deserialize_Logging__email_json(data.get('email'))
	hostlist = deserialize_list_Logging_host_json(data.get('hostList'))
	single_prioritylist = deserialize_list_Logging_single_priority_json(data.get('single-priorityList'))
	buffered = deserialize_Logging__buffered_json(data.get('buffered'))
	result = Logging(auditlog_cfg=auditlog_cfg, email_address_cfg=email_address_cfg, export_cfg=export_cfg, facility=facility, monitor_cfg=monitor_cfg, syslog_cfg=syslog_cfg, trap_cfg=trap_cfg, console=console, email=email, hostlist=hostlist, single_prioritylist=single_prioritylist, buffered=buffered)
	return result

def serialize_Logging__auditlog_cfg__audit_host_json(obj):
	output = OrderedDict()
	if obj.host6 is not None:
		output['host6'] = obj.host6
	if obj.host4 is not None:
		output['host4'] = obj.host4
	if obj.audit_facility is not None:
		output['audit-facility'] = obj.audit_facility
	return output

def serialize_Logging__auditlog_cfg_json(obj):
	output = OrderedDict()
	if obj.auditlog is not None:
		output['auditlog'] = obj.auditlog
	if obj.audit_host is not None:
		output['audit-host'] = serialize_Logging__auditlog_cfg__audit_host_json(obj.audit_host)
	return output

def serialize_Logging__email_address_cfg_json(obj):
	output = OrderedDict()
	if obj.email_add1 is not None:
		output['email-add1'] = obj.email_add1
	if obj.email_address2 is not None:
		output['email-address2'] = obj.email_address2
	return output

def serialize_Logging__export_cfg_json(obj):
	output = OrderedDict()
	if obj.export is not None:
		output['export'] = obj.export
	if obj.all is not None:
		output['all'] = obj.all
	if obj.use_mgmt_port is not None:
		output['use-mgmt-port'] = obj.use_mgmt_port
	if obj.tftp is not None:
		output['tftp'] = obj.tftp
	if obj.ftp is not None:
		output['ftp'] = obj.ftp
	if obj.scp is not None:
		output['scp'] = obj.scp
	if obj.rcp is not None:
		output['rcp'] = obj.rcp
	if obj.sftp is not None:
		output['sftp'] = obj.sftp
	return output

def serialize_Logging__monitor_cfg_json(obj):
	output = OrderedDict()
	if obj.monitor is not None:
		output['monitor'] = obj.monitor
	if obj.monitor_log_severity is not None:
		output['monitor-log-severity'] = obj.monitor_log_severity
	if obj.monitor_levelname is not None:
		output['monitor-levelname'] = obj.monitor_levelname
	return output

def serialize_Logging__syslog_cfg_json(obj):
	output = OrderedDict()
	if obj.syslog is not None:
		output['syslog'] = obj.syslog
	if obj.syslog_log_severity is not None:
		output['syslog-log-severity'] = obj.syslog_log_severity
	if obj.syslog_levelname is not None:
		output['syslog-levelname'] = obj.syslog_levelname
	return output

def serialize_Logging__trap_cfg_json(obj):
	output = OrderedDict()
	if obj.trap is not None:
		output['trap'] = obj.trap
	if obj.trap_log_severity is not None:
		output['trap-log-severity'] = obj.trap_log_severity
	if obj.trap_levelname is not None:
		output['trap-levelname'] = obj.trap_levelname
	return output

def serialize_Logging__console_json(obj):
	output = OrderedDict()
	if obj.console_levelnum is not None:
		output['console-levelnum'] = obj.console_levelnum
	if obj.console_levelname is not None:
		output['console-levelname'] = obj.console_levelname
	return output

def serialize_Logging__email__levelnum_cfg_json(obj):
	output = OrderedDict()
	if obj.levelnum is not None:
		output['levelnum'] = obj.levelnum
	if obj.email_levelname is not None:
		output['email-levelname'] = obj.email_levelname
	return output

def serialize_Logging__email__buffer_json(obj):
	output = OrderedDict()
	if obj.number is not None:
		output['number'] = obj.number
	if obj.time is not None:
		output['time'] = obj.time
	return output

def serialize_Logging__email__filter_json(obj):
	output = OrderedDict()
	if obj.filter_id is not None:
		output['filter-id'] = obj.filter_id
	if obj.expression is not None:
		output['expression'] = obj.expression
	if obj.trigger is not None:
		output['trigger'] = obj.trigger
	return output

def serialize_Logging__email_json(obj):
	output = OrderedDict()
	if obj.levelnum_cfg is not None:
		output['levelnum-cfg'] = serialize_Logging__email__levelnum_cfg_json(obj.levelnum_cfg)
	if obj.buffer is not None:
		output['buffer'] = serialize_Logging__email__buffer_json(obj.buffer)
	if obj.filter is not None:
		output['filter'] = serialize_Logging__email__filter_json(obj.filter)
	return output

def serialize_Logging_host__host_ipv4_json(obj):
	output = OrderedDict()
	output['host-ipv4'] = obj.host_ipv4
	output['host-ipv6'] = obj.host_ipv6
	output['port'] = obj.port
	output['tcp'] = obj.tcp
	output['udp'] = obj.udp
	output['use-mgmt-port'] = obj.use_mgmt_port
	output['use-data-port'] = obj.use_data_port
	return output

def serialize_Logging_host_json(obj):
	output = OrderedDict()
	output['host-ipv4'] = serialize_Logging_host__host_ipv4_json(obj.host_ipv4)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Logging_host_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Logging_host_json(item))
	return output

def serialize_Logging_single_priority_json(obj):
	output = OrderedDict()
	output['log-severity'] = obj.log_severity
	output['levelname'] = obj.levelname
	return output

def serialize_list_Logging_single_priority_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Logging_single_priority_json(item))
	return output

def serialize_Logging__buffered_json(obj):
	output = OrderedDict()
	if obj.buffersize is not None:
		output['buffersize'] = obj.buffersize
	if obj.levelnum is not None:
		output['levelnum'] = obj.levelnum
	if obj.levelname is not None:
		output['levelname'] = obj.levelname
	return output

def serialize_Logging_json(obj):
	output = OrderedDict()
	if obj.auditlog_cfg is not None:
		output['auditlog-cfg'] = serialize_Logging__auditlog_cfg_json(obj.auditlog_cfg)
	if obj.email_address_cfg is not None:
		output['email-address-cfg'] = serialize_Logging__email_address_cfg_json(obj.email_address_cfg)
	if obj.export_cfg is not None:
		output['export-cfg'] = serialize_Logging__export_cfg_json(obj.export_cfg)
	if obj.facility is not None:
		output['facility'] = obj.facility
	if obj.monitor_cfg is not None:
		output['monitor-cfg'] = serialize_Logging__monitor_cfg_json(obj.monitor_cfg)
	if obj.syslog_cfg is not None:
		output['syslog-cfg'] = serialize_Logging__syslog_cfg_json(obj.syslog_cfg)
	if obj.trap_cfg is not None:
		output['trap-cfg'] = serialize_Logging__trap_cfg_json(obj.trap_cfg)
	if obj.console is not None:
		output['console'] = serialize_Logging__console_json(obj.console)
	if obj.email is not None:
		output['email'] = serialize_Logging__email_json(obj.email)
	if obj.hostlist is not None:
		output['hostList'] = serialize_list_Logging_host_json(obj.hostlist)
	if obj.single_prioritylist is not None:
		output['single-priorityList'] = serialize_list_Logging_single_priority_json(obj.single_prioritylist)
	if obj.buffered is not None:
		output['buffered'] = serialize_Logging__buffered_json(obj.buffered)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Logging_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Logging_json(item))
	return list(container)

class Logging__auditlog_cfg__audit_host(AxapiObject):
	__metaclass__ = StructMeta 
	host6=SizedString(1, 255)
	host4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	audit_facility = Enum(['local0', 'local1', 'local2', 'local3', 'local4', 'local5', 'local6', 'local7'])
	def __init__(self, host6=None, host4=None, audit_facility=None):
		self.host6 = host6
		self.host4 = host4
		self.audit_facility = audit_facility

	def __str__(self):
		return ""

class Logging__auditlog_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	auditlog=PosRangedInteger(0, 1)
	def __init__(self, auditlog=None, audit_host=None):
		self.auditlog = auditlog
		self.audit_host = audit_host

	def __str__(self):
		return ""

class Logging__email_address_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	email_add1=SizedString(1, 63)
	email_address2=SizedString(1, 63)
	def __init__(self, email_add1=None, email_address2=None):
		self.email_add1 = email_add1
		self.email_address2 = email_address2

	def __str__(self):
		return ""

class Logging__export_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	export=PosRangedInteger(0, 1)
	all=PosRangedInteger(0, 1)
	use_mgmt_port=PosRangedInteger(0, 1)
	tftp=SizedString(1, 255)
	ftp=SizedString(1, 255)
	scp=SizedString(1, 255)
	rcp=SizedString(1, 255)
	sftp=SizedString(1, 255)
	def __init__(self, export=None, all=None, use_mgmt_port=None, tftp=None, ftp=None, scp=None, rcp=None, sftp=None):
		self.export = export
		self.all = all
		self.use_mgmt_port = use_mgmt_port
		self.tftp = tftp
		self.ftp = ftp
		self.scp = scp
		self.rcp = rcp
		self.sftp = sftp

	def __str__(self):
		return ""

class Logging__monitor_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	monitor=PosRangedInteger(0, 1)
	monitor_log_severity=PosRangedInteger(0, 7)
	monitor_levelname = Enum(['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debugging'])
	def __init__(self, monitor=None, monitor_log_severity=None, monitor_levelname=None):
		self.monitor = monitor
		self.monitor_log_severity = monitor_log_severity
		self.monitor_levelname = monitor_levelname

	def __str__(self):
		return ""

class Logging__syslog_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	syslog=PosRangedInteger(0, 1)
	syslog_log_severity=PosRangedInteger(0, 7)
	syslog_levelname = Enum(['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debugging'])
	def __init__(self, syslog=None, syslog_log_severity=None, syslog_levelname=None):
		self.syslog = syslog
		self.syslog_log_severity = syslog_log_severity
		self.syslog_levelname = syslog_levelname

	def __str__(self):
		return ""

class Logging__trap_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	trap=PosRangedInteger(0, 1)
	trap_log_severity=PosRangedInteger(0, 2)
	trap_levelname = Enum(['emergency', 'alert', 'critical'])
	def __init__(self, trap=None, trap_log_severity=None, trap_levelname=None):
		self.trap = trap
		self.trap_log_severity = trap_log_severity
		self.trap_levelname = trap_levelname

	def __str__(self):
		return ""

class Logging__console(AxapiObject):
	__metaclass__ = StructMeta 
	console_levelnum=PosRangedInteger(0, 7)
	console_levelname = Enum(['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debugging'])
	def __init__(self, console_levelnum=None, console_levelname=None):
		self.console_levelnum = console_levelnum
		self.console_levelname = console_levelname

	def __str__(self):
		return ""

class Logging__email__levelnum_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	levelnum = Enum([])
	email_levelname = Enum(['emergency', 'alert', 'critical', 'notification'])
	def __init__(self, levelnum=None, email_levelname=None):
		self.levelnum = levelnum
		self.email_levelname = email_levelname

	def __str__(self):
		return ""

class Logging__email__buffer(AxapiObject):
	__metaclass__ = StructMeta 
	number=PosRangedInteger(16, 256)
	time=PosRangedInteger(10, 1440)
	def __init__(self, number=None, time=None):
		self.number = number
		self.time = time

	def __str__(self):
		return ""

class Logging__email__filter(AxapiObject):
	__metaclass__ = StructMeta 
	filter_id=PosRangedInteger(1, 8)
	expression=SizedString(1, 511)
	trigger=PosRangedInteger(0, 1)
	def __init__(self, filter_id=None, expression=None, trigger=None):
		self.filter_id = filter_id
		self.expression = expression
		self.trigger = trigger

	def __str__(self):
		return ""

class Logging__email(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, levelnum_cfg=None, buffer=None, filter=None):
		self.levelnum_cfg = levelnum_cfg
		self.buffer = buffer
		self.filter = filter

	def __str__(self):
		return ""

class Logging__buffered(AxapiObject):
	__metaclass__ = StructMeta 
	buffersize=PosRangedInteger(10000, 50000)
	levelnum=PosRangedInteger(0, 7)
	levelname = Enum(['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debugging'])
	def __init__(self, buffersize=None, levelnum=None, levelname=None):
		self.buffersize = buffersize
		self.levelnum = levelnum
		self.levelname = levelname

	def __str__(self):
		return ""

class Logging(AxapiObject):
	__metaclass__ = StructMeta 
	facility = Enum(['local0', 'local1', 'local2', 'local3', 'local4', 'local5', 'local6', 'local7'])
	def __init__(self, auditlog_cfg=None, email_address_cfg=None, export_cfg=None, facility=None, monitor_cfg=None, syslog_cfg=None, trap_cfg=None, console=None, email=None, hostlist=None, single_prioritylist=None, buffered=None):
		self.auditlog_cfg = auditlog_cfg
		self.email_address_cfg = email_address_cfg
		self.export_cfg = export_cfg
		self.facility = facility
		self.monitor_cfg = monitor_cfg
		self.syslog_cfg = syslog_cfg
		self.trap_cfg = trap_cfg
		self.console = console
		self.email = email
		self.hostlist = hostlist
		self.single_prioritylist = single_prioritylist
		self.buffered = buffered

	def __str__(self):
		return ""

class Logging_host__host_ipv4(AxapiObject):
	__metaclass__ = StructMeta 
	host_ipv4 = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	host_ipv6=SizedString(1, 255)
	port=PosRangedInteger(1, 32767)
	tcp=PosRangedInteger(0, 1)
	udp=PosRangedInteger(0, 1)
	use_mgmt_port=PosRangedInteger(0, 1)
	use_data_port=PosRangedInteger(0, 1)
	def __init__(self, host_ipv4, host_ipv6, port, tcp, udp, use_mgmt_port, use_data_port):
		self.host_ipv4 = host_ipv4
		self.host_ipv6 = host_ipv6
		self.port = port
		self.tcp = tcp
		self.udp = udp
		self.use_mgmt_port = use_mgmt_port
		self.use_data_port = use_data_port

	def __str__(self):
		return str(self.host_ipv4) + '+' + str(self.host_ipv6) + '+' + str(self.port) + '+' + str(self.tcp) + '+' + str(self.udp) + '+' + str(self.use_mgmt_port) + '+' + str(self.use_data_port)

class Logging_host(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, host_ipv4):
		self.host_ipv4 = host_ipv4

	def __str__(self):
		return str(self.host_ipv4)

class Logging_single_priority(AxapiObject):
	__metaclass__ = StructMeta 
	log_severity=PosRangedInteger(0, 7)
	levelname = Enum(['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debugging'])
	def __init__(self, log_severity, levelname):
		self.log_severity = log_severity
		self.levelname = levelname

	def __str__(self):
		return str(self.log_severity) + '+' + str(self.levelname)

class LoggingClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getLogging(self):
		"""
		Retrieve the logging identified by the specified identifier
		
		Returns:
			An instance of the Logging class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified logging does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('logging')
		return deserialize_Logging_json(payload)

	def putLogging(self, logging):
		"""
		Replace the object logging
		
		Args:
			logging An instance of the Logging class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['logging']=serialize_Logging_json(logging)
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

	def deleteLogging(self):
		"""
		Remove the logging identified by the specified identifier from the system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified logging does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllLoggingsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitLogging(self, logging):
		"""
		Create the object logging
		
		Args:
			logging An instance of the Logging class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['logging']=serialize_Logging_json(logging)
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

	def getAllLoggings(self):
		"""
		Retrieve all logging objects currently pending in the system
		
		Returns:
			A list of Logging objects
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
			payload= data.get('loggingList')
		return deserialize_list_Logging_json(payload)

