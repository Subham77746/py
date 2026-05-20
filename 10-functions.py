#1.Functions in py...
def add_numbers(a,b):
    sum=(a+b)
    print(sum)

x=10
y=20
add_numbers(x,y)    #30

#2...
def compare(a,b):
    if(a>b):
        print("a is greater than b")
    elif(a==b):
        print("a is equal to b")
    else:
        print("b is greater than a")

p=20
q=20
compare(p,q)    #compare(20, 20)

#3...
def avg(a=2, b=6):
        print("Avg is",(a+b)/2)
    
avg(4,4)    #4.0....ignores upper values..
avg(b=8)    #5.0....takes a=2(above) & b=8..

#4...
def average(*numbers):  #here numbers creates a list or tuple where we set multiple values...
     sum=0
     for i in numbers:
        sum=sum+i
        print("average is: ",sum/len(numbers))

average(2,3,4,3)    #3.0
     