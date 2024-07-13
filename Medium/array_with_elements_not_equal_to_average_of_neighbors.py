'''
https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/description/
'''

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        ans = []
        for small, large in zip(nums[:len(nums) // 2], nums[len(nums) // 2:]):
            ans.append(large)
            ans.append(small)

        if len(nums) % 2 != 0:
            ans.append(nums[-1])

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.rearrangeArray(nums = [1, 2, 3, 4, 5])
    assert test1 == [3, 1, 4, 2, 5]
    
    test2 = sol.rearrangeArray(nums = [6, 2, 0, 9, 7])
    assert test2 == [6, 0, 7, 2, 9]
