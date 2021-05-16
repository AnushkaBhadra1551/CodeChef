X, Y = input().split()
X = float(X)
Y = float(Y)
s = Y - X - 0.50

if(X % 5 == 0) and (X + .5 <= Y):
    print('%.2f'%s)

else:
    print('%.2f'%Y)