from datetime import date

class Llama: 
    def __init__(self, name, species):
      self.name = name
      self.species = species
      self.date_added = date.today()
      
    def __str__(self):
      return f"This animal is named {self.name}, it is a {self.species} and it was added on {date_added}"

#outdoor corral (walking)
#donkey, kangaroo, goat, cow, horse

#glass tank(slithering)
#watersnake, rattlesnake, cottonmouth , ratsnake, copperhead

#goldfish pond(swimming)
#goldfish, red_fish, blue_fish, catfish, Koi_fisk




