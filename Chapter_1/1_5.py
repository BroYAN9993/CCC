def one_away(first: str, second: str) -> bool:
    size1, size2 = len(first), len(second)
    if abs(size1 - size2) > 1:
        return False
    if size1 == size2:
        counter = 0
        for i in range(size1):
            if first[i] != second[i]:
                counter += 1
            if counter > 1:
                return False
    else:
        if size2 > size1:
            first, second = second, first
            size1, size2 = size2, size1
        i = j = 0
        counter = 0
        while i < size1 and j < size2:
            if first[i] != second[j]:
                i += 1
                counter += 1
            i += 1
            j += 1
        if (counter == 0 and i == j) or (counter == 1 and i - j == 1):
            return True
        else:
            return False
    return True


if __name__ == '__main__':
    firsts = ["a", "", "abc", "abcd", "abc", "abcd", "abccc"]
    seconds = ["", "", "abc", "abc", "abcd", "abcc", "abcde"]
    for i in range(len(firsts)):
        print(one_away(firsts[i], seconds[i]))
