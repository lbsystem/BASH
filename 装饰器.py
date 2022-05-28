#!/usr/bin/python3
import time


def decorator(num):
    def sencond(fn):
        def inner(*args, **kwargs):
            while True:
                time.sleep(num)
                fn(*args, **kwargs)


        return inner

    return sencond


@decorator(2)
def test(i):
    print(i)





test(3)
