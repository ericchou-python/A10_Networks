########################################################################################################################
# File name: sflow.py
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
	'https://axapi.a10networks.com/axapi/v3/sflow',
]

def deserialize_Sflow__setting_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	max_header = data.get('max-header')
	source_ip_use_mgmt = data.get('source-ip-use-mgmt')
	packet_sampling_rate = data.get('packet-sampling-rate')
	counter_polling_interval = data.get('counter-polling-interval')
	result = Sflow__setting(max_header=max_header, source_ip_use_mgmt=source_ip_use_mgmt, packet_sampling_rate=packet_sampling_rate, counter_polling_interval=counter_polling_interval)
	return result

def deserialize_Sflow_collector_ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	addr = data.get('addr')
	port = data.get('port')
	result = Sflow_collector_ip(addr=addr, port=port)
	return result

def deserialize_list_Sflow_collector_ip_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_collector_ip_json(item))
	return list(container)

def deserialize_Sflow_collector_ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	addr = data.get('addr')
	port = data.get('port')
	result = Sflow_collector_ipv6(addr=addr, port=port)
	return result

def deserialize_list_Sflow_collector_ipv6_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_collector_ipv6_json(item))
	return list(container)

def deserialize_Sflow__collector_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	iplist = deserialize_list_Sflow_collector_ip_json(data.get('ipList'))
	ipv6list = deserialize_list_Sflow_collector_ipv6_json(data.get('ipv6List'))
	result = Sflow__collector(iplist=iplist, ipv6list=ipv6list)
	return result

def deserialize_Sflow__agent__address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip = data.get('ip')
	ipv6 = data.get('ipv6')
	result = Sflow__agent__address(ip=ip, ipv6=ipv6)
	return result

def deserialize_Sflow__agent_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	address = deserialize_Sflow__agent__address_json(data.get('address'))
	result = Sflow__agent(address=address)
	return result

def deserialize_Sflow__source_address_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ip = data.get('ip')
	ipv6 = data.get('ipv6')
	result = Sflow__source_address(ip=ip, ipv6=ipv6)
	return result

def deserialize_Sflow__polling__ddos_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	toggle = data.get('toggle')
	result = Sflow__polling__ddos(toggle=toggle)
	return result

def deserialize_Sflow__polling__http_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	toggle = data.get('toggle')
	result = Sflow__polling__http(toggle=toggle)
	return result

def deserialize_Sflow__polling__cpu_usage_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	toggle = data.get('toggle')
	result = Sflow__polling__cpu_usage(toggle=toggle)
	return result

def deserialize_Sflow_polling_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	start = data.get('start')
	interval = data.get('interval')
	result = Sflow_polling_ethernet(start=start, interval=interval)
	return result

def deserialize_list_Sflow_polling_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_polling_ethernet_json(item))
	return list(container)

def deserialize_Sflow_polling_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	start = data.get('start')
	interval = data.get('interval')
	result = Sflow_polling_ve(start=start, interval=interval)
	return result

def deserialize_list_Sflow_polling_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_polling_ve_json(item))
	return list(container)

def deserialize_Sflow__polling_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ddos = deserialize_Sflow__polling__ddos_json(data.get('ddos'))
	http = deserialize_Sflow__polling__http_json(data.get('http'))
	cpu_usage = deserialize_Sflow__polling__cpu_usage_json(data.get('cpu-usage'))
	ethernetlist = deserialize_list_Sflow_polling_ethernet_json(data.get('ethernetList'))
	velist = deserialize_list_Sflow_polling_ve_json(data.get('veList'))
	result = Sflow__polling(ddos=ddos, http=http, cpu_usage=cpu_usage, ethernetlist=ethernetlist, velist=velist)
	return result

def deserialize_Sflow_sampling_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	start = data.get('start')
	rate = data.get('rate')
	result = Sflow_sampling_ethernet(start=start, rate=rate)
	return result

def deserialize_list_Sflow_sampling_ethernet_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_sampling_ethernet_json(item))
	return list(container)

def deserialize_Sflow_sampling_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	start = data.get('start')
	rate = data.get('rate')
	result = Sflow_sampling_ve(start=start, rate=rate)
	return result

def deserialize_list_Sflow_sampling_ve_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Sflow_sampling_ve_json(item))
	return list(container)

def deserialize_Sflow__sampling_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ethernetlist = deserialize_list_Sflow_sampling_ethernet_json(data.get('ethernetList'))
	velist = deserialize_list_Sflow_sampling_ve_json(data.get('veList'))
	result = Sflow__sampling(ethernetlist=ethernetlist, velist=velist)
	return result

def deserialize_Sflow_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	setting = deserialize_Sflow__setting_json(data.get('setting'))
	collector = deserialize_Sflow__collector_json(data.get('collector'))
	agent = deserialize_Sflow__agent_json(data.get('agent'))
	source_address = deserialize_Sflow__source_address_json(data.get('source-address'))
	polling = deserialize_Sflow__polling_json(data.get('polling'))
	sampling = deserialize_Sflow__sampling_json(data.get('sampling'))
	result = Sflow(setting=setting, collector=collector, agent=agent, source_address=source_address, polling=polling, sampling=sampling)
	return result

