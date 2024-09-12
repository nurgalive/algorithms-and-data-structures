"""
Cracking the coding interview. Exercise 1.4. Page 91.

Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints:#92, #110


"""


def compress(string: str) -> str:
    """
    My brute force solution.
    O(s) - time and space.
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

if __name__ == "__main__":
    print(compress("aabcccccaaa"))  # a2blc5a3
    print(compress(""))  # a2blc5a3
    print(compress("abcdefg"))  # a2blc5a3