'''
https://leetcode.com/problems/count-vowels-permutation/description/?envType=daily-question&envId=2023-10-28
'''

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(1, n):
            a, e, i, o, u = e, a + i, a + e + o + u, i + u, a

        return (a + e + i + o + u) % (10 ** 9 + 7)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countVowelPermutation(n = 1)
    assert test1 == 5
    
    test2 = sol.countVowelPermutation(n = 2)
    assert test2 == 10
    
    test3 = sol.countVowelPermutation(n = 5)
    assert test3 == 68
    