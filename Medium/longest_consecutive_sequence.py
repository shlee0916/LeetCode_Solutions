'''
https://leetcode.com/problems/longest-consecutive-sequence/
'''
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberset = set(nums)
        best = 0
        
        for num in numberset:
            if num - 1 not in numberset:
                end = num + 1
                
                while end in numberset:
                    end += 1
                    
                best = max(best, end - num)
                
        return best
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]), 4
    
    print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9