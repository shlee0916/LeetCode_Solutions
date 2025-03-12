'''
https://leetcode.com/problems/add-strings/description/
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(str_num: str) -> int:
            res = 0
            for idx, ch in enumerate(str_num[::-1]):
                res += (10 ** idx) * (ord(ch) - ord("0"))
                
            return res
            
        return str(str2int(num1) + str2int(num2))
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.addStrings(num1 = "11", num2 = "123")
    print(test1, "134")
    assert test1 == "134"
    
    test2 = sol.addStrings(num1 = "456", num2 = "77")
    print(test2, "533")
    assert test2 == "533"
    