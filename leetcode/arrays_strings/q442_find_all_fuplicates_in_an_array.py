"""

https://leetcode.com/problems/find-all-duplicates-in-an-array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
and each integer appears at most twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, 
excluding the space needed to store the output.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:

Input: nums = [1,1,2]
Output: [1]

Example 3:

Input: nums = [1]
Output: []

Thoughts:
1. Numbers in range [1, n], where n is len()
2. In oder to get constant extra space we have to change the input data

Explanation
https://www.youtube.com/watch?v=Y8x0iAVEITo

"""


class Solution1:
    """
    Brute force solution.
    Quick - O(n), but uses extra space O(n).
    """

    def findDuplicates(self, nums: list[int]) -> list[int]:
        counter = set()
        answer = []
        for i in nums:
            if i in counter:
                answer.append(i)
            else:
                counter.add(i)

        return answer


class Solution2:
    """
    Optimal solution.
    Mark the visited values directly in the input array as negative.
    1. We take all numbers as abs, since it can be negative.
    2. Numbers can be from 1 to n. So we take i - 1 index.
    3. Because numbers are up to n == len(), we use our input array directly for storing data.
    4. We mark at position nums[i - 1], if have seen the number i.
        So array itself store original values and index store if it was visited.

    Time complexity: O(n). Every value visited only once.
    Space complexity: O(1). We reuse input array.

    """

    def findDuplicates(self, nums: list[int]) -> list[int]:
        answer = []
        for i in nums:
            i = abs(i)  # get the abs values in case of negative
            if nums[i - 1] < 0:  # numbers are 1 to n, but array start from 0
                answer.append(i)
            else:
                nums[i - 1] = -nums[i - 1]  # change the sign

        return answer
