'''
https://leetcode.com/problems/minimum-length-of-string-after-operations/?envType=daily-question&envId=2025-01-13
'''

from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        ans = len(s)
        ch_map = Counter(s)

        for ch, num in ch_map.items():
            ans -= (num - 2) if num % 2 == 0 else (num - 1)

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimumLength(s = "abaacbcbb")
    assert test1 == 5

    test2 = sol.minimumLength(s = "aa")
    assert test2 == 2

    test3 = sol.minimumLength(s = "ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj")
    assert test3 == 38
