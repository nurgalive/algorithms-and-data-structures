"""
Cracking the coding interview. Example 15. Page 53.

Improved version of searching for Nth fibonacci number function using cache.
For details about Fibonacci numbers loot in fib.py
"""

def allFib(n: int):
    memo = [0 for i in range(0, n)]  # init the cache
    for i in range(0, n):
        print(f"{i}: {fib(i, memo)}")

def fib(n: int, memo: list) -> int:
    if n <= 0: return 0
    elif n == 1: return 1
    elif memo[n] > 0: return memo[n]  # if there is a value in the cache, use it
    else:
        memo[n] = fib(n -1, memo) + fib(n -2, memo)  # else calculate value and put in cache
        return memo[n]
    

allFib(1000)