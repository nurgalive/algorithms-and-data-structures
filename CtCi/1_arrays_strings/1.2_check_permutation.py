# Cracking the coding interview. Exercise 1.2. Page 90.
# Check Permutation: Given two strings, write a method to decide 
# if one is a permutation of the other.

str1 = "abc"
str2 = "bca"

# brute force solution
def check_permutatoin(str1, str2):
	for s1 in str1:
		for s2 in str2:
			if s1 == s2:
				break
		else:
			return False
	return True

# use the array of ascii symbols 128, like in the previous task
# def check..
	
print(check_permutatoin(str1, str2))