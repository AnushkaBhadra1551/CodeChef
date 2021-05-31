t = int(input())
for i in range(0,t):
    a=list(map(int,input().split()))
    a.sort()
    print(a[1])