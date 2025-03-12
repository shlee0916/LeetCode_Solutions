'''
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/?envType=daily-question&envId=2024-08-06
'''

from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        word_map = list(Counter(word).items())
        word_map.sort(key = lambda x: -x[1])
        
        ans = 0
        for idx, (_, num) in enumerate(word_map):
            ans += ((idx  // 8) + 1) * num
            

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimumPushes(word = "abcde")
    assert test1 == 5 
    
    test2 = sol.minimumPushes(word = "xyzxyzxyzxyz")
    assert test2 == 12

    test3 = sol.minimumPushes(word = "aabbccddeeffgghhiiiiii")
    assert test3 == 24
    