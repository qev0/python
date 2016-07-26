#!/usr/bin/python
#
#
#

from datetime import datetime
from datetime import timedelta

threshold   = 30
pubDate     = datetime.now()
monthAgo    = datetime.now() - timedelta(days=threshold)

print "Start"
while(pubDate > monthAgo):
    print pubDate 
    pubDate -= timedelta(days=1)
print "Done"
