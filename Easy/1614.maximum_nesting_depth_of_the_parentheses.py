'''
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/?envType=daily-question&envId=2024-04-04
'''

class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        cur_depth = 0
        for ch in s:
            if ch == "(":
                cur_depth += 1
                max_depth = max(max_depth, cur_depth)
            if ch == ")":
                cur_depth -= 1

        return max_depth


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxDepth(s = "(1+(2*3)+((8)/4))+1")
    assert test1 == 3
    
    test2 = sol.maxDepth(s = "(1)+((2))+(((3)))")
    assert test2 == 3
    