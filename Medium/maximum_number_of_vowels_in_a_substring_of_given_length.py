'''
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=daily-question&envId=2023-09-02
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ("a", "e", "i", "o", "u")
        ans = -float("inf")
        cnt = 0
        for idx, ch in enumerate(s):
            if ch in vowels:
               cnt += 1
            if idx >= k and s[idx - k] in vowels:
                cnt -= 1

            ans = max(ans, cnt) 
            
        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxVowels(s = "abciiidef", k = 3)
    assert test1 == 3
    
    test2 = sol.maxVowels(s = "aeiou", k = 2)
    assert test2 == 2
    
    test3 = sol.maxVowels(s = "leetcode", k = 3)
    assert test3 == 2
    