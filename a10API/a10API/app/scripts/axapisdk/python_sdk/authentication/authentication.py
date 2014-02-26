########################################################################################################################
# File name: authentication.py
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
	'https://axapi.a10networks.com/axapi/v3/authentication',
]

def deserialize_Authentication__type_cfg__ldap_cfg__ldap_local_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ldap_local = data.get('ldap-local')
	ldap_local_radius = data.get('ldap-local-radius')
	ldap_local_radius_tacplus = data.get('ldap-local-radius-tacplus')
	ldap_local_tacplus = data.get('ldap-local-tacplus')
	ldap_local_tacplus_radius = data.get('ldap-local-tacplus-radius')
	result = Authentication__type_cfg__ldap_cfg__ldap_local_cfg(ldap_local=ldap_local, ldap_local_radius=ldap_local_radius, ldap_local_radius_tacplus=ldap_local_radius_tacplus, ldap_local_tacplus=ldap_local_tacplus, ldap_local_tacplus_radius=ldap_local_tacplus_radius)
	return result

def deserialize_Authentication__type_cfg__ldap_cfg__ldap_radius_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ldap_radius = data.get('ldap-radius')
	ldap_radius_local = data.get('ldap-radius-local')
	ldap_radius_local_tacplus = data.get('ldap-radius-local-tacplus')
	ldap_radius_tacplus = data.get('ldap-radius-tacplus')
	ldap_radius_tacplus_local = data.get('ldap-radius-tacplus-local')
	result = Authentication__type_cfg__ldap_cfg__ldap_radius_cfg(ldap_radius=ldap_radius, ldap_radius_local=ldap_radius_local, ldap_radius_local_tacplus=ldap_radius_local_tacplus, ldap_radius_tacplus=ldap_radius_tacplus, ldap_radius_tacplus_local=ldap_radius_tacplus_local)
	return result

def deserialize_Authentication__type_cfg__ldap_cfg__ldap_tacplus_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ldap_tacplus = data.get('ldap-tacplus')
	ldap_tacplus_local = data.get('ldap-tacplus-local')
	ldap_tacplus_local_radius = data.get('ldap-tacplus-local-radius')
	ldap_tacplus_radius = data.get('ldap-tacplus-radius')
	ldap_tacplus_radius_local = data.get('ldap-tacplus-radius-local')
	result = Authentication__type_cfg__ldap_cfg__ldap_tacplus_cfg(ldap_tacplus=ldap_tacplus, ldap_tacplus_local=ldap_tacplus_local, ldap_tacplus_local_radius=ldap_tacplus_local_radius, ldap_tacplus_radius=ldap_tacplus_radius, ldap_tacplus_radius_local=ldap_tacplus_radius_local)
	return result

def deserialize_Authentication__type_cfg__ldap_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	ldap = data.get('ldap')
	ldap_local_cfg = deserialize_Authentication__type_cfg__ldap_cfg__ldap_local_cfg_json(data.get('ldap-local-cfg'))
	ldap_radius_cfg = deserialize_Authentication__type_cfg__ldap_cfg__ldap_radius_cfg_json(data.get('ldap-radius-cfg'))
	ldap_tacplus_cfg = deserialize_Authentication__type_cfg__ldap_cfg__ldap_tacplus_cfg_json(data.get('ldap-tacplus-cfg'))
	result = Authentication__type_cfg__ldap_cfg(ldap=ldap, ldap_local_cfg=ldap_local_cfg, ldap_radius_cfg=ldap_radius_cfg, ldap_tacplus_cfg=ldap_tacplus_cfg)
	return result

def deserialize_Authentication__type_cfg__radius_cfg__radius_ldap_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	radius_ldap = data.get('radius-ldap')
	radius_ldap_local = data.get('radius-ldap-local')
	radius_ldap_local_tacplus = data.get('radius-ldap-local-tacplus')
	radius_ldap_tacplus = data.get('radius-ldap-tacplus')
	radius_ldap_tacplus_local = data.get('radius-ldap-tacplus-local')
	result = Authentication__type_cfg__radius_cfg__radius_ldap_cfg(radius_ldap=radius_ldap, radius_ldap_local=radius_ldap_local, radius_ldap_local_tacplus=radius_ldap_local_tacplus, radius_ldap_tacplus=radius_ldap_tacplus, radius_ldap_tacplus_local=radius_ldap_tacplus_local)
	return result

def deserialize_Authentication__type_cfg__radius_cfg__radius_local_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	radius_local = data.get('radius-local')
	radius_local_ldap = data.get('radius-local-ldap')
	radius_local_ldap_tacplus = data.get('radius-local-ldap-tacplus')
	radius_local_tacplus = data.get('radius-local-tacplus')
	radius_local_tacplus_ldap = data.get('radius-local-tacplus-ldap')
	result = Authentication__type_cfg__radius_cfg__radius_local_cfg(radius_local=radius_local, radius_local_ldap=radius_local_ldap, radius_local_ldap_tacplus=radius_local_ldap_tacplus, radius_local_tacplus=radius_local_tacplus, radius_local_tacplus_ldap=radius_local_tacplus_ldap)
	return result

def deserialize_Authentication__type_cfg__radius_cfg__radius_tacplus_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	radius_tacplus = data.get('radius-tacplus')
	radius_tacplus_ldap = data.get('radius-tacplus-ldap')
	radius_tacplus_ldap_local = data.get('radius-tacplus-ldap-local')
	radius_tacplus_local = data.get('radius-tacplus-local')
	radius_tacplus_local_ldap = data.get('radius-tacplus-local-ldap')
	result = Authentication__type_cfg__radius_cfg__radius_tacplus_cfg(radius_tacplus=radius_tacplus, radius_tacplus_ldap=radius_tacplus_ldap, radius_tacplus_ldap_local=radius_tacplus_ldap_local, radius_tacplus_local=radius_tacplus_local, radius_tacplus_local_ldap=radius_tacplus_local_ldap)
	return result

def deserialize_Authentication__type_cfg__radius_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	radius = data.get('radius')
	radius_ldap_cfg = deserialize_Authentication__type_cfg__radius_cfg__radius_ldap_cfg_json(data.get('radius-ldap-cfg'))
	radius_local_cfg = deserialize_Authentication__type_cfg__radius_cfg__radius_local_cfg_json(data.get('radius-local-cfg'))
	radius_tacplus_cfg = deserialize_Authentication__type_cfg__radius_cfg__radius_tacplus_cfg_json(data.get('radius-tacplus-cfg'))
	result = Authentication__type_cfg__radius_cfg(radius=radius, radius_ldap_cfg=radius_ldap_cfg, radius_local_cfg=radius_local_cfg, radius_tacplus_cfg=radius_tacplus_cfg)
	return result

