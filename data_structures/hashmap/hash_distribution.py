# Source: https://realpython.com/python-hash-table/#dive-deeper-into-pythons-hash

from collections import Counter
from string import ascii_lowercase, printable

import sys
from pathlib import Path

sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))

from services.prime import get_prime_numbers1

letter_dict = dict(zip(printable, get_prime_numbers1(100)))
def my_simple_hash(key) -> int:
    """
    My homebrew hash code calculation based on prime number.
    Every letter has own prime number, calculated by the get_prime_numbers(26) function.
    26 - is the amount of the lowercase letters.
    """
    letter_sum = 0
    for letter in key:
        letter_sum += letter_dict[letter]

    index = letter_sum  # -1 since the array has 0-based indexing
    # print("Calculated index:", index, "; for the key:", key)
    return index

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histogram):
    for key in sorted(histogram):
        # print("histogram", sorted(histogram))
        count = histogram[key]
        # print(count, "count")
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")

print("Values to distribute", printable)

# my simple hash
print("my simple hash")
plot(distribute(printable, num_containers=20, hash_function=my_simple_hash))

# default hash
print("default hash")
plot(distribute(printable, num_containers=20))
# 0 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ (51)
# 1 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   (49)

# plot(distribute(printable, num_containers=5))
# 0 ■■■■■■■■■■■■■■■            (15)
# 1 ■■■■■■■■■■■■■■■■■■■■■■■■■■ (26)
# 2 ■■■■■■■■■■■■■■■■■■■■■■     (22)
# 3 ■■■■■■■■■■■■■■■■■■         (18)
# 4 ■■■■■■■■■■■■■■■■■■■        (19)