# Grokking algos, page 56
# 4.1 Write out the code for the earlier sum function.


# my solustion
def sum_arr(arr):
    if len(arr) == 0:
        return "Zero sized array!"
    return get_sum(arr, len(arr) - 1) 

def get_sum(arr, size):
    if size == 0:
        return arr[size]
    else:
        return arr[size] + get_sum(arr, size - 1)

# solution from the book
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

exmp = [2, 4, 6]
print(sum_arr(exmp))
print(sum(exmp))
