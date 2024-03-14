# Grokking algrorithms, page 59
# Recursive binary search
# Excersice 4.4

def bin_search(arr: list[int], num: int) -> int:
	low = 0
	high = len(arr) - 1
	return find_num(arr, num, low, high)
	
def find_num(arr: list[int], num: int, low: int, high: int):
	mid = (low + high) // 2
	if num == arr[mid]:
		return num
	if low == high:
		return -1
	if num > arr[mid]:
		return find_num(arr, num, mid + 1, high)
	if num < arr[mid]:
		return find_num(arr, num, low, mid - 1)

# array have to be sorted
# lst = [1, 3, 4, 5, 7, 8, 10]
lst = [i for i in range(1, 100_000)]

print(bin_search(lst, 1))