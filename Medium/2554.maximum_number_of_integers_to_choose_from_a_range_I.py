'''
https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/?envType=daily-question&envId=2024-12-06
'''

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = 0
        ban_set = set(banned)
        cur_sum = 0

        for num in range(1, n + 1):
            if num in ban_set:
                continue
            
            if cur_sum + num <= maxSum:
                ans += 1
                cur_sum += num
                
        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxCount(banned = [1, 6, 5], n = 5, maxSum = 6)
    assert test1 == 2

    test2 = sol.maxCount(banned = [1, 2, 3, 4, 5, 6, 7], n = 8, maxSum = 1)
    assert test2 == 0

    test3 = sol.maxCount(banned = [11], n = 7, maxSum = 50)
    assert test3 == 7
    