def deserialize_Authentication__type_cfg__local_cfg__local_ldap_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_ldap = data.get('local-ldap')
	local_ldap_radius = data.get('local-ldap-radius')
	local_ldap_radius_tacplus = data.get('local-ldap-radius-tacplus')
	local_ldap_tacplus = data.get('local-ldap-tacplus')
	local_ldap_tacplus_radius = data.get('local-ldap-tacplus-radius')
	result = Authentication__type_cfg__local_cfg__local_ldap_cfg(local_ldap=local_ldap, local_ldap_radius=local_ldap_radius, local_ldap_radius_tacplus=local_ldap_radius_tacplus, local_ldap_tacplus=local_ldap_tacplus, local_ldap_tacplus_radius=local_ldap_tacplus_radius)
	return result

def deserialize_Authentication__type_cfg__local_cfg__local_radius_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_radius = data.get('local-radius')
	local_radius_ldap = data.get('local-radius-ldap')
	local_radius_ldap_tacplus = data.get('local-radius-ldap-tacplus')
	local_radius_tacplus = data.get('local-radius-tacplus')
	local_radius_tacplus_ldap = data.get('local-radius-tacplus-ldap')
	result = Authentication__type_cfg__local_cfg__local_radius_cfg(local_radius=local_radius, local_radius_ldap=local_radius_ldap, local_radius_ldap_tacplus=local_radius_ldap_tacplus, local_radius_tacplus=local_radius_tacplus, local_radius_tacplus_ldap=local_radius_tacplus_ldap)
	return result

def deserialize_Authentication__type_cfg__local_cfg__local_tacplus_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local_tacplus = data.get('local-tacplus')
	local_tacplus_ldap = data.get('local-tacplus-ldap')
	local_tacplus_ldap_radius = data.get('local-tacplus-ldap-radius')
	local_tacplus_radius = data.get('local-tacplus-radius')
	local_tacplus_radius_ldap = data.get('local-tacplus-radius-ldap')
	result = Authentication__type_cfg__local_cfg__local_tacplus_cfg(local_tacplus=local_tacplus, local_tacplus_ldap=local_tacplus_ldap, local_tacplus_ldap_radius=local_tacplus_ldap_radius, local_tacplus_radius=local_tacplus_radius, local_tacplus_radius_ldap=local_tacplus_radius_ldap)
	return result

def deserialize_Authentication__type_cfg__local_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	local = data.get('local')
	local_ldap_cfg = deserialize_Authentication__type_cfg__local_cfg__local_ldap_cfg_json(data.get('local-ldap-cfg'))
	local_radius_cfg = deserialize_Authentication__type_cfg__local_cfg__local_radius_cfg_json(data.get('local-radius-cfg'))
	local_tacplus_cfg = deserialize_Authentication__type_cfg__local_cfg__local_tacplus_cfg_json(data.get('local-tacplus-cfg'))
	result = Authentication__type_cfg__local_cfg(local=local, local_ldap_cfg=local_ldap_cfg, local_radius_cfg=local_radius_cfg, local_tacplus_cfg=local_tacplus_cfg)
	return result

def deserialize_Authentication__type_cfg__tacplus_cfg__tacplus_ldap_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tacplus_ldap = data.get('tacplus-ldap')
	tacplus_ldap_radius = data.get('tacplus-ldap-radius')
	tacplus_ldap_radius_local = data.get('tacplus-ldap-radius-local')
	tacplus_ldap_local = data.get('tacplus-ldap-local')
	tacplus_ldap_local_radius = data.get('tacplus-ldap-local-radius')
	result = Authentication__type_cfg__tacplus_cfg__tacplus_ldap_cfg(tacplus_ldap=tacplus_ldap, tacplus_ldap_radius=tacplus_ldap_radius, tacplus_ldap_radius_local=tacplus_ldap_radius_local, tacplus_ldap_local=tacplus_ldap_local, tacplus_ldap_local_radius=tacplus_ldap_local_radius)
	return result

def deserialize_Authentication__type_cfg__tacplus_cfg__tacplus_radius_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tacplus_radius = data.get('tacplus-radius')
	tacplus_radius_ldap = data.get('tacplus-radius-ldap')
	tacplus_radius_ldap_local = data.get('tacplus-radius-ldap-local')
	tacplus_radius_local = data.get('tacplus-radius-local')
	tacplus_radius_local_ldap = data.get('tacplus-radius-local-ldap')
	result = Authentication__type_cfg__tacplus_cfg__tacplus_radius_cfg(tacplus_radius=tacplus_radius, tacplus_radius_ldap=tacplus_radius_ldap, tacplus_radius_ldap_local=tacplus_radius_ldap_local, tacplus_radius_local=tacplus_radius_local, tacplus_radius_local_ldap=tacplus_radius_local_ldap)
	return result

def deserialize_Authentication__type_cfg__tacplus_cfg__tacplus_local_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tacplus_local = data.get('tacplus-local')
	tacplus_local_ldap = data.get('tacplus-local-ldap')
	tacplus_local_ldap_radius = data.get('tacplus-local-ldap-radius')
	tacplus_local_radius = data.get('tacplus-local-radius')
	tacplus_local_radius_ldap = data.get('tacplus-local-radius-ldap')
	result = Authentication__type_cfg__tacplus_cfg__tacplus_local_cfg(tacplus_local=tacplus_local, tacplus_local_ldap=tacplus_local_ldap, tacplus_local_ldap_radius=tacplus_local_ldap_radius, tacplus_local_radius=tacplus_local_radius, tacplus_local_radius_ldap=tacplus_local_radius_ldap)
	return result

def deserialize_Authentication__type_cfg__tacplus_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tacplus = data.get('tacplus')
	tacplus_ldap_cfg = deserialize_Authentication__type_cfg__tacplus_cfg__tacplus_ldap_cfg_json(data.get('tacplus-ldap-cfg'))
	tacplus_radius_cfg = deserialize_Authentication__type_cfg__tacplus_cfg__tacplus_radius_cfg_json(data.get('tacplus-radius-cfg'))
	tacplus_local_cfg = deserialize_Authentication__type_cfg__tacplus_cfg__tacplus_local_cfg_json(data.get('tacplus-local-cfg'))
	result = Authentication__type_cfg__tacplus_cfg(tacplus=tacplus, tacplus_ldap_cfg=tacplus_ldap_cfg, tacplus_radius_cfg=tacplus_radius_cfg, tacplus_local_cfg=tacplus_local_cfg)
	return result

