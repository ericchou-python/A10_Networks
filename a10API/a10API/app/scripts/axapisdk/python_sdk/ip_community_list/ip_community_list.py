########################################################################################################################
# File name: ip_community_list.py
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
	'https://axapi.a10networks.com/axapi/v3/ip/community-list',
]

def deserialize_Ip_community_list_rules__std_list_action_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	std_list_action = data.get('std-list-action')
	community_num = data.get('community-num')
	local_as = data.get('local-AS')
	no_advertise = data.get('no-advertise')
	no_export = data.get('no-export')
	result = Ip_community_list_rules__std_list_action_cfg(std_list_action=std_list_action, community_num=community_num, local_as=local_as, no_advertise=no_advertise, no_export=no_export)
	return result

def deserialize_Ip_community_list_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	seq_num = data.get('seq-num')
	std_list_action_cfg = deserialize_Ip_community_list_rules__std_list_action_cfg_json(data.get('std-list-action-cfg'))
	result = Ip_community_list_rules(seq_num=seq_num, std_list_action_cfg=std_list_action_cfg)
	return result

def deserialize_list_Ip_community_list_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_community_list_rules_json(item))
	return list(container)

def deserialize_Community_list__std_list_num_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	std_list_num = data.get('std-list-num')
	rules = deserialize_list_Ip_community_list_rules_json(data.get('rules'))
	result = Community_list__std_list_num_cfg(std_list_num=std_list_num, rules=rules)
	return result

def deserialize_Ip_community_list_ext_rules__ext_list_action_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ext_list_action = data.get('ext-list-action')
	value = data.get('value')
	result = Ip_community_list_ext_rules__ext_list_action_cfg(ext_list_action=ext_list_action, value=value)
	return result

def deserialize_Ip_community_list_ext_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	seq_num = data.get('seq-num')
	ext_list_action_cfg = deserialize_Ip_community_list_ext_rules__ext_list_action_cfg_json(data.get('ext-list-action-cfg'))
	result = Ip_community_list_ext_rules(seq_num=seq_num, ext_list_action_cfg=ext_list_action_cfg)
	return result

def deserialize_list_Ip_community_list_ext_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_community_list_ext_rules_json(item))
	return list(container)

def deserialize_Community_list__ext_list_num_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ext_list_num = data.get('ext-list-num')
	ext_rules = deserialize_list_Ip_community_list_ext_rules_json(data.get('ext-rules'))
	result = Community_list__ext_list_num_cfg(ext_list_num=ext_list_num, ext_rules=ext_rules)
	return result

def deserialize_Ip_community_list_name_rules__name_action_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name_action = data.get('name-action')
	value = data.get('value')
	result = Ip_community_list_name_rules__name_action_cfg(name_action=name_action, value=value)
	return result

def deserialize_Ip_community_list_name_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	seq_num = data.get('seq-num')
	name_action_cfg = deserialize_Ip_community_list_name_rules__name_action_cfg_json(data.get('name-action-cfg'))
	result = Ip_community_list_name_rules(seq_num=seq_num, name_action_cfg=name_action_cfg)
	return result

def deserialize_list_Ip_community_list_name_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_community_list_name_rules_json(item))
	return list(container)

def deserialize_Community_list__name_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	name = data.get('name')
	name_rules = deserialize_list_Ip_community_list_name_rules_json(data.get('name-rules'))
	result = Community_list__name_cfg(name=name, name_rules=name_rules)
	return result

def deserialize_Ip_community_list_std_rules__standard_action_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	standard_action = data.get('standard-action')
	community_num = data.get('community-num')
	local_as = data.get('local-AS')
	no_advertise = data.get('no-advertise')
	no_export = data.get('no-export')
	result = Ip_community_list_std_rules__standard_action_cfg(standard_action=standard_action, community_num=community_num, local_as=local_as, no_advertise=no_advertise, no_export=no_export)
	return result

