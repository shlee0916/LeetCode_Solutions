'''
https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/?envType=daily-question&envId=2024-11-20
'''

from collections import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnts = Counter(s)

        if any(cnts[char] < k for char in "abc"):
            return -1
        
        ans = len(s)
        left = 0
        for right in range(len(s)):
            cnts[s[right]] -= 1

            while cnts[s[right]] < k:
                cnts[s[left]] += 1
                left += 1

            ans = min(ans, len(s) - (right - left + 1))
            
        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.takeCharacters(s = "aabaaaacaabc", k = 2)
    assert test1 == 8

    test2 = sol.takeCharacters(s = "a", k = 1)
    assert test2 == -1
    