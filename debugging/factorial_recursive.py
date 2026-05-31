#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
    Calculates the factorial of a given number recursively.

    Parameters:
    n (int): The non-negative integer to calculate the factorial for.

    Returns:
    int: The factorial of the given number `n`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)