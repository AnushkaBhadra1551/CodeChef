n = int(input())
for i in range(0, n):
    num = int(input())
    num_1 = str(num)

    if(num_1[::-1]==str(num)):
        print("wins")
    else:
        print("loses")
