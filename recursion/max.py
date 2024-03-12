# Grokking algos, page 59
# 4.3 Find the maximum number in a list.

def calc_max(arr: list[int]) -> int:
    return get_max(arr, len(arr) - 1, arr[len(arr) - 1])

def get_max(arr: list[int], size: int, max_val: int) -> int:
    if size == 0:
        if arr[size] > max_val:
            return arr[size]
        else:
            return max_val
    if arr[size] > max_val:
        return get_max(arr, size - 1, arr[size])
    else: 
        return get_max(arr, size - 1, max_val)

lst = [2, 6, 4, 3, 2, 5]
print(calc_max(lst))