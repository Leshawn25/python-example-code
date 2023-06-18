
# Description: Example of how to generate random lottery numbers using Python.
# Lottery number mathematics: https://en.wikipedia.org/wiki/Lottery_mathematics.
# Our program will randomly select some amount of distinct numbers from a 
# range of numbers, e.g. 6 numbers from 1-28, using a range and amount of 
# numbers specified by the user.
# Import the random module so we can use the sample function to randomly 
# select distinct numbers from a range
import random
previous numbers= 6,9,15,19,24,27
lucky_nunbers=[]
# Generating additional lucky numbers
while len(lucky_numbers) < 3:
    number = random.randint(1, 28)
    if number not in previous_numbers and number not in lucky_numbers:
        lucky_numbers.append(number)

print("Lucky Numbers:")
for number in lucky_numbers:
    print(number)
