"""
https://leetcode.com/problems/longest-mountain-in-array/


"""

# arr: 2,1,4,7,3,2,5
# l:     ^
# r:               ^
# is increase?
# is decrease?
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        l = 0
        up = False
        down = False
        longest = 0
        for r in range(1, len(arr)):
            if arr[l] > arr[r]:
                up = True
            elif up and arr[l] < arr[r]:
                down = True
            else:
                up = False
                longest = r - l
                l = r
        
        return longest
                
            