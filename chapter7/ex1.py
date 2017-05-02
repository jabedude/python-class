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

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    def __str__(self):
        return "{} {} {}".format(self.name, self.age, self.gender)


def main():
    ''' Function tests Person object '''

    test_person = Person("Michael", 45, "M")
    print(test_person)


if __name__ == "__main__":
    main()
