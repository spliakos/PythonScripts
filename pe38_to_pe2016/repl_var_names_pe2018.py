#!/usr/bin/python

import sys
import os
import re
from shutil import copyfile
from find_files import find

#yaml = ruamel.yaml.YAML()
#yaml.indent(mapping=2, sequence=4, offset=2)

result_1 = []
result_2 = []
result_1 = find('*.yaml','./profiles')
#result_2 = find('*.stack','./templates')

for p in result_2: print p

for infile_1 in result_1:
  with open(infile_1,'r') as fr:
    content = fr.readlines()
    content = [x.rstrip() for x in content]

  outf_2018 = infile_1[:-5]+'_pe2018.yaml'
  outf_pe38 = infile_1[:-5]+'_pe38.yaml'

  with open(outf_2018, "w") as out_file_2018, open(outf_38, "w") as out_file_38 :
    for idx, line in enumerate(content):
      s = re.match("^(\s+):stack_template:", line)
      if s:
        if re.match(r"^\s+:puppetmaster", content[idx+1]):
          print "we are inside here now"
          out_file_2018.write("%s\n" %line)
          out_file_38.write("%s\n" %line)
          continue
        line_2018 = line + "\n   :puppetmaster: pe2016\n   :os_config: ol7-template"
        line_2018 = re.sub(r'[ \t]{2,}',s.group(1),line_2018)
        line_38 = line + "\n   :puppetmaster: pe38"
        line_2018 = re.sub(r'[ \t]{2,}',s.group(1),line_38)
      out_file_2018.write("%s\n" %line_2018)
      out_file_38.write("%s\n" %line_38)
      







  '''
  if not isinstance(data['desc'], list):
    data['desc'] = [data['desc']]  # change the non-list into a list
  l = data['desc']

  for elem in content:
    if elem['puppetmaster'] in content:
      break
    else:
      content.insert()



  outf = infile_1 + '.bak'
  for p in content: print p

  with open(outf, "w") as out_file:
    for idx, line in enumerate(content):
      if line.startswith("   :stack_template:"):
        if content[idx+1].startswith("   :puppetmaster:"):
          continue
        line = line + "   :puppetmaster: pe2016\n  :os_config: ol7-template\n"
      out_file.write(line)
'''

##########################

#  for infile_2 in result_2:
#   infile_no_ext = os.path.splitext(infile_2)
'''
with open(infile,'r') as fr:
  content = fr.readlines()
  content = [x.strip() for x in content]
  for vrs in content:
    if vrs.startswith("riak."):
      vrs.replace("riak.","riak_")

for infile_1 in result_1:
  with open(infile_1,'r') as fr:
    content = fr.readlines()
    content = [x.strip() for x in content]

  outf = infile_1 + '.bak'
  for p in content: print p

  with open(outf, "w") as out_file:
    for idx, line in enumerate(content):
      if line.startswith("   :stack_template:"):
        if content[idx+1].startswith("   :puppetmaster:"):
          continue
        line = line + "   :puppetmaster: pe2016\n  :os_config: ol7-template\n"
      out_file.write(line)

'''
