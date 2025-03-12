'''
https://leetcode.com/problems/design-graph-with-shortest-path-calculator/description/?envType=daily-question&envId=2023-11-11
'''

from collections import defaultdict
from heapq import heappop, heappush

from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.length = n
        self.graph = defaultdict(dict)
        
        for from_node, to_node, cost in edges:
            self.graph[from_node][to_node] = cost
        

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]][edge[1]] = edge[2]


    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        visit = set()
        while heap:
            cur_cost, cur_node = heappop(heap)

            if cur_node == node2:
                return cur_cost

            if cur_node not in visit and cur_node in self.graph:
                visit.add(cur_node)
                for next_node, next_cost in self.graph[cur_node].items():
                    heappush(heap, (cur_cost + next_cost, next_node))

        return -1


if __name__ == "__main__":
    graph = Graph(n = 4, edges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    
    assert graph.shortestPath(node1 = 3, node2 = 2) == 6
    assert graph.shortestPath(node1 = 0, node2 = 3) == -1
    graph.addEdge(edge = [1, 3, 4])
    assert graph.shortestPath(node1 = 0, node2 = 3) == 6
    

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)