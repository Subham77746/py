#using break print 5's table untill 5X10...
for i in range(15):
    if(i==10):
        print("Condition Satisfies")
        break
    print("5 X",i+1,"=",5*(i+1))    #break after 5X10
        
#using continue in 5's table        
for i in range(15):
    if(i==10):
        print("condition satisfies")
        continue
    print("5 X ",i+1,"=",5*(i+1))   #goes until 5X10 then print the statement and continue 