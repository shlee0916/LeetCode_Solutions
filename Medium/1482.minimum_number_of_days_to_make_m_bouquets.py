'''
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
'''

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left = 1
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            flower = 0
            bonquet = 0
            for day in bloomDay:
                if day > mid:
                    flower = 0
                else:
                    flower += 1
                
                if flower >= k:
                    flower = 0
                    bonquet += 1
                    if bonquet == m:
                        break

            if bonquet == m:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minDays(bloomDay = [1, 10, 3, 10, 2], m = 3, k = 1)
    assert test1 == 3
    
    test2 = sol.minDays(bloomDay = [1, 10, 3, 10, 2], m = 3, k = 2)
    assert test2 == -1
    
    test3 = sol.minDays(bloomDay = [7, 7, 7, 7, 12, 7, 7], m = 2, k = 3)
    assert test3 == 12
    