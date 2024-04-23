"""
Cracking the coding interview. Exercise 1.3. Page 90.

1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the 
string has sufficient space at the end to hold the additional characters,and that you are given 
the "true" length of the string. (Note: If implementing in Java, please use a character array 
so that you can perform this operation in place.)

EXAMPLE
Input:"Mr John Smith ", 13
Output:"Mr%20John%20Smith"

#53.1.3It's often easiest to modify strings by going from the end of the string to the beginning.
#118.1.3You might find you need to know the number of spaces. Can you just count them?
"""

def urlify(string: str, length: int) -> str:
    result = ""
    for i, s in enumerate(string):
        if i == 0 and s == " ":
            continue
        elif i == len(string) - 1 and s == " ":
            continue
        elif string[i - 1] == " " and string[i] == " ":
            continue
        elif string[i] == " ":
            result += "%20"
        else:
            result += string[i]

    return result

if __name__ == "__main__":
    print(urlify("Mr   John   Smith ", 13))