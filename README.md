### 1.1 Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?
- #### 简单方法， 通过维护一个数组实现
```
def isUniqueChars1(strs: str) -> bool:
    char_set = [False] * 256    # list长度为ascii字符数量
    for c in strs:
        ascii_code = ord(c)
        if char_set[ascii_code]:
            return False
        char_set[ascii_code] = True
    return True
```
时间复杂度O(n)
空间复杂度O(n)
- #### 位运算方法，将上一个函数维护的数组变为一个32位整型的位
>由于int位数限制，此方法只能用于判断小写a-z
```
def isUniqueChars2(strs: str) -> bool:
    checker = 0
    for c in strs:
        val = ord(c) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker += 1 << val
    return True
```
时间复杂度O(n)
空间复杂度O(1)
### 1.2 Write code to reverse a C-Style String. (C-String means that “abcd” is represented as five characters, including the null character.)
- #### 双指针实现
> 为了模仿Cstyle string，实现了一个双向链表，结果发现效果并不好，但是双指针的思想还是很简单的，下边的代码请酌情参考。
```
# A doubly linked list implement for  simulatting the C-Style Strings.
class PointStringNode(object):
    def __init__(self, character: str):
        self.character = character
        self.pre = None
        self.next = None

class CStyleString(object):
    def __init__(self, string: str):
        self.head = PointStringNode("head")
        self.length = len(string)
        point = self.head
        for c in string:
            node = PointStringNode(c)
            node.pre = point
            point.next = node
            point = point.next
        self.head = self.head.next
        self._tail = point

    def append(self, string: str):
        point = self._tail
        for c in string:
            node = PointStringNode(c)
            node.pre = point
            point.next = node
            point = point.next
            self.length += 1
        self._tail = point

    @property
    def tail(self):
        return self._tail

    def __str__(self):
        strs = ""
        point = self.head
        while point:
            strs += point.character
            point = point.next
        return strs

# Core code
def reverse(string: CStyleString):
    left, right = string.head, string.tail
    count = 0
    while count < string.length:
        left.character, right.character = right.character, left.character
        left = left.next
        right = right.pre
        count += 2
```
时间复杂度O(n)
空间复杂度O(1)
### 1.3 Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. 
> NOTE: One or two additional variables are fine. An extra copy of the array is not.
