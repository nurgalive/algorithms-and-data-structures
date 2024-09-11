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
"""

import unittest

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
    def test_palindrome_simple(self):
        self.assertEqual(palindrome_hashmap("taco cat"), True)
        self.assertEqual(palindrome_hashmap("Rats live on no evil star"), True)
        self.assertEqual(palindrome_hashmap("Able was I ere I saw Elba"), True)
        self.assertEqual(palindrome_hashmap("Lleve"), True)
        self.assertEqual(palindrome_hashmap("Tacotac"), True)
        self.assertEqual(palindrome_hashmap("asda"), False)
        self.assertEqual(palindrome_hashmap("A man, a plan, a canal, panama"), True)

    def test_palindrome_array(self):
        self.assertEqual(palindrome_array("taco cat"), True)
        self.assertEqual(palindrome_array("Rats live on no evil star"), True)
        self.assertEqual(palindrome_array("Able was I ere I saw Elba"), True)
        self.assertEqual(palindrome_array("Lleve"), True)
        self.assertEqual(palindrome_array("Tacotac"), True)
        self.assertEqual(palindrome_array("asda"), False)
        self.assertEqual(palindrome_array("A man, a plan, a canal, panama"), True)
        

class TestGetCharId(unittest.TestCase):
    def test_get_char_id(self):
        self.assertEqual(get_char_id("a"), 0)
        self.assertEqual(get_char_id("b"), 1)
        self.assertEqual(get_char_id("z"), 25)
        self.assertEqual(get_char_id("A"), 0)
        self.assertEqual(get_char_id("B"), 1)
        self.assertEqual(get_char_id("Z"), 25)
        self.assertEqual(get_char_id("@"), -1)
        self.assertEqual(get_char_id(" "), -1)
        self.assertEqual(get_char_id(","), -1)

if __name__ == "__main__":
    # print(palindrome_array("taco cat"))
    unittest.main()