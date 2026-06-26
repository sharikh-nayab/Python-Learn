import re
s="The event is scheduled on 15-08-2026."
x=r"[0-9]{2}-[0-9]{2}-[0-9]{4}"
a=re.search(x,s)
print(a)