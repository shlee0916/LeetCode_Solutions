'''
https://leetcode.com/problems/generate-parentheses/
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def dfs(left, right, paren):
            if left > right:
                return
            
            if left == 0 and right == 0:
                result.append(paren)
                return
            
            if left == 0:
                dfs(left, right - 1, paren + ")")
            else:
                dfs(left - 1, right, paren + "(")
                dfs(left, right - 1, paren + ")")
                
        dfs(n, n, "")
        return result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.generateParenthesis(3))