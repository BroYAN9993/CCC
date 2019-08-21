def isPalindrome(s: str) -> bool:
    checker = set()
    for c in s:
        if c not in checker:
            checker.add(c)
        else:
            checker.remove(c)
    return len(checker) < 2


def isPalindrome2(s: str) -> bool:
    checker = [0] * 26
    odd_num = 0
    for c in s:
        num = ord(c) - ord("a")
        checker[num] += 1
        if checker[num] % 2:
            odd_num += 1
        else:
            odd_num -= 1
    return odd_num < 2


if __name__ == '__main__':
    s1 = "aaaaaaaa"
    s2 = "asc"
    s3 = "abcddcb"
    s4 = ""
    print(isPalindrome(s1), isPalindrome(s2), isPalindrome(s3), isPalindrome(s4))
    print(isPalindrome2(s1), isPalindrome2(s2), isPalindrome2(s3), isPalindrome2(s4))
