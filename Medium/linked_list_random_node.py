'''
https://leetcode.com/problems/linked-list-random-node/description/
'''

from random import randint
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = 0
        node, count = self.head, 0

        while node:
            if randint(0, count) == 0:
                result = node.val

            node = node.next
            count += 1

        return result


if __name__ == "__main__":
    test1_list = ListNode(1, ListNode(2, ListNode(3)))
    sol = Solution(test1_list)

    count = [0, 0, 0]

    for _ in range(100000):
        count[sol.getRandom() - 1] += 1

    print(count)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()