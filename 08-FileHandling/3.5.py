###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input("enter username:")
password = input("enter password")

# pattern (criteria) for username and password
username_pattern = '.{6,}{^\W}'
password_pattern = '.{8,}{\w}{\W}'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if password_match and username_match:
   print("ok")
else:
   print("fail")