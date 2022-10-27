'''
https://leetcode.com/problems/gas-station/
'''
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        possible = sum(gas) - sum(cost)
        
        if possible < 0:
            return -1
        else:
            start_idx = 0
            surplus = 0
            for idx, (g, c) in enumerate(zip(gas, cost)):
                surplus += g - c
                if surplus < 0:
                    surplus = 0
                    start_idx = idx + 1
                    
            return start_idx


if __name__ == "__main__":
    sol = Solution()

    print(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
    print(sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]), -1)
    print(sol.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]), 4)