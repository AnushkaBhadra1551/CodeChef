n = int(input())
even = 0
odd = 0

a = list(map(int,input().split()))
for i in a:
    if(i%2==0):
        even = even + 1
        
    else:
        odd = odd + 1

if(even>odd):
    print("READY FOR BATTLE")
elif(even==odd):
    print("NOT READY")
else:
    print("NOT READY")
