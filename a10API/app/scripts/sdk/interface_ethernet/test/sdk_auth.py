import sys
from urlparse import urlparse
import httplib
import json
import urllib

BASE_URL = [
  'http://axapi.a10networks.com/axapi/v3',
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
  auth_uri = data.get('auth_uri')
  username = data.get('username')
  password = data.get('password')
  result = AuthorizationSchema(code=code, error=error, auth_uri=auth_uri, username=username, password=password)
  return result

def serialize_Credentials_json(obj):
  output = dict()
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

class RemoteException(Exception):
  def __init__(self, status, cause, details):
    Exception.__init__(self, cause)
    self.status = status
    self.details = details

class AbstractResourceClient:
  def __init__(self, endpoint, debug):
    if endpoint is not None:
      self.endpoint = endpoint
    else:
      self.endpoint = BASE_URL[0]
    self.debug = debug

  def get_connection(self):
    result = urlparse(self.endpoint)
    ssl = result.scheme == 'https'
    if ssl:
      conn = httplib.HTTPSConnection(result.netloc)
    else:
      conn = httplib.HTTPConnection(result.netloc)
    if self.debug:
      conn.set_debuglevel(1)
    return conn

  def get_path(self):
    result = urlparse(BASE_URL[0])
    return result.path

  def get_output(self, response, expected, errors):
    status = response.status
    payload = response.read()
    if not errors and errors.has_key(status):
      raise RemoteException(status, errors[status], payload)
    elif status != expected:
      raise RemoteException(status, 'Unexpected return status: ' + str(status), payload)
    return payload

class AuthorizationSchema:
  def __init__(self, code, error, auth_uri, username, password):
    self.code = code
    self.error = error
    self.auth_uri = auth_uri
    self.username = username
    self.password = password

class Credentials:
  def __init__(self, username, password):
    self.username = username
    self.password = password

class AuthResponse:
  def __init__(self, signature, description):
    self.signature = signature
    self.description = description

class AuthorizationschemaClient(AbstractResourceClient):
  def __init__(self, endpoint=None, debug=False):
    AbstractResourceClient.__init__(self, endpoint, debug)

  def getAuthorizationSchema(self):
    """
    Retrieve the authorization schema from AX
    
    Returns:
      An instance of the AuthorizationSchema class
    """
    query = ''
    conn = self.get_connection()
    conn.request('GET', self.get_path() + '/' + query)
    response = conn.getresponse()
    expected_status = 401
    errors = {500: 'An unexpected runtime exception', 403: 'Specified authorization does not exist'}
    payload = self.get_output(response, expected_status, errors)
    conn.close()
    if self.debug:
      print 'payload:', payload
    return deserialize_AuthorizationSchema_json(payload)

class AuthorizationClient(AbstractResourceClient):
  def __init__(self, endpoint=None, debug=False):
    AbstractResourceClient.__init__(self, endpoint, debug)

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
    headers = { 'Content-type' : 'application/json' }
    output=dict()
    output=serialize_Credentials_json(credentials)
    payload = serialize_final_json(output)
    conn.request('POST', self.endpoint + query, payload, headers)
    response = conn.getresponse()
    expected_status = 200
    errors = {500: 'An unexpected runtime exception'}
    payload = self.get_output(response, expected_status, errors)
    conn.close()
    if self.debug:
      print 'payload:', payload
    return deserialize_AuthResponse_json(payload)

