#### 11 Guess the number
import random
counter, count  = 1,0
lucky = random.randint(1, 10)
while counter <= 5:
    number = int(input(" Guess the lucky number between 1 - 10: "))
    if number == lucky:
        count = +1
        print("Good Guess")
        break
    elif counter <5:
        print("Try again!")
    counter = counter + 1
if count == 0:
    print("Sorry but that was not very successful")

print("Game over")