def deserialize_Authentication__type_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type = data.get('type')
	ldap_cfg = deserialize_Authentication__type_cfg__ldap_cfg_json(data.get('ldap-cfg'))
	radius_cfg = deserialize_Authentication__type_cfg__radius_cfg_json(data.get('radius-cfg'))
	local_cfg = deserialize_Authentication__type_cfg__local_cfg_json(data.get('local-cfg'))
	tacplus_cfg = deserialize_Authentication__type_cfg__tacplus_cfg_json(data.get('tacplus-cfg'))
	result = Authentication__type_cfg(type=type, ldap_cfg=ldap_cfg, radius_cfg=radius_cfg, local_cfg=local_cfg, tacplus_cfg=tacplus_cfg)
	return result

def deserialize_Authentication__enable_cfg__enable_local_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable_local = data.get('enable-local')
	enable_local_tacplus = data.get('enable-local-tacplus')
	result = Authentication__enable_cfg__enable_local_cfg(enable_local=enable_local, enable_local_tacplus=enable_local_tacplus)
	return result

def deserialize_Authentication__enable_cfg__enable_tacplus_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable_tacplus = data.get('enable-tacplus')
	enable_tacplus_local = data.get('enable-tacplus-local')
	result = Authentication__enable_cfg__enable_tacplus_cfg(enable_tacplus=enable_tacplus, enable_tacplus_local=enable_tacplus_local)
	return result

def deserialize_Authentication__enable_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	enable = data.get('enable')
	enable_local_cfg = deserialize_Authentication__enable_cfg__enable_local_cfg_json(data.get('enable-local-cfg'))
	enable_tacplus_cfg = deserialize_Authentication__enable_cfg__enable_tacplus_cfg_json(data.get('enable-tacplus-cfg'))
	result = Authentication__enable_cfg(enable=enable, enable_local_cfg=enable_local_cfg, enable_tacplus_cfg=enable_tacplus_cfg)
	return result

def deserialize_Authentication__login_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	login = data.get('login')
	privilege_mode = data.get('privilege-mode')
	local = data.get('local')
	result = Authentication__login_cfg(login=login, privilege_mode=privilege_mode, local=local)
	return result

def deserialize_Authentication__mode_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	mode = data.get('mode')
	multiple = data.get('multiple')
	single = data.get('single')
	result = Authentication__mode_cfg(mode=mode, multiple=multiple, single=single)
	return result

def deserialize_Authentication__console__type_cfg_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type = data.get('type')
	ldap = data.get('ldap')
	local = data.get('local')
	radius = data.get('radius')
	tacplus = data.get('tacplus')
	result = Authentication__console__type_cfg(type=type, ldap=ldap, local=local, radius=radius, tacplus=tacplus)
	return result

def deserialize_Authentication__console_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type_cfg = deserialize_Authentication__console__type_cfg_json(data.get('type-cfg'))
	result = Authentication__console(type_cfg=type_cfg)
	return result

def deserialize_Authentication_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	type_cfg = deserialize_Authentication__type_cfg_json(data.get('type-cfg'))
	disable_local = data.get('disable-local')
	enable_cfg = deserialize_Authentication__enable_cfg_json(data.get('enable-cfg'))
	login_cfg = deserialize_Authentication__login_cfg_json(data.get('login-cfg'))
	mode_cfg = deserialize_Authentication__mode_cfg_json(data.get('mode-cfg'))
	multiple_auth_reject = data.get('multiple-auth-reject')
	console = deserialize_Authentication__console_json(data.get('console'))
	result = Authentication(type_cfg=type_cfg, disable_local=disable_local, enable_cfg=enable_cfg, login_cfg=login_cfg, mode_cfg=mode_cfg, multiple_auth_reject=multiple_auth_reject, console=console)
	return result

def serialize_Authentication__type_cfg__ldap_cfg__ldap_local_cfg_json(obj):
	output = OrderedDict()
	if obj.ldap_local is not None:
		output['ldap-local'] = obj.ldap_local
	if obj.ldap_local_radius is not None:
		output['ldap-local-radius'] = obj.ldap_local_radius
	if obj.ldap_local_radius_tacplus is not None:
		output['ldap-local-radius-tacplus'] = obj.ldap_local_radius_tacplus
	if obj.ldap_local_tacplus is not None:
		output['ldap-local-tacplus'] = obj.ldap_local_tacplus
	if obj.ldap_local_tacplus_radius is not None:
		output['ldap-local-tacplus-radius'] = obj.ldap_local_tacplus_radius
	return output

def serialize_Authentication__type_cfg__ldap_cfg__ldap_radius_cfg_json(obj):
	output = OrderedDict()
	if obj.ldap_radius is not None:
		output['ldap-radius'] = obj.ldap_radius
	if obj.ldap_radius_local is not None:
		output['ldap-radius-local'] = obj.ldap_radius_local
	if obj.ldap_radius_local_tacplus is not None:
		output['ldap-radius-local-tacplus'] = obj.ldap_radius_local_tacplus
	if obj.ldap_radius_tacplus is not None:
		output['ldap-radius-tacplus'] = obj.ldap_radius_tacplus
	if obj.ldap_radius_tacplus_local is not None:
		output['ldap-radius-tacplus-local'] = obj.ldap_radius_tacplus_local
	return output

def serialize_Authentication__type_cfg__ldap_cfg__ldap_tacplus_cfg_json(obj):
	output = OrderedDict()
	if obj.ldap_tacplus is not None:
		output['ldap-tacplus'] = obj.ldap_tacplus
	if obj.ldap_tacplus_local is not None:
		output['ldap-tacplus-local'] = obj.ldap_tacplus_local
	if obj.ldap_tacplus_local_radius is not None:
		output['ldap-tacplus-local-radius'] = obj.ldap_tacplus_local_radius
	if obj.ldap_tacplus_radius is not None:
		output['ldap-tacplus-radius'] = obj.ldap_tacplus_radius
	if obj.ldap_tacplus_radius_local is not None:
		output['ldap-tacplus-radius-local'] = obj.ldap_tacplus_radius_local
	return output

