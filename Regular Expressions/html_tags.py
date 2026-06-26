import re

s="<div><p>Hello World</p></div>"
x=r"<([A-Za-z/]+)>"
a=re.findall(x,s)
print(a)