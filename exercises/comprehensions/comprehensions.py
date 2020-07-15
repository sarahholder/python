stuff = ["name", "age", "address", "phone"]

cap_stuff = []
for foo in stuff: 
  cap_stuff.append(foo.capitalize())  
  print(cap_stuff)

cap_stuff = list( map(lambda foo: foo.capitalize(), stuff) ) # stuff: get back an 'iterable object thing'
# hits why we wrap it in a list-- it will return a list that can be used

#  [*transform* for *item* in *iteration*]
cap_stuff = [foo.capitalize() for foo in stuff]

grades = {
  "math": .56,
  "english": .65,
  "history": .74,
  "spanish": .83
}

formatted_grades = { key.capitalize():f"{int(value*100)}%" for (key,value) in grades.items()}
print(formatted_grades)