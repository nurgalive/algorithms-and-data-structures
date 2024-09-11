"""
Cracking the coding interview. Exercise 1.4. Page 91.

One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if 
they are one edit (or zero edits) away.

EXAMPLE
pale,   ple  -> true
pales,  pale -> true
pale,   bale -> true
pale,   bake -> false

Hints:#23, #97, #130

#23. 1.5 Start with the easy thing. Can you check each of the conditions separately?
#97. 1.5 What is the relationship between the "insert character" option and the 
"remove character" option? Do these need to be two separate checks
#130. 1.5 Can you do all three checks in a single pass?


My examples:
Only edits
- pale, spale
- pale, pales
- pale, palse

"""

import unittest

def one_way(str1: str, str2) -> bool:
    """
    My brute force solution.
    O(s^2) - for every char do a loop.
    """

    longest_len = 0
    long_str = None
    short_str = None
    if len(str1) > len(str2): 
        longest_len = len(str1)
        long_str = str1
        short_str = str2
    else: 
        longest_len = len(str2)
        long_str = str2
        short_str = str1
    
    result = False
    diff_count = 0
    for s in long_str:
        if not find_char(short_str, s):
            diff_count += 1

    if diff_count > 1:
        return False
    else: 
        return True


def find_char(string: str, char: str) -> bool:
    for s in string:
        if s == char:
            return True
    return False

class TestOneWay(unittest.TestCase):
    def test_one_way_inserts(self):
        self.assertEqual(one_way("pale", "pales"), True)  # in the end
        self.assertEqual(one_way("pale", "spale"), True)  # in the beginning
        self.assertEqual(one_way("pale", "palse"), True)  # in the middle

    def test_one_way_removes(self):
        self.assertEqual(one_way("pale", "pal"), True)  # in the end
        self.assertEqual(one_way("pale", "ale"), True)  # in the beginning
        self.assertEqual(one_way("pale", "ple"), True)  # in the middle

    def test_one_way_replace(self):
        self.assertEqual(one_way("pale", "pals"), True)  # in the end
        self.assertEqual(one_way("pale", "sale"), True)  # in the beginning
        self.assertEqual(one_way("pale", "pase"), True)  # in the middle

if __name__ == "__main__":
    # print(one_way("pale", "pales"))
    unittest.main()

