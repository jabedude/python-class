#!/usr/bin/env python3

numbers = input("Please enter a sequence of numbers: ")

num_list = numbers.split()

for num in num_list:
    if int(num) > 0:
        print(num)
