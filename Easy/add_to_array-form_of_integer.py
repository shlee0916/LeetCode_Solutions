'''
https://leetcode.com/problems/add-to-array-form-of-integer/description/
'''

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        int_num = sum([10 ** idx * number for idx, number in enumerate(num[::-1])])
        return [int(char) for char in str(int_num + k)]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.addToArrayForm(num = [1, 2, 0, 0], k = 34)
    print(test1, [1, 2, 3, 4])
    assert test1 == [1, 2, 3, 4]

    test2 = sol.addToArrayForm(num = [2, 7, 4], k = 181)
    print(test2, [4, 5, 5])
    assert test2 == [4, 5, 5]

    test3 = sol.addToArrayForm(num = [2, 1, 5], k = 806)
    print(test3, [1, 0, 2, 1])
    assert test3 == [1, 0, 2, 1]
    