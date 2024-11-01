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
    Mark the visited values directly in the input array.
    """
    def findDuplicates(self, nums: list[int]) -> list[int]:
        pass