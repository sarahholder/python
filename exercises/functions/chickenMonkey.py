numbers_1_to_100 = range(1, 101)
for number in numbers_1_to_100:
    if(number % 5 == 0) and (number % 7 == 0):
        print("this is my number", number)
        number = "ChickenMonkey"
    elif(number % 7 == 0):
      number = "Monkey"
    elif(number % 5 == 0):
      number = "Chicken"
    print(number)

