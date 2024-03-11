'''
https://leetcode.com/problems/custom-sort-string/?envType=daily-question&envId=2024-03-11
'''

from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        left_ch = Counter(s)
        ans = ""

        for ch in order:
            if ch in left_ch:
                ans += ch * left_ch.pop(ch)

        for ch, num in left_ch.items():
            ans += ch * num

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.customSortString(order = "cba", s = "abcd" )
    assert test1 == "cbad"

    test2 = sol.customSortString(order = "bcafg", s = "abcd")
    assert test2 == "bcad"
