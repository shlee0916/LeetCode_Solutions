'''
https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/?envType=daily-question&envId=2025-04-02
'''

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        max_sub = 0
        max_num = 0

        for num in nums:
            ans = max(max_sub * num, ans)
            max_sub = max(max_num - num, max_sub)
            max_num = max(num, max_num)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumTripletValue(nums = [12, 6, 1, 2, 7])
    assert test1 == 77

    test2 = sol.maximumTripletValue(nums = [1, 10, 3, 4, 19])
    assert test2 == 133

    test3 = sol.maximumTripletValue(nums = [1, 2, 3])
    assert test3 == 0
    