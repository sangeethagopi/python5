import math 
  
# A function to print all prime factors of  
# a given number n 
def primeFactors(a1,b1): 
    if(b1==1 and a1>b1):
        n = 1
        for o in range(1,a1+1,1):
            n = n*o
    if((a1-b1)==1):
        n = a1
    if((a1-b1)>1 and b1!=1):
        n1 = b1+1
        n2 = a1
        n = 1
        for p in range(n1,n2+1,1):
            n = n*p
            
    pfun(n)
    
    
def pfun(n):    
    u = []
    while n % 2 == 0: 
        u.append(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            u.append(i)
            n = n / i 
    
    print(len(u))
        

m = input()
m = int(m)
for r in range(0,m+1,1):
    a1,b1 = input().split()
    a1 = int(a1)
    b1 = int(b1)
    if(a1>b1):
        primeFactors(a1,b1)
