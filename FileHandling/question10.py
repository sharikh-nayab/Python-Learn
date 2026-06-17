with open("FileHandling/Data.csv","r") as fp:
    fp.readline()
    r=fp.readline()
    while r:
        s=r.split(",")
        a=set((s[0],s[27]))
        print(a)
        r=fp.readline()