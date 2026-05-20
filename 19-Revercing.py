#reverce of integer
a=12345
rev=0
while a>0:
    digit=a%10
    rev=rev*10+digit
    a = a//10
print(rev) 

#swaping...
#1.
x=10
y=20
z=30

p=x
x=y
y=p
print(x,y,z)    #20,10,30
        #or
#2.        
x=40
y=2
a=(x+y)-x
b=(x+y)-y
x=a     #reassign a to x
y=b     #ressign b to y
print(x,y)  #2,40

#reverce of string
a="subham"
print(a[::-1])      #mahbus

#or

print("".join(reversed(a))) #mahbus

#or
i=len(a)-1
target=''
while(i>=0):
    target=target+a[i]
    i=i-1
print(target)       #mahbus