def deserialize_Ip_community_list_std_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	seq_num = data.get('seq-num')
	standard_action_cfg = deserialize_Ip_community_list_std_rules__standard_action_cfg_json(data.get('standard-action-cfg'))
	result = Ip_community_list_std_rules(seq_num=seq_num, standard_action_cfg=standard_action_cfg)
	return result

def deserialize_list_Ip_community_list_std_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_community_list_std_rules_json(item))
	return list(container)

def deserialize_Community_list__standard_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	standard = data.get('standard')
	std_rules = deserialize_list_Ip_community_list_std_rules_json(data.get('std-rules'))
	result = Community_list__standard_cfg(standard=standard, std_rules=std_rules)
	return result

def deserialize_Ip_community_list_exp_rules__expanded_action_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	expanded_action = data.get('expanded-action')
	value = data.get('value')
	result = Ip_community_list_exp_rules__expanded_action_cfg(expanded_action=expanded_action, value=value)
	return result

def deserialize_Ip_community_list_exp_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	seq_num = data.get('seq-num')
	expanded_action_cfg = deserialize_Ip_community_list_exp_rules__expanded_action_cfg_json(data.get('expanded-action-cfg'))
	result = Ip_community_list_exp_rules(seq_num=seq_num, expanded_action_cfg=expanded_action_cfg)
	return result

def deserialize_list_Ip_community_list_exp_rules_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Ip_community_list_exp_rules_json(item))
	return list(container)

def deserialize_Community_list__expanded_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	expanded = data.get('expanded')
	exp_rules = deserialize_list_Ip_community_list_exp_rules_json(data.get('exp-rules'))
	result = Community_list__expanded_cfg(expanded=expanded, exp_rules=exp_rules)
	return result

def deserialize_Community_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	std_list_num_cfg = deserialize_Community_list__std_list_num_cfg_json(data.get('std-list-num-cfg'))
	ext_list_num_cfg = deserialize_Community_list__ext_list_num_cfg_json(data.get('ext-list-num-cfg'))
	name_cfg = deserialize_Community_list__name_cfg_json(data.get('name-cfg'))
	standard_cfg = deserialize_Community_list__standard_cfg_json(data.get('standard-cfg'))
	expanded_cfg = deserialize_Community_list__expanded_cfg_json(data.get('expanded-cfg'))
	result = Community_list(std_list_num_cfg=std_list_num_cfg, ext_list_num_cfg=ext_list_num_cfg, name_cfg=name_cfg, standard_cfg=standard_cfg, expanded_cfg=expanded_cfg)
	return result

def serialize_Ip_community_list_rules__std_list_action_cfg_json(obj):
	output = OrderedDict()
	if obj.std_list_action is not None:
		output['std-list-action'] = obj.std_list_action
	if obj.community_num is not None:
		output['community-num'] = obj.community_num
	if obj.local_as is not None:
		output['local-AS'] = obj.local_as
	if obj.no_advertise is not None:
		output['no-advertise'] = obj.no_advertise
	if obj.no_export is not None:
		output['no-export'] = obj.no_export
	return output

def serialize_Ip_community_list_rules_json(obj):
	output = OrderedDict()
	if obj.seq_num is not None:
		output['seq-num'] = obj.seq_num
	if obj.std_list_action_cfg is not None:
		output['std-list-action-cfg'] = serialize_Ip_community_list_rules__std_list_action_cfg_json(obj.std_list_action_cfg)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def serialize_list_Ip_community_list_rules_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_community_list_rules_json(item))
	return output

def serialize_Community_list__std_list_num_cfg_json(obj):
	output = OrderedDict()
	output['std-list-num'] = obj.std_list_num
	if obj.rules is not None:
		output['rules'] = serialize_list_Ip_community_list_rules_json(obj.rules)
	return output

def serialize_Ip_community_list_ext_rules__ext_list_action_cfg_json(obj):
	output = OrderedDict()
	if obj.ext_list_action is not None:
		output['ext-list-action'] = obj.ext_list_action
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Ip_community_list_ext_rules_json(obj):
	output = OrderedDict()
	if obj.seq_num is not None:
		output['seq-num'] = obj.seq_num
	if obj.ext_list_action_cfg is not None:
		output['ext-list-action-cfg'] = serialize_Ip_community_list_ext_rules__ext_list_action_cfg_json(obj.ext_list_action_cfg)
	return output

