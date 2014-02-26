
################################################################################
# File name: sdk_auth.py
# Copyright(C) 2007-2013, A10 Networks Inc. All rights reserved.
# Software for all A10 products contain trade secrets and confidential
# information of A10 Networks and its subsidiaries and may not be
# disclosed, copied, reproduced or distributed to anyone outside of
# A10 Networks without prior written consent of A10 Networks, Inc.
################################################################################
import sys
import json
sys.path.append("../common")
from axapi_common import *

BASE_URL = [
    'https://axapi.a10networks.com/',
]

def deserialize_AuthorizationSchema_json(obj):
    if obj is None:
        return None
    if isinstance(obj, dict):
        data = obj
    else:
        data = json.loads(obj)
    code = data.get('code')
    error = data.get('error')
    auth_uri = data.get('auth-uri')
    username = data.get('username')
    password = data.get('password')
    result = AuthorizationSchema(code=code, error=error, auth_uri=auth_uri, username=username, password=password)
    return result

def serialize_Credentials_json(obj):
    output = OrderedDict()
    output['username'] = obj.username
    output['password'] = obj.password
    return output

def serialize_final_json(obj):
    return json.dumps(obj)

def deserialize_AuthResponse_json(obj):
    if obj is None:
        return None
    if isinstance(obj, dict):
        data = obj
    else:
        data = json.loads(obj)
    signature = data.get('signature')
    description = data.get('description')
    result = AuthResponse(signature=signature, description=description)
    return result

class AuthorizationSchema(AxapiObject):
    __metaclass__ = StructMeta
    error=String()
    auth_uri=String()
    username=String()
    password=String()
    def __init__(self, code, error, auth_uri, username, password):
        self.code = code
        self.error = error
        self.auth_uri = auth_uri
        self.username = username
        self.password = password

class Credentials(AxapiObject):
    __metaclass__ = StructMeta
    username=String()
    password=String()
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthResponse(AxapiObject):
    __metaclass__ = StructMeta
    signature=String()
    description=String()
    def __init__(self, signature, description):
        self.signature = signature
        self.description = description

class AuthorizationschemaClient(AbstractResourceClient):
    def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
        if not endpoint:
            if ipaddress:
                result = urlparse(BASE_URL[0])
                endpoint = result.scheme + '://' + ipaddress + result.path
        AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

    def getAuthorizationSchema(self):
        """
        Retrieve the authorization schema from AX

        Returns:
            An instance of the AuthorizationSchema class
        """
        query = ''
        conn = self.get_connection()
        headers = { 'Content-type' : 'application/json'}
        conn.request('GET', self.get_path() + '/' + query, headers=headers)
        response = conn.getresponse()
        expected_status = 401
        errors = {500: 'An unexpected runtime exception', 404: 'Specified authorization does not exist'}
        payload = self.get_output(response, expected_status, errors)
        conn.close()
        if self.debug:
            print 'payload:', payload
        data = json.loads(payload)
        payload= data.get('authorizationschema')
        return deserialize_AuthorizationSchema_json(payload)

class AuthorizationClient(AbstractResourceClient):
    def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
        if not endpoint:
            if ipaddress:
                result = urlparse(BASE_URL[0])
                endpoint = result.scheme + '://' + ipaddress + result.path
        AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

    def submitCredentials(self, credentials):
        """
        Submit the Authorization Credentials

        Args:
            credentials An instance of the Credentials class

        Returns:
            An instance of the AuthResponse class
        """
        query = ''
        conn = self.get_connection()
        headers = { 'Content-type' : 'application/json'}
        output=OrderedDict()
        output['credentials']=serialize_Credentials_json(credentials)
        payload = serialize_final_json(output)
        conn.request('POST', self.get_path() + '/auth' + query, payload, headers)
        response = conn.getresponse()
        expected_status = 200
        errors = {500: 'An unexpected runtime exception'}
        payload = self.get_output(response, expected_status, errors)
        conn.close()
        if self.debug:
            print 'payload:', payload
        data = json.loads(payload)
        payload= data.get('authresponse')
        self.authresponse = deserialize_AuthResponse_json(payload)
        return self.authresponse

    def submitlogoff(self, credentials):
        """
        Submit the Authorization Credentials

        Args:
            credentials An instance of the Credentials class

        Returns:
            An instance of the AuthResponse class
        """
        query = ''
        conn = self.get_connection()
        headers = {'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.authresponse.signature}
        output=OrderedDict()
        output['credentials']=serialize_Credentials_json(credentials)
        payload = serialize_final_json(output)
        conn.request('POST', self.get_path() + '/logoff' + query, payload, headers)
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
            payload= data.get('authresponse')
        return deserialize_AuthResponse_json(payload)

