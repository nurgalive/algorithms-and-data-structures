# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

# Hint 1: Try a hash table.
# Hint 2: Could a bit vector be useful?
# Hint 3: Can you solve it in O(N log N) time? What might a solution like that look like?

# Questions to aks
# Is it ASCII (128) or Unicode string?
# Create 128 array

# brute force solution
# time complexity - O(n^2)
def is_unique(string: str) -> bool:
    for i in string:
        counter = 0
        for j in string:
            if i == j:
                counter += 1
        if counter > 1:
            return False
    
    return True

# Improved solution using hints
# Time complexity - O(n), 
# Or O(c), where c - is the character set (all possible characters)
# Space complexity O(1) - constant to store all possible characters
def is_unique2(string: str) -> bool:
    if len(string) > 128:
        return False
    arr = [0 for _ in range(0, 129)]
    for s in string:
        if arr[ord(s)] == 1:
            return False
        else:
            arr[ord(s)] = 1
    return True

# using bit vectors
def is_unique3(string: str) -> bool:
    checker = 0

    for s in string:
        # we substract 'a' as a smallest number from other characters
        #        val        const
        val = ord(s) - ord('a')
        print(f"val    : {val:032b}")

        if checker & (1 << val) > 0:
            return False
        checker = checker | (1 << val)
        print(f"checker: {checker:032b}")
    
    return True

print(is_unique("abc"))
print(is_unique("abbc"))

# s1 = "abc"
# s2 = "abbc"
# print(is_unique2(s1))
# print(is_unique2(s2))