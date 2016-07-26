#!/usr/bin/python
#
#
#

import re, feedparser, csv
from datetime import datetime, timedelta

#get today
today = datetime.now()
#convert today to a string
dateConvert = datetime.strftime(today, '%Y-%m-%d')

#this is our xml rss feed
d = feedparser.parse('http://tools.cisco.com/security/center/psirtrss20/CiscoSecurityAdvisory.xml')

#convert date string to a time
dateConvert2 = datetime.strptime(dateConvert, '%Y-%m-%d')

#dateDelta = dateConvert2 - timedelta(days=60)
#define the reg ex for getting the vulnerability GUID
vulnGuidRegEx = re.compile(r'cisco-sa-[0-9]{8}-.+')

i = 0
numberOfEntries = len(d['entries'])
print numberOfEntries
while i < numberOfEntries: 
    vulnTitle = d.entries[i].title
    vulnLink = d.entries[i].link
    vulnGuidURL = d.entries[i].guid
    #get vuln pub date as a string
    vulnPubDateStr = d.entries[i].published
    #get rid of time zone on string 
    vulnPubStrNoTZone = vulnPubDateStr[:-4]
    #convert pub date string to a time
    vulnPubDate = datetime.strptime(vulnPubStrNoTZone, '%a, %d %b %Y %H:%M:%S')
    #change format of string to yyyy/mm/dd
    vulnPubDateStr = datetime.strftime(vulnPubDate, '%Y-%m-%d')
   #search the URL for our GUID
    vulnGuid = vulnGuidRegEx.search(vulnGuidURL)
   #get the differnece between today and the vuln pub date
    dateDifference = dateConvert2 - vulnPubDate
    #check if the date difference is less than 60 days
    if (dateDifference.days) < 60:
        # print stuff
        vulnCSV = 'vuln'+datetime.now().strftime('%Y%m%d')+'.csv'
        with open (vulnCSV, 'ab') as csvFile:
            csvWriter = csv.writer(csvFile, delimiter=',')
            csvWriter.writerow([vulnTitle] + [vulnGuid.group()] + [vulnPubDateStr])
        print vulnTitle+','+vulnGuid.group()+','+vulnPubDateStr
        i += 1
    else:
        print "no match found"
        i += 1
