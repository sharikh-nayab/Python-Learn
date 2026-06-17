with open("FileHandling/Data.csv","r") as fp:
    fp.readline()
    r=fp.readline()
    while r:
        s=r.split(",")
        sm=float(s[5])*float(s[15])
        if sm > 5000:
            print("Trade Id", s[2], "Client Name",s[19], "Calculated Trade Value",sm)
        r=fp.readline()