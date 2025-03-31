'''
https://leetcode.com/problems/partition-labels/?envType=daily-question&envId=2025-03-31
'''

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ch_idx = {ch: idx for idx, ch in enumerate(s)}

        left = right = 0
        ans = []

        for idx, ch in enumerate(s):
            right = max(right, ch_idx[ch])

            if idx == right:
                ans.append(right - left + 1)
                left = right + 1

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.partitionLabels(s = "ababcbacadefegdehijhklij")
    assert test1 == [9, 7, 8]

    test2 = sol.partitionLabels(s = "eccbbbbdec")
    assert test2 == [10]
    