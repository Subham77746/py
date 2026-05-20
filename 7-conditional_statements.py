#if...
a=10
if a>0:
    print("Positive number")
    
 #if...else
 #Count Total Salary By Taking Basic Salary...
BS=int(input("Enter Your Basic Salary: "))
print("As Your Basic Salary Is: ", BS)
if BS > 10000:
    hra=BS*0.25
    da=BS*0.10
    ta=BS*0.5
else:
    hra=BS*0.10
    da=BS*0.5
    ta=BS*0.2
tot=BS+hra+da+ta
print("HRA= ",hra, "DA= ",da, "TA= ",ta)
print("Your Net Salary Is: ",tot)

#ladder else if....
a=int(input("Please Enter Your Age: "))
if (a<18):
    print("You can't drive")
elif (a>=18):
    print("You can drive")
else:
    print("Invalid") #invalid

#MATCH (switch statement...)
day=int(input("enter your day number: "))
match day:
    case 1:
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case _ :                #Default
        print("Invalid")
