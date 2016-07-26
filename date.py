#!/usr/bin/python
#
#
#

from datetime import datetime, timedelta

pubStr = 'Tue, 1 May 2016 19:49:05 PDT'
date = datetime.now()
dateConvert = datetime.strftime(date, '%Y-%m-%d')#%H:%M:%S:%f
pubStrNoTzone = pubStr[:-4]
pubDate = datetime.strptime(pubStrNoTzone, '%a, %d %b %Y %H:%M:%S')

print 'published date'
print pubDate.date()


#pubDateDelta = pubDate - date

#convert the date from a string back to a time 
dateConvert2 = datetime.strptime(dateConvert, '%Y-%m-%d')#%H:%M:%S:%f

#THis is the delta between today and 30 days ago
dateDelta = dateConvert2 - timedelta(days=30)
dateDeltaStr = datetime.strftime(dateDelta, '%Y-%m-%d')

print 'This is the date 30 days ago'
print dateDeltaStr
print 'today\'s date'
#print date
#print 'today\'s date converted'
#print today's date converted to a easy string
print dateConvert

dateDifference = dateConvert2 - pubDate
if (dateDifference.days) > 60:
    print "greater than 60 days old"
else:
    print "younger than 60 days"
