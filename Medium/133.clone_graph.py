'''
https://leetcode.com/problems/clone-graph/?envType=study-plan-v2&envId=top-interview-150
'''

from collections import deque

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return

        new_graph = {node.val: Node(node.val, [])}
        que = deque([node])
        while que:
            cur_node = que.popleft()
            cur_clone_node = new_graph[cur_node.val]

            for neighbor in cur_node.neighbors:
                if neighbor.val not in new_graph:
                    new_graph[neighbor.val] = Node(neighbor.val, [])
                    que.append(neighbor)

                cur_clone_node.neighbors.append(new_graph[neighbor.val])

        return new_graph[node.val]


if __name__ == "__main__":
    sol = Solution()

    # Test1 graph
    test1_graph = {1: Node(1), 2: Node(2), 3: Node(3), 4: Node(4)}
    test1_graph[1].neighbors.extend([test1_graph[2], test1_graph[4]])
    test1_graph[2].neighbors.extend([test1_graph[1], test1_graph[3]])
    test1_graph[3].neighbors.extend([test1_graph[2], test1_graph[4]])
    test1_graph[4].neighbors.extend([test1_graph[1], test1_graph[3]])

    test1 = sol.cloneGraph(node = test1_graph[1])
    
    que = deque([test1])
    visit = set([test1.val])
    while que:
        cur_node = que.popleft()
        if cur_node.val not in visit:
            visit.add(cur_node.val)
            test1_node = test1_graph[cur_node.val]

            assert test1_node != test1 and test1_node.val == test1.val
            assert [neighbor.val for neighbor in test1_node.neighbors] == [neighbor.val for neighbor in test1.neighbors]
            

    # Test2 graph
    test2_node1 = Node(1)

    test2_graph = test2_node1
    test2 = sol.cloneGraph(node = test2_graph)
    assert test2_node1 != test2 and test2_node1.val == test2.val
    assert test2_node1.neighbors == test2.neighbors


    test3 = None
    test3 = sol.cloneGraph(node = test3)
    assert test3 == None
