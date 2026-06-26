import re
s="23:50"
x=r"^(0[00-09]|1[0-9]|2[0-3]):|(0-5)|(0-9)&"
if re.match(x,s):
    print("Valid")
else:
    print("Not Valid")