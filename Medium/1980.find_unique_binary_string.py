'''
https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2024-01-18
'''

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        binary = ["1" if num[idx] == "0" else "0" for idx, num in enumerate(nums)]

        return "".join(binary)
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findDifferentBinaryString(nums = ["01", "10"])
    assert test1 == "11"

    test2 = sol.findDifferentBinaryString(nums = ["00", "01"])
    assert test2 == "10"

    test3 = sol.findDifferentBinaryString(nums = ["111", "011", "001"])
    assert test3 == "000"
    