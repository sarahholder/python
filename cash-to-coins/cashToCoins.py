import math

dollarAmount = 8.69

piggy_bank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def cash_to_coins(amount, p_bank):
  print(p_bank)
  if amount > 0:
    p_bank["quarters"] = math.floor(amount // .25)
    p_bank["dimes"] = math.floor(amount % .25 // .10)
    p_bank["nickels"] = math.floor(amount % .25 % .1 // .05)
    p_bank["pennies"] = math.ceil(amount % .25 % .1 % .05 / .01)
    print(p_bank)
  else:
    print("Please enter a value amount!")

cash_to_coins(dollarAmount, piggy_bank)




