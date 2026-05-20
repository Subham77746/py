print("Exercise-1")

a=int(input("Enter a Number: "))
b=int(input("Enter Another Number: "))

print("Use an operator like Add,Sub,Mul,Div,Mod")
c=input(" Choose Add,Sub,Mul,Div,Mod: ")

if c== "Add":
    print(a+b)
          
elif c== "Sub":
    print(a-b)
          
elif c== "Mul":
    print(a*b)
          
elif c== "Div":
    print(a/b)
          
elif c== "Mod":
    print(a%b)
          
else:
    print("Invalid Operator")
           
              
#identity operator (is & is not)
a=10
b=10
if a is b:
    print("same")   #same

#membership operator (in & not in)
x=[10, 20, 30]
if 20 in x:
    print("present")    #present