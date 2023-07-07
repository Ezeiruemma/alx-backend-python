#!/usr/bin/env python3
'''
type-annotated function
'''


def add(a: float, b: float) -> float:
    '''function that add two float and return their output
    '''
    return (a + b)


if __name__ == '__main__':

    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
