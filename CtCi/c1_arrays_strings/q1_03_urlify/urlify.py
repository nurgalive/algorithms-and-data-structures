"""
Cracking the coding interview. Exercise 1.3. Page 90.

1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the 
string has sufficient space at the end to hold the additional characters,and that you are given 
the "true" length of the string. (Note: If implementing in Java, please use a character array 
so that you can perform this operation in place.)

EXAMPLE
Input:"Mr John Smith    ", 13
Output:"Mr%20John%20Smith"

Hints:
53.1.3 It's often easiest to modify strings by going from the end of the string to the beginning.
118.1.3 You might find you need to know the number of spaces. Can you just count them?

My interpreted task goal:
Write a method, which replaces all the spaces between words with '%20'. As an input given a string
array, which has enough space at the end in order to have an in-place updates. Use it as the only array to store the data.
And you are also given a true length of the string, which includes words and spaces between them.

My comments, after understanding the task:
- This is important to do in-place
- The input format is strictly limited by the format of the input,
it means that the 13 means exact the size of the input as it is from the beginning.
And the input array (char) size is 17, because for every existing space character,
two more spaces are added. It means, that the string has two spaces, which equals to 6 spaces required, 
in order to replace spaces with '%20' and have enough space.

"""


# O(S), linear based on the string length
def urlify1(string: str, length: int) -> str:
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

# Use array instead of string concatenation.
# Length used in order to create an array. In python not needed much

# Algo
# Start from the end.
# It it is a space - ignore, else add to the result.

def urlify2(string: str, length: int) -> str:
    string1 = list(string)
    result = [0 for i in range(length)]

    num_of_spaces = string1.count(" ")
    print(num_of_spaces)




if __name__ == "__main__":
    print(urlify1("Mr John Smith    ", 13))
    Mr%20John%20Smith
