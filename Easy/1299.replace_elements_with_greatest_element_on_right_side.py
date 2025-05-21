'''
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
'''

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = arr[-1]
        arr[-1] = -1
        for idx in range(len(arr) - 2, -1, -1):
            tmp = arr[idx]
            arr[idx] = max_num
            max_num = max(tmp, max_num)

        return arr


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.replaceElements([17, 18, 5, 4, 6, 1])
    assert test1 == [18, 6, 6, 6, 1, -1]

    test2 = sol.replaceElements([400])
    assert test2 == [-1]
    