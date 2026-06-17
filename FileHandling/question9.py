with open("FileHandling/Data.csv","r") as fp:
    fp.readline()
    r=fp.readline()
    while r:
        s=r.split(",")
        a=s[4]
        if a[:2] == "CA" and a[2:].isdigit():
            print("Valid")
        else:
            print("Invalid")
        r=fp.readline()