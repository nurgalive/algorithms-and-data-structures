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

def one_way_simple(str1: str, str2) -> bool:
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
    
    if len(long_str) - len(short_str) > 1:
        return False

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

def one_way_separate(str1: str, str2: str) -> bool:
    """
    O(s) - time complexity. s - for the shortest string.
    Improved time complexity function.
    Uses separate functions for replace and remove/insert.
    Function chosen based on the length of the string.
    """
    if len(str1) == len(str2):
       return check_replace(str1, str2)
    if len(str1) + 1 == len(str2) or len(str1) == len(str2) + 1:
        return check_insert_remove(str1, str2)
    if len(str1) - 1 == len(str2) or len(str1) == len(str2) - 1:
        return check_insert_remove(str2, str1)
    else:
        return False  # in case the difference more than one

def check_replace(str1: str, str2: str) -> bool:
    """
    Checks for the single difference in two strings.
    Supports only the same sized strings.
    """
    found_diff = False
    for i, _ in enumerate(str1):
        if str1[i] != str2[i]:
            if found_diff:
                return False
            else:
                found_diff = True
    return True

def check_insert_remove(str1: str, str2: str):
    """
    Function used in insert and remove cases.
    For the remove case, str1 and str2 have to be flipped.
    Two pointer approach is used.
    """
    id1 = 0
    id2 = 0
    while id1 < len(str1) and id2 < len(str2):
        if str1[id1] != str2[id2]:  # if index it it not same, is okay, change the
            if id1 != id2:
                return False
            id2 += 1
        else:
            id1 += 1
            id2 += 1
    return True


class TestOneWay(unittest.TestCase):
    def test_one_way_inserts(self):
        self.assertEqual(one_way_simple("pale", "pales"), True)  # in the end
        self.assertEqual(one_way_simple("pale", "spale"), True)  # in the beginning
        self.assertEqual(one_way_simple("pale", "palse"), True)  # in the middle

    def test_one_way_removes(self):
        self.assertEqual(one_way_simple("pale", "pal"), True)  # in the end
        self.assertEqual(one_way_simple("pale", "ale"), True)  # in the beginning
        self.assertEqual(one_way_simple("pale", "ple"), True)  # in the middle

    def test_one_way_replace(self):
        self.assertEqual(one_way_simple("pale", "pals"), True)  # in the end
        self.assertEqual(one_way_simple("pale", "sale"), True)  # in the beginning
        self.assertEqual(one_way_simple("pale", "pase"), True)  # in the middle

    def test_one_way_separate_replace(self):
        self.assertEqual(one_way_separate("pale", "pals"), True)  # in the end
        self.assertEqual(one_way_separate("pale", "sale"), True)  # in the beginning
        self.assertEqual(one_way_separate("pale", "pase"), True)  # in the middle

    def test_one_way_separate_inserts(self):
        self.assertEqual(one_way_separate("pale", "pales"), True)  # in the end
        self.assertEqual(one_way_separate("pale", "spale"), True)  # in the beginning
        self.assertEqual(one_way_separate("pale", "palse"), True)  # in the middle
    
    def test_one_way_separate_removes(self):
        self.assertEqual(one_way_simple("pale", "pal"), True)  # in the end
        self.assertEqual(one_way_simple("pale", "ale"), True)  # in the beginning
        self.assertEqual(one_way_simple("pale", "ple"), True)  # in the middle

if __name__ == "__main__":
    # print(one_way("pale", "pales"))
    unittest.main()

