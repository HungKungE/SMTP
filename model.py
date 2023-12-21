from email.mime.text import MIMEText

class User:
    def __init__(self, email:str, keywords:list[str]):
        self.email = email
        self.keywords = keywords
        
    def add(self, new_keyword:str):
        self.keywords.append(new_keyword)
         
    def delete(self, target:str):
        if self.keywords.count(target)>0:
            self.keywords.remove(target)
    
    def show(self):
        print("email:",self.email)
        print("keywords:",self.keywords)
        
class TextEmailInfo:
    def __init__(self, user:User, msg:MIMEText):
        self.user = user
        self.msg = msg