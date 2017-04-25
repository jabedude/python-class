#!/usr/bin/env python3

numbers = set()
count = 0

while 1:
    data = input("Please enter a number (end to quit): ")

    if data == "end":
        break

    if data in numbers:
        count += 1

    numbers.add(data)

print(numbers)
print("User gave {} duplicate entries".format(count))
