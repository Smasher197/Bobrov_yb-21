a = int(input())
b = int(input())
if a < b:
    R = a - b + 1
elif a > b and a > 3:
    R = b ** 2 - b
else:
    R = b ** 2 - 1
print(R)
