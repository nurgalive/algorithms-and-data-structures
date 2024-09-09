"""
Cracking the coding interview. Exercise 1.4. Page 90.

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
- one letter is unique

Count frequencies of the letters
- min O(s)

Hints: #106, #121, #134, #136
#106.1.4 You do not have to-and should not-generate all permutations. This would be very
inefficient. [Yes, use frequencies]
#121.1.4 What characteristics would a string that is a permutation of a palindrome have? [They have even number of letter, except one]
#134.1.4 Have you tried a hash table? You should be able to get this down to 0(N) time. [Yes]
#136.1.4 Can you reduce the space usage by using a bit vector?
"""

def palindrome_hashmap(input: str):
    """
    O(s)
    Int can be used to store . English letters < 32
    Count frequencies using hash map.
    """

    freq = dict()

    for s in input:  # O(s)
        if s == " ": continue
        freq[s] =  freq.get(s, 0) + 1

    not_even = False
    for val in freq.values():  # O(1)
        if val % 2 == 1:
            if not_even:
                return False
            else:
                not_even = True
    else:
        return True

def palindrome_bitvector(input: str):
    """
    Check is_unique.py for details.
    """
    pass

if __name__ == "__main__":
    print(palindrome_hashmap("taco cat"))