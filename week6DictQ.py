s1={}
v=int(input())
for i in range(v):
    ik=int(input())
    iv=int(input())
    s1[ik]=iv
s2={}
v=int(input())
for i in range(v):
    ik=int(input())
    iv=int(input())
    s2[ik]=iv
s3={}
for i in s2.keys():
    for j in s1.keys():
        if i==j:
            s3[i]=s1[i]*s2[j]
for i in s2.keys():
    for j in s1.keys():
        if j not in s3.keys():
            s3[j]=s2[j]
        elif i not in s1.keys():
            s3[i]=s1[i]
        else:
            pass
print(s3)
