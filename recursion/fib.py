# Example 14. Page 53.

def allFib(n: int):
    for i in range(0, n):
        print(f"{i}: {fib(i)}")
    
def fib(n: int) -> int:
    if n <= 0: return 0
    elif n == 1: return 1
    return fib(n -1) + fib(n - 2)

allFib(100) 