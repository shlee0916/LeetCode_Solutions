'''
https://leetcode.com/problems/count-sorted-vowel-strings/description/
'''

class Solution:
    def countVowelStrings(self, n: int) -> int:
        table = [[i for i in range(5, 0, -1)] for _ in range(n)]
        
        for n_idx in range(1, n):
            for a_idx in range(3, -1, -1):
                table[n_idx][a_idx] = table[n_idx - 1][a_idx] + table[n_idx][a_idx + 1]

        return table[n - 1][0]
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countVowelStrings(1)
    print(test1, 1)
    assert test1 == 5

    test2 = sol.countVowelStrings(2)
    print(test2, 15)
    assert test2 == 15

    test3 = sol.countVowelStrings(33)
    print(test3, 66045)
    assert test3 == 66045
