"""
Cracking the coding interview. Exercise 1.4. Page 91.

Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints:#92, #110

#92. 1.6 Do the easy thing first. Compress the string, then compare the lengths.
#110. 1.6 Be careful that you aren't repeatedly concatenating strings together. This can be very
inefficient.

LeetCode: https://leetcode.com/problems/string-compression

"""

import unittest

class Solution1:
    """
    Initial LeetCode solution.
    
    Run:
    chars = ["a","a","a","b","b","a","a"]
    print(chars[0:Solution().compress(chars)])
    """
    def compress(self, chars: list[str]) -> int:
        if len(chars) == 1:
            return len(chars)

        r = 0
        i = 0
        while i < len(chars):
            print("l", r)
            print("r", i)
            curr_char = chars[r]
            counter = 0
            while i < len(chars) and curr_char == chars[i]:
                counter += 1
                i += 1

            chars[r] = curr_char
            r += 1
            if counter > 1:
                counter_str = str(counter)
                for j in range(len(counter_str)):
                    chars[r] = counter_str[j]
                    r += 1

        return r
    
class Solution2:
    """
    Improved LeetCode solution.
    Used 3 pointer:
    - write: tracks the last position written in the sequence, used to mark where to write the next 
      character and result
    - left: holds the position of characters to compare with the right pointer. Moves to the position
      of the right pointer after writing the current occurrences
    - right: moves forward to scan characters, comparing each with the left pointer
    """
    def compress(self, chars: list[str]) -> int:
        l = 0  # left
        r = 0  # right
        write = 0  # write pointer and answer

        while l < len(chars):  # iterate until we reach the end
            
            while r < len(chars) and chars[l] == chars[r]:
                r += 1

            chars[write] = chars[l]  # write current char
            write += 1  # update last written pointer

            if r - l > 1:  # if index difference more than 1, write occurrences
                for digit in str(r - l):  # converting occurrences into string and iterating over them
                    chars[write] = digit  # adding occurrences to chars
                    write += 1  # update last written pointer
            l = r  # moving the left pointer to the right pointer position
        
        return write  # return last written position

def compress(string: str) -> str:
    """
    My brute force solution.
    O(s + c) - time and space. S - the size of the string to create compressed version.
    C - is for the converting array into the string.
    Have to iterate over every letter and count them.
    
    """
    if len(string) < 1:
        return ""
    result = []
    letter = string[0]
    count = 0
    for s in string:
        if s == letter:
            count += 1
            letter = s
        else:
            result.append(letter)
            result.append(str(count))
            count = 1
            letter = s

    result.append(letter)
    result.append(str(count))
    

    return "".join(result) if len(result) < len(string) else string

def compress_with_compare(string: str) -> str:
    """
    O(s1 + s2 + c)
    - s1 - get to know the size of the compressed string
    - s2 - calculate the compressed string
    - c - convert tuple to the string

    Write a function, which calculates in advance the size compressed string.
    Since we know in advance the size of the compressed string, we can use it:
      - directly decide, what is shorter: original or compressed string
      - more memory efficient, to use predefined list size instead of the list, which has default size
    """
    compressed_size = len_compress(string)
    if compressed_size > len(string):
        return string
    
    result = ["" for _ in range(0, compressed_size)]

    id = 0
    count = 0
    for i, s in enumerate(string):
        count += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            result[id] = string[i]
            result[id + 1] = str(count)
            id += 2
            count = 0

    return "".join(result)

        
def len_compress(string: str) -> int:
    """
    Returns the compressed string length.
    Gives us an answer, if need to caclulate the compressed string,
    as well as the size of required list.
    """
    compress_len = 0
    count = 0  # we need to keep count to now if the count one or more digits
    for i, _ in enumerate(string):
        count += 1 

        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compress_len += len(str(count)) + 1  # get the length of the count and add it to the len count
            count = 0

    return  compress_len


class TestCompress(unittest.TestCase):
    cases = [("aabcccccaaa", "a2b1c5a3",), ("abcdefg", "abcdefg",), 
             ("aaaaaaaaaaaa", "a12",)]
    
    def test_compress(self):
        for string, expected in self.cases:
            with self.subTest(string=string, expected=expected):
                self.assertEqual(compress(string), expected)
                self.assertEqual(compress_with_compare(string), expected)
    
    def test_len_compress(self):
        self.assertEqual(len_compress(""), 0)
        self.assertEqual(len_compress("aabcccccaaa"), 8)
        self.assertEqual(len_compress("aaaaaaaaaaaa"), 3)     


if __name__ == "__main__":
    unittest.main()