#!/usr/bin/env python3
''' Code for exercise 3 chapter 10 '''
from math import factorial


def main():
    ''' Docstring '''
    fact_dict = {x : factorial(x) for x in range(1, 11)}

    print(fact_dict[6] * fact_dict[5])

if __name__ == "__main__":
    main()
