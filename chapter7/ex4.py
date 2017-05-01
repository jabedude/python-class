#!/usr/bin/env python3
''' Code for exercise 4 chapter 7 '''

class Worker:
    '''
    This class represents a Worker.
    It has a name, salary, and years worked and a pension
    method.
    '''
    
    pension_fraction = 0.1

    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def years(self):
        return self._years

    @years.setter
    def years(self, years):
        self._years = years

    def pension(self):
        ''' Returns Worker's pension based on fraction, years, and salary '''
        return self.pension_fraction * self.years * self.salary

    def __str__(self):
        return "{} {} {}".format(self.name, self.salary, self.years)


class Manager(Worker):
    ''' This class represents a Manager object. Has a higher pension fraction than Worker '''
    pension_fraction = 0.2


class Executive(Manager):
    ''' This class represents an Executive object. Has a higher pension fraction than Manager '''
    pension_fraction = 0.3


def main():
    ''' Function tests Worker, Manager, and Executive object '''
    test_work = Worker("Josh", 30000, 20)
    print(test_work)
    print(test_work.pension())

    test_manage = Manager("Mike", 30000, 20)
    print(test_manage)
    print(test_manage.pension())

    test_exec = Executive("Hannah", 30000, 20)
    print(test_exec)
    print(test_exec.pension())


if __name__ == "__main__":
    main()
