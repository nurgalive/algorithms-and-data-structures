str1 = "abc"
str2 = "bca"

def check_permutatoin(str1, str2):
	for s1 in str1:
		for s2 in str2:
			if s1 == s2:
				break
		else:
			return False
	return True
	
print(check_permutatoin(str1, str2))