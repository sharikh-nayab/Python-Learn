import re
s="Logic Overflow"
x=r"[aA]|[eE]|[iI]|[Oo]|[uU]"
a=re.findall(x,s)
sm=0
for i in a:
    sm=sm+1
print(sm)