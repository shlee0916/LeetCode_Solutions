'''
https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2024-05-09
'''

from heapq import heapify, heappop

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        heap = [-happy for happy in happiness]
        heapify(heap)

        for turn in range(k):
            ans += max(-heappop(heap) - turn, 0)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maximumHappinessSum(happiness = [1, 2, 3], k = 2)
    assert test1 == 4
    
    test2 = sol.maximumHappinessSum(happiness = [1, 1, 1, 1], k = 2)
    assert test2 == 1
    
    test3 = sol.maximumHappinessSum(happiness = [2, 3, 4, 5], k = 1)
    assert test3 == 5
    