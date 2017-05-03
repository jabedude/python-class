#!/usr/bin/env python3
''' Code for exercise 1 chapter 8 '''

def main():
    ''' Docstring '''

    number_list = range(1, 11)
    prompt = "Please enter a number (end to quit): "

    while True:
        user_input = input(prompt)
        if user_input == "end":
            exit()
        try:
            user_input = int(user_input)
            print(number_list[user_input])
        except (ValueError, IndexError) as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
