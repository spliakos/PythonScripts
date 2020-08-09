#!/usr/bin/python

import sys
import urllib
import logging
import os.path
import httplib
import json
import os
import argparse

# no stacktrace on SIGINT
def signal_handler(signal, frame):
    print('Terminated with SIGINT (Ctrl+C)')
    sys.exit(0)
#signal.signal(signal.SIGINT, signal_handler)

# Parsing Arguments
parser = argparse.ArgumentParser()
parser.add_argument("command", type=str, help="Command for Infoblox Manipulator script. Possible values: 1. show_net 2. add_host 3. edit_host")
parser.add_argument("-n", "--network", type=str, help="search for specific network CIDR notation")
parser.add_argument("-u", type=str, help="user name for Infoblox user")
parser.add_argument("-p", type=str, help="password")
args = parser.parse_args()

user = args.u
paswd = args.p

try:
	args.command
except NameError:
	print "You need a valid command. Check --help"
        sys.exit(0)

if args.command == "show_net":
	command = "show_net"
	cidr_network = args.network
elif args.command == "add_host":
	command = "add_host"
	cidr_network = args.network
elif args.command == "edit_host":
	command = "edit_host"
else:
	print("You need a valid command. Check --help")
	sys.exit(0)

# Variables
WH_Infoblox_URL = "https://10.120.193.240/"
WH_wapi_latest_version = "v2.0"
curl_basic = "curl -k -u %s:%s -X" %(user,paswd)

if command == "show_net":
	print curl_basic
