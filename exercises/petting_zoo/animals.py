from datetime import date

#outdoor corral (walking)
class Donkey: 
    def __init__(self, name, species, shift, food):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.walking = True
      self.shift = shift
      self.food = food

    def feed(self):
      print(f'{self.name} was fed on {date.today().strftime("%m/%d/%Y")}')
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.walking)} that it walks and it is available to pet during the {self.shift} shift.\n"
class Sheep: 
    def __init__(self, name, species, shift, food):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.walking = True
      self.shift = shift
      self.food = food

    def feed(self):
      print(f'{self.name} was fed on {date.today().strftime("%m/%d/%Y")}')
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.walking)} that it walks and it is available to pet during the {self.shift} shift.\n"

class Goat: 
    def __init__(self, name, species, shift, food):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.walking = True
      self.shift = shift
      self.food = food
      
    def feed(self):
      print(f'{self.name} was fed on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.walking)} that it walks and it is available to pet during the {self.shift} shift.\n"

class Cow: 
    def __init__(self, name, species, shift, food):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.walking = True
      self.shift = shift
      self.food = food
      
    def feed(self):
      print(f'{self.name} was fed on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.walking)} that it walks and it is available to pet during the {self.shift} shift.\n"

class Horse: 
    def __init__(self, name, species, shift, food):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.walking = True
      self.shift = shift
      self.food = food

    def feed(self):
      print(f'{self.name} was fed on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.walking)} that it walks and it is available to pet during the {self.shift} shift.\n"

#glass tank(slithering)
class Watersnake: 
    def __init__(self, name, species):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.slithering = True
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.slithering)} that it slithers.\n"

class Rattlesnake: 
    def __init__(self, name, species):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.slithering = True
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.slithering)} that it slithers.\n"

class Cottonmouth: 
    def __init__(self, name, species):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.slithering = True
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.slithering)} that it slithers.\n"

class Ratsnake: 
    def __init__(self, name, species):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.slithering = True
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.slithering)} that it slithers.\n"

class Copperhead: 
    def __init__(self, name, species):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.slithering = True
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.slithering)} that it slithers.\n"

#goldfish pond(swimming)

class Goldfish: 
    def __init__(self, name, species):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.swimming = True
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.swimming)} that it swims.\n"

class RedFish: 
    def __init__(self, name, species):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.swimming = True
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.swimming)} that it swims.\n"

class BlueFish: 
    def __init__(self, name, species):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.swimming = True
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.swimming)} that it swims.\n"

class Catfish: 
    def __init__(self, name, species):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.swimming = True
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.swimming)} that it swims.\n"

class KoiFish: 
    def __init__(self, name, species):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.swimming = True
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.swimming)} that it swims.\n"

JA = Donkey("JA", "donkey", "morning", "straw")
Black = Sheep("Black", "sheep", "afternoon", "hay")
Billy = Goat("Billy", "goat", "midday", "pellets")
Milkshake = Cow("Milkshake", "Cow", "morning", "grass")
RedRum = Horse("RedRum", "horse", "midday", "apples")

Noodles = Watersnake("Noodles", "watersnake")
Zoe = Rattlesnake("Zoe", "rattlesnake")
Snape = Cottonmouth("Snape", "cottonmouth")
Buttercup = Ratsnake("Buttercup", "ratsnake")
Sssssam = Copperhead("Sssssam", "copperhead")

Goldie = Goldfish("Goldie", "goldfish")
Romeo = RedFish("Romeo", "red fish")
Batman = BlueFish("Batman", "blue fish")
Cleo = Catfish("Cleo", "catfish")
Kiki = KoiFish("Kiki", "koi fish")

print(JA, JA.feed(), Black, Black.feed(), Billy, Billy.feed(), Milkshake, Milkshake.feed(), RedRum, RedRum.feed())
print(Noodles, Zoe, Snape, Buttercup, Sssssam)
print(Goldie, Romeo, Batman, Cleo, Kiki)
# for prop, value in JA.__dict__.items():
#     print(f'{prop}:\n{value}\n')