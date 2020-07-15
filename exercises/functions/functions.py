def create_person(first_name, last_name, age, occupation):
  return {
    "first_name": first_name,
    "last_name": last_name,
    "age": age,
    "occupation": occupation,
  }

melissa = create_person("Melissa", "Bell", 25, "Software Developer")

print(melissa)

# *args and **kwargs (argurments and keyword arguments are like tacos -- call it whatever you want)
def list_colors(name, *colors):
  print(colors)

list_colors("Joe", "red", "yellow", "orange", "blue")

def list_fav_colors(name, *args):
  for color in args:
    print(f"My name is {name}, and one of my favorite colors is {color}.")

list_fav_colors("Joe", "red", "yellow")


def make_family(name, **info):
  print("our kwargs dictionary:", info)
  family_stuff = info.items()
  family_str = f"We are in the {name} family. "
  for title, person in family_stuff: 
    family_str += f"The {title} is {person}. "

  return family_str

family = make_family("Shepherd", mom="Anna", dad="Joe", dog="Murph")
other_family = make_family("Parker", aunt="May", nephew="Peter")

print(family)
print(other_family)


def fave_color(name, color="puce"):
  print(f'{name}\'s fave color is {color}')

fave_color("Fred")
fave_color("Linda", "orange")

def all_the_things(name, *color, **people):
  print(people)


