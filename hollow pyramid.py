''' *    
   * *   
  *   *  
 *     * 
*********   '''
n=int(input())
for i in range(1,n+1):
    for j in range(1,2*n):
        if j==n-i+1 or j==n-1+i or n==i:
            print('*',end='')
        else:
            print(' ',end='')
    print()   

