'''
https://leetcode.com/problems/longest-common-prefix/
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for chs in zip(*strs):
            tmp_set = set(chs)
            
            if len(tmp_set) == 1:
                result += list(tmp_set)[0]
            else:
                break
                
        return result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.longestCommonPrefix(["cir", "car"]))