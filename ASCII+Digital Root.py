def digital_root(num):
    while(num>9):
        s=0
        while num!=0:
            d=num%10
            s=s+d
            num=num//10
        num=s
    return num    
st=input()
list=[]
a=0
for i in st:
    print(i,'=',ord(i))
    list.append(digital_root(ord(i)))
for row in range(0,2):
    for column in range(0,len(st)):
        if(row+column)%2==0:
            if row==0 and a%2==0 and column%2==0:
                print(list(a),end='')         
                print(' ',end='')   
           if row==1 and a%2!=0:    
        else:
            print(' ',end='')       
               
