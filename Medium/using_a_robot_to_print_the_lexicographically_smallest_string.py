'''
https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description/
'''

from collections import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        all_ch = Counter(s)
        holds = []
        paper = []

        for ch in s:
            all_ch[ch] -= 1
            holds.append(ch)

            if all_ch[ch] == 0:
                all_ch.pop(ch)

            while all_ch and holds and min(all_ch) >= holds[-1]:
                paper.append(holds.pop())

        paper.extend(holds[::-1])

        return "".join(paper)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.robotWithString(s = "zza")
    assert test1 == "azz"
    
    test2 = sol.robotWithString(s = "bac")
    assert test2 == "abc"
    
    test3 = sol.robotWithString(s = "bdda")
    assert test3 == "addb"
    