'''
https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/?envType=daily-question&envId=2025-02-07
'''

from collections import defaultdict

from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        balls_map = {}
        colors_num = defaultdict(int)
        colors_set = set()

        for ball, color in queries:
            if ball in balls_map:
                cur_color = balls_map[ball]
                colors_num[cur_color] -= 1

                if colors_num[cur_color] == 0:
                    colors_set.remove(cur_color)

            balls_map[ball] = color
            colors_num[color] += 1
            colors_set.add(color)
            ans.append(len(colors_set))

        return ans
                
        
if __name__ == "__main__":
    sol = Solution()

    test1 = sol.queryResults(limit = 4, queries = [[1, 4], [2, 5], [1, 3], [3, 4]])
    assert test1 == [1, 2, 2, 3]

    test2 = sol.queryResults(limit = 4, queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]])
    assert test2 == [1, 2, 2, 3, 4]
