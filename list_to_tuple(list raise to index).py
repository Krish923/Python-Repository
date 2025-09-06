n=int(input())
listt=list(map(int,input().split()))
for i in range(n):
    listt[i]=listt[i]**i
print(tuple(listt))
