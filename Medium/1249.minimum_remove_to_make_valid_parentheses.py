'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/?envType=daily-question&envId=2024-04-11
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        new_str = list(s)
        stack = []
        for idx, ch in enumerate(new_str):
            if ch == "(":
                stack.append(idx)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    new_str[idx] = ""
        
        while stack:
            new_str[stack.pop()] = ""

        return "".join(new_str)
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minRemoveToMakeValid(s = "lee(t(c)o)de)")
    assert test1 == "lee(t(c)o)de"
    
    test2 = sol.minRemoveToMakeValid(s = "a)b(c)d")
    assert test2 == "ab(c)d"
    
    test3 = sol.minRemoveToMakeValid(s = "))((")
    assert test3 == ""
    