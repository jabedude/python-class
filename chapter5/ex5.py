#!/usr/bin/env python3


def outer():
    return lambda x, y: x + y


res = outer()
print(res(5, 7))
