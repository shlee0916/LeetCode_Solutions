'''
https://leetcode.com/problems/replace-words/description/?envType=daily-question&envId=2024-06-07
'''

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        words = sentence.split()
        ans = []

        for word in words:
            for length in range(len(word) + 1):
                prefix = word[:length]
                if prefix in roots:
                    ans.append(prefix)
                    break
            else:
                ans.append(word)

        return " ".join(ans)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.replaceWords(dictionary = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery")
    assert test1 == "the cat was rat by the bat"
    
    test2 = sol.replaceWords(dictionary = ["a", "b", "c"], sentence = "aadsfasf absbs bbab cadsfafs")
    assert test2 == "a a b c"
    