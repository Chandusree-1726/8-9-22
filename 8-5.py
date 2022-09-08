a = int(input("Please Enter the total Number of Rows  : "))
number = 0

print("Floyd's Triangle") 
for i in range(1, a + 1):
    for j in range(1, i + 1):        
        print(number, end = " ")
        number = number + 1
    print()
