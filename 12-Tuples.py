tup=(1,2,3) #list=[]...tuple=() list is changeble tuple is not changeble
print(tup)          #(1, 2, 3)
print(type(tup))    #<class 'tuple'>

if 2 in tup:
    print("yes 2 is present") #o/p
else:
    print("Not present")

tup2=tup[1:3]
print(tup2)     #(2, 3)

#Note:
# All properties are same as list.....


#Tuple manipulation (as tuple is immutable we first convert it into list then modify it)
countries=("india", "america", "russia")    #EX OF TUPLE

country=list(countries)     #converting tuple--->list

country.append("China")     #adding china to the list   (['india', 'america', 'russia', 'China'])
country[3]="SA"             #replace "SA" with "China"
print(country)              #['india', 'america', 'russia', 'SA']

countries=tuple(country)    #converting list--->tuple
print(countries)            #('india', 'america', 'russia', 'SA')

tot=countries.count("india")
print(tot)                  #1  ("india" is present in the tuple 1 time)

num=countries.index("india")
print(num)                  #0  ("india" is present at 0 index)

len=len(countries)
print(len)                  #4