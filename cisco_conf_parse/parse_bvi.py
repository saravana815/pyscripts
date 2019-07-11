#Usage - parse_conf.py ASR9K_run_cfg.txt IOS_device_run_cfg.txt

import sys, os
import re
from ciscoconfparse import CiscoConfParse

f1 = sys.argv[1]

cf1 = CiscoConfParse(f1)
print cf1

# intf_list = cf2.find_objects(r'^interface ')
# print intf_list[0].text
# ip_addr = '217.39.0.16'
# print intf_list[0].re_search_children(r'ip address ' + ip_addr)

def parse_bvi_int(cf_obj):
    intf_list = cf_obj.find_objects(r'^interface BVI')
    for intf in intf_list:
        print intf.text
        bvi_int_name = intf.text
        print bvi_int_name
        for child_obj in intf.children:
            if 'ipv4 address' in child_obj.text:
                print ' ip addr line found. swap ip address from XL'
            elif 'mac-address' in child_obj.text:
                print ' mac-address line found. swap mac address from XL'
            else:
                print child_obj.text

parse_bvi_int(cf1)
