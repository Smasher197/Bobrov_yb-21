x = int(input())
y = int(input())
if x < 2 and y == 2:
    B = x * y + 1
elif x > y:
    B = y ** 2 + x ** 2
else:
    B = x ** 2 + 2
print(B)
