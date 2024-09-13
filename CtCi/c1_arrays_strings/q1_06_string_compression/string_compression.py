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

"""


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
        


if __name__ == "__main__":
    print(compress("aabcccccaaa"))  # a2blc5a3
    print(compress(""))  # a2blc5a3
    print(compress("abcdefg"))  # a2blc5a3
    print(len_compress("aabcccccaaa"))  # 8
    print(compress_with_compare("aabcccccaaa"))  # a2blc5a3