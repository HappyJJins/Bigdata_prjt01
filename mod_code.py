import hashlib

class Code:
    def __init__(self,text):
        self.text=text

    def Ciser(self):
        return [chr(ord(x)+5) if x!=' ' else x for x in list(self.text)]

    def MD5(self):
        h=hashlib.md5()
        h.update(self.text.encode('utf-8'))
        return h.hexdigest()


    def Sha1(self):
        h=hashlib.sha1()
        h.update(self.text.encode('utf-8'))
        return h.hexdigest()

class Cal:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2  
    def div(self):
        return self.num1/self.num2
    def mul(self):
        return self.num1*self.num2  