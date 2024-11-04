"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

https://leetcode.com/problems/move-zeroes/

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Explanation
https://www.youtube.com/watch?v=aayNRwUN3Do
"""


class Solution1:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        My initial solution.
        Time: O(n)
        Space: O(1)
        """

        l = 0
        r = 1
        while l < len(nums) and r < len(nums):
            if nums[l] == 0:
                if nums[r] == 0:
                    r += 1  # r always updated
                else:
                    nums[l] = nums[r]
                    nums[r] = 0
                    r += 1  # r always updated
                    l += 1
            else:
                l += 1
                r += 1  # r always updated


class Solution2:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Improved solution after explanation.
        Time: O(n)
        Space: O(1)
        """

        l = 0  # left pointer
        for r in range(len(nums)):
            if nums[r]:  # if zero - ignore
                # swap left pointer position value with right pointer position
                nums[l], nums[r] = nums[r], nums[l]
                l += 1


nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
# l         ^
# r           ^
print(nums)
Solution2().moveZeroes(nums)
print(nums)
