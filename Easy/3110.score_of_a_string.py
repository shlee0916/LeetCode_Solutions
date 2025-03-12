'''
https://leetcode.com/problems/score-of-a-string/?envType=daily-question&envId=2024-06-01
'''

class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for idx, ch in enumerate(s[1:]):
            ans += abs(ord(s[idx]) - ord(ch))

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.scoreOfString(s = "hello")
    assert test1 == 13
    
    test2 = sol.scoreOfString(s = "zaz")
    assert test2 == 50
    