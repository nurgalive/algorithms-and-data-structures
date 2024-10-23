"""
Cracking the coding interview. Exercise 1.4. Page 91.

Palindrome Permutation: Given a string, write a function to check if it is a permutation 
of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited 
to just dictionary words.

EXAMPLE
Input:Tact Coa
Output:True (permutations: "taco cat", "atco eta", etc.)

My ideas:
Brut-force solution - s!

What palindrome is?
- all letters divided by two
- one or zero letter is unique
- example: anna, ana, an na

Count frequencies of the letters
- min O(s)

Hints: #106, #121, #134, #136
#106.1.4 You do not have to-and should not-generate all permutations. This would be very
inefficient. [Yes, use frequencies]
#121.1.4 What characteristics would a string that is a permutation of a palindrome have? [They have even number of letter, except one]
#134.1.4 Have you tried a hash table? You should be able to get this down to 0(N) time. [Yes]
#136.1.4 Can you reduce the space usage by using a bit vector?

Solution from the author:
https://github.com/careercup/CtCI-6th-Edition/tree/master/Java/Ch%2001.%20Arrays%20and%20Strings/Q1_04_Palindrome_Permutation


Python solution:
https://github.com/careercup/CtCI-6th-Edition-Python/blob/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter1/4_Palindrome%20Permutation/PalindromePermutation.py

odd - нечетный
even - четный


LeetCode - https://leetcode.com/problems/valid-palindrome
Requires premium - https://leetcode.com/problems/palindrome-permutation/

Interesting, thanks to LeetCode, I found an obvious error in the code.
And what is even more interesting, I found an error in code of the original author of book.
Unfortunately, the community solution in Python also has the same error.
Check tests below for the exact case.
Here is the power of community and the LeetCode.
For completeness I left old version of code.
"""

import unittest

class Solution1:
    """
    LeetCode solution.
    Using two pointers.
    Time complexity: O(S)
    Space complexity: O(1)
    """
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        s = self.clean(s).lower()
        mid = len(s) // 2 
        index = len(s) - 1

        for i in range(mid):
            if s[i] != s[index]:
                return False
            index -= 1
        return True  

    def clean(self, s: str) -> str:
        res = []
        for char in s:
            if self.pos(char) != -1:
                res.append(char)
        return "".join(res)

    def pos(self, s: str) -> int:
        if ord("a") <= ord(s) <= ord("z"):
            return ord(s) - ord("a")
        elif ord("A") <= ord(s) <= ord("Z"):
            return ord(s) - ord("A")
        elif ord("0") <= ord(s) <= ord("9"):
            return ord(s)
        elif s == " ":
            return -1
        else:
            return -1

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        head = 0
        tail = len(s) - 1

        while head < tail:
            if not s[head].isalnum():
                head += 1
                continue
            if not s[tail].isalnum():
                tail -= 1
                continue
            if s[head].lower() != s[tail].lower():
                return False
            else:
                head += 1
                tail -= 1
        return True


def isalnumchar(char: str) -> bool:
    """
    My own implementation of the .isalnum()
    """
    if ord("a") <= ord(char) <= ord("z"):
        return True
    elif ord("A") <= ord(char) <= ord("Z"):
        return True
    elif ord("0") <= ord(char) <= ord("9"):
        return True
    else:
        return False 

def to_lower(char: str) -> str:
    """
    My own implementation of lower()
    """
    arr = []
    print(arr)
    for c in char:
        print(c)
        if ord("A") <= ord(c) <= ord("Z"):
            arr.append(chr(ord("a") + ord(c) - ord("A")))
        else:
            arr.append(c)
    return "".join(arr)


def palindrome_hashmap(input: str):
    """
    O(s) - time and space.
    Simplest solution. Treats all letters as lowercase. Only checks for 
    Int can be used to store . English letters (26) < 32
    Count frequencies using hash map. Uses a bit more memory, than array. But
    does not require ord() conversion to find id.

    This approach uses two loops. But in the loop less operations.
    """

    freq = dict()

    non_letter_chars = {" ", ","}

    for s in input:  # O(s)
        if s in non_letter_chars: continue
        freq[s.lower()] =  freq.get(s.lower(), 0) + 1

    odd_found = False
    for val in freq.values():  # O(1)
        if val % 2 == 1:
            if odd_found:  # if found again
                return False  # return false (not a palindrome)
            else:  # found a first not even nuber
                odd_found = True
    else:
        return True

def palindrome_array(input: str) -> bool:
    """
    O(s) - time and space.
    Uses the same idea of applying ord() from the is_unique.py instead of
    using hashmap. Because of the a little bit more memory efficient.
    Uses the ord() conversion of the letters. Checks the result by every iteration of the
    loop. Only one loop, but does more operations per iteration.
    """
    #                                 122   -    97
    counter = [0 for _ in range(0, ord('z') - ord('a') + 1)]  # initializing the array with lowercase letters a-z

    odd_count = 0
    for s in input:
        char_id = get_char_id(s)
        if char_id != -1:
            counter[char_id] += 1
            if counter[char_id] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
                
    
    else:
        return odd_count <= 1


def get_char_id(char: str) -> int:

    # convert 'a-z' to a num '0-26'
    if ord("a") <= ord(char) <= ord("z"):
        return ord(char) - ord("a")
    else:
        # convert 'A-Z' to a num '0-26'
        if ord("A") <= ord(char) <= ord("Z"):
            return ord(char) - ord("A")
    return -1  # if it is not a letter



# def palindrome_bitvector(input: str):
#     """
#     Check is_unique.py for details.
#     """
#     pass


class TestPalindrome(unittest.TestCase):
    test_cases = [
        ("taco cat", True),
        ("Rats live on no evil star", True),
        ("Able was I ere I saw Elba", True),
        ("Lleve", False),
        ("Tacotac", False),
        ("asda", False),
        ("A man, a plan, a canal, panama", True),
        ("abb", False),  # this test from LeetCode is not working
        ("abba", True),
        ("abbt", False),
        (" ", True),
        ("a", True),
        ("a.", True),
        ("a0", False),
    ]

    # for completeness I left old version of code
    # def test_palindrome_simple(self):
    #     for string, result in self.test_cases:
    #         with self.subTest(string=string, result=result):
    #             self.assertEqual(palindrome_hashmap(string), result)

    # for completeness I left old version of code
    # def test_palindrome_array(self):
    #     for string, result in self.test_cases:
    #         with self.subTest(string=string, result=result):
    #             self.assertEqual(palindrome_array(string), result)
    
    def test_palindrome_sol1(self):
        for string, result in self.test_cases:
            with self.subTest(string=string, result=result):
                self.assertEqual(Solution1().isPalindrome(string), result)

    def test_palindrome_sol2(self):
        for string, result in self.test_cases:
            with self.subTest(string=string, result=result):
                self.assertEqual(Solution2().isPalindrome(string), result)
        

class TestGetCharId(unittest.TestCase):
    test_conversion = [
        ("a", 0),
        ("b", 1),
        ("z", 25),
        ("A", 0),
        ("B", 1),
        ("Z", 25),
        ("@", -1),
        (" ", -1),
        (",", -1)
    ]

    def test_get_char_id(self):
        for string, result in self.test_conversion:
            with self.subTest(string=string, result=result):
                self.assertEqual(get_char_id(string), result)

if __name__ == "__main__":
    # print(palindrome_array("taco cat"))
    unittest.main()