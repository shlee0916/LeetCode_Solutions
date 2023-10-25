'''
https://leetcode.com/problems/k-th-symbol-in-grammar/description/?envType=daily-question&envId=2023-10-25
'''

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            if k == 1:
                return 0
            else:
                return 1

        half = 2 ** (n - 1)
        if k <= half:
            return self.kthGrammar(n - 1, k)
        else:
            res = self.kthGrammar(n - 1, k - half)
            if res == 0:
                return 1
            else:
                return 0


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.kthGrammar(n = 1, k = 1)
    assert test1 == 0
    
    test2 = sol.kthGrammar(n = 2, k = 1)
    assert test2 == 0
    
    test3 = sol.kthGrammar(n = 2, k = 2)
    assert test3 == 1
    