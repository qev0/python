import csv

foo = 1
with open('C:\IOS\ipcsList.csv','rb') as ipcsListFile: #change your directory/source if need be
	with open('C:\IOS\smIPCS-IPs.csv','rb') as smIPs:  #change your source for the IPs w/o DNS
	
	
		ipcsListRdr = csv.reader(ipcsListFile, delimiter=',')
		ipcsServerRow1_Col2= [row[1] for row in ipcsListRdr]
		
		smIPsRdr = csv.reader(smIPs, delimiter=' ')
		smIPCSArpListRows = [row for row in smIPsRdr]
		
		only_b = []
		
		for row in smIPCSArpListRows:
			if smIPCSArpListRows in ipcsServerRow1_Col2:
				print "Comparing: %s with %s" % (smIPCSArpListRows[0], ipcsServerRow1_Col2[1])
				print "FOUND MATCH!!!"
				print "%s,%s" % (smIPCSArpListRows[0], ipcsServerRow1_Col2[1])