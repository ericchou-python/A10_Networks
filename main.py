
import method_call
from  base import AxError, AxAPI
import urllib2
from slb import ServiceGroup, ServiceGroupStats
from slb import RealServer, RealServerStats
from slb import VirtualServer, VirtualServerStats
from slb_template import *
from system import *
from gslb import *
from network import *


axapi_239 = method_call.AxApiContext("192.168.210.239", "user1", "aa&bb").authentication()
print axapi_239
#status = method_call.axapi_authentication()
#print method_call.AXAPI_SESSION_ID

intf = Interface()
intf.get(2)

#ints = Interface.getAll()
#for e in ints:
#    print e
                    
                    

caches = TemplateCache.getAll()
for e in caches:
    print e
    print e.dump()
    
cache1 = TemplateCache(name="my_cache_templ1")
cache1.policy_list = [{"uri": "abc", "action": 1}, {"uri": "123", "action": 1}]

cache1.create()

ntp1 = SystemNtp(server="2.2.2.2", status=0)
ntp1.add()
ntp = SystemNtp(server="myntp_srv", status=1)
ntp.add()
ntp.status = 1
ntp.update()
ntp.delete()

templates = TemplateSmtp.getAll()
for e in templates:
    print e

smtp = TemplateSmtp(name="my_smpt_temp3")
smtp.client_domain_switching_list = [{"client_domain": "domain1", "service_group": "sg1", "match_type": 0}]
smtp.create()
smtp.delete()

vip2 = VirtualServer.searchByName("vip2")
print vip2

vip_list = VirtualServer.getAll()
for e in vip_list:
    print e
vip1 = VirtualServer(name="test_vip1", address="100.10.10.1")
vip1.vport_list = [{"port" : 80, "protocol": AxAPI.SVC_HTTP, "http_template": ""}]
vip1.create()
vip1.vport_list = [{"port" : 80, "protocol": AxAPI.SVC_HTTP, "status": AxAPI.STATUS_DISABLED}]
vip1.update()
vip1.delete()

print vip1

#axapi_241 = method_call.AxApiContext("192.168.210.241", "admin", "a10$pass").authentication()

rs_list = RealServer.getAll()
for e in rs_list:
    print e

#axapi_239.switchContext()

s1 = RealServer(host="13.12.12.1", name="test1")
s1.port_list = [{"port_num" : 80, "protocol" : AxAPI.PROTO_TCP, "weight" : 2}, {"port_num" : 81, "protocol" : AxAPI.PROTO_TCP, "weight" : 3}]   
s1.create()
print s1
s1.status = AxAPI.STATUS_DISABLED
s1.update()
s1.delete()
 
svc_s4 = ServiceGroupStats.getAll()
for e in svc_s4:
    print e
svc_s1 = ServiceGroupStats.searchByName(name='g1')
print svc_s1

svc_s2 = ServiceGroupStats(name="abc")
print svc_s2
#svc_s2.status = 1
    
svc_group_list = ServiceGroup.getAll()
for svc in svc_group_list:
    print svc
    
svc = ServiceGroup.searchByName("g1")
#print svc.name
#print svc.health_monitor
#print svc.member_list
svc2 = ServiceGroup()
svc2.name = "g3" #svc.name
svc2.protocol = svc.protocol
svc2.lb_method = AxAPI.LB_LEAST_CONNECTED_ON_SERVICE_PORT
svc2.member_list = [{"server":"1.1.1.2", "port": 80, "status": AxAPI.STATUS_ENABLED}, {"server":"1.1.1.3", "port": 80}]
svc2.create()
svc2.delete()
print svc2


svc3 = ServiceGroup(name='g5', protocol=AxAPI.PROTO_TCP, lb_method=AxAPI.LB_LEAST_REQ)
svc3.member_list = [{"server":"1.1.11.2", "port": 80}, {"server":"1.1.11.3", "port": 80}]
svc3.create()

svc4 = ServiceGroup(name='g5')
svc4.member_list = [{"server":"1.1.1.2", "port": 80, "status": AxAPI.STATUS_DISABLED}, {"server":"1.1.1.3", "port": 80, "status": AxAPI.STATUS_ENABLED}]
svc4.update()


svc4.delete()

print svc3

svc_s1 = ServiceGroupStats.searchByName(name='g1')
print svc_s1


