#list=[....], tuple=(....), sets={.....}
s={1,2,3,4}
print (s)   #{1, 2, 3, 4}

u={1,2,3,4,4}
print(u)    #{1, 2, 3, 4} (avoids duplication)

b={"subham", 4, False, 3.87}
print(b)    #{False, 3.87, 4, 'subham'} (not in order but accept multiple data types)

#an empty set is a dictionary..
h={}
print(type(h))      #<class 'dict'>

#to create an empty set use set()....
a=set()
print(type(a))      #<class 'set'>

#SET operations...
a={1,2,3,4,5}
b={3,4,5}

#union...
print(a.union(b))      #{1, 2, 3, 4, 5} (give all elements)

#intersection...
print(a.intersection(b))  #{3, 4, 5} (give elments present in both side)

#update
a={1,2,3,4}
b={5,6,7}
a.update(b)     #include all ements in a that presents in b
print(a, b)     #{1, 2, 3, 4, 5, 6, 7} {5, 6, 7}        

#symmetric diference......(analies both sides)
a={"subham", "sachi", "sachin"}
b={"shivam", "sachin", "sachi"}
c=a.symmetric_difference(b)     #gives elements not present in both sides
print(c)        #{'subham', 'shivam'} 

#difference....(analies only one side)
a={"subham", "sachi", "sachin"}
b={"shivam", "sachin", "sachi"}
c=a.symmetric_difference(b)   # a-b (gives values present in a but not in b)

#disjoint
a={"subham", "sachi2", "sachin2"}
b={"shivam", "sachin", "sachi"}
c=a.isdisjoint(b)
print(c)            #True

#superset
a={"subham", "sachi", "sachin"}
b={"shivam", "sachin", "sachi"}
c=a.issuperset(b)
print(c)            #False (all elements of b not in a)

#subset
a={"subham", "sachi", "sachin"}
b={"subham", "sachin", "sachi"}
c=a.issubset(b)
print(c)            #true (all elem. of b is in a)

#adding element specificly in set...
a={"subham", "sachi", "sachin"}
a.add("rohan")
print(a)        #{'rohan', 'sachin', 'subham', 'sachi'}

#remeove an specific element from a set
a={"rohan", "subham", "sachi", "sachin"}
a.remove("rohan")
print(a)        #{'subham', 'sachin', 'sachi'}

#pop
a={"rohan", "subham", "sachi", "sachin"}
a.pop()
print(a)    #{'sachi', 'sachin', 'subham'} (remove diff element in diff. time)

#clear
a={"rohan", "subham", "sachi", "sachin"}
a.clear()
print(a)     #set()

a={"rohan", "subham", "sachi", "sachin"}
if "subham" in a:
    print("present")        #present
else:
    print("not present")