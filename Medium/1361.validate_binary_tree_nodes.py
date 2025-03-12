'''
https://leetcode.com/problems/validate-binary-tree-nodes/description/
'''

from collections import deque

from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        children = set(leftChild + rightChild)
        for node in range(n):
            if node not in children:
                root = node

        visit = set()
        que = deque([root])
        while que:
            for _ in range(len(que)):
                cur_node = que.popleft()

                if cur_node in visit:
                    return False

                visit.add(cur_node)

                if leftChild[cur_node] != -1:
                    que.append(leftChild[cur_node])
                if rightChild[cur_node] != -1:
                    que.append(rightChild[cur_node])

        return len(visit) == n


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.validateBinaryTreeNodes(n = 4, leftChild = [1, -1, 3, -1], rightChild = [2, -1, -1, -1])
    assert test1 == True

    test2 = sol.validateBinaryTreeNodes(n = 4, leftChild = [1, -1, 3, -1], rightChild = [2, 3, -1, -1])
    assert test2 == False

    test3 = sol.validateBinaryTreeNodes(n = 2, leftChild = [1, 0], rightChild = [-1, -1])
    assert test3 == False
    