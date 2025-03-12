'''
https://leetcode.com/problems/earliest-possible-day-of-full-bloom/description/
'''

from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        res = 0
        for grow_time, plant_time in sorted(zip(growTime, plantTime)):
            res = max(res, grow_time) + plant_time

        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.earliestFullBloom(plantTime = [1, 4, 3], growTime = [2, 3, 1])
    assert test1 == 9
    
    test2 = sol.earliestFullBloom(plantTime = [1, 2, 3, 2], growTime = [2, 1, 2, 1])
    assert test2 == 9
    
    test3 = sol.earliestFullBloom(plantTime = [1], growTime = [1])
    assert test3 == 2
    