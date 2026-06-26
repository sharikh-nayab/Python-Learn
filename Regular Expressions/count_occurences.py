import re
s="Regex is great. I love regex."
x=r"\bregex\b"
a=re.findall(x,s, re.IGNORECASE)
print(len(a))