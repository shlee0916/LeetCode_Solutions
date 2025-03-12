'''
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/?envType=daily-question&envId=2025-02-05
'''

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_idx = -1
        second_idx = -1

        for idx, (s1_ch, s2_ch) in enumerate(zip(s1, s2)):
            if s1_ch != s2_ch:
                if first_idx == -1:
                    first_idx = idx
                elif second_idx == -1:
                    second_idx = idx
                else:
                    return False

        return s1[first_idx] == s2[second_idx] and s1[second_idx] == s2[first_idx]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.areAlmostEqual(s1 = "bank", s2 = "kanb")
    assert test1 == True

    test2 = sol.areAlmostEqual(s1 = "attack", s2 = "defend")
    assert test2 == False

    test3 = sol.areAlmostEqual(s1 = "kelb", s2 = "kelb")
    assert test3 == True
    