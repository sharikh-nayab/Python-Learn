import re
s="-125"
x=r"^[+-]?[0-9]+$"
if re.search(x,s):
    print("valid")
else:
    print("invalid")