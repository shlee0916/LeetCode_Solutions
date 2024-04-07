'''
https://leetcode.com/problems/smallest-string-with-swaps/
'''

from collections import defaultdict

from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.union_find = list(range(len(s)))

        def find(node):
            if self.union_find[node] != node:
                self.union_find[node] = find(self.union_find[node])
            
            return self.union_find[node]

        def union(from_node, to_node):
            self.union_find[find(from_node)] = find(to_node)

        
        for from_node, to_node in pairs:
            union(from_node, to_node)

        groups = defaultdict(lambda : ([], []))
        for idx, ch in enumerate(s):
            node = find(idx)
            groups[node][0].append(idx)
            groups[node][1].append(ch)

        res = [""] * len(s)
        for idxs, chs in groups.values():
            idxs.sort()
            chs.sort()

            for idx, ch in zip(idxs, chs):
                res[idx] = ch

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.smallestStringWithSwaps(s = "dcab", pairs = [[0, 3], [1, 2]])
    assert test1 == "bacd"
    
    test2 = sol.smallestStringWithSwaps(s = "dcab", pairs = [[0, 3], [1, 2], [0, 2]])
    assert test2 == "abcd"
    
    test3 = sol.smallestStringWithSwaps(s = "cba", pairs = [[0, 1], [1, 2]])
    assert test3 == "abc"
    