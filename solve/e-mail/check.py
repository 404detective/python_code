# smtplib 用于邮件的发信动作
import smtplib
import random
import string
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头
 
# 发信方的信息：发信邮箱，QQ 邮箱授权码
admin = '1029975697@qq.com'
password = 'nnygifmhmalkbejf'
 
# 收信方邮箱
user = input('请输入您的邮箱')
 
# 发信服务器
smtp_server = 'smtp.qq.com'

num=string.digits

def check_num():
    num_digits = ""
    for i in range(6):
        num1 = random.choice(num)
        num_digits = num_digits + num1

    return num_digits


content="验证码: " + "<font color='orange' size='5px'><b>" + check_num() + "</b></font>"
# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText(content,'html','utf-8')
 
# 邮件头信息
msg['From'] = Header(admin)
msg['To'] = Header(user)
msg['Subject'] = Header('验证码')
 
# 开启发信服务，这里使用的是加密传输
server=smtplib.SMTP_SSL(smtp_server)

server.connect(smtp_server,465)
# 登录发信邮箱
server.login(admin, password)
# 发送邮件
for i in range(100):
    server.sendmail(admin, user, msg.as_string())
# 关闭服务器
server.quit()