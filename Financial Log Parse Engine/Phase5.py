with open("Financial Log Parse Engine\Data.csv","r") as fp:
    fp.readline()
    r=fp.readline()
    l=[]
    sm=0
    c={}
    while r:
        s=r.split(",")
        a=s[6]+s[7]
        a=a.replace('"',"")
        a=a.replace(",","")
        t=(s[2],s[3],a,s[19])
        l.append(t)
        r=fp.readline()
    # print(l)
    for i in l:
        # print(i[2])
        sm=sm+int(i[2])
    b=i[1]
    if b in c:
        c[b]+=1
    else:
        c[b]=1
    print(sm,c)

