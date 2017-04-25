#!/usr/bin/env python3

low_limit = int(input("Please enter a low limit: "))
high_limit = int(input("Please enter a upper limit: "))
step_value = int(input("Please enter a step value: "))

for num in range(low_limit, high_limit, step_value):
    print(num)
