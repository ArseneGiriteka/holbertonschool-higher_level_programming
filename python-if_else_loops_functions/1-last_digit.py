#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
print("Last digit of {} is {}".format(number, digit), end=" ")
if digit > 5:
    print("and is greater than 5")
elif digit == 0:
    print("and is zero")
else:
    print("and is less than 6 and not 0")
