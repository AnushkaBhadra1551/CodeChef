a = b = 0

l = m = 0
n = int(input())
for i in range(0,n):
    si, ti = input().split()
    si = int(si)
    ti = int(ti)
    l = si + l
    m = ti + m

    if(l > m):
        a = max(a, l-m)

    else:
        b = max(b, m-l)

if(a > b):
    print(1 , a)
else:
    print(2 , b)