"""

Similar question being asked in the Google mock interview
https://www.youtube.com/watch?app=desktop&v=XKu_SEDAykw

https://leetcode.com/problems/two-sum
"""

class Solution:
    """
    Create a dict comp, which store complements to a target.
    Iterate over nums, 
    check if this number is already presented in the dict,
    if not, store the complement as key, and index as a value
    key = target - nums[i], val = i.
    
    Time complexity: O(nums)
    Space complexity: O(nums)
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        comp = {}  # complements
        for i in range(len(nums)):
            if nums[i] in comp:
                return i, comp[nums[i]]
            else:
                comp[target - nums[i]] = i

print(Solution().twoSum([2,7,11,15], 9))