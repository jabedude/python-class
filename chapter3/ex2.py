#!/usr/bin/env python3

num_one = int(input("Please enter a number: "))
num_two = int(input("Please enter another number: "))

sum = 0

for num in range(num_one, num_two + 1):
    sum += num

print(sum)
