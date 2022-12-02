'''
https://leetcode.com/problems/determine-if-two-strings-are-close/description/
'''

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Operation1
        op1_flag = set(word1) == set(word2)

        # Operation2
        op2_flag = Counter(Counter(word1).values()) == Counter(Counter(word2).values())

        return op1_flag and op2_flag


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.closeStrings("abc", "bca")
    print(test1, True)
    assert test1 == True

    test2 = sol.closeStrings("a", "aa")
    print(test2, False)
    assert test2 == False

    test3 = sol.closeStrings("cabbba", "abbccc")
    print(test3, True)
    assert test3 == True

    test4 = sol.closeStrings("abbzccca", "babzzczc")
    print(test4, True)
    assert test4 == True
