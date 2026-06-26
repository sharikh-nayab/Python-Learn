import re
s="Python,Regex;Logic Overflow"
x=r"[,]|[;]|[ ]"
a=re.split(x,s)
print(a)