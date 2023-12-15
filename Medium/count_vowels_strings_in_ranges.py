'''
https://leetcode.com/problems/count-vowel-strings-in-ranges/description/
'''

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"

        vowels_nums = [0]
        prefix_sum = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum += 1
            vowels_nums.append(prefix_sum)

        ans = []
        for start, end in queries:
            ans.append(vowels_nums[end + 1] - vowels_nums[start])

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.vowelStrings(words = ["aba", "bcb", "ece", "aa", "e"], queries = [[0, 2], [1, 4], [1, 1]])
    assert test1 == [2, 3, 0]
    
    test2 = sol.vowelStrings(words = ["a", "e", "i"], queries = [[0, 2], [0, 1], [2, 2]])
    assert test2 == [3, 2, 1]
    