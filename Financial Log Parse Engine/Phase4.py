with open("Financial Log Parse Engine\Data.csv","r") as fp:
    fp.readline()
    r=fp.readline()
    l=[]
    g=set()
    while r:
        s=r.strip().split(",")
        a=s[6]+s[7]
        a=a.replace('"',"")
        a=a.replace(",","")
        t=(s[2],s[3],a,s[19])
        l.append(t)
        r=fp.readline()
    for i in l:
        g.add(i[3])
    p=list(g).sort()
    print(repr(p))