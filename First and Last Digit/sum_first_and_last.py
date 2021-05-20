t = int(input())

if(0<t<1001):
    for i in range(0, t):
        n = int(input())
        first = n
        last = n % 10
        while(first >= 10):
            first = first // 10
        s = first + last    
        print(s)