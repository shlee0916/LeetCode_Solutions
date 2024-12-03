'''
https://leetcode.com/problems/adding-spaces-to-a-string/?envType=daily-question&envId=2024-12-03
'''

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        space_idx = 0
        for idx, ch in enumerate(s):
            if space_idx < len(spaces) and idx == spaces[space_idx]:
                ans.append(" ")
                space_idx += 1

            ans.append(ch)

        return "".join(ans)
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8, 13, 15])
    assert test1 == "Leetcode Helps Me Learn"

    test2 = sol.addSpaces(s = "icodeinpython", spaces = [1, 5, 7, 9])
    assert test2 == "i code in py thon"

    test3 = sol.addSpaces(s = "spacing", spaces = [0, 1, 2, 3, 4, 5, 6])
    assert test3 == " s p a c i n g"
