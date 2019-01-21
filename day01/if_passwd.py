# Author:黑猴子

import getpass

_username = 'abc'
_password = 'abc123'

username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")

#缩进
'''
ssh if  fi
java {}
没有关系，一定要顶格写
'''
if _username == username and _password == password:
    print("Welcome user {name} login...".format( name = username))
else:
    print("Invalid username or password!")
