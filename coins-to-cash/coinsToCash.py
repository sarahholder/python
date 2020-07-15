def calc_dollars(**coins):
    sum = 0
    for money, amt in coins.items():
      if money == 'pennies':
         sum += amt * .01
      elif money == 'nickels':
        sum += amt * .05
      elif money == 'dimes':
        sum += amt * .10
      elif money == 'quarters':
        sum += amt + .25
    print(f'The sum is ${sum}')

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)







