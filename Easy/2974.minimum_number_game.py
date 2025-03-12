'''
https://leetcode.com/problems/minimum-number-game/description/
'''

from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()

        for idx in range(0, len(nums), 2):
            ans.append(nums[idx + 1])
            ans.append(nums[idx])

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numberGame(nums = [5, 4, 2, 3])
    assert test1 == [3, 2, 5, 4]
    
    test2 = sol.numberGame(nums = [2, 5])
    assert test2 == [5, 2]
    