k = int(input())
v = int(input())
if v < k:
    Z = v - k + 1
elif k > v:
    Z = k ** 2 - v ** 2
else:
    Z = k ** 2 - k
print(Z)
