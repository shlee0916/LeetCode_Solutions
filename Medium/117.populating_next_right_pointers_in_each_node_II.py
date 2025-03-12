'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
'''

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root

        while node:
            cur_node = dummy = Node(0)
            while node:
                if node.left:
                    cur_node.next = node.left
                    cur_node = cur_node.next

                if node.right:
                    cur_node.next = node.right
                    cur_node = cur_node.next
                    
                node = node.next

            node = dummy.next

        return root

    
if __name__ == "__main__":
    def tree2level_list(root: 'Node'):
        if not root:
            return

        que = [root]
        levels = []
        while que:
            cur_level = []
            cur_level_len = len(que)
            for _ in range(cur_level_len):
                cur_node = que.pop(0)

                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)

                cur_level.append(cur_node.val)

            levels.append(cur_level)
            

        return levels


    def level_list_from_left_node(root: 'Node'):
        levels = []
        while root:
            cur_levels = []
            cur_node = root
            while cur_node:
                cur_levels.append(cur_node.val)
                cur_node = cur_node.next

            levels.append(cur_levels)
            root = root.left

        return levels


    sol = Solution()

    test1_tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
    test1 = sol.connect(test1_tree)
    test1_list = tree2level_list(test1_tree)
    test1_res = level_list_from_left_node(test1)
    print(test1_list, test1_res)
    assert test1_list == test1_res

    test2_tree = Node()
    test2 = sol.connect(test2_tree)
    test2_list = tree2level_list(test2_tree)
    test2_res = level_list_from_left_node(test2)
    print(test2_list, test2_res)
    assert test2_list == test2_res
    