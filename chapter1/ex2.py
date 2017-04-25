#!/usr/bin/env python3

num_one = int(input("Please enter your first number: "))
# Entering a decimal number here results in a invalid literal
# for int() with base 10 error
# This is because python is expecting an int, not a float
num_two = int(input("Please enter your second number: "))
# Entering a non-numeric value here results in a invalid literal
# for int() with base 10 error

product = num_one * num_two

print(product)
