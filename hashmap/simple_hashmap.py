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
            nodes.append(str(node.data))
            node = node.next
        # nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    # TODO: Implement deletion of the a node
    # def delete_node(self):
        

# 1. What happens, if there is already a value in the index? -> Collision resolution. Store values as linked list pairs
# 2. What if we need to grow the array? -> calculate load factor and resizing
# 3. Make it work with any character: from string import printable and convert to string (int, float)
# 4. Add tests for distribution of the index function
class Hashmap:
    """
    Simple hash map. As a hash function used sum of the prime numbers.
    Where each prime number calculated based on the position of the letter.
    a - has first prime number, b - second, z - 26th prime number.
    Data is stored in the array. Where every cell of the array called bucket.
    Every bucket is represented as a Linked List.
    """
    letter_dict = dict(zip(ascii_lowercase, get_prime_numbers1(26)))
    load_factor_threshold = 0.7

    def __init__(self, size):
        self.array: list[None] | list[LinkedList] = [None for i in range(size)]  # initial size 10
        print("Created hashmap with size:", len(self.array))
    def __len__(self):
        return len(self.array)
    
    def __repr__(self) -> str:
        result = []
        for bucket in self.array:
            if bucket is not None:
                for node in bucket:
                    result.append(f"{node.data[0]}: {node.data[1]}")
        return " ".join(result)

    def calculate_index(self, key) -> int:
        """
        My homebrew hash code calculation based on prime number.
        Every letter has own prime number, calculated by the get_prime_numbers(26) function.
        26 - is the amount of the lowercase letters.
        """
        letter_sum = 0
        for letter in key:
            letter_sum += self.letter_dict[letter]

        index = letter_sum % self.size  # -1 since the array has 0-based indexing
        print("Calculated index:", index, "; for the key:", key)
        return index

    def put(self, key: str, val: int) -> None:
        """
        Store keys and values in hashmap.
        """
        print("Put value:", val, "; for the key:", key)
        current_load_factor = self.load_factor
        print("current_load_factor", current_load_factor)
        if current_load_factor >= self.load_factor_threshold:
            print("load_factor", current_load_factor, "is bigger than", self.load_factor_threshold)
            self.resize()
        index = self.calculate_index(key)
        if self.array[index]: # if there is LinkedList in the bucket, add to it
            self.array[index].add_first((key, val))
        else: # if there is no LinkedList in the bucker, create it
            self.array[index] = LinkedList()
            self.array[index].add_first((key, val))
        
        print("Data array:", self.array)

    def get(self, key: str) -> int:
        bucket = self.array[self.calculate_index(key)]  # bucket == LinkedList
        if bucket is None:  # bucket not initialized
            raise KeyError(key)
        for node in bucket:  # iterate over bucket (linked list) to search for value
            # node(key, value)
            if node.data[0] == key:
                return node.data[1]
        raise KeyError(key)  # key not found in bucket (linked list)


    def resize(self):
        """
        This method called, if the load_factor_threshold is reached and
        the array for storing data have to be resized and elements have to be
        copied over and rehashed.
        """
        print("Resizing the hashmap's underlying array...")
        old_array = self.array
        new_size = len(old_array) * 2
        print("new size is:", new_size)
        self.array = [None for i in range(new_size)]
        for bucket in old_array:
            if bucket is not None:
                for node in bucket:  # bucket is Linked List, and node is Node.
                    self.put(node.data[0], node.data[1])

    @property
    def load_factor(self) -> float:
        # occupied / overall_size 
        # 3 / 10 
        occupied = sum([1 for val in self.array if val is not None])
        load_factor = round(occupied / len(self.array), 2)
        return load_factor

    
    @property
    def size(self):
        return len(self.array)
    
    # TODO: Implement the deletion of the key-value pair.
    # def delete(self, key):

if __name__ == "__main__":


    # hashmap = Hashmap(3)
    # # hashmap.put("withdrawal", 1)

    # val_iterator = 1
    # # random_words = get_random_words(3)
    # random_words = ["withdrawal", "registration", "guidelines"]
    # for word in random_words:
    #     hashmap.put(word, val_iterator)
    #     val_iterator += 1

    # hashmap.put("bro", 4)

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

    ## Testing the linked list
    # llist = LinkedList()
    # llist.add_first(("a", "b"))
    # llist.add_first("b")
    # llist.add_first("c")
    # print(llist)
    # for val in llist:
    #     print(val.data)

    ## testing collisions with the linked list
    hashmap = Hashmap(5)

    val_iterator = 1
    # random_words = get_random_words(3)
    random_words = ["withdrawal", "withdrwaal", "iwthdrawal"]
    for word in random_words:
        hashmap.put(word, val_iterator)
        val_iterator += 1

    for word in random_words:
        print("For word:", word, "we got value:", hashmap.get(word))