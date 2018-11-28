#!/usr/bin/env python

import sys
import yaml

#env = sys.argv[1]
infile = sys.argv[1]
env1 = 'sbw01'
env2 = 'wsc01'

with open(infile, "r") as f:
     list_doc = yaml.load(f)

if env1 in list_doc and env2 in list_doc:
     print "sbw01=%s;wsc01=%s" % (list_doc[env1]["ref"], list_doc[env2]["ref"])
