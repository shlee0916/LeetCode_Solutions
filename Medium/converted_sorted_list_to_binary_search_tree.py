'''
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
'''

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return

        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        root_node = slow.next
        slow.next = None
        root = TreeNode(root_node.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(root_node.next)

        return root
    
    
if __name__ == "__main__":
    # test helper
    def print_levels(root: TreeNode) -> List[Optional[int]]:
        if not root:
            return []
        
        que = [root]
        levels = []
        while que:
            cur_len = len(que)
            for _ in range(cur_len):
                cur_node = que.pop(0)
                levels.append(cur_node.val)
                
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
                
        return levels
    ############################
    
    sol = Solution()
    
    test1_list = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
    test1 = sol.sortedListToBST(test1_list)
    test1_res = print_levels(test1)
    print(test1_res, [0, -3, 9, -10, 5])
    assert test1_res == [0, -3, 9, -10, 5]
    
    test2_list = None
    test2 = sol.sortedListToBST(test2_list)
    print(test2, None)
    assert test2 == None
    