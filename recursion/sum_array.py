# Grokking algos, page 56
# 4.1 Write out the code for the earlier sum function.

def sum_arr(arr):
    if len(arr) == 0:
        return "Zero sized array!"
    return get_sum(arr, len(arr) - 1) 

def get_sum(arr, size):
    if size == 0:
        return arr[size]
    else:
        return arr[size] + get_sum(arr, size - 1)

exmp = [2, 4, 6]
print(sum_arr(exmp))