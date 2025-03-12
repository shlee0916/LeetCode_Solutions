'''
https://leetcode.com/problems/permutation-in-string/?envType=daily-question&envId=2024-10-05
'''

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        win_size = len(s1)
        mat_num = 0

        for idx in range(len(s2)):
            if s2[idx] in cnt:
                cnt[s2[idx]] -= 1

            if idx >= win_size and s2[idx - win_size] in cnt:
                cnt[s2[idx - win_size]] += 1

            if all(val == 0 for val in cnt.values()):
                return True

        return False
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.checkInclusion(s1 = "ab", s2 = "eidbaooo")
    assert test1 == True
    
    test2 = sol.checkInclusion(s1 = "ab", s2 = "eidboaoo")
    assert test2 == False
    