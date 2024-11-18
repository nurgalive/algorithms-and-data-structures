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


class Solution2:
    """
    A bit more optimal solution using prefixsum (cumsum).
    Disadvantage, we still recalculate cumsum for the every subarray.
    Time: O(N^2)
    Space: O(1)
    """

    def findMaxLength(self, nums):
        max_length = 0
        n = len(nums)

        # Convert 0s to -1s
        nums = [-1 if num == 0 else 1 for num in nums]

        for i in range(n):
            prefix_sum = 0
            for j in range(i, n):
                prefix_sum += nums[j]
                if prefix_sum == 0:
                    max_length = max(max_length, j - i + 1)

        return max_length


class Solution3:
    """
    Optimal solution, using cum sum and hashmap.
    We use hashmap in order to save the cum sum for subarrays.
    Key idea: If we encounter the same cum sum at two different indices,
    it means the subarray between those indices has an equal number of 0s and 1s.
    """

    def findMaxLength(self, nums: list[int]) -> int:
        max_len = 0
        cumsum = 0
        cumsum_map = {0: -1}  # cumsum: index
        for i, ival in enumerate(nums):
            if ival == 0:
                cumsum -= 1
            else:
                cumsum += 1
            if cumsum in cumsum_map:
                max_len = (
                    i - cumsum_map[cumsum]
                )  # current index minus index with the cumsum
            else:
                cumsum_map[cumsum] = i

        return max_len


class Solution4:
    """
    Alternative optimal solution.
    Here we do not init the dict with 0: -1 for the case,
    when the entire array is the biggest subarray.
    But instead treat this case directly in the code.
    """

    def findMaxLength(self, nums: list[int]) -> int:
        max_len = 0
        cumsum = 0
        cumsum_map = {}  # cumsum: index
        for i, ival in enumerate(nums):
            if ival == 0:
                cumsum -= 1
            else:
                cumsum += 1
            if cumsum not in cumsum_map:
                cumsum_map[cumsum] = i
            if cumsum == 0:  # if subarray is entire array
                max_len = i + 1
            else:
                max_len = max(
                    max_len, i - cumsum_map[cumsum]
                )  # current index minus index with the cumsum

        return max_len


nums1 = [0, 1, 0]
nums2 = [0, 0, 1, 0, 0, 0, 1, 1]
nums3 = [0, 1, 1, 0, 1, 1, 1, 0]  # interesting case
print(Solution1().findMaxLength(nums2))
