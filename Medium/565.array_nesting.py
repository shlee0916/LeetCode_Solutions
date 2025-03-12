'''
https://leetcode.com/problems/array-nesting/description/
'''

from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visit = [0] * len(nums)

        for idx in range(len(nums)):
            next_idx = idx
            length = 1

            while visit[next_idx] == 0:
                visit[next_idx] = length
                next_idx = nums[next_idx]
                length += 1

        return max(visit)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.arrayNesting(nums = [5, 4, 0, 3, 1, 6, 2])
    assert test1 == 4
    
    test2 = sol.arrayNesting(nums = [0, 1, 2])
    assert test2 == 1
    