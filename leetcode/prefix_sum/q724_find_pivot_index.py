"""

https://leetcode.com/problems/find-pivot-index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 
Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

Explanation
https://www.youtube.com/watch?v=u89i60lYx8U

My comments:
Return index.

"""


class Solution1:
    """
    Brute force solution.
    Time: O(N^2)
    Space: O(1)
    """

    def pivotIndex(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0

        left_sum = 0
        for i in range(len(nums)):
            right_sum = 0
            for j in range(i + 1, len(nums)):
                right_sum += nums[j]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


class Solution2:
    """
    Optimal solution using prefix sum.
    We calculate sum once - O(N)
    Then iterate over array and we calculate left sum and subtract it from total.
    And compare it.
    Time: O(N)
    Space: O(1)
    """

    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)  # O(n)

        left_sum = 0
        for i, ival in enumerate(nums):
            right_sum = total - left_sum - ival
            if left_sum == right_sum:
                return i
            left_sum += ival
        return -1


# experimenting with the assert based simple tests

assert Solution1().pivotIndex([]) == -1
assert Solution1().pivotIndex([1]) == 0
assert Solution1().pivotIndex([1, 0]) == 0
assert Solution1().pivotIndex([1, 0, 1]) == 1

assert Solution2().pivotIndex([]) == -1
assert Solution2().pivotIndex([1]) == 0
assert Solution2().pivotIndex([1, 0]) == 0
assert Solution2().pivotIndex([1, 0, 1]) == 1
