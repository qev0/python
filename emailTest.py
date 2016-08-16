#!/usr/bin/python
#
#
import smtplib
from email.mime.text import MIMEText
textfile = 'test.txt'

#open a file for reading - no error checking for non ascii chars
fp = open(textfile,'rb')

#create the message 
msg = MIMEText(fp.read())

fp.close


sender   = 'NetscalerBackups@aeraenergy.com'
recipient = 'kdmusser@aeraenergy.com'
msg['Subject'] = 'Netscaler back up successful'
msg['From'] = sender
msg['To'] = recipient


#send message to SMTP server
smtpServer = '137.206.96.184'
s = smtplib.SMTP(smtpServer)
s.sendmail(recipient, [sender], msg.as_string())
s.quit()