class Sflow__setting(AxapiObject):
	__metaclass__ = StructMeta 
	max_header=PosRangedInteger(14, 512)
	source_ip_use_mgmt=PosRangedInteger(0, 1)
	packet_sampling_rate=PosRangedInteger(10, 1000000)
	counter_polling_interval=PosRangedInteger(1, 200)
	def __init__(self, max_header=None, source_ip_use_mgmt=None, packet_sampling_rate=None, counter_polling_interval=None):
		self.max_header = max_header
		self.source_ip_use_mgmt = source_ip_use_mgmt
		self.packet_sampling_rate = packet_sampling_rate
		self.counter_polling_interval = counter_polling_interval

	def __str__(self):
		return ""

class Sflow__collector(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, iplist=None, ipv6list=None):
		self.iplist = iplist
		self.ipv6list = ipv6list

	def __str__(self):
		return ""

class Sflow__agent__address(AxapiObject):
	__metaclass__ = StructMeta 
	ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6=SizedString(1, 255)
	def __init__(self, ip=None, ipv6=None):
		self.ip = ip
		self.ipv6 = ipv6

	def __str__(self):
		return ""

class Sflow__agent(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, address=None):
		self.address = address

	def __str__(self):
		return ""

class Sflow__source_address(AxapiObject):
	__metaclass__ = StructMeta 
	ip = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ipv6=SizedString(1, 255)
	def __init__(self, ip=None, ipv6=None):
		self.ip = ip
		self.ipv6 = ipv6

	def __str__(self):
		return ""

class Sflow__polling__ddos(AxapiObject):
	__metaclass__ = StructMeta 
	toggle = Enum(['enable', 'disable'])
	def __init__(self, toggle=None):
		self.toggle = toggle

	def __str__(self):
		return ""

class Sflow__polling__http(AxapiObject):
	__metaclass__ = StructMeta 
	toggle = Enum(['enable', 'disable'])
	def __init__(self, toggle=None):
		self.toggle = toggle

	def __str__(self):
		return ""

class Sflow__polling__cpu_usage(AxapiObject):
	__metaclass__ = StructMeta 
	toggle = Enum(['enable', 'disable'])
	def __init__(self, toggle=None):
		self.toggle = toggle

	def __str__(self):
		return ""

class Sflow__polling(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ddos=None, http=None, cpu_usage=None, ethernetlist=None, velist=None):
		self.ddos = ddos
		self.http = http
		self.cpu_usage = cpu_usage
		self.ethernetlist = ethernetlist
		self.velist = velist

	def __str__(self):
		return ""

class Sflow__sampling(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, ethernetlist=None, velist=None):
		self.ethernetlist = ethernetlist
		self.velist = velist

	def __str__(self):
		return ""

class Sflow(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, setting=None, collector=None, agent=None, source_address=None, polling=None, sampling=None):
		self.setting = setting
		self.collector = collector
		self.agent = agent
		self.source_address = source_address
		self.polling = polling
		self.sampling = sampling

	def __str__(self):
		return ""

class Sflow_collector_ip(AxapiObject):
	__metaclass__ = StructMeta 
	addr = RegexString('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	port=PosRangedInteger(1, 65535)
	def __init__(self, addr, port):
		self.addr = addr
		self.port = port

	def __str__(self):
		return str(self.addr) + '+' + str(self.port)

class Sflow_collector_ipv6(AxapiObject):
	__metaclass__ = StructMeta 
	addr=SizedString(1, 255)
	port=PosRangedInteger(1, 65535)
	def __init__(self, addr, port):
		self.addr = addr
		self.port = port

	def __str__(self):
		return str(self.addr) + '+' + str(self.port)

class Sflow_polling_ethernet(AxapiObject):
	__metaclass__ = StructMeta 
	start=PosRangedInteger(1, 2048)
	interval=PosRangedInteger(1, 200)
	def __init__(self, start, interval=None):
		self.start = start
		self.interval = interval

	def __str__(self):
		return str(self.start)

class Sflow_polling_ve(AxapiObject):
	__metaclass__ = StructMeta 
	start=PosRangedInteger(2, 4094)
	interval=PosRangedInteger(1, 200)
	def __init__(self, start, interval=None):
		self.start = start
		self.interval = interval

	def __str__(self):
		return str(self.start)

class Sflow_sampling_ethernet(AxapiObject):
	__metaclass__ = StructMeta 
	start=PosRangedInteger(1, 2048)
	rate=PosRangedInteger(10, 1000000)
	def __init__(self, start, rate=None):
		self.start = start
		self.rate = rate

	def __str__(self):
		return str(self.start)

class Sflow_sampling_ve(AxapiObject):
	__metaclass__ = StructMeta 
	start=PosRangedInteger(2, 4094)
	rate=PosRangedInteger(10, 1000000)
	def __init__(self, start, rate=None):
		self.start = start
		self.rate = rate

	def __str__(self):
		return str(self.start)

class SflowClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getSflow(self):
		"""
		Retrieve the sflow identified by the specified identifier
		
		Returns:
			An instance of the Sflow class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified sflow does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('sflow')
		return deserialize_Sflow_json(payload)

