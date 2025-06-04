'''
https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description/?envType=daily-question&envId=2025-06-04
'''

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        res = ""
        length = len(word) - numFriends + 1
        for idx in range(0, len(word)):
            if res < word[idx : idx + length]:
                res = word[idx : idx + length]

        return res


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.answerString(word = "dbca", numFriends = 2)
    assert test1 == "dbc"

    test2 = sol.answerString(word = "gggg", numFriends = 4)
    assert test2 == "g"
    