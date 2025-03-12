'''
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        left = 0
        cnt = {"a": 0, "b": 0, "c": 0}

        for right in range(len(s)):
            cnt[s[right]] += 1
            
            while all(cnt.values()):
                cnt[s[left]] -= 1
                left += 1
            
            ans += left

        return ans
        

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numberOfSubstrings(s = "abcabc")
    assert test1 == 10
    
    test2 = sol.numberOfSubstrings(s = "aaacb")
    assert test2 == 3
    
    test3 = sol.numberOfSubstrings(s = "abc")
    assert test3 == 1
    