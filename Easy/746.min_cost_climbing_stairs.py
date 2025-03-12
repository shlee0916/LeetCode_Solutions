'''
https://leetcode.com/problems/min-cost-climbing-stairs/
'''
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = []
        min_cost.append(cost[0])
        min_cost.append(cost[1])
        
        for c in cost[2:]:
            min_cost.append(min(min_cost[-1], min_cost[-2]) + c)
            
        return min(min_cost[-1], min_cost[-2])
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))