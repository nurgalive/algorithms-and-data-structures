# Grokking algos, page 59
# 4.2 Write a recursive function to count the number of items in a list.

def count(arr):
    if len(arr) == 0:
        return "Zero sized array!"
    return get_count(arr, len(arr) - 1)

def get_count(arr, size):
    if size == 0:
        return 1
    else:
        return 1 + get_count(arr, size - 1)

test = [2, 4, 6]
print(count(test))
