'''
https://leetcode.com/problems/three-consecutive-odds/?envType=daily-question&envId=2024-07-01
'''

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for num in arr:
            if num % 2 == 1:
                cnt += 1
            else:
                cnt = 0
            
            if cnt == 3:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.threeConsecutiveOdds(arr = [2, 6, 4, 1])
    assert test1 == False

    test2 = sol.threeConsecutiveOdds(arr = [1, 2, 34, 3, 4, 5, 7, 23, 12])
    assert test2 == True
    