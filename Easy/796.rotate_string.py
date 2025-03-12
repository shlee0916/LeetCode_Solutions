'''
https://leetcode.com/problems/rotate-string/description/
'''

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.rotateString(s = "abcde", goal = "cdeab")
    assert test1 == True
    
    test2 = sol.rotateString(s = "abcde", goal = "abced")
    assert test2 == False
    