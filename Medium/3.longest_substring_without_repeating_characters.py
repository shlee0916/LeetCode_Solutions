'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0
        cnt = dict()
        for idx, ch in enumerate(s):
            if ch in cnt:
                start = max(start, cnt[ch])
            res = max(res, idx - start + 1)
            cnt[ch] = idx + 1
            
        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.lengthOfLongestSubstring("aaaaaa"))
    print(sol.lengthOfLongestSubstring("abcabcdd"))
    