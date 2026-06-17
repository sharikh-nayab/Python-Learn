with open("FileHandling/Data.csv","r") as fp:
    fp.readline()
    r=fp.readline()
    while r:
        s=r.split(",")
        # print(s[2],s[28],s[29])
        a=float(s[28])+float(s[29])
        print("Trade ID: ",s[2],"Total of Comission & Tax: ",a)
        r=fp.readline()