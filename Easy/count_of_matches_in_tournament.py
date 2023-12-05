'''
https://leetcode.com/problems/count-of-matches-in-tournament/description/?envType=daily-question&envId=2023-12-05
'''

class Solution:
    def numberOfMatches(self, n: int) -> int:
        match_cnt = 0

        while n > 1:
            if n % 2 == 0:
                n //= 2
                match_cnt += n
            else:
                match_cnt += n // 2
                n = (n - 1) // 2 + 1

        return match_cnt
    
    # def numberOfMatches(self, n: int) -> int:
    #     return n - 1
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numberOfMatches(n = 7)
    assert test1 == 6

    test2 = sol.numberOfMatches(n = 14)
    assert test2 == 13
