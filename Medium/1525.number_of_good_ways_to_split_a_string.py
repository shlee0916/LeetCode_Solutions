'''
https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description/
'''

from collections import  Counter


class Solution:
    def numSplits(self, s: str) -> int:
        left = set()
        right = Counter(s)
        result = 0
        for ch in s:
            left.add(ch)
            right[ch] -= 1
            if right[ch] == 0:
                right.pop(ch)

            if len(left) == len(right):
                result += 1

        return result
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numSplits(s = "aacaba")
    print(test1, 2)
    assert test1 == 2
    
    test2 = sol.numSplits(s = "abcd")
    print(test2, 1)
    assert test2 == 1
    