import smtplib
from email.mime.text import MIMEText
from email.header import Header
smtpserver='smtp.163.com'
user='15680488752@163.com'
password='ma2222de'
sender='15680488752@163.com'
receive='1375914761@qq.com'
subject='charley chen 发送的第一个邮件'
content='<html><h1 style="color:red">very good</h1></html>'
msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']=sender
msg["To"]=receive
smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)
print('开始发送')
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print('发送完成')