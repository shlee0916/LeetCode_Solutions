'''
https://leetcode.com/problems/second-largest-digit-in-a-string/description/
'''

class Solution:
    def secondHighest(self, s: str) -> int:
        digit_set = list(set([int(ch) for ch in s if ch.isdigit()]))
        digit_set.sort()

        return digit_set[-2] if len(digit_set) > 1 else -1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.secondHighest(s = "dfa12321afd")
    assert test1 == 2
    
    test2 = sol.secondHighest(s = "abc1111")
    assert test2 == -1
    