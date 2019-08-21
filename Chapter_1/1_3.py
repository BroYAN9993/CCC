# Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer. NOTE: One or two additional variables are fine.
# An extra copy of the array is not.
# FOLLOW UP
# Write the test cases for this method.


# Simple version
def removeDuplicates(string: str) -> str:
    ans = ""
    for i in range(len(string)):
        isDuplicate = False
        for c in ans:
            if c == string[i]:
                isDuplicate = True
                break
        if not isDuplicate:
            ans += string[i]
    return ans

# 

if __name__ == '__main__':
    s1 = "aaaaaa"
    s2 = "abc"
    s3 = "aaaaacccccc"
    print(removeDuplicates(s1), removeDuplicates(s2), removeDuplicates(s3))
