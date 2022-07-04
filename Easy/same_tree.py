'''
https://leetcode.com/problems/same-tree/
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        p_que = [p]
        q_que = [q]
        
        while p_que and q_que:
            cur_p = p_que.pop(0)
            cur_q = q_que.pop(0)
            
            if cur_p.val != cur_q.val:
                return False
            
            p_left, p_right = cur_p.left, cur_p.right
            q_left, q_right = cur_q.left, cur_q.right
            
            if (not p_left) ^ (not q_left):
                return False
            if (not p_right) ^ (not q_right):
                return False
            
            if p_left:
                p_que.append(p_left)
            if q_left:
                q_que.append(q_left)
            if p_right:
                p_que.append(p_right)
            if q_right:
                q_que.append(q_right)
                
        
        return not p_que and not q_que

        
if __name__ == "__main__":
    sol = Solution()
    
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    
    print(sol.isSameTree(p, q))
    
    q = TreeNode(1, TreeNode(3), TreeNode(2))
    
    print(sol.isSameTree(p, q))