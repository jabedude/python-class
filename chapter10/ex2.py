#!/usr/bin/env python3
''' Code for exercise 1 chapter 10 '''
from math import factorial


def main():
    ''' Docstring '''
    tup_list = [(x, factorial(x)) for x in range(5, 11)]
    print(tup_list)

if __name__ == "__main__":
    main()