def serialize_list_Ip_community_list_ext_rules_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_community_list_ext_rules_json(item))
	return output

def serialize_Community_list__ext_list_num_cfg_json(obj):
	output = OrderedDict()
	output['ext-list-num'] = obj.ext_list_num
	if obj.ext_rules is not None:
		output['ext-rules'] = serialize_list_Ip_community_list_ext_rules_json(obj.ext_rules)
	return output

def serialize_Ip_community_list_name_rules__name_action_cfg_json(obj):
	output = OrderedDict()
	if obj.name_action is not None:
		output['name-action'] = obj.name_action
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Ip_community_list_name_rules_json(obj):
	output = OrderedDict()
	if obj.seq_num is not None:
		output['seq-num'] = obj.seq_num
	if obj.name_action_cfg is not None:
		output['name-action-cfg'] = serialize_Ip_community_list_name_rules__name_action_cfg_json(obj.name_action_cfg)
	return output

def serialize_list_Ip_community_list_name_rules_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_community_list_name_rules_json(item))
	return output

def serialize_Community_list__name_cfg_json(obj):
	output = OrderedDict()
	output['name'] = obj.name
	if obj.name_rules is not None:
		output['name-rules'] = serialize_list_Ip_community_list_name_rules_json(obj.name_rules)
	return output

def serialize_Ip_community_list_std_rules__standard_action_cfg_json(obj):
	output = OrderedDict()
	if obj.standard_action is not None:
		output['standard-action'] = obj.standard_action
	if obj.community_num is not None:
		output['community-num'] = obj.community_num
	if obj.local_as is not None:
		output['local-AS'] = obj.local_as
	if obj.no_advertise is not None:
		output['no-advertise'] = obj.no_advertise
	if obj.no_export is not None:
		output['no-export'] = obj.no_export
	return output

def serialize_Ip_community_list_std_rules_json(obj):
	output = OrderedDict()
	if obj.seq_num is not None:
		output['seq-num'] = obj.seq_num
	if obj.standard_action_cfg is not None:
		output['standard-action-cfg'] = serialize_Ip_community_list_std_rules__standard_action_cfg_json(obj.standard_action_cfg)
	return output

def serialize_list_Ip_community_list_std_rules_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_community_list_std_rules_json(item))
	return output

def serialize_Community_list__standard_cfg_json(obj):
	output = OrderedDict()
	output['standard'] = obj.standard
	if obj.std_rules is not None:
		output['std-rules'] = serialize_list_Ip_community_list_std_rules_json(obj.std_rules)
	return output

def serialize_Ip_community_list_exp_rules__expanded_action_cfg_json(obj):
	output = OrderedDict()
	if obj.expanded_action is not None:
		output['expanded-action'] = obj.expanded_action
	if obj.value is not None:
		output['value'] = obj.value
	return output

def serialize_Ip_community_list_exp_rules_json(obj):
	output = OrderedDict()
	if obj.seq_num is not None:
		output['seq-num'] = obj.seq_num
	if obj.expanded_action_cfg is not None:
		output['expanded-action-cfg'] = serialize_Ip_community_list_exp_rules__expanded_action_cfg_json(obj.expanded_action_cfg)
	return output

def serialize_list_Ip_community_list_exp_rules_json(obj):
	output = list()
	for item in obj:
		output.append(serialize_Ip_community_list_exp_rules_json(item))
	return output

def serialize_Community_list__expanded_cfg_json(obj):
	output = OrderedDict()
	output['expanded'] = obj.expanded
	if obj.exp_rules is not None:
		output['exp-rules'] = serialize_list_Ip_community_list_exp_rules_json(obj.exp_rules)
	return output

