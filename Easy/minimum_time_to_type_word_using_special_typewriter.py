'''
https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
'''

class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = len(word)
        prev = "a"
        for ch in word:
            val = (ord(ch) - ord(prev)) % 26
            ans += min(val, 26 - val)
            prev = ch
        
        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minTimeToType(word = "abc")
    assert test1 == 5
    
    test2 = sol.minTimeToType(word = "bza")
    assert test2 == 7
    
    test3 = sol.minTimeToType(word = "zjpc")
    assert test3 == 34
    