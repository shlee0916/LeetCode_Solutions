'''
https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/?envType=daily-question&envId=2024-02-01
'''

from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for pointer in range(0, len(nums), 3):
            sub_array = nums[pointer : pointer + 3]

            if max(sub_array) - min(sub_array) <= k:
                ans.append(sub_array)
            else:
                return []

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.divideArray(nums = [1, 3, 4, 8, 7, 9, 3, 5, 1], k = 2)
    assert test1 == [[1, 1, 3], [3, 4, 5], [7, 8, 9]]

    test2 = sol.divideArray(nums = [1, 3, 3, 2, 7, 3], k = 3)
    assert test2 == []
    