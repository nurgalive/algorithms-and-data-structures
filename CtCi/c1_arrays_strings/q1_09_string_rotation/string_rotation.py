"""
Cracking the coding interview. Exercise 1.9. Page 91.

1.9 String Rotation: Assume you have a method 'isSubstring' which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
Hints: #34, #88, #104

#34 1.9 If a string is a rotation of another, then it's a rotation at a particular point. For example,
a rotation of waterbottle at character 3 means cutting waterbottle at character 3
and putting the right half (erbottle) before the left half (wat).

#88 1.9 We are essentially asking if there's a way of splitting the first string into two parts, x and
y, such that the first string is xy and the second string is yx. For example, x = wat and
y = erbottle. The first string is xy = waterbottle. The second string is yx =
erbottlewat.

#104 1.9 Think about the earlier hint. Then think about what happens when you concatenate
erbottlewat to itself. You get erbottlewaterbottlewat.

Examples:
https://github.com/careercup/CtCI-6th-Edition/blob/master/Java/Ch%2001.%20Arrays%20and%20Strings/Q1_09_String_Rotation/Question.java
https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_01/p09_string_rotation.py

Explanation:
https://www.youtube.com/watch?v=JVoHZbmdrD0

It took me quite some time to understand what is actually required.
So, goal is to find if the string1 is a rotation of the string2.
"waterbottle" is a rotation of "erbottlewat"

I don't like this question. It is vague.

"""

def string_rotation1(orig: str, s2: str) -> bool:
    """
    Naive solution.
    """
    if len(orig) != len(s2):
        return False
    concat = s2+s2
    # print(concat)

    correct_letters = 0
    orig_pointer = 0
    for c in concat:
        if c == orig[orig_pointer]:
            correct_letters += 1
            orig_pointer += 1
            if orig_pointer == len(orig):
                break

    if correct_letters == len(orig):
        return True
    else: 
        return False
    
def string_rotation2(s1: str, s2: str) -> bool:
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    s3: str = s2 + s2
    if s1 in s3:
        return True
    else: 
        return False


if __name__ == "__main__":
    print(string_rotation1("waterbottle", "erbottlewat"))
    print(string_rotation2("waterbottle", "erbottlewat"))