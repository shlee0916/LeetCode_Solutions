'''
https://leetcode.com/problems/maximum-odd-binary-number/description/
'''

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        length = len(s)
        num_ones = s.count("1")

        new_str = ""
        for _ in range(num_ones - 1):
            new_str += "1"

        for _ in range(length - num_ones):
            new_str += "0"

        return new_str + "1"


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maximumOddBinaryNumber(s = "010")
    assert test1 == "001"
    
    test2 = sol.maximumOddBinaryNumber(s = "0101")
    assert test2 == "1001"
    