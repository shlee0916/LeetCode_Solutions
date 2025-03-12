'''
https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digit = int("".join(str(num) for num in digits)) + 1

        return [int(num) for num in str(new_digit)]
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.plusOne(digits = [1, 2, 3])
    assert test1 == [1, 2, 4]

    test2 = sol.plusOne(digits = [4, 3, 2, 1])
    assert test2 == [4, 3, 2, 2]

    test3 = sol.plusOne(digits = [9])
    assert test3 == [1, 0]
    