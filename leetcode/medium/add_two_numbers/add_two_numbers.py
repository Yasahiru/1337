from typing import Optional, Tuple, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def get_numbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Tuple[int, int]:
        if (l1.next and l2.next):
            ret = self.get_numbers(l1.next, l2.next)
            res = (ret[0] * 10 + l1.val, ret[1] * 10 + l2.val)
            return (res)
        return (l1.val, l2.val)

    # converte the number into list[int]

    def fill_lkd(self, vals: List[int]):
        nodes = []
        for v in vals:
            node = ListNode(v)
            nodes.append(node)

        next_node = None
        for n, i in enumerate(nodes, start=0):
            next_node = nodes[i + 1]
            n.next = next_node

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1, num2 = self.get_numbers(l1, l2)
        result = num1 + num2
        return result


if __name__ == "__main__":

    node2 = ListNode(3)
    node1 = ListNode(4, node2)
    head1 = ListNode(2, node1)

    node4 = ListNode(4)
    node3 = ListNode(6, node4)
    head2 = ListNode(5, node3)

    s = Solution()
    res = s.addTwoNumbers(head1, head2)
    s.fill_lkd()
