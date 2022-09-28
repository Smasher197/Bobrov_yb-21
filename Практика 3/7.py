v = int(input())
k = int(input())
if v < 2 and k == 1:
    B = v - k + 1
elif k > v:
    B = k ** 2 + v ** 2
else:
    B = k ** 2 + v
print(B)
