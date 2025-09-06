n=int(input())
h=int(input())
for r in range(h):
    for i in range(n):
        for j in range(n-i):
            print(' ',end='')#1st method to print space
        for k in range(i+1):
            print('*', end=' ')
        print()
    for i in range(n-1,0,-1):
        print(end=' ')
        for j in range(n-i):
            print(end=' ')#2st method to print space
        for k in range(i):
            print('*', end=' ')
        print()
