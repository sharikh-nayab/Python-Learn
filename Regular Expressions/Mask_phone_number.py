import re
s="9552747966"
x=r"^(.{6})"
a=re.sub(x,"******",s,count=6)
print(a)