a=[1,2,3]
print(a,type(a))    #1, 2, 3] <class 'list'>

#we can store multiple with different data tye values in a lits...
s=["subham", "B.sc CS", "802", 55, 44, True]
print(s)    #['subham', 'B.sc CS', '802', 55, 44, True]

print(s[1:4])       #['B.sc CS', '802', 55]
print(s[1:6:2])     #['B.sc CS', 55, True]....print 1st index upto 6th with jumping 2 values
print(s[-3])        #55
print(s[len(s)-3])  #55
print(s[1:-3])      #['B.sc CS', '802']


if 55 in s:
    print("Yes") #Yes..(in s 55 present)
else:
   print("No")

list=[i for i in range(4)]
print(list) #[0, 1, 2, 3]

#list methods...
#1.
a=[5,1,2,3,9]
print(a)        #[5, 1, 2, 3, 9]
print(type(a))  #<class 'list'>

#2
a.append(4)     # add 4 at last
print(a)        #[5, 1, 2, 3, 9, 4]

#3
a.sort()        #//ASSENDING ORDER
print(a)        #[1, 2, 3, 4, 5, 9]

#4
a.sort(reverse=True)    #DESCENDING ORDER
print(a)         #[9, 5, 4, 3, 2, 1]

#4
a.reverse()       # reverce the original list
print(a)          #[1, 2, 3, 4, 5, 9]

#5
print(a.index(9))
print(a)        #5 (gives the index number of 9)

#6
print(a.count(1))   #gives howmany times 1 repeat in list
print(a)           #1


    #HERE   (a = [1, 2, 3, 4, 5, 9])

#7
b=a         
b[0]=0
print(b)    #[0, 2, 3, 4, 5, 9]
print(a)    #[0, 2, 3, 4, 5, 9] (changes list(a) also so here use copy method)

#8
b=a.copy()  
b[0]=0
print(b)    #[0, 2, 3, 4, 5, 9]
print(a)    #[1, 2, 3, 4, 5, 9] (here due to copy is used a remains unchanged)

#9
a.insert(5, 6)  #at 5th index adds 6 
print(a)        #[1, 2, 3, 4, 5, 6, 9]

#10
b=[10,11,12]
a.extend(b) #adds list b in last of list a
print(a)    #[1, 2, 3, 4, 5, 9, 10, 11, 12]

#11
a=[1, 2, 3, 4, 5, 9]
b=[10,11,12]
c=a + b
print(c)    #[1, 2, 3, 4, 5, 9, 10, 11, 12]