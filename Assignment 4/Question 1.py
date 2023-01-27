x=int(input("Enter the Marks of the Student:"))
if x<25:
    print("The Student gets the grade F")
elif 25<=x<45:
    print("The Student gets the grade E")
elif 45<=x<50:
    print("The Student gets the grade D")
elif 50<=x<60:
    print("The Student gets the grade C")
elif 60<=x<80:
    print("The Student gets the grade B")
elif 80<=x<100:
    print("The Student gets the grade A")
elif x>100:
    print("Error! Marks can't be higher than 100")
