"""

https://leetcode.com/problems/subarray-sum-equals-k

"""


class Solution:
    """
    Brute force solution.
    Tries every possible subarray.
    Time complexity: O(N^2)
    Space comlexity: O(1)
    
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


nums = [1, 1, 1]
k = 12450
# print(nums)

print(Solution().subarraySum(nums, k))
