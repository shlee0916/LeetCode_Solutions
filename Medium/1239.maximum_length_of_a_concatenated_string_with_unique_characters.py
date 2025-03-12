'''
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        
        for word in arr:
            if len(word) > len(set(word)):
                continue
            
            word = set(word)
            for word_set in dp[:]:
                if word & word_set:
                    continue
                
                dp.append(word | word_set)
        
        return max(len(s) for s in dp)


if __name__ == "__main__":
    sol = Solution()

    print(sol.maxLength(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]), 16)
    print(sol.maxLength(["abcdefghijklmnopqrstuvwxyz"]), 26)
    print(sol.maxLength(["cha", "r", "act", "ers"]), 6)