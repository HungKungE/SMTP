import smtplib
import os
from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
import time
from email.utils import formataddr
import logging
from model import *

# smtp 서버와 연결 ------------------------------------------------------------
def connect_smtp_server():
  try :
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    smtp_connect = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connect.starttls()
    smtp_connect.login(os.getenv('ADMIN_EMAIL'), os.getenv('ADMIN_PASSWORD'))
    
    return smtp_connect

  except Exception as e:
    logging.error("smtp connect fail:"+str(e))
    
# msg 생성 (text) ------------------------------------------------------------
def create_text_form(user:User, context:str):
  msg = MIMEText(context)
  msg["Subject"] = "오늘의 기사"
  msg["From"] = formataddr(("KeywordKatch", os.getenv('ADMIN_EMAIL')))
  msg["To"] = user.email

  return msg

# user, msg -> mail info 생성
def create_email_info(user:User, msg:MIMEText):
    return TextEmailInfo(user,msg)

# 사용자 리스트 -> TextEmailInfo 리스트 생성
def create_email_infos(users:list[User]):
    emailInfos : list[TextEmailInfo] = []
    for user in users:
        msg = create_text_form(user, "test TEXT 입니다.")
        emailInfo = create_email_info(user, msg)
        emailInfos.append(emailInfo)
    return emailInfos

# smtp를 통한 이메일 전송
def send_email(email_infos:list[TextEmailInfo]):
  try:
      start = int(time.time())
      smtp_connect = connect_smtp_server()
      for email_info in email_infos:
        smtp_connect.sendmail(os.getenv('ADMIN_EMAIL'), email_info.user.email, email_info.msg.as_string())
      print("send users:", str(len(email_infos)))
      print("run time(sec):", int(time.time()) - start)
    
  except Exception as e:
    logging.error("email send fail:"+str(e))

  finally:
      smtp_connect.close()
