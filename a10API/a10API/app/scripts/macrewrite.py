from jsonrpclib import Server
 
username = "admin"
password = "admin"
host = "172.22.28.156"
sip = "10.1.1.1"
smac = "0000.aaaa.bbbb"
dmac = "1111.aaaa.bbbb"
urlString = "https://{}:{}@{}/command-api".format(username, password, switch)
switchReq = Server( urlString )
# The following rpc request will match on the source IP, then change both source and dest mac
response = switchReq.runCmds( 1, ["enable", "configure", "openflow", "flow a10", "persistent", "match source ip {}".format(sip), "action set source mac ".format(smac), "action set destination mac".format(dmac)] )

