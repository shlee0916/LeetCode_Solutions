'''
https://leetcode.com/problems/sort-characters-by-frequency/
'''

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        ch_cnt = Counter(s)
        return "".join([ch * no for ch, no in ch_cnt.most_common()])
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.frequencySort("tree")
    print(test1, "eetr")
    assert test1 == "eetr"
    
    test2 = sol.frequencySort("cccaaa")
    print(test2, "cccaaa or aaaccc")
    assert test2 == "cccaaa" or test2 == "aaaccc"
    
    test3 = sol.frequencySort("Aabb")
    print(test3, "bbAa")
    assert "bbAa" == "bbAa"