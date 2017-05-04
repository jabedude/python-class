#!/usr/bin/env python3
''' Code for exercise 1 chapter 10 '''


def main():
    ''' Docstring '''
    num_list = range(0, 100)
    fives_list = [x for x in num_list if x % 5 == 0]

    print(fives_list)

if __name__ == "__main__":
    main()
