"""

https://leetcode.com/problems/subarray-sum-equals-k

Given an array of integers nums and an integer k, return the total number of subarrays 
whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Explanation
https://www.youtube.com/watch?v=fFVZt-6sgyo

"""


class Solution1:
    """
    Brute force solution.
    Tries every possible subarray.
    Time complexity: O(N^2)
    Space complexity: O(1)
    """

    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        for nleft in range(len(nums)):
            cur_sum = 0
            for nright in range(nleft, len(nums)):
                cur_sum += nums[nright]
                if cur_sum == k:
                    result += 1
        return result


class Solution2:
    """
    Optimal solution.
    Time complexity: O(N)
    Space complexity: O(N)

    This solutions uses very clever trick.
    It stores prefix sums (cumulative sums) frequencies in the hashmap.
    It iterates over array, keep the current sum. If current sum - k exists in the hashmap,
    it means there are subarrays with sum k.
    """

    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        prefix_dict = {0: 1}

        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            result += prefix_dict.get(prefix_sum - k, 0)
            prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1

        print(prefix_dict)
        return result


nums1 = [1, 1, 1]
nums2 = [1, -1, 1, 1, 1, 1]
k = 3
# print(nums)

print(Solution2().subarraySum(nums2, k))
