# arr: 2,1,4,7,3,2,5
# l:           ^
# r:             ^
# is increase?
# is decrease?
class Solution1:
    """
    TODO: Optimize solution, gives a wrong answer.
    
    Optimal solution, which is always O(n),
    but harder to implement.
    """
    def longestMountain(self, arr: list[int]) -> int:
        if len(arr) < 3:
            return 0

        l = 0
        mount_stopped = False
        mount_started = False
        longest = 0
        left = 0
        right = 0
        for r in range(1, len(arr)):
            if arr[l] < arr[r] or r == len(arr) - 1:
                if mount_stopped:
                    mount_started = False
                    if r == len(arr) - 1:
                        count += 1
                    count += 1
                    longest = max(count, longest)
                    count = 0

                mount_started = True
                l +=1
                count += 1
            # elif arr[l] > arr[r] and mount_started:
            #     l +=1
            #     count += 1
            elif arr[l] > arr[r] and not mount_started:
                l += 1

            else:
                mount_stopped = True
                l +=1
                count += 1
        
        return longest

class Solution2:
    def longestMountain(self, arr: list[int]) -> int:
        if len(arr) < 3:
            return 0

        longest = 0
        count = 1  # Initialize count to 1 since we start with a single element
        isIncreasing = True

        for r in range(1, len(arr)):
            if arr[r] > arr[r - 1]:
                isIncreasing = True # We are in the increasing phase of a potential mountain.
                count += 1
            elif arr[r] < arr[r - 1]:
                if isIncreasing:  # Only count as a mountain if we were previously increasing
                    longest = max(longest, count)
                isIncreasing = False
                count += 1
            else: # arr[r] == arr[r - 1] : Reset
                isIncreasing = True
                count = 1

        # Check if the last sequence formed a mountain
        if isIncreasing and count > longest:
            longest = max(longest, count)
        
        return longest


class Solution3:
    """
    Suboptimal solution, which is easy to understand and implement.
    We iterate over array, until we find a peak.
    Then start two-pointers in the left and in the right directions from the peak.
    
    Time complexity: average O(N), but worst case O(N^2)
    Example of of worst case:
    [1, 2, 1, 2, 1, 2, 1]
    In this case we will have to iterate two times over the array.
    
    Space complexity: O(1)
    
    """
    def longestMountain(self, arr: list[int]) -> int:
        if len(arr) < 3:
            return 0

        # search for the peak
        l = 0
        r = 0
        longest = 0
        for i in range(1, len(arr) - 1):  # start from 1, because peak cannot be at 0
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l = i - 1
                r = i + 1

                # start from peak in both directions
                # go left till the end of inreasing part
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1

                # go right in the decreasing part
                while r < len(arr) - 1 and arr[r + 1] < arr[r]:
                    r += 1

                # find len of the mountain
                longest = max(longest, r - l + 1)

                # move i to the end of the current mountain to skip redundant checks
                i = r
        
        return longest

arr1 = [2,1,4,7,3,2,5]
arr2 = [0,1,2,3,4,5,4,3,2,1,0]
arr3 = [2, 2, 2]
print(Solution3().longestMountain(arr1))
# print(Solution3().longestMountain(arr2))