def serialize_Authentication__type_cfg__ldap_cfg_json(obj):
	output = OrderedDict()
	if obj.ldap is not None:
		output['ldap'] = obj.ldap
	if obj.ldap_local_cfg is not None:
		output['ldap-local-cfg'] = serialize_Authentication__type_cfg__ldap_cfg__ldap_local_cfg_json(obj.ldap_local_cfg)
	if obj.ldap_radius_cfg is not None:
		output['ldap-radius-cfg'] = serialize_Authentication__type_cfg__ldap_cfg__ldap_radius_cfg_json(obj.ldap_radius_cfg)
	if obj.ldap_tacplus_cfg is not None:
		output['ldap-tacplus-cfg'] = serialize_Authentication__type_cfg__ldap_cfg__ldap_tacplus_cfg_json(obj.ldap_tacplus_cfg)
	return output

def serialize_Authentication__type_cfg__radius_cfg__radius_ldap_cfg_json(obj):
	output = OrderedDict()
	if obj.radius_ldap is not None:
		output['radius-ldap'] = obj.radius_ldap
	if obj.radius_ldap_local is not None:
		output['radius-ldap-local'] = obj.radius_ldap_local
	if obj.radius_ldap_local_tacplus is not None:
		output['radius-ldap-local-tacplus'] = obj.radius_ldap_local_tacplus
	if obj.radius_ldap_tacplus is not None:
		output['radius-ldap-tacplus'] = obj.radius_ldap_tacplus
	if obj.radius_ldap_tacplus_local is not None:
		output['radius-ldap-tacplus-local'] = obj.radius_ldap_tacplus_local
	return output

def serialize_Authentication__type_cfg__radius_cfg__radius_local_cfg_json(obj):
	output = OrderedDict()
	if obj.radius_local is not None:
		output['radius-local'] = obj.radius_local
	if obj.radius_local_ldap is not None:
		output['radius-local-ldap'] = obj.radius_local_ldap
	if obj.radius_local_ldap_tacplus is not None:
		output['radius-local-ldap-tacplus'] = obj.radius_local_ldap_tacplus
	if obj.radius_local_tacplus is not None:
		output['radius-local-tacplus'] = obj.radius_local_tacplus
	if obj.radius_local_tacplus_ldap is not None:
		output['radius-local-tacplus-ldap'] = obj.radius_local_tacplus_ldap
	return output

def serialize_Authentication__type_cfg__radius_cfg__radius_tacplus_cfg_json(obj):
	output = OrderedDict()
	if obj.radius_tacplus is not None:
		output['radius-tacplus'] = obj.radius_tacplus
	if obj.radius_tacplus_ldap is not None:
		output['radius-tacplus-ldap'] = obj.radius_tacplus_ldap
	if obj.radius_tacplus_ldap_local is not None:
		output['radius-tacplus-ldap-local'] = obj.radius_tacplus_ldap_local
	if obj.radius_tacplus_local is not None:
		output['radius-tacplus-local'] = obj.radius_tacplus_local
	if obj.radius_tacplus_local_ldap is not None:
		output['radius-tacplus-local-ldap'] = obj.radius_tacplus_local_ldap
	return output

def serialize_Authentication__type_cfg__radius_cfg_json(obj):
	output = OrderedDict()
	if obj.radius is not None:
		output['radius'] = obj.radius
	if obj.radius_ldap_cfg is not None:
		output['radius-ldap-cfg'] = serialize_Authentication__type_cfg__radius_cfg__radius_ldap_cfg_json(obj.radius_ldap_cfg)
	if obj.radius_local_cfg is not None:
		output['radius-local-cfg'] = serialize_Authentication__type_cfg__radius_cfg__radius_local_cfg_json(obj.radius_local_cfg)
	if obj.radius_tacplus_cfg is not None:
		output['radius-tacplus-cfg'] = serialize_Authentication__type_cfg__radius_cfg__radius_tacplus_cfg_json(obj.radius_tacplus_cfg)
	return output

def serialize_Authentication__type_cfg__local_cfg__local_ldap_cfg_json(obj):
	output = OrderedDict()
	if obj.local_ldap is not None:
		output['local-ldap'] = obj.local_ldap
	if obj.local_ldap_radius is not None:
		output['local-ldap-radius'] = obj.local_ldap_radius
	if obj.local_ldap_radius_tacplus is not None:
		output['local-ldap-radius-tacplus'] = obj.local_ldap_radius_tacplus
	if obj.local_ldap_tacplus is not None:
		output['local-ldap-tacplus'] = obj.local_ldap_tacplus
	if obj.local_ldap_tacplus_radius is not None:
		output['local-ldap-tacplus-radius'] = obj.local_ldap_tacplus_radius
	return output

def serialize_Authentication__type_cfg__local_cfg__local_radius_cfg_json(obj):
	output = OrderedDict()
	if obj.local_radius is not None:
		output['local-radius'] = obj.local_radius
	if obj.local_radius_ldap is not None:
		output['local-radius-ldap'] = obj.local_radius_ldap
	if obj.local_radius_ldap_tacplus is not None:
		output['local-radius-ldap-tacplus'] = obj.local_radius_ldap_tacplus
	if obj.local_radius_tacplus is not None:
		output['local-radius-tacplus'] = obj.local_radius_tacplus
	if obj.local_radius_tacplus_ldap is not None:
		output['local-radius-tacplus-ldap'] = obj.local_radius_tacplus_ldap
	return output

def serialize_Authentication__type_cfg__local_cfg__local_tacplus_cfg_json(obj):
	output = OrderedDict()
	if obj.local_tacplus is not None:
		output['local-tacplus'] = obj.local_tacplus
	if obj.local_tacplus_ldap is not None:
		output['local-tacplus-ldap'] = obj.local_tacplus_ldap
	if obj.local_tacplus_ldap_radius is not None:
		output['local-tacplus-ldap-radius'] = obj.local_tacplus_ldap_radius
	if obj.local_tacplus_radius is not None:
		output['local-tacplus-radius'] = obj.local_tacplus_radius
	if obj.local_tacplus_radius_ldap is not None:
		output['local-tacplus-radius-ldap'] = obj.local_tacplus_radius_ldap
	return output

