# Based on Grokking algorithms: page 93-D

import sys
from pathlib import Path
sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))

from services.prime import get_prime_numbers1
from string import ascii_lowercase

def get_random_words(number_of_random_words: int) -> list[str]:
    import random
    import requests
    WORD_SITE = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(WORD_SITE)
    WORDS = response.content.decode("utf-8").splitlines()
    # print(WORDS)
    random_words = random.choices(WORDS, k=number_of_random_words)
    print("Random  words:", random_words)
    return random_words

# TODO:
# 1. What happends, if there is already a value in the index?
# 2. What if we need to grow the array?
# 3. Make it work with any character: from string import printable and convert to string (int, float)
class Hashmap:
    letter_dict = dict(zip(ascii_lowercase, get_prime_numbers1(26)))
    def __init__(self):
        self.array = [None for i in range(10)]  # initial size 10
        print("Created hashmap with size:", len(self.array))

    def calculate_index(self, key):
        letter_sum = 0
        for letter in key:
            letter_sum += self.letter_dict[letter]
        
        index = letter_sum % 10 - 1  # -1 since the array has 0-based indexing
        print("Calculated index:", index, "; for the key:", key)
        return index

    def put(self, key: str, val: int) -> None:
        self.array[self.calculate_index(key)] = val
        print("Put value:", val, "; for the key:", key)
        print("Data array:", self.array)

    def get(self, key: str) -> int:
        return self.array[self.calculate_index(key)]
    

hashmap = Hashmap()
val_iterartor = 1
# random_words = get_random_words(3)
random_words = ['withdrawal', 'registration', 'guidelines']
for word in random_words:
    hashmap.put(word, val_iterartor)
    val_iterartor += 1

for word in random_words:
    print("For word:", word, "we got value:", hashmap.get(word))

### testing
# letter_dict = dict(zip(ascii_lowercase, get_prime_numbers1(26)))

# word = "bag"
# w_sum = 0
# for w in word:
#     w_sum += letter_dict[w]

# res = w_sum % 10
# print(res)



