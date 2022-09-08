print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<90:
    print("Your Grade is A2")
elif avg>=71 and avg<80:
    print("Your Grade is B1")
elif avg>=61 and avg<70:
    print("Your Grade is B2")
elif avg>=51 and avg<60:
    print("Your Grade is C1")
elif avg>=41 and avg<50:
    print("Your Grade is c2")
elif avg>=0 and avg<50:
    print("Your Grade is D")
else:
    print("Invalid Input!")
