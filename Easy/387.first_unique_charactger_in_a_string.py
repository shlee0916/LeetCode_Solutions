'''
https://leetcode.com/problems/first-unique-character-in-a-string/
'''
from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx_list = [s.index(ch) for ch, num in Counter(s).items() if num == 1]
        return min(idx_list) if idx_list else -1
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.firstUniqChar("leetcode"), 0)
    print(sol.firstUniqChar("loveleetcode"), 2)
    print(sol.firstUniqChar("aabb"), -1)