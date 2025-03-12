'''
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/
'''

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for idx in range(len(s) - 2):
            sub_str = s[idx : idx + 3]
            if len(set(sub_str)) == len(sub_str):
                ans += 1

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countGoodSubstrings(s = "xyzzaz")
    assert test1 == 1
    
    test2 = sol.countGoodSubstrings(s = "aababcabc")
    assert test2 == 4
    