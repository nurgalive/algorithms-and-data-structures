# Grokking algos, page 9
# Complexity: O(log n)

# LeetCode
# https://leetcode.com/problems/binary-search/description/

def binary_search(arr: list, item: int) -> int: 
    low = 0
    high = len(arr) - 1  # actual last index

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(binary_search(arr, 17))