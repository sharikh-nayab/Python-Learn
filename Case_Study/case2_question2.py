with open(r"Case_Study\byte_telemetry.txt","r") as fp:
    r=fp.readline()
    while r:
        print(fp.tell())
        r=fp.readline()