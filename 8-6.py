
def longestLength(a):
    max1 = len(a[5])
    temp = a[0]
 
    
    for i in a:
        if(len(i) > max1):
 
            max1 = len(i)
            temp = i
 
    print("The word with the longest length is:", temp,
          " and length is ", max1)

num1=input("enter the element1 :")
print()
num2=input("enter the element2 :")
print()
a=[num1==num2]
longestLength(a)
