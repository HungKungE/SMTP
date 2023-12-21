from smtp import *
from test import *

def main():
    emailInfos : list[TextEmailInfo] = []
    for test_user in combine2_users:
        msg = create_text_form(test_user, "test TEXT 입니다.")
        emailInfo = create_email_info(test_user, msg)
        emailInfos.append(emailInfo)
    
    send_email(emailInfos)
    
main()