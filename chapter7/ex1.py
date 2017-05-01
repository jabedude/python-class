#!/usr/bin/env python3
''' Code for exercise 1 chapter 7 '''

class Person:
    '''
    This class represents a Person.
    It has a name, age, and gender.
    '''

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __get__(self):
        pass

    def __set__(self):
        pass

    def __str__(self):
        pass


def main():
    ''' Function tests Person object '''

    test_person = Person()

if __name__ == "__main__":
    main()
