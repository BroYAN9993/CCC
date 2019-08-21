from data_struct import ListNode


def remove_node(node: ListNode):
    if node.next is None:
        return False
    node.val = node.next.val
    node.next = node.next.next


def main():
    root = ListNode(0)
    root.append([1, 3, 5, 7, 9])
    point = root
    while point.val != 3:
        point = point.next
    print(root)
    print(point)
    remove_node(point)
    print(root)


if __name__ == '__main__':
    main()
