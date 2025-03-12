'''
https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/?envType=daily-question&envId=2023-10-31
'''

from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]

        for idx, num in enumerate(pref[1:]):
            ans.append(num ^ pref[idx])

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findArray(pref = [5, 2, 0, 3, 1])
    assert test1 == [5, 7, 2, 3, 2]

    test2 = sol.findArray(pref = [13])
    assert test2 == [13]
    