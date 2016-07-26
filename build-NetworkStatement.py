fileName = 'C:\IOS\BL-BGP-OUT.txt'
output = ""
stringToAdd = "network"
file = open(fileName, 'r')
for line in file.readlines():
	cidr = line[-3:]
	if "12" in cidr:		 
		print "%s %s %s" % (stringToAdd, line[:-4], "255.240.0.0")
	if "24" in cidr:		 
		print "%s %s %s" % (stringToAdd, line[:-4], "255.255.255.0")
	if "21" in cidr:		 
		print "%s %s %s" % (stringToAdd, line[:-4], "255.255.248.0")
	if "23" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "255.255.254.0")
	if "22" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "255.255.252.0")
	if "29" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "255.255.255.248")
	if "28" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "255.255.255.240")			
	if "32" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "255.255.255.255")
	if "30" in cidr:
		print "%s %s %s" % (stringToAdd, line[:-4], "255.255.255.252")
file.close() 