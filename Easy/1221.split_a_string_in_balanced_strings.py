'''
https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        cnt = 0
        for ch in s:
            cnt += 1 if ch == "L" else - 1
            if cnt == 0:
                result += 1

        return result
                
                
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.balancedStringSplit(s = "RLRRLLRLRL")
    assert test1 == 4
    
    test2 = sol.balancedStringSplit(s = "RLRRRLLRLL")
    assert test2 == 2
    
    test3 = sol.balancedStringSplit(s = "LLLLRRRR")
    assert test3 == 1
    