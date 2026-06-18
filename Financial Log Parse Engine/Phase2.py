with open("Financial Log Parse Engine\Data.csv") as fp:
    fp.readline()
    r=fp.readline()
    a=[]
    while r:
        s=r.split(",")
        if s[2]!="":
            a.append(s[0:])
        else:
            print("empty Trade ID found")
        r=fp.readline()
    print(a)