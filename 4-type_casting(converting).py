#Type Conversion...
# 1. Converting string to int...
a = "1"
b = "2" 
print(a+b)      #12...( due to string)
print(int (a)+int (b))  #3(string-->int)

# 2. int --> string
a=1
b= str(a)
print(type(b))  #string

# 3. int --> complex
a=10
b= complex(a)
print(b)    #(10+0j)

#[or]

c=complex(a, 5)
print(c)    #(10+5j)

# 4. bool --> int
a=True
b= int(a)
print(b)    #1

# 5. int --> bool
x=0.123
y=""
z="ab"

a=bool(x)
print(a)    #True

b=bool(y)
print(b)    #False(ASCII)

c=bool(z)
print(c)    #True (ASCII)

# 6. hexa --> complex
a="0XIC"
b=int(a)
print(b) # 28+0j

# 7. complex --> str
a=10+0j
b= str(a)
print(b)    #10+0j

#8. str --> complex
a="10+0j"
b=str(a)
print(b)    #10+0j

#Implicit typecasting (where python automatically convert)...
a=6      #int.
b=1.7    #float
c= a+b   #(a=int -> float) + b=float
print(c) #7.7 (python converts a->float then add with b)
