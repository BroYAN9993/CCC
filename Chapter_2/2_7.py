from data_struct import ListNode


def find_insertion_node(root1: ListNode, root2: ListNode) -> ListNode or None:
    length1, length2 = root1.length, root2.length
    if length1 > length2:
        root2 = pad_list(root2, length1 - length2)
    else:
        root1 = pad_list(root1, length2 - length1)
    p1, p2 = root1, root2
    while p1 and p2:
        if p1 == p2:
            return p1
        p1 = p1.next
        p2 = p2.next
    return "No insertion"


def pad_list(root: ListNode, n: int) -> ListNode:
    for _ in range(n):
        root = insert_first_node(root)
    return root


def insert_first_node(root: ListNode) -> ListNode:
    node = ListNode(0)
    node.next = root
    return node


def main():
    root1 = ListNode(1)
    root1.append([2, 3, 4, 5, 6])
    root2 = ListNode(0)
    root2.append([100, 200])
    point = root2
    while point.next:
        point = point.next
    point.next = root1
    print(find_insertion_node(root1, root2))


if __name__ == '__main__':
    main()
