# Write code to reverse a C-Style String.
# (C-String means that “abcd” is represented as five characters, including the null character.)


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


def reverse(string: CStyleString):
    left, right = string.head, string.tail
    count = 0
    while count < string.length:
        left.character, right.character = right.character, left.character
        left = left.next
        right = right.pre
        count += 2


if __name__ == '__main__':
    string = 'abcdefg'
    Cstring = CStyleString(string)
    print(Cstring, Cstring.length)
    Cstring.append("hijk")
    print(Cstring, Cstring.length)
    reverse(Cstring)
    print(Cstring, Cstring.length)

