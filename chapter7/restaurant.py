#!/usr/bin/env python3


class Category():
    
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
        return "Name: {}\n Description: {}\n Price: ${}".format(self.name, self.desc, self.price)


class Restaurant():
    def __init__(self, *menu_items):
        self.menu_items = list(menu_items)

    @property
    def menu_items(self):
        return self._menu_items

    @menu_items.setter
    def menu_items(self, menu_items):
        self._menu_items = menu_items

    def __str__(self):
        return "\n".join(self.menu_items)
