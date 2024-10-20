"""
This task is similar to 1.3 Urlify from CtCi, but not so much. Because of that I moved it to a separate file.
https://github.com/nurgalive/algorithms-and-data-structures/blob/main/CtCi/c1_arrays_strings/q1_03_urlify/urlify.py


Thanks to AI, found an analog on LeetCode:
https://leetcode.com/problems/rearrange-spaces-between-words

LeetCode task is not exactly the same.
It is about properly counting the spaces and arranging them.
In order to solve this question knowledge of the Python methods is important.
split() - find words
count() - count spaces
.join - creating strings

"""

class Solution:
    """
    My bruteforce to leetcode.
    """
    def reorderSpaces(self, text: str) -> str:
        words_count = len(text.split())
        space_count = len(text) - len("".join(text.split()))

        if words_count > 1:
            is_additional_space_needed = False
            additional_spaces = space_count % (words_count - 1)
            if additional_spaces > 0:
                is_additional_space_needed = True
            
            if words_count > 1:
                spaces_bw_words = space_count // (words_count - 1)

            result = []
            words = text.split()
            for i in range(len(words)):
                result.append(words[i])
                if i < len(words) - 1:
                    result.extend([" "] * spaces_bw_words)

            if is_additional_space_needed:
                result.extend([" " * additional_spaces])
        else:
            result = []
            result.append("".join(text.split()))
            result.extend([" "] * space_count)
    
        return "".join(result)

class Solution:
    """
    Improved leetcode solution.
    Time: O(text)
    Space: O(1)?. Not exactly because of the join function, which creates copies of the string.
    """
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        words_count = len(words)
        space_count = text.count(" ")

        if words_count > 1:
            additional_spaces = space_count % (words_count - 1)
            spaces_bw_words = space_count // (words_count - 1)

            return (" " * spaces_bw_words).join(words) + " " * additional_spaces
            
        else:
            return "".join(words[0]) + " " * space_count

