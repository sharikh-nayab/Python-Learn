a=int(input("Please enter value "))
b=int(input("Please enter value "))
if a > 0 and b >0:
    print("1")
elif a < 0 and b > 0:
    print("2")
elif a < 0 and b < 0:
    print("3")
elif a > 0 and b < 0:
    print("4")
elif a != 0 and b == 0:
    print("X")
elif a==0 and b != 0:
    print("Y")
else:
    print("Origin")
