t = int(input())

if(0<t<1001):
    for i in range(0, t):
        a, b = input().split()
        a = int(a)
        b = int(b)
        rem = a % b
        print(rem)