def serialize_Authentication__type_cfg__local_cfg_json(obj):
	output = OrderedDict()
	if obj.local is not None:
		output['local'] = obj.local
	if obj.local_ldap_cfg is not None:
		output['local-ldap-cfg'] = serialize_Authentication__type_cfg__local_cfg__local_ldap_cfg_json(obj.local_ldap_cfg)
	if obj.local_radius_cfg is not None:
		output['local-radius-cfg'] = serialize_Authentication__type_cfg__local_cfg__local_radius_cfg_json(obj.local_radius_cfg)
	if obj.local_tacplus_cfg is not None:
		output['local-tacplus-cfg'] = serialize_Authentication__type_cfg__local_cfg__local_tacplus_cfg_json(obj.local_tacplus_cfg)
	return output

def serialize_Authentication__type_cfg__tacplus_cfg__tacplus_ldap_cfg_json(obj):
	output = OrderedDict()
	if obj.tacplus_ldap is not None:
		output['tacplus-ldap'] = obj.tacplus_ldap
	if obj.tacplus_ldap_radius is not None:
		output['tacplus-ldap-radius'] = obj.tacplus_ldap_radius
	if obj.tacplus_ldap_radius_local is not None:
		output['tacplus-ldap-radius-local'] = obj.tacplus_ldap_radius_local
	if obj.tacplus_ldap_local is not None:
		output['tacplus-ldap-local'] = obj.tacplus_ldap_local
	if obj.tacplus_ldap_local_radius is not None:
		output['tacplus-ldap-local-radius'] = obj.tacplus_ldap_local_radius
	return output

def serialize_Authentication__type_cfg__tacplus_cfg__tacplus_radius_cfg_json(obj):
	output = OrderedDict()
	if obj.tacplus_radius is not None:
		output['tacplus-radius'] = obj.tacplus_radius
	if obj.tacplus_radius_ldap is not None:
		output['tacplus-radius-ldap'] = obj.tacplus_radius_ldap
	if obj.tacplus_radius_ldap_local is not None:
		output['tacplus-radius-ldap-local'] = obj.tacplus_radius_ldap_local
	if obj.tacplus_radius_local is not None:
		output['tacplus-radius-local'] = obj.tacplus_radius_local
	if obj.tacplus_radius_local_ldap is not None:
		output['tacplus-radius-local-ldap'] = obj.tacplus_radius_local_ldap
	return output

def serialize_Authentication__type_cfg__tacplus_cfg__tacplus_local_cfg_json(obj):
	output = OrderedDict()
	if obj.tacplus_local is not None:
		output['tacplus-local'] = obj.tacplus_local
	if obj.tacplus_local_ldap is not None:
		output['tacplus-local-ldap'] = obj.tacplus_local_ldap
	if obj.tacplus_local_ldap_radius is not None:
		output['tacplus-local-ldap-radius'] = obj.tacplus_local_ldap_radius
	if obj.tacplus_local_radius is not None:
		output['tacplus-local-radius'] = obj.tacplus_local_radius
	if obj.tacplus_local_radius_ldap is not None:
		output['tacplus-local-radius-ldap'] = obj.tacplus_local_radius_ldap
	return output

def serialize_Authentication__type_cfg__tacplus_cfg_json(obj):
	output = OrderedDict()
	if obj.tacplus is not None:
		output['tacplus'] = obj.tacplus
	if obj.tacplus_ldap_cfg is not None:
		output['tacplus-ldap-cfg'] = serialize_Authentication__type_cfg__tacplus_cfg__tacplus_ldap_cfg_json(obj.tacplus_ldap_cfg)
	if obj.tacplus_radius_cfg is not None:
		output['tacplus-radius-cfg'] = serialize_Authentication__type_cfg__tacplus_cfg__tacplus_radius_cfg_json(obj.tacplus_radius_cfg)
	if obj.tacplus_local_cfg is not None:
		output['tacplus-local-cfg'] = serialize_Authentication__type_cfg__tacplus_cfg__tacplus_local_cfg_json(obj.tacplus_local_cfg)
	return output

def serialize_Authentication__type_cfg_json(obj):
	output = OrderedDict()
	if obj.type is not None:
		output['type'] = obj.type
	if obj.ldap_cfg is not None:
		output['ldap-cfg'] = serialize_Authentication__type_cfg__ldap_cfg_json(obj.ldap_cfg)
	if obj.radius_cfg is not None:
		output['radius-cfg'] = serialize_Authentication__type_cfg__radius_cfg_json(obj.radius_cfg)
	if obj.local_cfg is not None:
		output['local-cfg'] = serialize_Authentication__type_cfg__local_cfg_json(obj.local_cfg)
	if obj.tacplus_cfg is not None:
		output['tacplus-cfg'] = serialize_Authentication__type_cfg__tacplus_cfg_json(obj.tacplus_cfg)
	return output

def serialize_Authentication__enable_cfg__enable_local_cfg_json(obj):
	output = OrderedDict()
	if obj.enable_local is not None:
		output['enable-local'] = obj.enable_local
	if obj.enable_local_tacplus is not None:
		output['enable-local-tacplus'] = obj.enable_local_tacplus
	return output

def serialize_Authentication__enable_cfg__enable_tacplus_cfg_json(obj):
	output = OrderedDict()
	if obj.enable_tacplus is not None:
		output['enable-tacplus'] = obj.enable_tacplus
	if obj.enable_tacplus_local is not None:
		output['enable-tacplus-local'] = obj.enable_tacplus_local
	return output

def serialize_Authentication__enable_cfg_json(obj):
	output = OrderedDict()
	if obj.enable is not None:
		output['enable'] = obj.enable
	if obj.enable_local_cfg is not None:
		output['enable-local-cfg'] = serialize_Authentication__enable_cfg__enable_local_cfg_json(obj.enable_local_cfg)
	if obj.enable_tacplus_cfg is not None:
		output['enable-tacplus-cfg'] = serialize_Authentication__enable_cfg__enable_tacplus_cfg_json(obj.enable_tacplus_cfg)
	return output

def serialize_Authentication__login_cfg_json(obj):
	output = OrderedDict()
	if obj.login is not None:
		output['login'] = obj.login
	if obj.privilege_mode is not None:
		output['privilege-mode'] = obj.privilege_mode
	if obj.local is not None:
		output['local'] = obj.local
	return output

def serialize_Authentication__mode_cfg_json(obj):
	output = OrderedDict()
	if obj.mode is not None:
		output['mode'] = obj.mode
	if obj.multiple is not None:
		output['multiple'] = obj.multiple
	if obj.single is not None:
		output['single'] = obj.single
	return output

