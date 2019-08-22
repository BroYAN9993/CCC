from data_struct import ListNode


def remove_duplicate_node(root: ListNode):
    pre = ListNode(0)
    memo = set()
    pre.next = root
    point = pre
    while point.next:
        if point.next.val not in memo:
            memo.add(point.next.val)
            point = point.next
        else:
            point.next = point.next.next


def remove_duplicate_node_without_extra_memory(root: ListNode):
    pre = ListNode(0)
    pre.next = root
    point = pre
    while point.next:
        point0 = root
        flag = False
        while point0 != point.next:
            if point0.val == point.next.val:
                flag = True
                point.next = point.next.next
                break
            point0 = point0.next
        if not flag:
            point = point.next


def main():
    root = ListNode(0)
    root.append([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 8])
    print(root)
    remove_duplicate_node_without_extra_memory(root)
    print(root)


if __name__ == '__main__':
    main()
