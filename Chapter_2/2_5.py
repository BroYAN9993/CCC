from data_struct import ListNode


def sum_lists_post_order(root1: ListNode, root2: ListNode) -> ListNode:
    ans = ListNode(0)
    carry = 0
    p1, p2, p3 = root1, root2, ans
    while p1 or p2 or carry:
        val1 = p1.val if p1 else 0
        val2 = p2.val if p2 else 0
        temp = carry + val1 + val2
        carry = temp // 10
        temp %= 10
        node = ListNode(temp)
        p3.next = node
        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next
        p3 = p3.next
    return ans.next


class Summation(object):
    def __init__(self):
        self.summ = None
        self.carry = 0


def sum_lists_pre_order(root1: ListNode, root2: ListNode):
    len1 = root1.length
    len2 = root2.length
    if len1 < len2:
        root1 = pad_list(root1, len2 - len1)
    else:
        root2 = pad_list(root2, len1 - len2)
    ans = sum_lists_helper(root1, root2)
    return insert_first_node(ans.summ, ans.carry) if ans.carry else ans.summ


def sum_lists_helper(root1: ListNode, root2: ListNode) -> Summation:
    if root1 is None and root2 is None:
        return Summation()

    ans = sum_lists_helper(root1.next, root2.next)
    val = ans.carry + root1.val + root2.val
    real_ans = insert_first_node(ans.summ, val % 10)
    ans.summ = real_ans
    ans.carry = val // 10
    return ans


def pad_list(root: ListNode, length: int):
    for i in range(length):
        root = insert_first_node(root, 0)
    return root


def insert_first_node(root: ListNode, val) -> ListNode:
    node = ListNode(val)
    node.next = root
    return node


def main():
    root1, root2 = ListNode(0), ListNode(0)
    root1.append([1])
    root2.append([9, 9, 9, 5, 2, 5, 3])
    sum_node1 = sum_lists_post_order(root1, root2)
    sum_node2 = sum_lists_pre_order(root1, root2)
    print(f"{root1} + {root2} = {sum_node1}")
    print(sum_node2)


if __name__ == '__main__':
    main()
