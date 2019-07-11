
#Usage - parse_conf.py ASR9K_run_cfg.txt IOS_device_run_cfg.txt

import sys, os
import re
from ciscoconfparse import CiscoConfParse

f1 = sys.argv[1]
f2 = sys.argv[2]

cf1 = CiscoConfParse(f1)
cf2 = CiscoConfParse(f2)
print cf1
print cf2

# intf_list = cf2.find_objects(r'^interface ')
# print intf_list[0].text
# ip_addr = '217.39.0.16'
# print intf_list[0].re_search_children(r'ip address ' + ip_addr)

def find_ip_intf(cf_obj, ip_addr, rtr1_vrf):
    intf_list = cf_obj.find_objects(r'^interface ')
    intf_found = False
    for intf in intf_list:
        #print intf.text
        intf_match = intf.re_search_children(r'ip.* address ' + re.escape(ip_addr) + ' ')
        if len(intf_match) > 0:
            intf_found = True
            print '----------------------------------------------------------',
            print '----------------------------------------------------------'
            rtr2_vrf = intf.re_search_children('ip vrf forwarding')[0]
            print 'On RTR1,      vrf:', rtr1_vrf, '\tOn RTR2, intf_name:', intf.text, ' vrf:', rtr2_vrf.text 
            print 'On RTR1, nei_cfgd:', ip_addr,  '\tOn RTR2, ip_addr  :', intf_match[0].text

    return intf_found

        
bgp_obj = cf1.find_objects(r'router bgp')
bgp_obj = bgp_obj[0]
vrf_list = bgp_obj.re_search_children(r' vrf ')
for vrf in vrf_list:
    #print vrf.text.split(' ')[2]
    vrf_name = vrf.text.split(' ')[2]
    vrf_nei_list = vrf.re_search_children(r'neighbor ')
    for nei in vrf_nei_list:
        #print nei.text.split(' ')[3]
        nei_ip = nei.text.split(' ')[3]
        #find_ip_intf(cf2, nei_ip)
        find_ip_intf(cf2, nei_ip, vrf_name)
