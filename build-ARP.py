import socket

# Purpose: use a mac table of a switch and an arp table of an L3 device to 
# determine which services will be impacted by a switch outage. 


#Ask the user what for the file name of the switch mac table print out

fileName = raw_input('Enter complete path of switch MAC table, ex: "C:/IOS/example.txt" ')

#Open the file in read only

file = open(fileName, 'r')

# Create a list called macTable
macTable = []
# for each line in the file, strip the first 11 characters 
# and last 39 characters, strip the end /n and remove the dots
for line in file:
	macTable.append(line[11:-39].rstrip().replace(".",""))
#print MacTable  #<--- for troubleshooting output
file.close() #close the file. 

# Ask the user for the file name of the arp table. 
arpFile = raw_input('Enter complete path of ARP table, ex: "C:/IOS/example.txt" ')
arpTable = open(arpFile, 'r')
arpArray = []  #create a list for the arp entries
# for each line take remove the last 27 digits, strip the /name
# and remove the colons. 
for entry in arpTable:
	arpArray.append(entry[:-27].rstrip().replace(":",""))
#print arpArray  #<---- for troubleshooting output
arpTable.close()  #close the file. 

#Print the list of IP addresses

print "==========="
print "List of IP addresses followed by FQDN (if available) that correspond to MAC table on switch"
print "==========="
for i in arpArray: #for each item in the arp table
	for j in macTable: #and for each item in the mac table
		if j in i: #if the mac table is in the arp table
			#print j #print the mac on the top line
			print i[13:] , socket.getfqdn(i[13:])   # Print the IP and FQDN (if availble) for each entry



