import math
t = int(input())

if(0<t<21):
    for i in range(0, t):
        n = int(input())
        square = math.sqrt(n)
        s = math.floor(square)
        print(s)