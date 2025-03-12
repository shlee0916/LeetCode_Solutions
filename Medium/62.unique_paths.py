'''
https://leetcode.com/problems/unique-paths/
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths = [1] * n
        
        for row in range(m - 1):
            for col in range(n - 1):
                num_paths[col + 1] += num_paths[col]
            
        return num_paths[-1]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.uniquePaths(3, 7))