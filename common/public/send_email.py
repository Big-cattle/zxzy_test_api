import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from ZXZY_API_AUTO.common.public.abs_path import *

class SendEmail:
	def __init__(self,user,pwd):
		self.user = user
		self.pwd = pwd
	def send_email(self,email_to,filepath):
		now = time.strftime('%Y-%m-%d %H:%M:%S')
		msg = MIMEMultipart()
		msg['subject'] = now +"甄选自研接口测试报告"
		msg['From'] = self.user
		msg['To'] = email_to
		
		part = MIMEText("这是这次甄选接口测试报告结果，请查收！")
		msg.attach(part)
		
		part = MIMEApplication(open(filepath,'rb').read())
		part.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', filepath))
		msg.attach(part)
		
		s=smtplib.SMTP_SSL('smtp.qq.com',timeout=30)
		s.login(self.user,self.pwd)
		s.sendmail(self.user,email_to,msg.as_string())
		s.close()
		
if __name__ == '__main__':
	user = '460290847@qq.com'
	pwd = 'yiizwrytnpqkcbbe'
	SendEmail(user,pwd).send_email('xiaohaoyong@richinfo.cn',test_report_path)