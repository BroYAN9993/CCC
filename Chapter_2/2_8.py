from CCC.data_struct import ListNode


def find_loop_entry(root: ListNode) -> ListNode or None:
    slow, fast = root, root
    while fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            break
    if fast.next is None or fast is None:
        return None
    other = root
    while other is not slow:
        other = other.next
        slow = slow.next
    return other


def main():
    a = ListNode(0)
    a.append([1, 2, 3, 4, 5])
    p1 = a
    p2 = a
    while p1.next:
        p1 = p1.next
        p2 = p2.next if p2.val != 3 else p2
    p1.next = p2
    ans = find_loop_entry(a)
    print(ans)


if __name__ == '__main__':
    main()