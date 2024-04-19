# Cracking the coding interview. Exercise 1.2. Page 90.
# Check Permutation: Given two strings, write a method to decide 
# if one is a permutation of the other.

# Hints:
#1. 1.2 Describe what it means for two strings to be permutations of each other. Now, look at
#that definition you provided. Can you check the strings against that definition?

#84. 1.2 There is one solution that is 0(N log N) time. Another solution uses some space, but
# isO(N) time.

#122. 1.2 Could a hash table be useful?

#131. 1.2 Two strings that are permutations should have the same characters, but in different
# orders. Can you make the orders the same?

# simple case
# str1 = "abc"
# str2 = "bca"

# duplicates case
str1 = "babb"
str2 = "abaa"


# brute force solution
# O(N^2)
def check_permutation1(str1: str, str2: str) -> bool: # does not work with duplicates
	for s1 in str1:
		for s2 in str2:
			if s1 == s2:
				break
		else:
			return False
	return True

# Hacky solution using hashmap
# O(S1 + S2)
def check_permutation2(str1: str, str2: str) -> bool:
	if len(str1) != len(str2): # O(1)
		return False
	# not a set, because set is immutable
	str1_dict = {s: 0 for s in str1}  # Creating a dict from the string: O(S1)
	print(str1_dict)

	for s in str2: # Iterating over S2: O(S2)
		if s not in str1_dict:
			return False
		else:
			del str1_dict[s]  # O(1)
	if len(str1_dict) == 0:  # O(1) 
		return True
	else: 
		return False

# using sorting
def check_permutation3(str1: str, str2: str) -> bool:
	if len(str1) != len(str2):
		return False
	
	return sorted(str1) == sorted(str2) # O(s1 log s1 + s2 log s2)

# using counting frequencies
def check_permutation4(str1: str, str2: str) -> bool:
	letters = [0 for i in range(128)]

	for s in str1:  # O(S1)
		letters[ord(s)] += 1

	for s in str2:  # O(S2)
		letters[ord(s)] -= 1
	
		if letters[ord(s)] < 0:
			return False
	
	return True
	
print(check_permutation4(str1, str2))