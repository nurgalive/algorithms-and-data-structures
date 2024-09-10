"""
Cracking the coding interview. Exercise 1.1. Page 90.
Is Unique: Implement an algorithm to determine if a string has all unique characters.
Follow-up: What if you cannot use additional data structures?

Hint 1: Try a hash table.
Hint 2: Could a bit vector be useful?
Hint 3: Can you solve it in O(N log N) time? What might a solution like that look like?

Questions to aks
Is it ASCII (128) or Unicode string?
Create 128 array
"""

import unittest
from timeit import timeit


def is_unique1(string: str) -> bool:
    """
    Brute force solution.
    Take the first character, and check if it is presented again in the string.
    Time complexity - O(n^2)
    """
    for i in string:
        counter = 0
        for j in string:
            if i == j:
                counter += 1
        if counter > 1:
            return False

    return True


def is_unique2(string: str) -> bool:
    """
    Improved solution using hints.
    The max size of the string == number of character, which is 128. Since 
    ASCII has only 128 symbols (code points).
    Counts the frequencies for the every character of the string.
    If the count exceeds 1, it has duplicated characters.
    If has only count up to 1, all values are unique.
    Uses ord() function, which returns the code point for the character. Works
    like a hash map.
    Time complexity - O(n),
    Or O(c), where c - is the character set (all possible characters)
    Space complexity O(1) - constant to store all possible characters
    """
    if len(string) > 128:  # if lengths more than 128, means that there are duplicates
        return False
    arr = [0 for _ in range(0, 129)]  # create empty array
    for s in string:
        if arr[ord(s)] == 1:  # using 'ord()' find the location for the letter 's'
            return False
        else:
            arr[ord(s)] = 1
    return True


def is_unique3(string: str) -> bool:
    """
    Hacky solution, using bit vectors. It uses less memory.
    Instead of using full-fledged array, used integer, which has 32 bits.
    32 bits are enough, because if we consider only lowercase letters, they are only 26.
    If bit is occupied, then the character is not unique.
    For reading and setting bits special bitwise operations are used.
    """

    # string = string.lower()  # this functions only works with the lowercase

    checker = 0  # initial integer value, which is 32 zeros

    for s in string:
        # we substract 'a' as a smallest number from other characters
        #        val        const
        val = ord(s) - ord("a")  # we get the bit value for the character
        # print(f"val    : {val:032b}")  # uncomment this for the content
        
        if (  # bitwise read operation
            checker & (1 << val) > 0  # here we read the bit value, and check if it is bigger than zero
        ):  
            return False  # return false, if equals to zero
            # bitwise write operation
        checker = checker | (1 << val)  # set the values to 1, if not
        # print(f"checker: {checker:032b}")  # uncomment this for the content

    return True


class TestIsUnique(unittest.TestCase):
    basic_cases = [("", True), ("abc", True), ("abbc", False)]

    edge_cases = [
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("abcdefghijklmnopqrstuvwxyza", False),
        # ("abcdefghijklmnopqrstuvwxyz1", True),  # does not work with bit vector
        ("a" * 128, False),
        ("a" * 128 + "b", False),
    ]

    def test_basic_cases(self):
        for string, result in self.basic_cases:
            with self.subTest(input_data=string, result=result):
                self.assertEqual(is_unique1(string), result)
                self.assertEqual(is_unique2(string), result)
                self.assertEqual(is_unique3(string), result)

    def test_edge_cases(self):
        for string, result in self.edge_cases:
            with self.subTest(input_data=string, result=result):
                self.assertEqual(is_unique1(string), result)
                self.assertEqual(is_unique2(string), result)
                self.assertEqual(is_unique3(string), result)


if __name__ == "__main__":
    unittest.main()
