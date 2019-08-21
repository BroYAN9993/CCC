class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        memo = set()
        display = []
        point = self
        while point:
            if point not in memo:
                display.append(point.val)
                memo.add(point)
            else:
                break
            point = point.next
        return str(display)

    def append(self, nodes: list):
        point = self
        for node in nodes:
            new_node = ListNode(node)
            point.next = new_node
            point = point.next

    @property
    def length(self):
        count = 0
        p = self
        while p:
            p = p.next
            count += 1
        return count
