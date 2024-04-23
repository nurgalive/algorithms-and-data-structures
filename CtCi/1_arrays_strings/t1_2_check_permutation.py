"""
Cracking the coding interview. Exercise 1.2. Page 90.
Check Permutation: Given two strings, write a method to decide if one is a permutation
of the other.

Check also
https://github.com/TheAlgorithms/Python/blob/master/strings/check_anagrams.py

Hints:
1. 1.2 Describe what it means for two strings to be permutations of each other.
Now, look at that definition you provided. Can you check the strings against that definition?
84. 1.2 There is one solution that is 0(N log N) time. [sorting] Another solution uses some space, 
but is O(N) time [array or dict for storing frequencies]
122. 1.2 Could a hash table be useful? [Yes, we can use it for storing frequencies]
131. 1.2 Two strings that are permutations should have the same characters, but in different
orders. Can you make the orders the same? [yes, by using sorting]
"""

import unittest


def check_permutation1(str1: str, str2: str) -> bool:
    """
    Sorting strings and comparing them.
    Time complexity: (S1 logS1 + S2 logS2)
    """
    if len(str1) != len(str2):
        return False
    
    str1_sorted = sorted(str1)  # O(S1 log S1)
    str2_sorted = sorted(str2)  # O(S2 log S2)
    return str1_sorted == str2_sorted


def check_permutation2(str1: str, str2: str) -> bool:
    """
    Using HashMap (dict) for storing frequencies per character.
    Time complexity: O(S1) + S(S2)
    """
    if len(str1) != len(str2):  # O(1)
        return False
    
    str1_dict = {}
    for s in str1:  # Creating a dict with frequencies S1: O(S1)
        str1_dict[s] = str1_dict.get(s, 0) + 1

    # print(str1_dict)

    for s in str2:  # Iterating over S2: O(S2)
        if s not in str1_dict:
            return False
        else:
            str1_dict[s] -= 1
            if str1_dict[s] < 0:
                return False

    return True


def check_permutation3(str1: str, str2: str) -> bool:
    """
    Array of ASCII characters (128) with frequencies.
    Works only for A-z, 0-9
    """
    letters = [0 for i in range(128)]

    for s in str1:  # O(S1)
        letters[ord(s)] += 1

    for s in str2:  # O(S2)
        letters[ord(s)] -= 1

        if letters[ord(s)] < 0:
            return False

    return True


class TestCheckPermutation(unittest.TestCase):
    basic_cases = [
        ("", "", True),  # empty string
        ("aaa", "aaa", True),  # identical strings
        ("abc", "bca", True),  # same characters, different order
        ("aab", "baa", True),  # same characters, different order with duplicates
        ("aaa", "aab", False),  # duplicates, not the same
        ("aaa", "bbb", False),  # different characters 1
        ("abc", "def", False),  # different characters 2
    ]

    edge_cases = [
        ("abc", "abcd", False),  # different length
        ("baab", "abab", True),  # duplicates of the letter
        ("abc123", "321cba", True),  # numbers
        ("hello world", "world hello", True),
    ]

    def test_basic_cases(self):
        for str1, str2, result in self.basic_cases:
            with self.subTest(input_data=(str1, str2), expected_result=result):
                self.assertEqual(check_permutation1(str1, str2), result)
                self.assertEqual(check_permutation2(str1, str2), result)
                self.assertEqual(check_permutation3(str1, str2), result)

    def test_edge_cases(self):
        for str1, str2, result in self.edge_cases:
            with self.subTest(input_data=(str1, str2), expected_result=result):
                self.assertEqual(check_permutation1(str1, str2), result)
                self.assertEqual(check_permutation2(str1, str2), result)
                self.assertEqual(check_permutation3(str1, str2), result)


if __name__ == "__main__":
    unittest.main()

