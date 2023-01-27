x=int(input("Enter the Year to check if it is a leap year or not:"))
if x%4==0 and x%100!=0:
    print("The entered Year is a leap year")
elif x%100==0 and x%400==0:
    print("The entered Year is a leap year")
else:
    print("The entered Year is not a leap year")