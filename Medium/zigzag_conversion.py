'''
https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        new_s = [""] * numRows
        new_s_idx = 0
        step = 1
        for ch in s:
            new_s[new_s_idx] += ch

            if new_s_idx == 0:
                step = 1
            elif new_s_idx == numRows - 1:
                step = -1

            new_s_idx += step

        return "".join(new_s)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.convert(s = "PAYPALISHIRING", numRows = 3)
    assert test1 == "PAHNAPLSIIGYIR"

    test2 = sol.convert(s = "PAYPALISHIRING", numRows = 4)
    assert test2 == "PINALSIGYAHRPI"

    test3 = sol.convert(s = "A", numRows = 1)
    assert test3 == "A"
    