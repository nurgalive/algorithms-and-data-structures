# Based on Grokking algorithms: page 93-D

# Implementation of the simple unordered hash table (HashMap)

import sys
from pathlib import Path

sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))

from string import ascii_lowercase
from services.prime import get_prime_numbers1


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

### TODO: Implement simple single-linked linked list here
# def add_first
# def find
# def delete

class LinkedList():
    """
    Simple single-linked linked list.
    """
    class Node:
        """
        Node class which stores data.
        """
        def __init__(self, data: int):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
    
    def add_first(self, data):
        old_head = self.head
        self.head = self.Node(data)
        self.head.next = old_head
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

# 1. What happens, if there is already a value in the index? -> Collision resolution. Store values as linked list pairs
# 2. What if we need to grow the array? -> calculate load factor and resizing
# 3. Make it work with any character: from string import printable and convert to string (int, float)
# 4. Add tests for distribution of the index function
class Hashmap:
    """
    Simple hash map. As a hash function used sum of the prime numbers.
    Where each prime number calculated based on the position of the letter.
    a - has first prime number, b - second, z - 26th prime number.
    """
    letter_dict = dict(zip(ascii_lowercase, get_prime_numbers1(26)))

    def __init__(self, size):
        self.array = [None for i in range(size)]  # initial size 10
        print("Created hashmap with size:", len(self.array))
    def __len__(self):
        return len(self.array)

    def calculate_index(self, key) -> int:
        """
        My homebrew hash code calculation based on prime number.
        Every letter has own prime number, calculated by the get_prime_numbers(26) function.
        26 - is the amount of the lowercase letters.
        """
        letter_sum = 0
        for letter in key:
            letter_sum += self.letter_dict[letter]

        index = letter_sum % 10 - 1  # -1 since the array has 0-based indexing
        print("Calculated index:", index, "; for the key:", key)
        return index

    def put(self, key: str, val: int) -> None:
        """
        Store keys and values in 
        """
        index = self.calculate_index(key)
        if self.array[index]:
            self.array[index].add_first((key, val))
        else:
            self.array[index] = LinkedList()
            self.array[index].add_first((key, val))
        
        print("Put value:", val, "; for the key:", key)
        print("Data array:", self.array)

    def get(self, key: str) -> int:
        value = self.array[self.calculate_index(key)]
        if value:
            return value
        raise KeyError(key)

    def load_factor(self):
        pass

    def resize(self):
        pass


# hashmap = Hashmap(10)
# val_iterator = 1
# # random_words = get_random_words(3)
# random_words = ["withdrawal", "registration", "guidelines"]
# for word in random_words:
#     hashmap.put(word, val_iterator)
#     val_iterator += 1

# for word in random_words:
#     print("For word:", word, "we got value:", hashmap.get(word))

# hashmap.get("aaa")

### testing
# letter_dict = dict(zip(ascii_lowercase, get_prime_numbers1(26)))

# word = "bag"
# w_sum = 0
# for w in word:
#     w_sum += letter_dict[w]

# res = w_sum % 10
# print(res)

llist = LinkedList()
llist.add_first("a")
llist.add_first("b")
llist.add_first("c")
print(llist)