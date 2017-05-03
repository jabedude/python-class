#!/usr/bin/env python3
''' Code for exercise 7 chapter 9 '''
import sys


def main():
    ''' Docstring '''
    in_one = sys.argv[1]
    in_two = sys.argv[2]
    set_one = set()
    set_two = set()
    
    with open(in_one, "r") as file_one, open(in_two, "r") as file_two:
        while True:
            line_one = file_one.readline()
            line_two = file_two.readline()
            if not line_one or not line_two:
                break
            set_one.add(line_one.strip())
            set_two.add(line_two.strip())

    print(set_one & set_two)


if __name__ == "__main__":
    main()
