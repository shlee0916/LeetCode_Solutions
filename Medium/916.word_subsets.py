'''
https://leetcode.com/problems/word-subsets/?envType=daily-question&envId=2025-01-10
'''

from collections import Counter

from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        req_freq = Counter()
        ans = []

        for word in words2:
            word_freq = Counter(word)
            for ch, num in word_freq.items():
                req_freq[ch] = max(req_freq[ch], num)

        for word in words1:
            word_freq = Counter(word)
            if all(word_freq[ch] >= req_freq[ch] for ch in req_freq):
                ans.append(word)        
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.wordSubsets(words1 = ["amazon", "apple", "facebook", "google", "leetcode"], words2 = ["e", "o"])
    assert test1 == ["facebook", "google", "leetcode"]

    test2 = sol.wordSubsets(words1 = ["amazon", "apple", "facebook", "google", "leetcode"], words2 = ["l", "e"])
    assert test2 == ["apple", "google", "leetcode"]
