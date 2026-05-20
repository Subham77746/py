#1
name= "Subham"
for i in name:
    print(i)    #S u b h....

#in list
colors=["Red","Green","Blue"]
for color in colors:
    print(color)    #Red..Green..Blue...
    for i in color:
        print(i)    #Red..R..e..d...Green..G..r..e..e..n....

#RANGE...
for i in range(5):
    print(i)    #1..2..3..4

for i in range(1,10):
    print(i)    #1..2..3..4..5.....9

#multiplication table..
a=int(input("Enter a number: "))
print("multiplication table of ",a, "is: ")
for i in range (1, 11):
    print(f"{a} X {i} = {a*i}")

#adding all even from(1-10)   
sum=0
for i in range (1, 11) :
    if(i%2==0):
        print(i)
        sum=sum+i
print("sum= ",sum)

#While loop...
a=1
while(a<=10):
    print(a)    #1.2.3.4.5.6.7.8.9.10
    a=a+1

b=5
while(b>0):
    print(b)    #5..4..3..2..1
    b=b-1

#DO WHILE IN PY...
while True: 
    i=int(input("Enter a number: "))
    print(i)
    if(i>=10):
     print("you entered: ", i)
     break

#for with else
#1....
for i in range(5):
    print(i)
else:
    print("loop ends here")         #0134..loop ends

#2....
i=0
while i<6:
    print(i)
    i=i+1
else:
    print("end")            #012345...end

#3...
i=0
while i<6:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("end")            #01234


#one liner in if....else (Short-Hand)
a=2 
b=5
print("2") if a>b else print("5") if b>a else print("=")
#or
print("b>a") if a<b else " "    