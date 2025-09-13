'''
https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/?envType=daily-question&envId=2025-09-13
'''

class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = {}

        v_max = 0
        c_max = 0

        for ch in s:
            freq_num = ord(ch) - ord("a")
            freq[freq_num] = freq.get(freq_num, 0) + 1
            if ch in "aeiou":
                v_max = max(v_max, freq[freq_num])

            else:
                c_max = max(c_max, freq[freq_num])

        return v_max + c_max
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxFreqSum(s = "successes")
    assert test1 == 6

    test2 = sol.maxFreqSum(s = "aeiaeia")
    assert test2 == 3
    