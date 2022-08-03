'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
'''

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        tmp_list = []
        for row in matrix:
            tmp_list.extend(row)
            
        tmp_list.sort()
        
        return tmp_list[k - 1]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8), 13)