def serialize_Authentication__console__type_cfg_json(obj):
	output = OrderedDict()
	if obj.type is not None:
		output['type'] = obj.type
	if obj.ldap is not None:
		output['ldap'] = obj.ldap
	if obj.local is not None:
		output['local'] = obj.local
	if obj.radius is not None:
		output['radius'] = obj.radius
	if obj.tacplus is not None:
		output['tacplus'] = obj.tacplus
	return output

def serialize_Authentication__console_json(obj):
	output = OrderedDict()
	if obj.type_cfg is not None:
		output['type-cfg'] = serialize_Authentication__console__type_cfg_json(obj.type_cfg)
	return output

def serialize_Authentication_json(obj):
	output = OrderedDict()
	if obj.type_cfg is not None:
		output['type-cfg'] = serialize_Authentication__type_cfg_json(obj.type_cfg)
	if obj.disable_local is not None:
		output['disable-local'] = obj.disable_local
	if obj.enable_cfg is not None:
		output['enable-cfg'] = serialize_Authentication__enable_cfg_json(obj.enable_cfg)
	if obj.login_cfg is not None:
		output['login-cfg'] = serialize_Authentication__login_cfg_json(obj.login_cfg)
	if obj.mode_cfg is not None:
		output['mode-cfg'] = serialize_Authentication__mode_cfg_json(obj.mode_cfg)
	if obj.multiple_auth_reject is not None:
		output['multiple-auth-reject'] = obj.multiple_auth_reject
	if obj.console is not None:
		output['console'] = serialize_Authentication__console_json(obj.console)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_Authentication_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_Authentication_json(item))
	return list(container)

class Authentication__type_cfg__ldap_cfg__ldap_local_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ldap_local=PosRangedInteger(0, 1)
	ldap_local_radius=PosRangedInteger(0, 1)
	ldap_local_radius_tacplus=PosRangedInteger(0, 1)
	ldap_local_tacplus=PosRangedInteger(0, 1)
	ldap_local_tacplus_radius=PosRangedInteger(0, 1)
	def __init__(self, ldap_local=None, ldap_local_radius=None, ldap_local_radius_tacplus=None, ldap_local_tacplus=None, ldap_local_tacplus_radius=None):
		self.ldap_local = ldap_local
		self.ldap_local_radius = ldap_local_radius
		self.ldap_local_radius_tacplus = ldap_local_radius_tacplus
		self.ldap_local_tacplus = ldap_local_tacplus
		self.ldap_local_tacplus_radius = ldap_local_tacplus_radius

	def __str__(self):
		return ""

class Authentication__type_cfg__ldap_cfg__ldap_radius_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ldap_radius=PosRangedInteger(0, 1)
	ldap_radius_local=PosRangedInteger(0, 1)
	ldap_radius_local_tacplus=PosRangedInteger(0, 1)
	ldap_radius_tacplus=PosRangedInteger(0, 1)
	ldap_radius_tacplus_local=PosRangedInteger(0, 1)
	def __init__(self, ldap_radius=None, ldap_radius_local=None, ldap_radius_local_tacplus=None, ldap_radius_tacplus=None, ldap_radius_tacplus_local=None):
		self.ldap_radius = ldap_radius
		self.ldap_radius_local = ldap_radius_local
		self.ldap_radius_local_tacplus = ldap_radius_local_tacplus
		self.ldap_radius_tacplus = ldap_radius_tacplus
		self.ldap_radius_tacplus_local = ldap_radius_tacplus_local

	def __str__(self):
		return ""

class Authentication__type_cfg__ldap_cfg__ldap_tacplus_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ldap_tacplus=PosRangedInteger(0, 1)
	ldap_tacplus_local=PosRangedInteger(0, 1)
	ldap_tacplus_local_radius=PosRangedInteger(0, 1)
	ldap_tacplus_radius=PosRangedInteger(0, 1)
	ldap_tacplus_radius_local=PosRangedInteger(0, 1)
	def __init__(self, ldap_tacplus=None, ldap_tacplus_local=None, ldap_tacplus_local_radius=None, ldap_tacplus_radius=None, ldap_tacplus_radius_local=None):
		self.ldap_tacplus = ldap_tacplus
		self.ldap_tacplus_local = ldap_tacplus_local
		self.ldap_tacplus_local_radius = ldap_tacplus_local_radius
		self.ldap_tacplus_radius = ldap_tacplus_radius
		self.ldap_tacplus_radius_local = ldap_tacplus_radius_local

	def __str__(self):
		return ""

class Authentication__type_cfg__ldap_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	ldap=PosRangedInteger(0, 1)
	def __init__(self, ldap=None, ldap_local_cfg=None, ldap_radius_cfg=None, ldap_tacplus_cfg=None):
		self.ldap = ldap
		self.ldap_local_cfg = ldap_local_cfg
		self.ldap_radius_cfg = ldap_radius_cfg
		self.ldap_tacplus_cfg = ldap_tacplus_cfg

	def __str__(self):
		return ""

class Authentication__type_cfg__radius_cfg__radius_ldap_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	radius_ldap=PosRangedInteger(0, 1)
	radius_ldap_local=PosRangedInteger(0, 1)
	radius_ldap_local_tacplus=PosRangedInteger(0, 1)
	radius_ldap_tacplus=PosRangedInteger(0, 1)
	radius_ldap_tacplus_local=PosRangedInteger(0, 1)
	def __init__(self, radius_ldap=None, radius_ldap_local=None, radius_ldap_local_tacplus=None, radius_ldap_tacplus=None, radius_ldap_tacplus_local=None):
		self.radius_ldap = radius_ldap
		self.radius_ldap_local = radius_ldap_local
		self.radius_ldap_local_tacplus = radius_ldap_local_tacplus
		self.radius_ldap_tacplus = radius_ldap_tacplus
		self.radius_ldap_tacplus_local = radius_ldap_tacplus_local

	def __str__(self):
		return ""

class Authentication__type_cfg__radius_cfg__radius_local_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	radius_local=PosRangedInteger(0, 1)
	radius_local_ldap=PosRangedInteger(0, 1)
	radius_local_ldap_tacplus=PosRangedInteger(0, 1)
	radius_local_tacplus=PosRangedInteger(0, 1)
	radius_local_tacplus_ldap=PosRangedInteger(0, 1)
	def __init__(self, radius_local=None, radius_local_ldap=None, radius_local_ldap_tacplus=None, radius_local_tacplus=None, radius_local_tacplus_ldap=None):
		self.radius_local = radius_local
		self.radius_local_ldap = radius_local_ldap
		self.radius_local_ldap_tacplus = radius_local_ldap_tacplus
		self.radius_local_tacplus = radius_local_tacplus
		self.radius_local_tacplus_ldap = radius_local_tacplus_ldap

	def __str__(self):
		return ""

