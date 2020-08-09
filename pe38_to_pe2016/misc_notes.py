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
