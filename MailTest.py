from email.mime.text import MIMEText
import smtplib
import os

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

from_addr = os.environ.get('MAIL_USERNAME')
password = os.environ.get('MAIL_PASSWORD')
to_addr = 'ezchou@qq.com'
smtp_server = 'smtp.163.com'

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()