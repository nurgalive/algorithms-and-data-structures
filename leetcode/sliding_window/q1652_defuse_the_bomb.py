"""
https://leetcode.com/problems/defuse-the-bomb

You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

    If k > 0, replace the ith number with the sum of the next k numbers.
    If k < 0, replace the ith number with the sum of the previous k numbers.
    If k == 0, replace the ith number with 0.

As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

Example 1:
Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

Example 2:
Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 

Example 3:
Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.

Constraints:

    n == code.length
    1 <= n <= 100
    1 <= code[i] <= 100
    -(n - 1) <= k <= n - 1

Explanation
https://www.youtube.com/watch?v=c4oOIi5YTE4

My comments:
This task requires good understanding of the math and how to make the iterating over loop circular.
"""


class Solution1:
    """
    Brute force solution.
    Iterating in both directions of size k.
    Key difficulty for is to implement proper circulation.
    Time: O(n * |k|). Two loops, one over n and second in size k.
    Space: O(n). Storing the same sized array for the answer.

    This solution is influences by the editorials.
    """

    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n
        if k != 0:
            for i in range(n):
                if k > 0:
                    for j in range(i + 1, i + k + 1):
                        res[i] += code[j % n]
                elif k < 0:
                    for j in range(i - abs(k), i):
                        res[i] += code[j + len(code) % len(code)]
        return res


class Solution2:
    """
    Cleaner solution influenced by NeetCode.

    Trick with the modulo division.
    0 % 4 = 0
    2 % 4 = 2
    4 % 4 = 0
    5 % 4 = 1
    Using mod we make the array circular for the second for loop (j)
    """

    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n  # creating resulting array in size of input

        # no need to handle 0 case, it will be handled automatically
        # if k == 0:
        #     return res

        for i in range(n):
            if k > 0:
                for j in range(i + 1, i + k + 1):  # iterating forward
                    res[i] += code[j % n]  # modulo division trick used here
            elif k < 0:
                for j in range(i - 1, i - 1 - abs(k), -1):  # iterating backwards
                    res[i] += code[j % n]  # we always stay within index n

        return res