class Authentication__type_cfg__radius_cfg__radius_tacplus_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	radius_tacplus=PosRangedInteger(0, 1)
	radius_tacplus_ldap=PosRangedInteger(0, 1)
	radius_tacplus_ldap_local=PosRangedInteger(0, 1)
	radius_tacplus_local=PosRangedInteger(0, 1)
	radius_tacplus_local_ldap=PosRangedInteger(0, 1)
	def __init__(self, radius_tacplus=None, radius_tacplus_ldap=None, radius_tacplus_ldap_local=None, radius_tacplus_local=None, radius_tacplus_local_ldap=None):
		self.radius_tacplus = radius_tacplus
		self.radius_tacplus_ldap = radius_tacplus_ldap
		self.radius_tacplus_ldap_local = radius_tacplus_ldap_local
		self.radius_tacplus_local = radius_tacplus_local
		self.radius_tacplus_local_ldap = radius_tacplus_local_ldap

	def __str__(self):
		return ""

class Authentication__type_cfg__radius_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	radius=PosRangedInteger(0, 1)
	def __init__(self, radius=None, radius_ldap_cfg=None, radius_local_cfg=None, radius_tacplus_cfg=None):
		self.radius = radius
		self.radius_ldap_cfg = radius_ldap_cfg
		self.radius_local_cfg = radius_local_cfg
		self.radius_tacplus_cfg = radius_tacplus_cfg

	def __str__(self):
		return ""

class Authentication__type_cfg__local_cfg__local_ldap_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	local_ldap=PosRangedInteger(0, 1)
	local_ldap_radius=PosRangedInteger(0, 1)
	local_ldap_radius_tacplus=PosRangedInteger(0, 1)
	local_ldap_tacplus=PosRangedInteger(0, 1)
	local_ldap_tacplus_radius=PosRangedInteger(0, 1)
	def __init__(self, local_ldap=None, local_ldap_radius=None, local_ldap_radius_tacplus=None, local_ldap_tacplus=None, local_ldap_tacplus_radius=None):
		self.local_ldap = local_ldap
		self.local_ldap_radius = local_ldap_radius
		self.local_ldap_radius_tacplus = local_ldap_radius_tacplus
		self.local_ldap_tacplus = local_ldap_tacplus
		self.local_ldap_tacplus_radius = local_ldap_tacplus_radius

	def __str__(self):
		return ""

class Authentication__type_cfg__local_cfg__local_radius_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	local_radius=PosRangedInteger(0, 1)
	local_radius_ldap=PosRangedInteger(0, 1)
	local_radius_ldap_tacplus=PosRangedInteger(0, 1)
	local_radius_tacplus=PosRangedInteger(0, 1)
	local_radius_tacplus_ldap=PosRangedInteger(0, 1)
	def __init__(self, local_radius=None, local_radius_ldap=None, local_radius_ldap_tacplus=None, local_radius_tacplus=None, local_radius_tacplus_ldap=None):
		self.local_radius = local_radius
		self.local_radius_ldap = local_radius_ldap
		self.local_radius_ldap_tacplus = local_radius_ldap_tacplus
		self.local_radius_tacplus = local_radius_tacplus
		self.local_radius_tacplus_ldap = local_radius_tacplus_ldap

	def __str__(self):
		return ""

class Authentication__type_cfg__local_cfg__local_tacplus_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	local_tacplus=PosRangedInteger(0, 1)
	local_tacplus_ldap=PosRangedInteger(0, 1)
	local_tacplus_ldap_radius=PosRangedInteger(0, 1)
	local_tacplus_radius=PosRangedInteger(0, 1)
	local_tacplus_radius_ldap=PosRangedInteger(0, 1)
	def __init__(self, local_tacplus=None, local_tacplus_ldap=None, local_tacplus_ldap_radius=None, local_tacplus_radius=None, local_tacplus_radius_ldap=None):
		self.local_tacplus = local_tacplus
		self.local_tacplus_ldap = local_tacplus_ldap
		self.local_tacplus_ldap_radius = local_tacplus_ldap_radius
		self.local_tacplus_radius = local_tacplus_radius
		self.local_tacplus_radius_ldap = local_tacplus_radius_ldap

	def __str__(self):
		return ""

class Authentication__type_cfg__local_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	local=PosRangedInteger(0, 1)
	def __init__(self, local=None, local_ldap_cfg=None, local_radius_cfg=None, local_tacplus_cfg=None):
		self.local = local
		self.local_ldap_cfg = local_ldap_cfg
		self.local_radius_cfg = local_radius_cfg
		self.local_tacplus_cfg = local_tacplus_cfg

	def __str__(self):
		return ""

class Authentication__type_cfg__tacplus_cfg__tacplus_ldap_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tacplus_ldap=PosRangedInteger(0, 1)
	tacplus_ldap_radius=PosRangedInteger(0, 1)
	tacplus_ldap_radius_local=PosRangedInteger(0, 1)
	tacplus_ldap_local=PosRangedInteger(0, 1)
	tacplus_ldap_local_radius=PosRangedInteger(0, 1)
	def __init__(self, tacplus_ldap=None, tacplus_ldap_radius=None, tacplus_ldap_radius_local=None, tacplus_ldap_local=None, tacplus_ldap_local_radius=None):
		self.tacplus_ldap = tacplus_ldap
		self.tacplus_ldap_radius = tacplus_ldap_radius
		self.tacplus_ldap_radius_local = tacplus_ldap_radius_local
		self.tacplus_ldap_local = tacplus_ldap_local
		self.tacplus_ldap_local_radius = tacplus_ldap_local_radius

	def __str__(self):
		return ""

class Authentication__type_cfg__tacplus_cfg__tacplus_radius_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tacplus_radius=PosRangedInteger(0, 1)
	tacplus_radius_ldap=PosRangedInteger(0, 1)
	tacplus_radius_ldap_local=PosRangedInteger(0, 1)
	tacplus_radius_local=PosRangedInteger(0, 1)
	tacplus_radius_local_ldap=PosRangedInteger(0, 1)
	def __init__(self, tacplus_radius=None, tacplus_radius_ldap=None, tacplus_radius_ldap_local=None, tacplus_radius_local=None, tacplus_radius_local_ldap=None):
		self.tacplus_radius = tacplus_radius
		self.tacplus_radius_ldap = tacplus_radius_ldap
		self.tacplus_radius_ldap_local = tacplus_radius_ldap_local
		self.tacplus_radius_local = tacplus_radius_local
		self.tacplus_radius_local_ldap = tacplus_radius_local_ldap

	def __str__(self):
		return ""

