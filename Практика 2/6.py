x = 16.55 * 10 ** -3
y = -2.75
z = 0.15
import math
s = math.sqrt(10 * (x ** (1./3.) + x ** (y + 2))) * (math.asin(z)**2 - abs(x - y))
print(round(s, 4))
