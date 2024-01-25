#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
positive_number = 0
if number < 0:
    positive_number = number * -1
else:
    positive_number = number
digit = positive_number % 10
print("Last digit of {} is {}".format(number, digit), end=" ")
if digit > 5:
    print("and is greater than 5")
elif digit == 0:
    print("and is zero")
else:
    print("and is less than 6 and not 0")
