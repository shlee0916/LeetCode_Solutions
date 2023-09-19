'''
https://leetcode.com/problems/find-the-duplicate-number/description/?envType=daily-question&envId=2023-09-19
'''

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        begin = 1
        end = len(nums) - 1

        while begin + 1 <= end:
            mid = (begin + end) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count <= mid:
                begin = mid + 1
            else:
                end = mid

        return end


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findDuplicate(nums = [1, 3, 4, 2, 2])
    assert test1 == 2
    
    test2 = sol.findDuplicate(nums = [3, 1, 3, 4, 2])
    assert test2 == 3
    