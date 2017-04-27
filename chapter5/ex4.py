#!/usr/bin/env python3


def outer():

    def inner(a, b):
        return a + b

    return inner


res = outer()
print(res(5, 7))
