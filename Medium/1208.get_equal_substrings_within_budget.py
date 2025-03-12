'''
https://leetcode.com/problems/get-equal-substrings-within-budget/description/?envType=daily-question&envId=2024-05-28
'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        cur_cost = 0
        for right in range(len(s)):
            cur_cost += abs(ord(s[right]) - ord(t[right]))

            if cur_cost > maxCost:
                cur_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
        
        return right - left + 1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.equalSubstring(s = "abcd", t = "bcdf", maxCost = 3)
    assert test1 == 3
    
    test2 = sol.equalSubstring(s = "abcd", t = "cdef", maxCost = 3)
    assert test2 == 1
    
    test3 = sol.equalSubstring(s = "abcd", t = "acde", maxCost = 0)
    assert test3 == 1
    