sum = 2 + 2

print ("the value of sum is", sum)

name = "Fred"

def say_name():
    global name
    name = "Linda"
    print("inernal", name)

say_name()
print("external", name)


# if/else
name = "Larry"
if name == "Linda" :
    print("I am Linda. Larry is on vacation.")
elif name == "Fred":
    print("Welcome to Costco. I am Fred")
else:
    print("I am Larry")

# String interpolation 
print (f"My name is {name}")

"hello" + "world"
2 + 4 

# Collections:
# arrays (nope) and objects (yes! but....)

# js
# let stuff = {name: "", category: ""}

#python: dictionary
stuff = {"name": "", "category": "", 20: "wtf?"}

# list 
more_stuff = [2, "things", True]

more_stuff.append("wow!")
print(more_stuff[2])
print(more_stuff[-1])
# (works backwards using a negative from the back of the list)

more_stuff.insert(0, "Sorry bout that")
# insert places things in a specific place in list
print(more_stuff)

more_stuff.extend([45, False, "blah"])
print(more_stuff)

stuff = {"name": "Sally", "category": "Manager"}

stuff["name"] = "Regina"
print(stuff["name"])

stuff["salary"] = "60,000"

print(stuff)

stuff["address"] = {"street": "Sesame", "num": 123}
print(stuff)

print(stuff["address"]["street"])

# Sets (no indexing)
junk = {"Curlies", "lies", 34, None}

junk.add("more stuff")
print(junk)

junk.add("lies")
print(junk)

names = ["Joe", "Linda", "Fred", "Linda"]
print(names)

example = set()
example.add("hello")
print(example)

names = set(names)
print(names)

colors = []
print(colors)

addresses = {}
addresses["num"] = 123
print(type(addresses))

# tuple is cool because it is immputable (cannot be changed)

my_tup = (1,2,3, "hello")
print(my_tup[3])

# How does it now that it is a tuple?
# It knows it is a tuple after you type a comma after a value
# Has to have a comma after a value even if there is only one value

my_tup = (12,)
print(type(my_tup))
print(my_tup)

# Loops
# for... in 

my_tup = (1, 2, 3, 3, "hello")
my_set = {1, 2, 3}
junk = ["Fred", True, [1,2,3], 234]

for foo in junk: 
  print(f"Why is {foo} still in here")

for foo in my_tup:
    print(f"This is in my tup: {foo}")

for foo in my_set:
  print(f"is this in any order? {foo}")

my_dict = {
  123: "number", 
  "name": "Broomhilda"
}

# for foo in my_dict: 
# for foo in my_dict.values():
# for foo in my_dict.items():
for key, value in my_dict.items():
  print(f"What is the value? {key}: {value}")

# Slicing
my_list = [1, 2, 4, "hello", "monkey"]
# The JS way
# my_subset = my_list.slice(0,3)

my_subset = my_list[1:3]
print(my_subset)
my_subset = my_list[:3]
print(my_subset)
my_subset = my_list[3:]
print(my_subset)
my_subset = my_list[3:-1]
print(my_subset)
my_subset = my_list[1:34] #doesn't break
print(my_subset)

# What kind of file is this?
print("name", __name__)

if __name__ == "__main__":
  print("shut up, Joe.") 












