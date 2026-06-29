import re
with open(r"Case_Study\transaction_logs.txt","r") as fp:
    r=fp.readline()
    q=set()
    while r:
        x=r"[A-Za-z]+@[A-Za-z.-]+\.[A-Za-z]{2,}+"
        a=re.findall(x,r)
        # print(a)
        for i in a:
            b=i.split("@")
            q.add(b[1])
        r=fp.readline()
    # print(q)
with open("Case_Study\harvested_domains.txt","w") as fp:
    g=list(q)
    g.sort()
    fp.writelines(g)
        