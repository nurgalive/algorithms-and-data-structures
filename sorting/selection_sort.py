# Grokking algos, page 35
# Complexity: O(n^2)

def find_smallest(arr: list) -> int:
    smallest = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[smallest]:
            smallest = i
    return smallest

def selection_sort(arr: list[int]) -> list[int]:
    result = []
    for _ in range(0, len(arr)):
        result.append(arr.pop(find_smallest(arr)))
    
    return result

test_arr = [3, 8, 1, 5, 9, 6]
print(selection_sort(test_arr))