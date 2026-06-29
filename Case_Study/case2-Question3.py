with open(r"Case_Study\byte_telemetry.txt","r") as fp:
    fp.seek(10,0)
    print(fp.readline().strip())
    