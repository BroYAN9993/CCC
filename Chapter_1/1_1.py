# Implement an algorithm to determine if a string has all unique characters.
# What if you can not use additional data structures?


# 简单方法， 通过维护一个数组实现
def isUniqueChars1(strs: str) -> bool:
    char_set = [False] * 256
    for c in strs:
        ascii_code = ord(c)
        if char_set[ascii_code]:
            return False
        char_set[ascii_code] = True
    return True


# 位运算方法，将上一个函数维护的数组变为一个32位整型的位
# 由于数组长度限制，此方法只能用于判断小写a-z
def isUniqueChars2(strs: str) -> bool:
    checker = 0
    for c in strs:
        val = ord(c) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker += 1 << val
    return True


if __name__ == '__main__':
    chars1 = "aaaavvvvv"
    chars2 = "zbcgsye"
    print(isUniqueChars1(chars1))
    print(isUniqueChars1(chars2))
    print(isUniqueChars2(chars1))
    print(isUniqueChars2(chars2))


