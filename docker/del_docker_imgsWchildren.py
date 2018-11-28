#!/usr/bin/python

import subprocess

if __name__ == "__main__":
    
    bashCommand = "docker images -a|grep '^<none>'|tr -s ' '|cut -d' ' -f 3|xargs docker rmi"
    process = subprocess.Popen(bashCommand,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = process.communicate()[0]

    splitl_output = output.splitlines()
    for line in splitl_output:
       if "unable to delete" in line:
          fields = line.split()
          print fields[8]
          bashC2 = "docker inspect --format='{{.Id}} {{.Parent}}' $(docker images --filter since=" + str(fields[8]) + "-q)"
          print bashC2
          #process = subprocess.Popen(bashC2,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)  




"""
    with open('dep_docker-imgs.txt') as f:
       content = f.readlines()
       # you may also want to remove whitespace characters like `\n` at the end of each line
       content = [x.strip() for x in content]

       for img in content:
"""
