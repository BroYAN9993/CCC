from data_struct import ListNode


def kth_last_node(root: ListNode, k: int):
    fast = slow = root
    count = k
    while count > 0:
        if fast is None and count > 0:
            return
        if fast is None:
            break
        count -= 1
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow


def main():
    root = ListNode(0)
    root.append([1, 3, 4, 5, 6])
    print(kth_last_node(root, 6))


if __name__ == '__main__':
    main()
