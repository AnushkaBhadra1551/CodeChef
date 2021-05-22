t = int(input())

if(0<t<1001):
    for i in range(0, t):
        n = input()
        c=n[::-1].strip('0')
        print(c)