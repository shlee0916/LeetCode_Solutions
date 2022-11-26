'''
https://leetcode.com/problems/find-the-difference/description/
'''
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)

        for ch, nums in t_counter.items():
            if ch not in s_counter or s_counter[ch] != nums:
                return ch
            
            
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findTheDifference("abcd", "abcde")
    print(test1, "e")
    assert test1 == "e"
    
    test2 = sol.findTheDifference("", "y")
    print(test2, "y")
    assert test2 == "y"
    