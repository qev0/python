#!/usr/bin/python
#
#

import re
import csv

users   = 'webexusers.txt'
others  = 'newfile.txt'

with open (users,'rb') as f:
    for line in f:
        cleanedLine = line.strip()
        if cleanedLine:
            if '@' in cleanedLine:
                print cleanedLine
