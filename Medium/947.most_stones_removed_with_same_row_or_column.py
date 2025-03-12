'''
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
'''
from typing import List
from collections import defaultdict


# BFS
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        visit = set()

        rows = defaultdict(list)
        cols = defaultdict(list)
        for r_idx, c_idx in stones:
            rows[r_idx].append(c_idx)
            cols[c_idx].append(r_idx)

        island = 0
        for r_idx, c_idx in stones:
            if (r_idx, c_idx) not in visit:
                que = [(r_idx, c_idx)]

                while que:
                    x, y = que.pop(0)

                    if (x, y) not in visit:
                        visit.add((x, y))

                        for tmp_y in rows[x]:
                            que.append((x, tmp_y))
                        for tmp_x in cols[y]:
                            que.append((tmp_x, y))
            
                island += 1

        return len(stones) - island


# Union and Find
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        UF = {}

        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])

            return UF[x]

        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)

            UF[find(x)] = find(y)

        for x, y in stones:
            union(x, ~y)

        return len(stones) - len({find(x) for x in UF})


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])
    print(test1, 5)
    assert test1 == 5

    test2 = sol.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]])
    print(test2, 3)
    assert test2 == 3

    test3 = sol.removeStones([[0, 0]])
    print(test3, 0)
    assert test3 == 0
    