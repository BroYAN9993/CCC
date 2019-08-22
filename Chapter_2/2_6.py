from data_struct import ListNode


def is_palindrome(root: ListNode) -> bool:
    stack = list()
    slow = fast = root
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast is None:
        stack.pop()
    slow = slow.next
    while slow:
        if slow.val != stack.pop():
            return False
        slow = slow.next
    return True


def main():
    list1 = ListNode(0)
    list2 = ListNode(1)
    list3 = ListNode(1)
    list1.append([1, 2, 3])
    list2.append([2, 3, 4, 5, 4, 3, 2, 1])
    list3.append([1])
    print(is_palindrome(list1), is_palindrome(list2), is_palindrome(list3))


if __name__ == '__main__':
    main()
