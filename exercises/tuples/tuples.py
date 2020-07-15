children = ("Sally", "Hansel", "Gretel", "Svetlana")
(first_child, second_child, third_child, fourth_child) = children
print(first_child) # Output is "Sally"
print(second_child) # Output is "Hansel"
print(third_child) # Output is "Gretel"
print(fourth_child) # Output is "Svetlana"

children = list(children)
print(children)
children.extend(["Freddie", "Jason", "Chuckie"])
print(children)
children = tuple(children)
print(children)

zoo = ("monkey", "lion", "tigers", "kangaroo", "hippo", "giraffe", "snake", "koala", "zebra", "penguins")
print(zoo.index("koala"))

animal_to_find = "koala"
if animal_to_find in zoo:
   print(f"I found a {animal_to_find}")
else:
   print(f"I didn't find a {animal_to_find}")

print(type(animal_to_find))


for animal in zoo:
  print ('Animal in zoo: ', animal)

zoo_tuple_to_list = list(zoo)
print(zoo_tuple_to_list)

zoo_tuple_to_list.extend(["panda", "Cheeta", "sloth"])
print(zoo_tuple_to_list)
zoo_to_tuple = tuple(zoo_tuple_to_list)
print(zoo_to_tuple)


