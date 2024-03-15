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

# solution from the book
# 1. reduce the array to the 2 elements: list[1:]
# 2. compare last two elements and get the max
# 3. return back to the array with one more element and compare previous max with it: list[0] > sub_max
# 4. if the first element is bigger list[0], than sub_max, it becomes a new max
# 5. It goes so up to the whole array, but it only compares the first element and max,
# which we got from comparing two elements
def max(list):
    print(list)
    if len(list) == 2:  # base case
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    print(sub_max)
    return list[0] if list[0] > sub_max else sub_max

lst = [2, 6, 4, 3, 2, 5]
print(max(lst))