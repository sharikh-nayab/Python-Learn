import re

s="Coding is fun! #Python #Regex_101 #logic"
x=r"#[A-Za-z0-9_]+"
a=re.findall(x,s)
print(a)