'''
https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/?envType=daily-question&envId=2024-11-07
'''

from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0

        for idx in range(32):
            cnt = sum(1 for cand in candidates if cand & (1 << idx))
            ans = max(cnt, ans)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.largestCombination(candidates = [16, 17, 71, 62, 12, 24, 14])
    assert test1 == 4

    test2 = sol.largestCombination(candidates = [8, 8])
    assert test2 == 2
