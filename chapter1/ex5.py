#!/usr/bin/env python3

user_string = input("Please enter a string: ")

if user_string.endswith("."):
    print("Ends with a period.")

if user_string.isalpha():
    print("Is all alphabetic chars.")

if "x" in user_string:
    print("x is in string.")

print(user_string.replace("e", "E"))
