from data_struct import ListNode


def partition(root: ListNode, part_num: int):
    left, right = ListNode("l"), ListNode("r")
    left.next = root
    point1, point2 = left, right
    while point1.next:
        node = point1.next
        if node.val >= part_num:
            point1.next = node.next
            node.next = None
            point2.next = node
            point2 = point2.next
        else:
            point1 = point1.next
    point1.next = right.next


def main():
    root = ListNode(0)
    root.append([10, 20, 30, 4, 5, 6, 7, 8])
    print(root)
    partition(root, 8)
    print(root)


if __name__ == '__main__':
    main()
