#Operation On List...
#len()...max()...min()
a=[1,2,3,4,5]
print(len(a))       #5
print(max(a))       # max number :- 5
print(min(a))       # min number :- 1

#list()...
a='subham'
b=list(a)           # convert any data type into list
print(b)            #['s', 'u', 'b', 'h', 'a', 'm']

#sorted()..
a=[4,2,3,1,5]
b=sorted(a)         #assending order
print(b)            #[1, 2, 3, 4, 5]

#reverse
a=[1,2,3,4,5]
a.sort(reverse=True)
print(a)             #[5, 4, 3, 2, 1]

#append()...
a=[5, 4, 3, 2, 1]
a.append(6)
print(a)             #[5, 4, 3, 2, 1, 6]

#del :- To delete any element from list 
a=[1,2,3,4,5]
del(a[2])
print(a)            #[1, 2, 4, 5]
del(a[2:4])         
print(a)            #[1, 2, 5]  