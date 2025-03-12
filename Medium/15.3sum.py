'''
https://leetcode.com/problems/3sum/description/
'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left, right = idx + 1, len(nums) - 1
            while left < right:
                sumation = nums[left] + nums[right] + nums[idx]
                if sumation < 0:
                    left += 1
                elif sumation > 0:
                    right -=1
                else:
                    result.append([nums[idx], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right - 1] == nums[right]:
                        right -= 1

                    left += 1
                    right -= 1               

        return result
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.threeSum(nums = [-1, 0, 1, 2, -1, -4])
    print(test1, [[-1, -1, 2], [-1, 0, 1]])
    assert test1 == [[-1, -1, 2], [-1, 0, 1]]

    test2 = sol.threeSum(nums = [0, 1, 1])
    print(test2, [])
    assert test2 == []

    test3 = sol.threeSum(nums = [0, 0, 0])
    print(test3, [[0, 0, 0]])
    assert test3 == [[0, 0, 0]]
    