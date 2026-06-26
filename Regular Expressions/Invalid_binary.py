import re
s="10101102"
x=r"^[01]+"
if re.fullmatch(x,s):
    print("valid")
else:
    print("invalid")