'''
https://leetcode.com/problems/best-sightseeing-pair/
'''

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        cur = 0

        for idx in range(1, len(values)):
            cur = max(cur, values[idx - 1] + idx - 1)
            ans = max(ans, cur + values[idx] - idx)

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxScoreSightseeingPair(values = [8, 1, 5, 2, 6])
    assert test1 == 11
    
    test2 = sol.maxScoreSightseeingPair(values = [1, 2])
    assert test2 == 2
    