class Authentication__type_cfg__tacplus_cfg__tacplus_local_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tacplus_local=PosRangedInteger(0, 1)
	tacplus_local_ldap=PosRangedInteger(0, 1)
	tacplus_local_ldap_radius=PosRangedInteger(0, 1)
	tacplus_local_radius=PosRangedInteger(0, 1)
	tacplus_local_radius_ldap=PosRangedInteger(0, 1)
	def __init__(self, tacplus_local=None, tacplus_local_ldap=None, tacplus_local_ldap_radius=None, tacplus_local_radius=None, tacplus_local_radius_ldap=None):
		self.tacplus_local = tacplus_local
		self.tacplus_local_ldap = tacplus_local_ldap
		self.tacplus_local_ldap_radius = tacplus_local_ldap_radius
		self.tacplus_local_radius = tacplus_local_radius
		self.tacplus_local_radius_ldap = tacplus_local_radius_ldap

	def __str__(self):
		return ""

class Authentication__type_cfg__tacplus_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	tacplus=PosRangedInteger(0, 1)
	def __init__(self, tacplus=None, tacplus_ldap_cfg=None, tacplus_radius_cfg=None, tacplus_local_cfg=None):
		self.tacplus = tacplus
		self.tacplus_ldap_cfg = tacplus_ldap_cfg
		self.tacplus_radius_cfg = tacplus_radius_cfg
		self.tacplus_local_cfg = tacplus_local_cfg

	def __str__(self):
		return ""

class Authentication__type_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	type=PosRangedInteger(0, 1)
	def __init__(self, type=None, ldap_cfg=None, radius_cfg=None, local_cfg=None, tacplus_cfg=None):
		self.type = type
		self.ldap_cfg = ldap_cfg
		self.radius_cfg = radius_cfg
		self.local_cfg = local_cfg
		self.tacplus_cfg = tacplus_cfg

	def __str__(self):
		return ""

class Authentication__enable_cfg__enable_local_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	enable_local=PosRangedInteger(0, 1)
	enable_local_tacplus=PosRangedInteger(0, 1)
	def __init__(self, enable_local=None, enable_local_tacplus=None):
		self.enable_local = enable_local
		self.enable_local_tacplus = enable_local_tacplus

	def __str__(self):
		return ""

class Authentication__enable_cfg__enable_tacplus_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	enable_tacplus=PosRangedInteger(0, 1)
	enable_tacplus_local=PosRangedInteger(0, 1)
	def __init__(self, enable_tacplus=None, enable_tacplus_local=None):
		self.enable_tacplus = enable_tacplus
		self.enable_tacplus_local = enable_tacplus_local

	def __str__(self):
		return ""

class Authentication__enable_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	enable=PosRangedInteger(0, 1)
	def __init__(self, enable=None, enable_local_cfg=None, enable_tacplus_cfg=None):
		self.enable = enable
		self.enable_local_cfg = enable_local_cfg
		self.enable_tacplus_cfg = enable_tacplus_cfg

	def __str__(self):
		return ""

class Authentication__login_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	login=PosRangedInteger(0, 1)
	privilege_mode=PosRangedInteger(0, 1)
	local=PosInteger()
	def __init__(self, login=None, privilege_mode=None, local=None):
		self.login = login
		self.privilege_mode = privilege_mode
		self.local = local

	def __str__(self):
		return ""

class Authentication__mode_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	mode=PosRangedInteger(0, 1)
	multiple=PosRangedInteger(0, 1)
	single=PosRangedInteger(0, 1)
	def __init__(self, mode=None, multiple=None, single=None):
		self.mode = mode
		self.multiple = multiple
		self.single = single

	def __str__(self):
		return ""

class Authentication__console__type_cfg(AxapiObject):
	__metaclass__ = StructMeta 
	type=PosRangedInteger(0, 1)
	ldap=PosRangedInteger(0, 1)
	local=PosRangedInteger(0, 1)
	radius=PosRangedInteger(0, 1)
	tacplus=PosRangedInteger(0, 1)
	def __init__(self, type=None, ldap=None, local=None, radius=None, tacplus=None):
		self.type = type
		self.ldap = ldap
		self.local = local
		self.radius = radius
		self.tacplus = tacplus

	def __str__(self):
		return ""

class Authentication__console(AxapiObject):
	__metaclass__ = StructMeta 
	def __init__(self, type_cfg=None):
		self.type_cfg = type_cfg

	def __str__(self):
		return ""

class Authentication(AxapiObject):
	__metaclass__ = StructMeta 
	disable_local=PosRangedInteger(0, 1)
	multiple_auth_reject=PosRangedInteger(0, 1)
	def __init__(self, type_cfg=None, disable_local=None, enable_cfg=None, login_cfg=None, mode_cfg=None, multiple_auth_reject=None, console=None):
		self.type_cfg = type_cfg
		self.disable_local = disable_local
		self.enable_cfg = enable_cfg
		self.login_cfg = login_cfg
		self.mode_cfg = mode_cfg
		self.multiple_auth_reject = multiple_auth_reject
		self.console = console

	def __str__(self):
		return ""

class AuthenticationClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getAuthentication(self):
		"""
		Retrieve the authentication identified by the specified identifier
		
		Returns:
			An instance of the Authentication class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified authentication does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('authentication')
		return deserialize_Authentication_json(payload)

	def putAuthentication(self, authentication):
		"""
		Replace the object authentication
		
		Args:
			authentication An instance of the Authentication class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['authentication']=serialize_Authentication_json(authentication)
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

	def deleteAuthentication(self):
		"""
		Remove the authentication identified by the specified identifier from the
		system
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified authentication does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllAuthenticationsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitAuthentication(self, authentication):
		"""
		Create the object authentication
		
		Args:
			authentication An instance of the Authentication class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['authentication']=serialize_Authentication_json(authentication)
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

	def getAllAuthentications(self):
		"""
		Retrieve all authentication objects currently pending in the system
		
		Returns:
			A list of Authentication objects
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
			payload= data.get('authenticationList')
		return deserialize_list_Authentication_json(payload)

