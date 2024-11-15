"""

https://leetcode.com/problems/contiguous-array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    
Explanation
https://www.youtube.com/watch?v=agB1LyObUNE&t=28

"""


class Solution1:
    """
    Brute force solution.
    Check every possible subarray.
    Time complexity: O(N^2)
    Space complexity: O(1)
    """

    def findMaxLength(self, nums: list[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            zeroes = 0
            ones = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zeroes += 1
                if nums[j] == 1:
                    ones += 1
                if zeroes == ones:
                    max_len = max(max_len, j - i + 1)
        return max_len


nums1 = [0, 1, 0]
nums2 = [0, 0, 1, 0, 0, 0, 1, 1]
print(Solution1().findMaxLength(nums2))
