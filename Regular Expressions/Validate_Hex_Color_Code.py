import re
# s=input("Enter ")
s="#A3C1AD"
x=r"^#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$"

if re.search(x,s):
    print("Valid")
else:
    print("Invalid")