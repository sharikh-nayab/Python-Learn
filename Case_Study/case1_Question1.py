import re
with open(r"Case_Study\transaction_logs.txt","r") as fp:
    # fp.readline()
    r=fp.readline()
    while r:
        x=r"^TXN-\d+"
        a=re.findall(x,r)
        print(a)
        r=fp.readline()