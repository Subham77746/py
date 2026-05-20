a=int(input("Enter a number: "))
print("multiplication table of ",a, "is: ")
for i in range (1, 11):
    print(f"{a} X {i} = {a*i}")


#try.......expect Expections as i (print the error in your code then continue remaining code not break it)
try:
    a=int(input("Enter number: "))
except Exception as i:
    print(i)
    print("Succesful")      #Enter number: subham
                            #invalid literal for int() with base 10: 'subham'
                            #Succesful

#if for loop makes error then execution will be end here. imp codes after this not execute so to execute remaining code use exception....after or loop...
try:
    a=int(input("Enter a number: "))                                                     
    print(f"Your entered number for multiplication is: {a}")
    for i in range (1, 11):
        print(f"{int (a)} X {int (i)} = {int (a*i)}") 
        
except Exception as e:
    print(e)

print("some important codes...")     

#printing multiple except for diff. errors
try:
    a=int(input("Enter a number: "))
    b=[6, 3]
    print(b[a])     #if 0 give 6 if 1 gives 3

except ValueError:
    print("invalid") #if we enter alphabet shows invlid
except IndexError:
    print("print 0 or 1")   #if we enter more than 1 index sows 9 or 1 only

#finally in try...except
try:
    a=[1,2,3,4,5]
    b=int(input("enter a number: "))
    print(a[b]) #print the index of a...
except:
    print("invlid")
finally:        #no matter either try runs or except finally always runs at the end.
    print("prog. ends here")    

#raising value error in py...
a=int(input("Enter a number between 1-5: "))    
if(a>5 or a<1):
    raise ValueError ("You entered wrong number...")