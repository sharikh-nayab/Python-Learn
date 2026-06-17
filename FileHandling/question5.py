with open("FileHandling/Data.csv","r") as fp:
    fp.readline()
    r=fp.readline()
    a=0
    b=0
    while r:
        s=r.split(",")
        d=s[13]
        f=s[5]
        if d == "R":
            a=a+int(f)
        elif d == "S":
            b=b+int(f)
        r=fp.readline()
    if a >b:
        print("sales trades had higher volume \n sell total= ",a, " receive total= ",b)
    else:
        print("Receieve trades had higher volume \n Receive total= ",b, " sell total= ",a)
