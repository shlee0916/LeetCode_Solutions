'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                break
        
        return root
    

if __name__ == "__main__":
    sol = Solution()
    
    test_tree = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    
    print(sol.lowestCommonAncestor(test_tree, TreeNode(2), TreeNode(4)).val)