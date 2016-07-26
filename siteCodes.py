#!/bin/env python

import re
import socket

#====L3 Devices===
#BKMDFA = 10.128.64.254
#BKMDFB = 137.206.100.200
#cgmdf = 10.224.64.254
#samdf = 10.208.64.254
#blmdf = 10.144.64.254
#nmmdf = 10.160.64.254
#smmdf = 10.176.64.254
#vnmdf = 10.192.64.254

#Site Codes
siteEH = 245
siteBR = 240
siteCG = 224
siteSA = 208
siteVN = 192
siteSM = 176
siteNM = 160
siteBL = 144
siteBK = 128

#Print the show ip int br vlans that are not down.
filename1 = 'intbr.txt'
filename2 = 'showIPAdd.txt' 

with open(filename1, 'r') as f:
 fileData1 = f.readlines()
 with open(filename2,'r') as f2:
  fileData2 = f2.readlines()
  for fileData1 in f: 
   if "down" not in fileData1:
    vlanInterface = fileData1[:-37]
    pattern = re.compile('(255\.255\.[0-9]{1,3}\.[0-9]{1,3})')
    for fileData2 in f2:
     result = re.search(pattern, fileData2)
     if result and 'secondary' not in fileData2:
      ipAddMask = result.groups()[0]
      print '%s %s' % (vlanInterface, ipAddMask)

