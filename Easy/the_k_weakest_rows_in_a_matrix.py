'''
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
'''

class Solution:
    def kWeakestRows(self, mat, k):
        return [sol for _, sol in sorted([(sum(row), ind) for ind, row in enumerate(mat)])[:k]]


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.kWeakestRows(mat = [[1, 1, 0, 0, 0], 
                                    [1, 1, 1, 1, 0], 
                                    [1, 0, 0, 0, 0], 
                                    [1, 1, 0, 0, 0], 
                                    [1, 1, 1, 1, 1]],  
                                    k = 3)
    assert test1 == [2, 0, 3]
    
    test2 = sol.kWeakestRows(mat = [[1, 0, 0, 0], 
                                    [1, 1, 1, 1], 
                                    [1, 0, 0, 0], 
                                    [1, 0, 0, 0]],  
                                    k = 2)
    assert test2 == [0, 2]
    