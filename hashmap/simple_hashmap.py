from string import ascii_lowercase


def get_prime_numbers1(
    size: int,
) -> list[int]:  # Test, so pylint: disable=missing-function-docstring
    arr = [i for i in range(2, size + 2)]

    for i in range(
        1, len(arr)
    ):  # Algo depends on indexes, so pylint: disable=consider-using-enumerate
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
    print(arr[-1])
    return arr


# class Hashmap:
#     letter_dict = {key: val for key, val in zip(ascii_lowercase, get_prime_numbers1(26))}
#     def __init__(self):
#         self.array = [0 for i in range(10)]  # initial size 10

#     def put(self, val: str):

letter_dict = {key: val for key, val in zip(ascii_lowercase, get_prime_numbers1(26))}

word = "bag"
w_sum = 0
for w in word:
    w_sum += letter_dict[w]

res = w_sum % 10
print(res)

import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.decode("utf-8").splitlines()
print(WORDS)
import random
print(random.choices(WORDS, k=3))

