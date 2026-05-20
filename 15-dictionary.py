dict = {"name": "subham", "id": 7, "salary": "25.30"}
print(dict)             #{'name': 'subham', 'id': 7, 'salary': '25.30'}
print(dict["id"])       #7
print(dict.get("id"))   #7

#print(dict["salary2"])          #salary2 not exist so it throws an error
print(dict.get("salary2"))      #salary2 not exist but indtead of error it shows NONE...

for i in dict:
    print (dict[i])     #subham
                        #7
                        #25.30

print(dict.items())     #dict_items([('name', 'subham'), ('id', 7), ('salary', '25.30')])

#dictionary methods
#adding two
subham={"math": 89, "english": 88}
sachi={"cs": 98, "phy": 77}
subham.update(sachi)
print(subham)           #{'math': 89, 'english': 88, 'cs': 98, 'phy': 77}

#pop (removes only one value)
subham={"math": 89, "english": 88}
subham.pop("math")
print(subham)           #{'english': 88}

#popitem    (removes only last item/value)
subham={"math": 89, "english": 88}
subham.popitem()
print(subham)           #{'math': 89}

#del (delete whole dictionary or any item you want)
del subham
print(subham)           #deletes whole dictionary

subham={"math": 89, "english": 88}
del subham["math"]      #deletes only defines element
print(subham)           #{'english': 88}