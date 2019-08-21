def string_compression(string: str) -> str:
    compressed_string = ""
    size = len(string)
    if size <= 2:
        return string
    nsize = size
    temp = 0
    counter = 0
    for c in string:
        if c != temp:
            compressed_string += str(counter) + c
            nsize += 2 - counter
            temp = c
            counter = 1
        else:
            counter += 1
    compressed_string += str(counter)
    nsize += 2 - counter
    return compressed_string[1:] if nsize < size else string


if __name__ == '__main__':
    strings = ["abc", "", "a", "aa", "aaaaacccccdddddaaaaa", "aaccdd", "aaabcc"]
    for s in strings:
        print(string_compression(s))
