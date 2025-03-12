'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
'''

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return []
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.twoSum(numbers = [2, 7, 11, 15], target = 9)
    assert test1 == [1, 2]

    test2 = sol.twoSum(numbers = [2, 3, 4], target = 6)
    assert test2 == [1, 3]

    test3 = sol.twoSum(numbers = [-1, 0], target = -1)
    assert test3 == [1, 2]
    