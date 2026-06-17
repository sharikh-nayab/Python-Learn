with open("Filehandling/Data.csv","r") as fp:
    a=[]
    fp.readline()
    r=fp.readline()
    while r:
        s=r.split(",")
        b=s[2],s[3],s[15]
        a.append(tuple(b))
        r=fp.readline()
    for i in a:
        print(f"Trade {i[0]} was handled by Broker {i[1]} at unit price of ${i[2]}")