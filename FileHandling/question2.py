with open("Filehandling/Data.csv") as fp:
    # print(fp.readlines())
    fp.readline()
    r=fp.readline()
    sm_v=0
    sm_c=0
    while r:
        data=r.split(",")
        s=data[2]
        if s != "":
            sm_v=sm_v+1
        else:
            sm_c=sm_c+1
        r=fp.readline()
    print("Valid Transaction: ", sm_v)
    print("Corrupted Transaction:", sm_c)
