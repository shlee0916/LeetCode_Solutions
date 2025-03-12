'''
https://leetcode.com/problems/linked-list-in-binary-tree/description/
'''

from typing import Optional


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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, root):
            if not head:
                return True

            if not root:
                return False

            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))

        if head is None:
            return True

        if root is None:
            return False

        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


if __name__ == "__main__":
    sol = Solution()
    
    test1_list = ListNode(4, ListNode(2, ListNode(8)))
    test1_tree = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1))), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3)))))
    test1 = sol.isSubPath(test1_list, test1_tree)
    assert test1 == True
    
    test2_list = ListNode(1, ListNode(4, ListNode(2, ListNode(6))))
    test2_tree = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1))), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3)))))
    test2 = sol.isSubPath(test2_list, test2_tree)
    assert test2 == True
    