'''
https://leetcode.com/problems/minimum-window-substring/?envType=daily-question&envId=2024-02-04
'''

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        t_cnt = Counter(t)

        left = 0
        target_len = len(t)

        for right in range(len(s)):
            if t_cnt[s[right]] > 0:
                target_len -= 1
            
            t_cnt[s[right]] -= 1

            while target_len == 0:
                sub_len = right - left + 1
                if ans == "" or sub_len < len(ans):
                    ans = s[left : right + 1]

                t_cnt[s[left]] += 1
                
                if t_cnt[s[left]] > 0:
                    target_len += 1

                left += 1

        return ans
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minWindow(s = "ADOBECODEBANC", t = "ABC")
    assert test1 == "BANC"

    test2 = sol.minWindow(s = "a", t = "a")
    assert test2 == "a"

    test3 = sol.minWindow(s = "a", t = "aa")
    assert test3 == ""
    