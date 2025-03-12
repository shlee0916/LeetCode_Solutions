'''
https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/?envType=daily-question&envId=2023-12-04
'''

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for single_num in range(9, -1, -1):
            if str(single_num) * 3 in num:
                return str(single_num) * 3

        return ""


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.largestGoodInteger(num = "6777133339")
    assert test1 == "777"
    
    test2 = sol.largestGoodInteger(num = "2300019")
    assert test2 == "000"
    
    test3 = sol.largestGoodInteger(num = "42352338")
    assert test3 == ""
    