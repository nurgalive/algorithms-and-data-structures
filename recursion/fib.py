"""
Cracking the coding interview. Example 14. Page 53.

https://en.wikipedia.org/wiki/Fibonacci_sequence

F(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ....
n:    0  1  2  3  4  5  6  7   8   9   10  11  12

Next number is sum of two previous numbers.
Common example of applying a recursive algo.

LeetCode
https://leetcode.com/problems/fibonacci-number/solutions/1853283/nth-fibonacci/

Recursion by default limited to the stack size of 1000 in Python.
Which gives 995 for the real code, since other things also have to be stored in the stack.
Overwise we will get a stack over flow error.
In that regard iterative approach shines, which does not have such a disadvantage.
But recursive implementation looks more elegant.
"""


def allFib1(n: int):
    """
    Prints fibonacci numbers from 0 to Nth.
    Time complexity: O(branches^depth), O(2^N)
    Space complexity: O(N)
    """
    for i in range(0, n):
        print(f"{i}: {fib1(i)}")
    
def fib1(n: int) -> int:
    """
    Searches for the Nth fibonacci number using recursion.
    """
    if n <= 0: return 0
    elif n == 1: return 1
    return fib1(n -1) + fib1(n - 2)


def allFib2(n: int):
    """
    Improved version of searching for Nth fibonacci number function using cache.

    Time complexity: O(N)
    Space complexity: O(N)
    """
    memo = [0 for i in range(0, n)]  # init the cache
    for i in range(0, n):
        print(f"{i}: {fib2(i, memo)}")

def fib2(n: int, memo: list) -> int:
    if n <= 0: return 0
    elif n == 1: return 1
    elif memo[n] > 0: return memo[n]  # if there is a value in the cache, use it
    else:
        memo[n] = fib2(n -1, memo) + fib2(n -2, memo)  # else calculate value and put in cache
        return memo[n]
    


def recursive_fib(n: int) -> int:
    """
    Recursive implementation for the Fibonacci function.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fib(n - 2) + recursive_fib(n - 1)

def iterative_fib(n: int) -> int:
    """
    Iterative counterpart to the Fibonacci function.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(n - 1):
            # 1. fancy
            # a, b = b, a + b
            
            # 2. clear
            c = a + b
            a = b
            b = c
            
        return c
        # return b
    
allFib1(10)
allFib2(10)
print(recursive_fib(10))
print(iterative_fib(10))
