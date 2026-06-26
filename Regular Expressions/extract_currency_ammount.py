import re
s="The total cost is $45.99 and shipping is £5.00."
x=r"([$£][0-9.]{4}+)"
a=re.findall(x,s)
print(a)