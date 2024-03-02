# Example 15. Page 53.

def allFib(n: int):
    memo = [0 for i in range(0, n)]
    for i in range(0, n):
        print(f"{i}: {fib(i, memo)}")

def fib(n: int, memo: list) -> int:
    if n <= 0: return 0
    elif n == 1: return 1
    elif memo[n] > 0: return memo[n]
    else:
        memo[n] = fib(n -1, memo) + fib(n -2, memo)
        return memo[n]
    

allFib(1000)