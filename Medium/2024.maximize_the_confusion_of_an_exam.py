'''
https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/
'''

from collections import Counter


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        length = Counter()

        max_len = 0
        left = 0
        for right, answer in enumerate(answerKey):
            length[answer] += 1

            if length["T"] > k and length["F"] > k:
                length[answerKey[left]] -= 1
                left += 1
            else:
                max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxConsecutiveAnswers(answerKey = "TTFF", k = 2)
    assert test1 == 4
    
    test2 = sol.maxConsecutiveAnswers(answerKey = "TFFT", k = 1)
    assert test2 == 3
    
    test3 = sol.maxConsecutiveAnswers(answerKey = "TTFTTFTT", k = 1)
    assert test3 == 5
    