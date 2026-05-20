a="Subham"
b="Panigrahy"

#merging Strings...
print("My Name Is: ",a+" "+b)   #My Name Is:  Subham Panigrahy

#join of string
x=["subham","panigrahy"]
y='_'.join(x)
print(y)        #subham_panigrahy

#lenght of a...
print(len(a))   #6

#printing single character...
print(a[0])     #S

#Printing whole characters using for loop...
for character in a:     #S   #b  #a
    print(character)    #u   #h  #m

#String Slicing...
print(a[0:4])       # 0 included 4 excluded ---> o/p= Subh
    #Negative Slicing (python automatically do ---> -2= len(a)-2)
print(a[0:-3])      #a[0:len(a)-3] ---> a[0:2] ---> o/p= Su
print(a[-4:-2])     #(a[len(a)-4 : len(a)-2]) ---> 2:4 ---> o/p= bh
print(a[::-1])      #mahbus (reverce)

#Functions...
print(len(a))       #6
print(a.upper())    #SUBHAM
print(a.lower())    #subham

b="sachi777@"
c="subham  777  sachi"

print(b.rstrip("@"))                #trim only right side white space or  character part  #sachi777
print(b.lstrip("s"))                # trim left side only  #achi777@
print(c.strip("s,i"))               #trim both sides space or character if given

print(b.replace("sachi","subham"))  #subham777@

print(c.split(" "))                 #['subham', '', '777', '', 'sachi']

print(b.center(40))                 #               sachi777@ 

print(b.count("7"))                 #3 (7 repeats 3 times)

print(b.endswith("@"))              #True
print(c.endswith("777", 7, 11))     #True

print(c.startswith("subham"))       #True

#find() & index() both same but if ch. is not present find returns (-1) but index returns ERROR
print(c.find("777"))                #8 (start at index-8)
print(c.index("7"))                 #8 

print(b.isalnum())                  #(False) isalnum = Alpha Numeric (contain only A-Z, a-z, 0-9)

print(b.isalpha())                  #(False) isalpha = Alphabets only (A-Z, a-z)

print(b.isupper())                  #(False)isupper = Only in Upper case
print(b.islower())                  #(True) islower = Only in Lower case

print(b.isprintable())              #(True) if \n then not printable

print(c.isspace())                  #(false) returns true olny if space or tab is present

print(c.istitle())                  #(false) identifies if the title is in each letter of word is capitalized

#Change Case of STRING...
print(c.title())                    # Subham  777  Sachi (convert into title case-> first ch of each word capital)
print(b.capitalize())               #Sachi777@ (first ch of sentence is capital)
print(b.swapcase())                 # SACHI777@ (convert lower-->upper, upper-->lower)


#Formating of string...
name="subham"
age=18
print("{}'s age is {}".format(name, age))

#f-STRING method in py.....
place="india"
name="subham"
line=(f"Hello My name is {name}, I am from {place}")
print(line)         #Hello My name is subham, I am from india

number=10.12345
print(f"2 number after decimal is: {number:.2f}")   #2 number after decimal is: 10.12

print(f"{2*30}")        #60