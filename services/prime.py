# Cracking the coding interview, page 50, exercise 10

# This scripts calculates the prime number.
# Prime number is a number, which is bigger than and divided only by 1 and by itself.

import time

def timeit(some_function):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = some_function(*args, **kwargs)
        total_time = round(time.perf_counter() -  start_time, 3)
        print(f'Function {some_function.__name__}{args} Took {total_time} seconds')
        print(total_time)
        return result
    return wrapper

# ver 1. My naive implementation
# @timeit
def get_prime_numbers1(size: int) -> list[int]: # Test, so pylint: disable=missing-function-docstring
    arr = [i for i in range(2, size + 2)]

    for i in range(1, len(arr)): # Algo depends on indexes, so pylint: disable=consider-using-enumerate
        # print(f"Id: {i}")
        start = arr[i - 1] + 1
        while True:  # until we find the prime number
            # print(f"Start: {start}")
            dividers = []
            for guess in range(2, start + 1):  # second value exclusive
                if start % guess == 0:
                    dividers.append(guess)
            if dividers == [start]:
                arr[i] = start
                # print(arr)
                break
            start += 1
    # print(arr[-1])
    return arr

# ver 2. Influenced by the doc example
@timeit
def get_prime_numbers2(size: int) -> list[int]: # Test, so pylint: disable=missing-function-docstring
    arr = []
    for num in range(2, size):
        # print(f"num: {num}")
        for guess in range(2, num+1):
            # print(guess, "guess") 
            if num % guess == 0:
                if guess < num:
                    break
                else:
                    arr.append(guess)
                    # print(arr)
                    break
    return arr
# ver 3. Influenced by the CtCi book and wikipedia https://en.wikipedia.org/wiki/Prime_number and python docs
@timeit
def get_prime_numbers3(size: int) -> list[int]: # Test, so pylint: disable=missing-function-docstring
    arr = []
    for num in range(2, size):
        # print(f"num: {num}")
        for guess in range(2, num+1):
            # print("guess:", guess)
            if guess * guess <= num: # guess goes from 2 up to sqrt(n)
                if num % guess == 0:
                        break
            else:
                if guess == num:
                    arr.append(guess)
                    break
        else:
            arr.append(guess)
            # print(arr)
    return arr

if __name__ == "__main__":
    # from the doc https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
    # example of using else in loops
    @timeit
    def get_prime_numbers4(size: int) -> list[int]:
        res = []
        for n in range(2, size):
            for x in range(2, n):
                if n % x == 0:
                    # print(n, 'equals', x, '*', n//x)
                    break
            else:
                # loop fell through without finding a factor
                # print(n, 'is a prime number')
                res.append(n)
        return res

    print(len(get_prime_numbers1(1000)))
    print(len(get_prime_numbers2(7910)))
    print(len(get_prime_numbers3(7910)))
    print(len(get_prime_numbers4(7910)))