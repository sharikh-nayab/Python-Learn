import re
s="The loop ends code here"
x=r"[A-Za-z]{4}"
a=re.findall(x,s)
print(a)