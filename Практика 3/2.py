f = int(input())
k = int(input())
if f < 5 and k > 2:
    R = f + k - 1
elif k < 2:
    R = k ** 2
elif k == 2:
    R = 1
print(R)
