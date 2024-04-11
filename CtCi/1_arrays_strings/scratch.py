
def is_unique(string: str) -> bool:
    checker = 0

    for s in string:
        # we substract 'a' as a smallest number from other characters
        #        val        const
        val = ord(s) - ord('a')
        print(f"val    : {val:032b}")
        # setting the bit
        # val | (1 << bit_index)
        # checker |= (1 << val)
        if checker & (1 << val) > 0:
            return False
        checker = checker | (1 << val)
        print(f"checker: {checker:032b}")
    
    return True

print(is_unique("abc"))
print(is_unique("abbc"))