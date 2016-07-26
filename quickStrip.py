#strip ports in mac table. 
import re

fileName = 'C:\IOS\BK-Row1Rack2-Nx5k.txt'

#Open the file in read only

file = open(fileName, 'r')
for line in file.readlines():
	mac = line[11:]
	print mac

#line.index('dynamic')