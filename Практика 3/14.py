k = int(input())
f = int(input())
if f < k:
    R = f + k ** 2 - 1
elif f == 3 and k < 2:
    R = k ** 2
else:
    R = f - 1
print(R)
