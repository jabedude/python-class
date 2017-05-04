#!/usr/bin/env python3
''' Code for exercise 3 chapter 8 '''


def main():
    ''' Docstring '''

    prompt = "Please enter an integer: "
    error = "\nPlease exit with ctrl+d on Linux or ctrl+z on Windows"
    total = 0

    while True:
        try:
            user_input = input(prompt)
            user_input = int(user_input)
            total += user_input
        except (ValueError, IndexError) as e:
            print("Error:", e)
        except KeyboardInterrupt:
            print(error)
        except EOFError:
            break

    print("\nThe total is {}".format(total))

if __name__ == "__main__":
    main()
