def digital_root(num):
    while(num>9):
        s=0
        while num!=0:
            d=num%10
            s=s+d
            num=num//10
        num=s
    return num    
'''def digital_root(num):
    if (num==0):
       return 0
    elif(num%9==0):
       return 9
    else:
       return num%9'''
num = int(input())
print(digital_root(num))    