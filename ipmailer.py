#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText
import datetime
from urllib.request import urlopen
import json

ip = urlopen('http://httpbin.org/ip').read()
ip = ip.decode('utf-8')
ip = json.loads(ip)

# Change to your own account information:
to = '####@stud.ntnu.no,'
gmail_user = '###@gmail.com'
gmail_password = '######'
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
# If error, check less secure app setting for this account (should be set to 'on'):
# https://www.google.com/settings/security/lesssecureapps

smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
my_msg = '%s' % today.strftime('%b %d %Y')
msg = MIMEText(my_msg)
msg['Subject'] = 'Raspberry Pi IP: %s' % ip['origin']
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
