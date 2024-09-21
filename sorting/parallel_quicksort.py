import multiprocessing
import timeit
import random
from quicksort import quicksort as sequential_quicksort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def parallel_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    with multiprocessing.Pool(processes=2) as pool:
        left_sorted, right_sorted = pool.map(quicksort, (left, right))

    return left_sorted + middle + right_sorted

def timeit_sorting():
    # arr = [3, 6, 8, 10, 1, 2, 1]
    arr = [random.randint(0, i) for i in range(100_000)]
    # print("Original array:", arr)
    time_taken = timeit.timeit(lambda: parallel_quicksort(arr), number=1)
    time_taken2 = timeit.timeit(lambda: sequential_quicksort(arr), number=1)
    # print("Sorted array:", parallel_quicksort(arr))
    print("Time taken parallel:", time_taken, "seconds")
    print("Time taken sequential:", time_taken2, "seconds")

if __name__ == "__main__":
    timeit_sorting()

# output
# Time taken parallel: 0.13551990400446812 seconds
# Time taken sequeintial: 2.287965677001921 seconds