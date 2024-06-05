'''
https://leetcode.com/problems/find-common-characters/description/?envType=daily-question&envId=2024-06-05
'''

from collections import Counter

from typing import List 


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        std_cnt = Counter(words[0])

        for word in words:
            cnt = Counter(word)
            for ch in std_cnt.keys():
                std_cnt[ch] = min(std_cnt[ch], cnt[ch])
        
        return std_cnt.elements()
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.commonChars(words = ["bella", "label", "roller"])
    assert set(test1) == set(["e", "l", "l"])
    
    test2 = sol.commonChars(words = ["cool", "lock", "cook"])
    assert set(test2) == set(["c", "o"])
