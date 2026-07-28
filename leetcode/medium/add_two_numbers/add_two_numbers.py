from typing import Optional, Tuple, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def get_number(self, l1: Optional[ListNode]) -> Tuple[int, int]:
        if l1.next:
            ret = self.get_number(l1.next)
            res = (ret * 10 + l1.val)
            return (res)
        return (l1.val)

    def num_to_lst(self, number) -> List[int]:
        nbs = []
        while number > 9:
            nbs.append(number % 10)
            number = (number // 10)
            print(number)
        nbs.append(number)
        return nbs

    def someTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1 = self.get_number(l1)
        num2 = self.get_number(l2)
        result = num1 + num2
        return result

    @staticmethod
    def fill_lkd(vals: List[int]):
        nodes = []
        for i, v in enumerate(vals, start=0):
            node = ListNode(v)
            nodes.append(node)
        i = 0
        while i < len(nodes) - 1:
            if i < len(nodes):
                nodes[i].next = nodes[i + 1]
            i += 1
        return nodes[0]

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = self.someTwoNumbers(l1, l2)
        print(nums)
        lst = self.num_to_lst(nums)
        lkd = self.fill_lkd(lst)
        return (lkd)

    def size(self, head: ListNode) -> int:
        count = 0
        current = head

        while current is not None:
            count += 1
            current = current.next

        return count


if __name__ == "__main__":

    s = Solution()

    head1 = s.fill_lkd(
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    )

    head2 = s.fill_lkd([5, 6, 4])
    res = s.addTwoNumbers(head1, head2)
    node = res
    # while node:
    #     print(node.val, end=" ")
    #     node = node.next
