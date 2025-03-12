'''
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/?envType=daily-question&envId=2023-12-27
'''

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        max_cost = 0
        sum_cost = 0

        for idx in range(len(colors)):
            if idx > 0 and colors[idx - 1] != colors[idx]:
                ans += sum_cost - max_cost
                sum_cost = 0
                max_cost = 0
            
            sum_cost += neededTime[idx]
            max_cost = max(max_cost, neededTime[idx])

        ans += sum_cost - max_cost
        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minCost(colors = "abaac", neededTime = [1, 2, 3, 4, 5])
    assert test1 == 3
    
    test2 = sol.minCost(colors = "abc", neededTime = [1, 2, 3])
    assert test2 == 0
    
    test3 = sol.minCost(colors = "aabaa", neededTime = [1, 2, 3, 4, 1])
    assert test3 == 2
    