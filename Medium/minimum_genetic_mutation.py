'''
https://leetcode.com/problems/minimum-genetic-mutation/
'''
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        que = [(start, 0)]
        
        while que:
            cur_gene, step = que.pop(0)
            
            if cur_gene == end:
                return step
            
            for cur_idx in range(len(cur_gene)):
                for nucleic in "ACGT":
                    mutant = cur_gene[:cur_idx] + nucleic + cur_gene[cur_idx + 1:]
                    if mutant in bank:
                        bank.remove(mutant)
                        que.append((mutant, step + 1))
                        
        return -1


if __name__ == "__main__":
    sol = Solution()


    test1 = sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
    print(test1, 1)
    assert test1 == 1

    test2 = sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
    print(test2, 2)
    assert test2 == 2

    test3 = sol.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"])
    print(test3, 3)
    assert test3 == 3

    test4 = sol.minMutation("AAAACCCC", "CCCCCCCC", ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"])
    print(test4, 4)
    assert test4 == 4