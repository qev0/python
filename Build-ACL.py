fileName = 'C:\IOS\All-MPLS-Networks.txt'
output = ""
stringToAdd = "permit"
file = open(fileName, 'r')
for line in file.readlines():
	cidr = line[-3:]
	if "12" in cidr:		 
		print "%s %s %s" % (stringToAdd, line[:-4], "0.15.255.255")
	if "24" in cidr:		 
		print "%s %s %s" % (stringToAdd, line[:-4], "0.0.0.255")
	if "21" in cidr:		 
		print "%s %s %s" % (stringToAdd, line[:-4], "0.0.7.255")
	if "23" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "0.0.1.255")
	if "22" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "0.0.3.255")
	if "29" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "0.0.0.7")
	if "28" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "0.0.0.15")			
	if "32" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "0.0.0.0")
	if "30" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "0.0.0.3")
file.close() 