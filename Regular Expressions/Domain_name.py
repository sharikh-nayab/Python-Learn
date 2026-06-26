import re
s="https://www.logicoverflow.com/index.html"
x=r"https://www.([A-Za-z/]+)"
a=re.findall(x,s)
print(a)
