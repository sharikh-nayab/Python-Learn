import re
s="2_user_name"
x=r"^[A-Za-z][A-Za-z0-9]*"
if re.match(x,s):
    print("valid")
else:
    print("invalid")