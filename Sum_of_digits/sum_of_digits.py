t = int(input())
m = 0

if(t>0):
    for i in range(0, t):
        n = int(input())
        s=0
        while(n>0):
            m = n%10
            s=s+m
            n=n//10
            
        print(s)