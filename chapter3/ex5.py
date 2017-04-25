#!/usr/bin/env python3

for num in range(0, 50):
    if not num:
        print("", num, end="")
    elif num % 10 == 0:
        print("\n" + str(num), end=" ")
    elif num < 10:
        print(" ", num, end="")
        continue
    else:
        print(num, end=" ")

print()
