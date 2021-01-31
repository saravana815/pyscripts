#!/bin/env python3

import os, re, argparse
from pprint import pprint
from netmiko import ConnectHandler

import pandas as pd
import numpy as np
import jinja2

parser = argparse.ArgumentParser()
parser.add_argument('--host', help='router ip address', required=True)
parser.add_argument('--user', help='router login username', required=True)
parser.add_argument('--password', help='router login password', required=True)
args = parser.parse_args()

cisco1 = {
    "device_type": "cisco_xr",
    "host": args.host,
    "username": args.user,
    "password": args.password,
}

# Show bgp origin-as validity command execution
command1 = "show bgp origin-as validity invalid"
command2 = "show bgp ipv6 unicast origin-as validity invalid"

with ConnectHandler(**cisco1) as net_connect:
    output1 = net_connect.send_command(command1)
    output2 = net_connect.send_command(command2)

def get_bgp_ipv4_invalid_prefix_list(output):
    prefix_start_flag = False
    match1 = []; match2 = []; bgp_prefixes = []

    pat1 = re.compile(r"^[\S]*\s+(\d+\.\d+\.\d+\.\d+\/\d+)\s+(\d+\.\d+\.\d+\.\d+)\s")
    pat2 = re.compile(r"^[\S]*\s+(\d+\.\d+\.\d+\.\d+)\s")
    as_num = re.compile(r"(\d+)\s+")
    lines = output.splitlines(); line_no = 0
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
                prefix = match1[0][0]
                nexthop = match2[0]
                as_path = line[as_path_start_index:]
                as_list = as_num.findall(as_path)
                as_last = int(as_list[-1])
                bgp_prefixes.append([prefix,nexthop,as_last])
            else:
                match1 = pat1.findall(line)
                if len(match1) == 0: continue
                prefix = match1[0][0]
                nexthop = match1[0][1]
                as_path = line[as_path_start_index:]
                as_list = as_num.findall(as_path)
                as_last = int(as_list[-1])
                bgp_prefixes.append([prefix,nexthop,as_last])
        line_no = line_no + 1
    return bgp_prefixes


def get_bgp_ipv6_invalid_prefix_list(output):
    prefix_start_flag = False
    match1 = []; match2 = []; bgp_prefixes = []

    pat1 = re.compile(r"^[\S]*\s+([0-9a-fA-F\:\/]+)\s+([0-9a-fA-F\.\:]+)\s")
    pat2 = re.compile(r"^[\S]*\s+[^0-9a-fA-F\:\/]+\s+([0-9a-fA-F\.\:]+)\s")
    as_num = re.compile(r"(\d+)\s+")
    lines = output.splitlines(); line_no = 0
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
                as_list = as_num.findall(as_path)
                as_last = int(as_list[-1])
                bgp_prefixes.append([prefix,nexthop,as_last])
            else:
                match1 = pat1.findall(line)
                if len(match1) == 0: continue
                prefix = match1[0][0]
                nexthop = match1[0][1]
                as_path = line[as_path_start_index:]
                as_list = as_num.findall(as_path)
                as_last = int(as_list[-1])
                bgp_prefixes.append([prefix,nexthop,as_last])
        line_no = line_no + 1
    return bgp_prefixes


ipv4_bgp_prefixes = get_bgp_ipv4_invalid_prefix_list(output1)
pprint(ipv4_bgp_prefixes)
ipv6_bgp_prefixes = get_bgp_ipv6_invalid_prefix_list(output2)
pprint(ipv6_bgp_prefixes)

ipv4_bgp_prefixes.extend(ipv6_bgp_prefixes)

# data = [['Geeks', 10], ['for', 15], ['geeks', 20]]
# df = pd.DataFrame(data, columns = ['Name', 'Age'])
df = pd.DataFrame(ipv4_bgp_prefixes, columns = ['BGP Prefix', 'Nexthop', 'AS Last'])

def color_negative_red(val):
    # color = 'red' if val < 0 else 'black'
    color = 'red'
    return f'color: {color}'

styler = df.style.applymap(color_negative_red)

# Template handling
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
template = env.get_template('template.html')
html = template.render(my_table=styler.render())
# html = template.render()

# Plot
ax = df.plot.bar()
fig = ax.get_figure()
fig.savefig('plot.svg')

# Write the HTML file
with open('report.html', 'w') as f:
    f.write(html)
