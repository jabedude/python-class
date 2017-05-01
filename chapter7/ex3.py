#!/usr/bin/env python3
''' Code for exercise 3 chapter 7 '''
from ex1 import Person


class Family:
    '''
    This class represents a Family.
    It is constructed with at two Person objects
    and a list of Person objects (for the children).
    '''

    def __init__(self, mom, dad, *children):
        self.mom = mom
        self.dad = dad
        self.children = children

    @property
    def mom(self):
        return self._mom

    @mom.setter
    def mom(self, mom):
        self._mom = mom

    @property
    def dad(self):
        return self._dad

    @dad.setter
    def dad(self, dad):
        self._dad = dad

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        self._children = list(children)

    def add(self, child):
        ''' adds child to list of children in Family '''
        self._children.append(child)

    def __eq__(self, obj):
        ''' compares Family objects number of children and returns True if equal '''
        if type(obj) != Family:
            return False
        else:
            return len(self.children) == len(obj.children)

    def __lt__(self, obj):
        ''' compares Family objects number of children and returns True if less than '''
        if type(obj) != Family:
            return False
        else:
            return len(self.children) < len(obj.children)

    def __gt__(self, obj):
        ''' compares Family objects number of children and returns True if greater than '''
        if type(obj) != Family:
            return False
        else:
            return len(self.children) > len(obj.children)

    def __str__(self):
        mom = "Mom: {}\n".format(self.mom)
        dad = "Dad: {}\n".format(self.dad)
        children = []
        for child in self.children:
            children.append("Child: {}".format(child))
        return mom + dad + "\n".join(children) + "\n"


def main():
    ''' Function tests Family object '''
    mother = Person("Mom", 45, "F")
    father = Person("Dad", 45, "M")
    kid1 = Person("Johnie", 2, "M")
    kid2 = Person("Janie", 3, "F")

    myFamily = Family(mother, father, kid1, kid2)
    smiths = Family(mother, father, kid1, kid2)

    if (myFamily > smiths):
        print("We have more kids than the smiths")
    if (myFamily == smiths):
        print("We have the same number of kids as the smiths")
    if (myFamily < smiths):
        print("We have fewer kids than the smiths")

if __name__ == "__main__":
    main()
