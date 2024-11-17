"""
Prefix sum also called cumulative sum is a technique for quickly solving range (subarray) questions.
0-based prefix sum is preferred, because it makes code easier and cleaner.
Array               = [2, 3, 1, 4]
Prefix sum array    = [0, 2, 5, 6, 10] 

With negative numbers
Array               = [1, 2, -3, 5]
Prefix sum array    = [0, 1, 3, 0, 5]

Formula to get the range sum of the subarray depends of the approach/

"""


def build_prefix_sum_1_based(arr):
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    
    return prefix_sum

def build_prefix_sum_0_based(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    
    for i in range(0, n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    return prefix_sum

def range_sum_1_based(prefix_sum, l, r):
    """
    l - left pointer
    r - right pointer
    Prefix sum array has the same length, at the original array.
    Find range sum formula: prefix_sum[r] - prefix_sum[l -1]
    """
    if l == 0:
        return prefix_sum[r]
    else:
        return prefix_sum[r] - prefix_sum[l - 1]
    
def range_sum2(prefix_sum, l, r):
    """
    l - left pointer
    r - right pointer
    Prefix sum array has length n + 1.
    Formula for the range queries: prefix_sum[r + 1] - prefix_sum[l]
    """
    return prefix_sum[r + 1] - prefix_sum[l]

def subarraySum(nums: list[int], k: int) -> int:
    cumsum = 0
    cumsum_map = {0: 1}
    res = 0

    print("cumsum_map", cumsum_map)
    for num in nums:
        cumsum += num
        res += cumsum_map.get(cumsum - k, 0)
        print(res)
        cumsum_map[cumsum] = cumsum_map.get(cumsum, 0) + 1
        print("cumsum_map", cumsum_map)
    return res

# arr = [1, 2, 3, -1, -2, -3]
arr = [1, -1, 1, -1, 1, 1]

k = 1
print(arr)
print(build_prefix_sum_0_based(arr))
print(subarraySum(arr, k))

# Example usage
# 0  1  2  3   4
# A = [3, 1, 4, 1, 5]
# P = build_prefix_sum(A)
# P2 = build_prefix_sum2(A)
# print("Prefix Sum Array:", P)
# print("Prefix Sum Array2:", P2)
# print("Sum from index 1 to 3:", range_sum(P, 0, 3))  # Output: 6
# print("Sum from index 1 to 3:", range_sum2(P2, 0, 3))  # Output: 6



