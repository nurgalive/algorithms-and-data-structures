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

More solutions:
https://codereview.stackexchange.com/questions/141281/urlify-a-string-using-python
https://codereview.stackexchange.com/questions/141391/urlify-a-character-array-using-python-follow-up

Commentators in those links point out, that it is not possible to comply with the O(1) requirement,
since in python we have to make a copy of the string. Strings in python are immutable.

"""

# my naive solution
def urlify1(string: str, length: int) -> str:
    """
    O(S), linear based on the string length
    """
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

# pythonic simple solution
def urlify2(string: str, length: int):
    return "%20".join(string.split())


# java-way
def urlify3(string: str, true_length: int) -> str:
    """
    Algo:
    1. Create an array from the string
    2. Count spaces using true_length
    3. Starting from back, move characters to the back of the array.
    If character is a space, add '%20'
    Start from the end.
    It it is a space - ignore, else add to the result.

    """
    space_count = 0
    string1 = list(string)  # created an string array from string
    print("string1", string1)

    # check that string is smaller than true_length
    if len(string1) < true_length:
        return "Error, true length smaller than the string"

    for s in range(true_length):
        if string1[s] == ' ':
            space_count += 1
    print(space_count)

    # this how we calculate the end of the array
    # 1 space is already in the true_length, we need to add two more for a every space
    # since ' ' should become '%20'
    index = true_length + (space_count * 2)
    # index keeps track of the location from the end of array

    # this loop should repeat true_lengths times
    for i in range(true_length - 1, 0, -1):
        if string1[i] == ' ':
            string1[index - 1] = '0'
            string1[index - 2] = '2'
            string1[index - 3] = '%'
            index -= 3
        else:
            # shifting the letters to the right to free up space for the space chars
            string1[index - 1] = string[i]
            index -= 1
    
    print(string1)

    return "".join(string1)


# def urlify4(string: str, length: int) -> str:
#     string1 = list(string) # ?
#     result = [0 for i in range(length)]

#     space_count = string1.count(" ")
#     print(space_count)


if __name__ == "__main__":
    print(urlify3("Mr John Smith    ", 13))
    # Expected output: 
    # Mr%20John%20Smith
