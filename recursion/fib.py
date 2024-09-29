"""
Cracking the coding interview. Example 14. Page 53.

https://en.wikipedia.org/wiki/Fibonacci_sequence

F(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ....
n:    0  1  2  3  4  5  6  7   8   9   10  11  12

Next number is sum of two previous numbers.
Common example of applying a recursive algo.

Time complexity: O(branches^depth), O(2^N)
Space complexity: O(N)

"""


def allFib(n: int):
    """
    Prints fibonacci numbers from 0 to Nth.
    """
    for i in range(0, n):
        print(f"{i}: {fib(i)}")
    
def fib(n: int) -> int:
    """
    Searches for the Nth fibonacci number.
    """
    if n <= 0: return 0
    elif n == 1: return 1
    return fib(n -1) + fib(n - 2)

allFib(100) 