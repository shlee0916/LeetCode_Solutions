'''
https://leetcode.com/problems/first-letter-to-appear-twice/description/
'''

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()

        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.repeatedCharacter(s = "abccbaacz")
    assert test1 == "c"
    
    test2 = sol.repeatedCharacter(s = "abcdd")
    assert test2 == "d"
    