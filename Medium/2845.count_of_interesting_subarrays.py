'''
https://leetcode.com/problems/count-of-interesting-subarrays/description/?envType=daily-question&envId=2025-04-25
'''

from collections import defaultdict

from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = 0
        acc = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for num in nums:
            acc = (acc + (1 if num % modulo == k else 0)) % modulo
            ans += cnt[(acc - k + modulo) % modulo]
            cnt[acc] += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countInterestingSubarrays(nums = [3, 2, 4], modulo = 2, k = 1)
    assert test1 == 3

    test2 = sol.countInterestingSubarrays(nums = [3, 1, 9, 6], modulo = 3, k = 0)
    assert test2 == 2
    