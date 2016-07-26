fileName = 'appendServices.txt'
output = ""
stringToAdd = ""
file = open(fileName, 'r')
for line in file.readlines():		 
	print "%s %s %s" % ("<li>", line.rstrip(), "</li>")
file.close() 