# DOC STRING has to declare before the print statement...
def square(n):
    "This is not a comment.. it's a doc string..."
    print(n**2)
square(5)

print(square.__doc__)  #using of doc_string...


#Resursion is basically a function (calling a function inside itself)...
#factorial...
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) 

print(factorial(3))

#FIBONACCI series   1-1-2-3-5-8-13....(get the line by adding previous two no. 5 comes adding 3+2)
def fibonic(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonic(n-1) + fibonic(n-2)
    
print(fibonic(6)) #Fn=Fn-1 + Fn-2 (F6= F5+F4 = 5th + 4th fibonacci no. [5+3=8]))