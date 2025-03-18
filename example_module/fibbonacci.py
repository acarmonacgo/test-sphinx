"""
This module provides a function to generate the Fibonacci sequence up to a given limit.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, 
starting from 0 and 1. This implementation returns the sequence as a list up to the specified limit.

Example:
    >>> from fibonacci_module import fibonacci
    >>> fibonacci(10)
    [0, 1, 1, 2, 3, 5, 8]
"""

def fibonacci(n: int) -> list:
    """
    Generates the Fibonacci sequence up to a given number.

    :param n: The upper limit for the Fibonacci sequence.
    :type n: int
    :return: A list containing the Fibonacci sequence up to `n`.
    :rtype: list

    **Example usage:**

    >>> fibonacci(10)
    [0, 1, 1, 2, 3, 5, 8]
    
    >>> fibonacci(1)
    [0]
    
    >>> fibonacci(0)
    []
    """

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)
    
    return fib_sequence
