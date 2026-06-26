import re
s="Python programmers prefer patterns."
x=r"([Pp][A-Za-z]+)"
a=re.findall(x,s)
print(a)