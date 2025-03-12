'''
https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
'''

from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = range(1, 10)

        for _ in range(n - 1):
            ans = {start_num * 10 + next_num for start_num in ans for next_num in [start_num % 10 - k, start_num % 10 + k] if 0 <= next_num <= 9}

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numsSameConsecDiff(n = 3, k = 7)
    assert test1 == set([181, 292, 707, 818, 929])

    test2 = sol.numsSameConsecDiff(n = 2, k = 1)
    assert test2 == set([10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98])
