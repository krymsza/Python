#! /usr/bin/env
import re, json

class My_Exception(Exception):
    pass

class email:
    email= {}
    def __init__(self,text):
        regex_email = re.compile(
            r'''(?P<adres> [\w+.]+ @ \w+(\.\w+)+ )''',
            re.IGNORECASE | re.VERBOSE
        )
        if (not regex_email.match(text)):
            print ("None")      
            try:
                raise My_Exception("zły format")
            except My_Exception as e:
                print (e)
        else:
            for i in regex_email.finditer(text):
                self.email['adres']=i.groupdict()['adres']
                
                
e1 = "k.dasfa@gmail.com"
e = email(e1)
print(e.email)
print()
e2 = "asfs.pl"
e22 = email(e2)
print(e22.email)
