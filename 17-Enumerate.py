#ENUMERATE IN PY...

#without using ENUMERATE
marks=[12,23,34,56,99]
index=0
for i in marks:
    print(i)
    if(index==2):
        print("hello")
    index += 1

#with using ENUMERATE ....    
marks=[12,23,34,56,99]
for index, i in enumerate(marks):
    print(i)
    if(index==2):
        print("hello")  