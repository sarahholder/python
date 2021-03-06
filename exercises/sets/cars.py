
'''
Create an empty set named showroom.
Add four of your favorite car model names to the set.
Print the length of your set.
Pick one of the items in your show room and add it to the set again.
Print your showroom. Notice how there's still only one instance of that model in there.
Using update(), add two more car models to your showroom with another set.
You've sold one of your cars. Remove it from the set with the discard() method.
'''
# Acquiring more cars
'''
Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
Use the intersection method to see which cars exist in both the showroom and that junkyard.
Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
'''

showroom = set()
showroom.add("Chevy Bolt")
showroom.update({"Tesla Model 3", "Nissan Leaf", "Polestar 2"})
print(len(showroom))
showroom.add("Nissan Leaf")

showroom.discard("Polestar 2")


junkyard = {"Byton foo", "Polestar 1", "C40 PuttPutt", "Nissan Leaf"}
both = showroom.intersection(junkyard)


showroom = junkyard.union(showroom)
print(showroom)
showroom.discard("C40 PuttPutt")
print(showroom)
