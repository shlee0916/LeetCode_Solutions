'''
https://leetcode.com/problems/spiral-matrix/
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        result.extend(matrix.pop(0))
        while matrix:
            matrix = [list(row) for row in list(zip(*matrix))[::-1]]
            result.extend(matrix.pop(0))
            
        return result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])