'''
https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/?envType=daily-question&envId=2025-03-10
'''

from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def _at_least_k(k):
            ans = 0
            left = 0
            vow_map = defaultdict(int)
            cur_cons = 0
            
            for right in range(len(word)):
                if word[right] in "aeiou":
                    vow_map[word[right]] += 1
                else:
                    cur_cons += 1

                while len(vow_map) == 5 and cur_cons >= k:
                    ans += len(word) - right

                    if word[left] in "aeiou":
                        vow_map[word[left]] -= 1
                        if vow_map[word[left]] == 0:
                            del vow_map[word[left]]

                    else:
                        cur_cons -= 1

                    left += 1

            return ans
        
        return _at_least_k(k) - _at_least_k(k + 1)
            

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countOfSubstrings(word = "aeioqq", k = 1)
    assert test1 == 0

    test2 = sol.countOfSubstrings(word = "aeiou", k = 0)
    assert test2 == 1

    test3 = sol.countOfSubstrings(word = "ieaouqqieaouqq", k = 1)
    assert test3 == 3
