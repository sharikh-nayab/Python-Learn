import re
s="Regex@2026"
x=r"[A-Z]"
y=r"[a-z]"
z=r"[0-9]"
t=r"[$*+?{}\\()@#!%&_]"
if re.search(x,s):
    if re.search(y,s):
        if re.search(z,s):
            if re.search(t,s):
                print("strong")
            else:
                print("weak t")
        else:
            print("weak z")
    else:
        print("weak x")

else:
    print("weak s")