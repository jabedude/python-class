#!/usr/bin/env python3

from restaurant import Restaurant, MenuItem

def main():
    food_one = MenuItem("Pasta", "Delicious", 15)
    food_two = MenuItem("Lasanga", "Fat", 20)
    og = Restaurant()

    og.add(food_one)
    og.add(food_two)

    print(og)

if __name__ == "__main__":
    main()
