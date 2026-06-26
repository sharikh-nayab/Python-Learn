import re

s="Python is    awesome"
x=r"[ \t\n]+"
a=re.sub(x," ",s)
print(a)