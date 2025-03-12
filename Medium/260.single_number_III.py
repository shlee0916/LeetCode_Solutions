'''
https://leetcode.com/problems/single-number-iii/description/
'''

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnt = {}

        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1

        return [key for key, value in cnt.items() if value == 1]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.singleNumber([1, 2, 1, 3, 2, 5])
    print(test1, [3, 5])
    assert test1 == [3, 5]

    test2 = sol.singleNumber([-1, 0])
    print(test2, [-1, 0])
    assert test2 == [-1, 0]

    test3 = sol.singleNumber([0, 1])
    print(test3, [1, 0])
    assert test3 == [0, 1]
