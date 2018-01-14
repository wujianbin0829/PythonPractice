# -*- coding: UTf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr
import smtplib

fromAddr = raw_input("FROM:")
password = raw_input("PASSWORD:")
toAddr = raw_input("TO:")
#server smtp.qq.com
smtp_server =  raw_input('SMTP server: ')

mailContext = """
<p>你好，我是XXX，这个我通过python发送的邮件</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
"""

message = MIMEText(mailContext, 'html', 'utf-8')
message['From'] = Header("%s" % fromAddr ,'utf-8')
message['To'] = Header("%s" % toAddr,'utf-8')
message['Subject'] = Header("my python test", 'utf-8')

try:
    #server=smtplib.SMTP_SSL(smtp_server, 465)
    server=smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(fromAddr, password)
    server.sendmail(fromAddr, [toAddr], message.as_string())
    print "send mail success"
except smtplib.SMTPException,e:
    print e
    print "send mail fail"
finally:
    server.quit()

