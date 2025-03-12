'''
https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=daily-question&envId=2023-09-05
'''

from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        cache = {}
        dummy = Node(-1)
        new_head = dummy
        
        while head:
            if head in cache:
                new_node = cache[head]
            else:
                new_node = Node(head.val)
                cache[head] = new_node

            new_head.next = new_node
            new_head = new_head.next

            if head.random:
                if head.random in cache:
                    new_random = cache[head.random]
                else:
                    new_random = Node(head.random.val)
                    cache[head.random] = new_random

                new_head.random = new_random

            head = head.next

        return dummy.next


if __name__ == "__main__":
    ####### Test helper
    def make_linked(nodes: List[List[int]]) -> Node:
        cache = {None: None}
        new_head = dummy = Node(-1)

        for idx, (val, _) in enumerate(nodes):
            cache[idx] = Node(val)

        for (idx, node), (_, random) in zip(cache.items(), [[None, None]] + nodes):
            if node:
                new_head.next = node
                node.random = cache[random]

                new_head = new_head.next

        return dummy.next
    ##################################
    def compare_linked(origin: Node, copied: Node) -> bool:
        while origin or copied:
            if origin is None or copied is None or origin == copied:
                return False
            
            if origin.val != copied.val:
                return False
            
            if origin.random and copied.random:
                if origin.random == copied.random or origin.random.val != copied.random.val:
                    return False
            
            origin = origin.next
            copied = copied.next
        
        return True


    sol = Solution()

    test1_list = make_linked(nodes = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    test1 = sol.copyRandomList(test1_list)
    assert compare_linked(test1_list, test1)

    test2_list = make_linked(nodes = [[1, 1], [2, 1]])
    test2 = sol.copyRandomList(test2_list)
    assert compare_linked(test2_list, test2)

    test3_list = make_linked(nodes = [[3, None], [3, 0], [3, None]])
    test3 = sol.copyRandomList(test3_list)
    assert compare_linked(test3_list, test3)
