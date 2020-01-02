import smtplib
from email.mime.text import MIMEText
from email.header import  Header
from smtplib import SMTP_SSL


smtpObj = SMTP_SSL()

smtpObj.connect("smtp.qq.com",465)
smtpObj.set_debuglevel(1)
smtpObj.ehlo("smtp.qq.com")

smtpObj.login("317828332@qq.com","Luffyfly#21")

sender = "lijie3721@126.com"
receivers = ["alex@oldboyedu.com","alex@luffycity.com"]

msg = MIMEText('''
    hey alex,
    please check this out..
    fuyc...''')
msg["From"] = Header("dd")
msg["To"] = Header("test...")


msg["Subject"] = Header("三体")

smtpObj.sendmail(sender,receivers,msg.as_string())
print("发送成功。。。")