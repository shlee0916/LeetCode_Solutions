'''
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        stack = [root]
        self.seen = set()

        while stack:
            cur_node = stack.pop()
            self.seen.add(cur_node.val)

            if cur_node.left:
                cur_node.left.val = cur_node.val * 2 + 1
                stack.append(cur_node.left)
            if cur_node.right:
                cur_node.right.val = cur_node.val * 2 + 2
                stack.append(cur_node.right)


    def find(self, target: int) -> bool:
        return target in self.seen


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
    
    
    test_tree = TreeNode(-1, TreeNode(-1, TreeNode(-1), TreeNode(-1)), TreeNode(-1))
    
    fe = FindElements(test_tree)
    
    assert fe.find(1) == True
    assert fe.find(3) == True
    assert fe.find(5) == False
    
    assert print_levels(test_tree) == [0, 1, 2, 3, 4]


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)