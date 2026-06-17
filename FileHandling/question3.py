with open("FileHandling/Data.csv","r") as fp:
    fp.readline()
    r=fp.readline()
    sm=0
    while r:
        s=r.split(",")
        a=(s[8]+s[9]).strip().replace('"','')
        b=float(a)
        sm=sm+b
        r=fp.readline()
    print(sm)