def serialize_Community_list_json(obj):
	output = OrderedDict()
	output['std-list-num-cfg'] = serialize_Community_list__std_list_num_cfg_json(obj.std_list_num_cfg)
	if obj.ext_list_num_cfg is not None:
		output['ext-list-num-cfg'] = serialize_Community_list__ext_list_num_cfg_json(obj.ext_list_num_cfg)
	if obj.name_cfg is not None:
		output['name-cfg'] = serialize_Community_list__name_cfg_json(obj.name_cfg)
	if obj.standard_cfg is not None:
		output['standard-cfg'] = serialize_Community_list__standard_cfg_json(obj.standard_cfg)
	if obj.expanded_cfg is not None:
		output['expanded-cfg'] = serialize_Community_list__expanded_cfg_json(obj.expanded_cfg)
	return output

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Community_list_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Community_list_json(item))
	return list(container)

class Community_list__std_list_num_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	std_list_num=PosRangedInteger(1, 99)
	def __init__(self, std_list_num, rules=None):
		self.std_list_num = std_list_num
		self.rules = rules

	def __str__(self):
		return str(self.std_list_num)

class Community_list__ext_list_num_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ext_list_num=PosRangedInteger(100, 199)
	def __init__(self, ext_list_num, ext_rules=None):
		self.ext_list_num = ext_list_num
		self.ext_rules = ext_rules

	def __str__(self):
		return str(self.ext_list_num)

class Community_list__name_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	name=SizedString(1, 255)
	def __init__(self, name, name_rules=None):
		self.name = name
		self.name_rules = name_rules

	def __str__(self):
		return str(self.name)

class Community_list__standard_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	standard=SizedString(1, 255)
	def __init__(self, standard, std_rules=None):
		self.standard = standard
		self.std_rules = std_rules

	def __str__(self):
		return str(self.standard)

class Community_list__expanded_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	expanded=SizedString(1, 255)
	def __init__(self, expanded, exp_rules=None):
		self.expanded = expanded
		self.exp_rules = exp_rules

	def __str__(self):
		return str(self.expanded)

class Community_list(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, std_list_num_cfg, ext_list_num_cfg=None, name_cfg=None, standard_cfg=None, expanded_cfg=None):
		self.std_list_num_cfg = std_list_num_cfg
		self.ext_list_num_cfg = ext_list_num_cfg
		self.name_cfg = name_cfg
		self.standard_cfg = standard_cfg
		self.expanded_cfg = expanded_cfg

	def __str__(self):
		return str(self.std_list_num_cfg)

class Ip_community_list_rules__std_list_action_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	std_list_action = Enum(['deny', 'permit'])
	community_num=SizedString(1, 255)
	local_as=PosRangedInteger(0, 1)
	no_advertise=PosRangedInteger(0, 1)
	no_export=PosRangedInteger(0, 1)
	def __init__(self, std_list_action=None, community_num=None, local_as=None, no_advertise=None, no_export=None):
		self.std_list_action = std_list_action
		self.community_num = community_num
		self.local_as = local_as
		self.no_advertise = no_advertise
		self.no_export = no_export

	def __str__(self):
		return ""

class Ip_community_list_rules(AxapiObject):
	__metaclass__ = StructMeta 
	seq_num=PosRangedInteger(1, 8192)
	def __init__(self, seq_num=None, std_list_action_cfg=None):
		self.seq_num = seq_num
		self.std_list_action_cfg = std_list_action_cfg

	def __str__(self):
		return ""

class Ip_community_list_ext_rules__ext_list_action_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ext_list_action = Enum(['deny', 'permit'])
	value=SizedString(0, 255)
	def __init__(self, ext_list_action=None, value=None):
		self.ext_list_action = ext_list_action
		self.value = value

	def __str__(self):
		return ""

class Ip_community_list_ext_rules(AxapiObject):
	__metaclass__ = StructMeta 
	seq_num=PosRangedInteger(1, 8192)
	def __init__(self, seq_num=None, ext_list_action_cfg=None):
		self.seq_num = seq_num
		self.ext_list_action_cfg = ext_list_action_cfg

	def __str__(self):
		return ""

