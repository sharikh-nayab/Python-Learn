import re
s="The price is cheap (only for today)."
x=r"\(.*\)"
a=re.sub(x,"[Masked]",s)
print(a)