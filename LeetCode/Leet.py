# x=input("enter ")
# if x == x[::-1]:
#     print("palindrome")
# else:
#     print("Not palindrom")
x = input("enter ")
s = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
total = 0
i = 0
while i < len(x):
    if i < len(x) - 1:
        current = s.get(x[i])
        next_value = s.get(x[i + 1])
        if current < next_value:
            total = total + (next_value - current)
            i = i + 2
            continue
    total = total + s.get(x[i])
    i = i + 1
print(total)
