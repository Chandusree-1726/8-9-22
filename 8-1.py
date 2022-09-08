def isHappy(n):    
    r = s = 0;    
    while(n > 0):    
        r = n%10    
        s += r**2     
    return s  
        
n = int(input())    
res = n;    

while(res != 1 and res != 4):    
    print("happy number")
else   :
    print("not a happy number")
ishappy(n)
