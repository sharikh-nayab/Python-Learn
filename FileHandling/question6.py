with open("Filehandling/Data.csv","r") as fp:
    fp.readline()
    r=fp.readline()
    a=[]
    c=[]
    while r:
        s=r.split(",")
        a.append(s[3])
        r=fp.readline()
    b=set(a)
    for i in b:
        w=a.count(i)
        c.append(w)
    l=max(c)
    # print(l)
    p=c.index(l)
    # print(p)
    print(l,a[p])