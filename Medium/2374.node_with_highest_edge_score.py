'''
https://leetcode.com/problems/node-with-highest-edge-score/
'''

from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0] * len(edges)

        for idx, edge in enumerate(edges):
            scores[edge] += idx

        max_score = max(scores)
        for idx, score in enumerate(scores):
            if score == max_score:
                return idx


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.edgeScore(edges = [1, 0, 0, 0, 0, 7, 7, 5])
    assert test1 == 7

    test2 = sol.edgeScore(edges = [2, 0, 0, 2])
    assert test2 == 0
    