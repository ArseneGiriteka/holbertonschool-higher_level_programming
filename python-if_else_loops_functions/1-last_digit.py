#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
positive_number = 0
digit = 0
if number < 0:
    positive_number = number * -1
    digit = (positive_number % 10) * -1
else:
    digit = number % 10
print("Last digit of {} is {} and is".format(number, digit), end=" ")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
