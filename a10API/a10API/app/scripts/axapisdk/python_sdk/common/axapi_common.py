import sys
from urlparse import urlparse
from collections import OrderedDict
import httplib
import urllib
import re
from abc import ABCMeta, abstractmethod


class Path(object):
    __metaclass__ = ABCMeta
    @staticmethod
    @abstractmethod
    def getUrl():
        return 'https://axapi.a10networks.com/'

class RemoteException(Exception):
        def __init__(self, status, cause, details):
                self.status = status
                self.details = details
                Exception.__init__(self, cause, details)

class AxapiObject(object):
        pass

class StructMeta(type):
        def __prepare__(cls, name, bases=None):
                        return OrderedDict()

        def __new__(cls, name, bases, clsdict):
                        fields = [key for key, val in clsdict.items()
                                                                if isinstance(val, Descriptor)]
                        for field_name in fields:
                                clsdict[field_name].name = field_name
                        clsobj = type.__new__(cls, name, bases, dict(clsdict))
                        setattr(clsobj, '_fields', fields)
                        return clsobj

class Descriptor(object):
        def __init__(self, name=None):
                        self.name = name

        def __get__(self, instance, cls):
                        if instance is None:
                                return self
                        elif instance.__dict__.has_key(self.name):
                                return instance.__dict__[self.name]

        def __set__(self, instance, value):
                        instance.__dict__[self.name] = value

        def __delete__(self, instance):
                         del instance.__dict__[self.name]

class Typed(Descriptor):
        def __init__(self, *args, **kwargs):
                        self.as_super = super(Typed, self)
                        self.as_super.__init__(*args, **kwargs)
        def __set__(self, instance, value):
                        if not isinstance(value, type(None)):
                                if isinstance(value, unicode):
                                        value = str(value)
                                if not (isinstance(value, self.ty) or isinstance(value, type(None))):
                                        raise TypeError('Expected %s' % self.ty)
                        #super(Typed,self).__set__(instance, value)
                        self.as_super.__set__(instance, value)

class Sized(Descriptor):
        def __init__(self, minlen, maxlen, *args, **kwargs):
                        self.minlen = minlen
                        self.maxlen = maxlen
                        self.as_super = super(Sized, self)
                        self.as_super.__init__(*args, **kwargs)

        def __set__(self, instance, value):
                        if not isinstance(value, type(None)):
                                if len(value) > self.maxlen:
                                        raise ValueError('Size must be <= ' + str(self.maxlen) )
                                if len(value) < self.minlen:
                                        raise ValueError('Size must be >= ' +  str(self.minlen) )
                        #super(Sized, self).__set__(instance,value)
                        self.as_super.__set__(instance, value)

class Ranged(Descriptor):
        def __init__(self, minimum, maximum, *args, **kwargs):
                        self.minimum = minimum
                        self.maximum = maximum
                        self.as_super = super(Ranged, self)
                        self.as_super.__init__(*args, **kwargs)

        def __set__(self, instance, value):
                        if not isinstance(value, type(None)):
                                if value <  self.minimum :
                                        raise ValueError('Value must be >= ' +  str(self.minimum) )
                                if value >  self.maximum :
                                        raise ValueError('Value must be <= ' + str(self.maximum) )
                        #super(Ranged,self).__set__(instance, value)
                        self.as_super.__set__(instance, value)

class Positive(Descriptor):
        def __init__(self, *args, **kwargs):
                        self.as_super = super(Positive, self)
                        self.as_super.__init__(*args, **kwargs)
        def __set__(self, instance, value):
                        if not isinstance(value, type(None)):
                                if value <  0 :
                                        raise ValueError('Expected >= 0')
                        #super(Positive,self).__set__(instance, value)
                        self.as_super.__set__(instance, value)

class Enum(Descriptor):
        def __init__(self, enumlist, *args, **kwargs):
                        self.as_super = super(Enum, self)
                        self.as_super.__init__(*args, **kwargs)
                        self.enumlist = enumlist

        def __set__(self, instance, value):
                        if not isinstance(value, type(None)):
                                if value not in  self.enumlist:
                                        raise ValueError(str(value) + ' not in the allowed list ' +  str(self.enumlist) )
                        #super(Enum,self).__set__(instance, value)
                        self.as_super.__set__(instance, value)


class Regex(Descriptor):
        def __init__(self, pat, *args, **kwargs):
                self.as_super = super(Regex, self)
                self.as_super.__init__(*args, **kwargs)
                if not isinstance(pat, type(None)):
                        self.pat = re.compile(pat)
                        super(Regex,self).__init__(*args, **kwargs)

        def __set__(self, instance, value):
                if not isinstance(value, type(None)):
                        if not self.pat.match(value):
                                raise ValueError('Invalid string value')
                #super(Regex,self).__set__(instance, value)
                self.as_super.__set__(instance, value)

class String(Typed):
        ty=str
        pass

class Integer(Typed):
        ty=int
        pass

class Float(Typed):
        ty=float
        pass

class PosInteger(Integer,Positive):
        pass

class PosRangedInteger(Integer,Positive,Ranged):
        pass

class PosFloat(Float,Positive):
        pass

class SizedString(String,Sized):
        pass

class RegexString(String,Regex):
        pass

class SizedRegexString(String,Sized,Regex):
        pass

class AbstractResourceClient(AxapiObject):
        __metaclass__ = StructMeta
        def __init__(self, endpoint, sessionid, debug):
                pat = r'(?P<ipaddr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                try:
                        regex = re.compile(pat, re.VERBOSE)
                        result = regex.finditer(endpoint)
                        _it = iter(result)
                        if _it is not None:
                                val = next(_it)
                except StopIteration:
                        raise RemoteException(400, "No IP address is given to the endpoint or BASE_URL", endpoint)
                self.endpoint = endpoint
                self.sessionid = sessionid
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
                result = urlparse(self.endpoint)
                return result.path

        def get_output(self, response, expected, errors):
                status = response.status
                payload = response.read()
                if not errors and errors.has_key(status):
                        raise RemoteException(status, errors[status], payload)
                elif status != expected:
                        raise RemoteException(status, 'Unexpected return status: ' + str(status), payload)
                return payload


