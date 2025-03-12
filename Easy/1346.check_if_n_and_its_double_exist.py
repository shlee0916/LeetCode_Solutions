'''
https://leetcode.com/problems/check-if-n-and-its-double-exist/description/
'''

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True

            seen.add(num)

        return False


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.checkIfExist(arr = [10, 2, 5, 3])
    assert test1 == True

    test2 = sol.checkIfExist(arr = [3, 1, 7, 11])
    assert test2 == False
    