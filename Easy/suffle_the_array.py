'''
https://leetcode.com/problems/shuffle-the-array/description/
'''

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        for num1, num2 in zip(nums[:n], nums[n:]):
            ans.append(num1)
            ans.append(num2)

        return ans


if __name__  == "__main__":
    sol = Solution()
    
    test1 = sol.shuffle(nums = [2, 5, 1, 3, 4, 7], n = 3)
    assert test1 == [2, 3, 5, 4, 1, 7]

    test2 = sol.shuffle(nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4)
    assert test2 == [1, 4, 2, 3, 3, 2, 4, 1]

    test3 = sol.shuffle(nums = [1, 1, 2, 2], n = 2)
    assert test3 == [1, 2, 1, 2]
    