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
    def num_to_lst(self, number) -> List[int]:
        nbs = []
        while number > 9:
            nbs.append(number % 10)
            number = int(number / 10)
        nbs.append(number)
        return nbs

    def fill_lkd(self, vals: List[int]):
        nodes = []
        for v in vals:
            node = ListNode(v)
            nodes.append(node)

        i = 0
        while i < len(nodes) - 1:
            if i < len(nodes):
                nodes[i].next = nodes[i + 1]
            i += 1
        return nodes

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
    nums = s.addTwoNumbers(head1, head2)
    lst = s.num_to_lst(nums)
    lkd = s.fill_lkd(lst)
