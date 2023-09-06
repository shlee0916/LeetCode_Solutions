'''
https://leetcode.com/problems/split-linked-list-in-parts/description/?envType=daily-question&envId=2023-09-06
'''

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        len_head = head
        length = 0
        while len_head:
            length += 1
            len_head = len_head.next

        chunk_size = length // k
        additional_chunk = length % k
        prev_node = None
        cur_node = head
        ans = [chunk_size + 1] * additional_chunk + [chunk_size] * (k - additional_chunk)
        for idx, num in enumerate(ans):
            if prev_node:
                prev_node.next = None
            ans[idx] = cur_node
            for _ in range(num):
                prev_node = cur_node
                cur_node = cur_node.next
            
        return ans


if __name__ == "__main__":
    ## Test Helper ##########
    def linked2list(nodes: List[ListNode]):
        res = []
        for node in nodes:
            part = []
            while node:
                part.append(node.val)
                node = node.next
            res.append(part)
                
        return res
    ###############################
    
    sol = Solution()
    
    test1_list = ListNode(1, ListNode(2, ListNode(3)))
    test1 = sol.splitListToParts(head = test1_list, k = 5)
    assert linked2list(test1) == [[1], [2], [3], [], []]

    test2_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
    test2 = sol.splitListToParts(head = test2_list, k = 3)
    assert linked2list(test2) == [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    