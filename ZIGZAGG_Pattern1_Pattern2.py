l=[1,4,6,3,5,7,8]
#n=int(input())
for i in range(0,len(l),2):
        print(l[i],end=" ")
print()
for i in range(1,len(l),2):
        print(" ",l[i],sep="",end="")
print()
#
#for 3
for i in range(0,len(l),4):
        print(l[i],end=" "*3)
print()
for i in range(1,len(l),2):
        print(" ",l[i],sep="",end="")
print()
for i in range(2,len(l),4):
    if i==2:
        print("  ",l[i],sep="",end="")
    else:
        print("   ",l[i],sep="",end="")