class Ip_community_list_name_rules__name_action_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	name_action = Enum(['deny', 'permit'])
	value=SizedString(1, 255)
	def __init__(self, name_action=None, value=None):
		self.name_action = name_action
		self.value = value

	def __str__(self):
		return ""

class Ip_community_list_name_rules(AxapiObject):
	__metaclass__ = StructMeta 
	seq_num=PosRangedInteger(1, 8192)
	def __init__(self, seq_num=None, name_action_cfg=None):
		self.seq_num = seq_num
		self.name_action_cfg = name_action_cfg

	def __str__(self):
		return ""

class Ip_community_list_std_rules__standard_action_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	standard_action = Enum(['deny', 'permit'])
	community_num=SizedString(1, 255)
	local_as=PosInteger()
	no_advertise=PosInteger()
	no_export=PosInteger()
	def __init__(self, standard_action=None, community_num=None, local_as=None, no_advertise=None, no_export=None):
		self.standard_action = standard_action
		self.community_num = community_num
		self.local_as = local_as
		self.no_advertise = no_advertise
		self.no_export = no_export

	def __str__(self):
		return ""

class Ip_community_list_std_rules(AxapiObject):
	__metaclass__ = StructMeta 
	seq_num=PosRangedInteger(1, 8192)
	def __init__(self, seq_num=None, standard_action_cfg=None):
		self.seq_num = seq_num
		self.standard_action_cfg = standard_action_cfg

	def __str__(self):
		return ""

class Community_list_std_list_num_cfg__std_list_num_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	std_list_num=PosRangedInteger(1, 99)
	def __init__(self, std_list_num, rules=None):
		self.std_list_num = std_list_num
		self.rules = rules

	def __str__(self):
		return str(self.std_list_num)

class Community_list_std_list_num_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, std_list_num_cfg):
		self.std_list_num_cfg = std_list_num_cfg

	def __str__(self):
		return str(self.std_list_num_cfg)

class Ip_community_list_exp_rules__expanded_action_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	expanded_action = Enum(['deny', 'permit'])
	value=SizedString(1, 255)
	def __init__(self, expanded_action=None, value=None):
		self.expanded_action = expanded_action
		self.value = value

	def __str__(self):
		return ""

class Ip_community_list_exp_rules(AxapiObject):
	__metaclass__ = StructMeta 
	seq_num=PosRangedInteger(1, 8192)
	def __init__(self, seq_num=None, expanded_action_cfg=None):
		self.seq_num = seq_num
		self.expanded_action_cfg = expanded_action_cfg

	def __str__(self):
		return ""

class IpCommunitylistClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getIpCommunitylist(self, community_list_std_list_num_cfg):
		"""
		Retrieve the community_list identified by the specified identifier
		
		Args:
			community_list_std_list_num_cfg Community_list_std_list_num_cfg
		
		Returns:
			An instance of the Community_list class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(community_list_std_list_num_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified community_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('community-list')
		return deserialize_Community_list_json(payload)

	def putIpCommunitylist(self, community_list_std_list_num_cfg, community_list):
		"""
		Replace the object community_list
		
		Args:
			community_list_std_list_num_cfg Community_list_std_list_num_cfg
			community_list An instance of the Community_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['community-list']=serialize_Community_list_json(community_list)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(community_list_std_list_num_cfg) .replace("/", "%2f") + query, payload, headers)
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

	def deleteIpCommunitylist(self, community_list_std_list_num_cfg):
		"""
		Remove the community_list identified by the specified identifier from the
		system
		
		Args:
			community_list_std_list_num_cfg Community_list_std_list_num_cfg
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(community_list_std_list_num_cfg) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified community_list does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllIpCommunitylistsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitIpCommunitylist(self, community_list):
		"""
		Create the object community_list
		
		Args:
			community_list An instance of the Community_list class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['community-list']=serialize_Community_list_json(community_list)
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

	def getAllIpCommunitylists(self):
		"""
		Retrieve all community_list objects currently pending in the system
		
		Returns:
			A list of Community_list objects
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
			payload= data.get('community-listList')
		return deserialize_list_Community_list_json(payload)

