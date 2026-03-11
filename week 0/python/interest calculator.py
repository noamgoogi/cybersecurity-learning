import math
P = int(input())
r = int(input())
t = int(input())

A = P*(math.pow((1+(r/100)),t))
print(A)