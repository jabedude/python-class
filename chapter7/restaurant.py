#!/usr/bin/env python3


class Category():
    ''' Class represents Category objects. Only has a name '''
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return self.name


class MenuItem(Category):
    ''' Class represents a MenuItem object. Has a name, description, and price. '''
    def __init__(self, name, desc, price):
        super().__init__(name)
        self.desc = desc
        self.price = price

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, desc):
        self._desc = desc

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    def __str__(self):
        return "Name: {}\nDescription: {}\nPrice: ${}".format(self.name, self.desc, self.price)


class Restaurant():
    '''
    Class represents a Restaurant object, a list of MenuItems. Has add() method
    to add MenuItems to list.
    '''
    def __init__(self, *menu_items):
        self.menu_items = list(menu_items)

    @property
    def menu_items(self):
        return self._menu_items

    @menu_items.setter
    def menu_items(self, menu_items):
        self._menu_items = menu_items

    def add(self, item):
        ''' Method adds MenuItem to Restaurant obj '''
        self.menu_items.append(item)

    def __str__(self):
        results = []
        for num, item in enumerate(self.menu_items):
            results.append("Item {}\n{}\n".format(num + 1, item))

        return "\n".join(results)
