print("hello world")
print(5+4)

#line break statement
print("Subham \n Panigrahy")

#variables...
a = 5
b = 2
print(a+b)

#Data Types...
#Funamental Data Type...
a=5
print(type(a))   #int
b="subham"
print(type(b))   #string
c=2.24
print(type(c))   #float
d=True
print(type(d))   #boolean
e=10+0j
print(type(e))   #complex

#Other Data Types...
#1. LIST
l1=[]                               #empty list
l2=[1,2,3,4,5]                      #same data type list
l3=[1,2,3,4,5,"subham","sachi"]     #diff D.T list
print(type(list));                  #list

#2.TUPLE
f=(1,2,3,4,5)
print(type(f));                      #tuple

#3.COMPLEX (real + imaginary)
g= complex(1, 8)
print(g)                                #(1+8j)
print(type(g));                         #complex

#4.BYTES...
a=[1,2,3,4,5]
b=bytes(a)
print(type(b))      # bytes(values of byted can't changeble)

#5.BYTEARRAY...
a=[1,2,3,4,5]
b=bytearray(a)
print(type(b))      # bytearray(values of bytearray can changeble)

