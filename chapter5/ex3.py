#!/usr/bin/env python3


def outer(a, b):
    def inner():
        return a + b

    return inner


res = outer(5, 7)
print(res())
