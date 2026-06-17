with open("FileHandling\Data.csv","r") as fp:
    fp.readline()
    r=fp.readline()
    sm=0
    a=set()
    while r:
        data=r.split(",")
        s=data[19]
        a.add(s)
        r=fp.readline()
    l=list(a)
    l.sort()
    for i in l:
        sm=sm+1
    print(l,"unique client name", sm)
        

