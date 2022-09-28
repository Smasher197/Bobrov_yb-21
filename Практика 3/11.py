x = int(input())
y = int(input())
if x == 4 and y < 2:
    q = x + x * y
elif x < y:
    q = y ** 2 + 1
else:
    q = y ** 2 + 4
print(q)
