#!/bin/env python3

import os, re
from pprint import pprint
from netmiko import ConnectHandler

cisco1 = {
    "device_type": "cisco_xr",
    "host": "10.51.117.224",
    "username": "root",
    "password": "cisco1234",
}

# Show command that we execute.
command1 = "show bgp origin-as validity invalid"
command2 = "show bgp ipv6 unicast origin-as validity invalid"

with ConnectHandler(**cisco1) as net_connect:
    output1 = net_connect.send_command(command1)
    output2 = net_connect.send_command(command2)

def get_bgp_ipv4_invalid_prefix_list(output):
    prefix_start_flag = False
    match1 = []
    match2 = []
    bgp_prefixes = []

    pat1 = re.compile(r"^[\S]*\s+(\d+\.\d+\.\d+\.\d+\/\d+)\s+(\d+\.\d+\.\d+\.\d+)\s")
    pat2 = re.compile(r"^[\S]*\s+(\d+\.\d+\.\d+\.\d+)\s")
    for line in output.splitlines():
        # print(line)
        if 'Network' in line:
            as_path_start_index = line.find('Path')
            # print('as_path_start_index', as_path_start_index)
            prefix_start_flag = True
            continue
        elif prefix_start_flag == True:
            match2 = pat2.findall(line)
            if len(match2) > 0:
                prefix = match1[0][0]
                nexthop = match2[0]
                as_path = line[as_path_start_index:]
                bgp_prefixes.append([prefix,nexthop,as_path])
            else:
                match1 = pat1.findall(line)
                if len(match1) == 0: continue
                prefix = match1[0][0]
                nexthop = match1[0][1]
                as_path = line[as_path_start_index:]
                bgp_prefixes.append([prefix,nexthop,as_path])
    return bgp_prefixes


def get_bgp_ipv6_invalid_prefix_list(output):
    prefix_start_flag = False
    match1 = []
    match2 = []
    bgp_prefixes = []

    pat1 = re.compile(r"^[\S]*\s+([0-9a-fA-F\:\/]+)\s+([0-9a-fA-F\.\:]+)\s")
    pat2 = re.compile(r"^[\S]*\s+[^0-9a-fA-F\:\/]+\s+([0-9a-fA-F\.\:]+)\s")
    lines = output.splitlines()
    line_no = 0
    for line in lines:
        # print(line)
        if 'Network' in line:
            as_path_start_index = line.find('Path')
            # print('as_path_start_index', as_path_start_index)
            prefix_start_flag = True
            continue
        elif prefix_start_flag == True:
            match2 = pat2.findall(line)
            if len(match2) > 0:
                try:
                    prefix = match1[0][0]
                except IndexError:
                    print('ERROR: Not able to parse the CLI output correctly')
                    print('LINE: ', lines[line_no-1])
                    print('Check CLI command output and input given to this function')
                    exit(1)
                nexthop = match2[0]
                as_path = line[as_path_start_index:]
                bgp_prefixes.append([prefix,nexthop,as_path])
            else:
                match1 = pat1.findall(line)
                if len(match1) == 0: continue
                prefix = match1[0][0]
                nexthop = match1[0][1]
                as_path = line[as_path_start_index:]
                bgp_prefixes.append([prefix,nexthop,as_path])
        line_no = line_no + 1
    return bgp_prefixes


bgp_prefixes = get_bgp_ipv4_invalid_prefix_list(output1)
pprint(bgp_prefixes)
bgp_prefixes = get_bgp_ipv6_invalid_prefix_list(output2)
pprint(bgp_prefixes)
