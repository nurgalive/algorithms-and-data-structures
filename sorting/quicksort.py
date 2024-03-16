# Grokking algos, page 65
# Quick sort

import random

# implementation 1
def quicksort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        return arr if arr[1] > arr[0] else [arr[1], arr[0]]
    
    pivot = arr[0]  # simple implementation
    # pivot = arr[random.randrange(len(arr))]  # more efficient impl
    sub_min = []
    sub_max = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            sub_min.append(arr[i])
            
        else:
            sub_max.append(arr[i])
    return quicksort(sub_min) + [pivot] + quicksort(sub_max)

# implementation from the book
def quicksort2(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

lst1 = [2]
lst2 = [5, 2]
lst3 = [5, 2, 3]
lst4 = [5, 2, 3, 7]
lst5 = [5, 2, 3, 7, 1, 9, 4, 8, 4, 6]
arr = [random.randint(0, 10000) for i in range(1, 10000)]
# print(quicksort2(arr))


# idea
# implement parallel quicksort for python