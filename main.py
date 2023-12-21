from smtp import *
from test import *

def main():
    emailInfos = create_email_infos(naver_users)
    send_email(emailInfos)
    
main()